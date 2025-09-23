"""
Purpose: Streamlit web application

High-level Overview:
Comprehensive web interface built with Streamlit that provides all CLI functionality through a user-friendly web interface with interactive charts and visualizations.

Key Components:
- Multi-page Streamlit application
- Interactive analysis interface
- Real-time chat functionality
- Data visualization with Plotly
- Session state management

Functions/Classes:
- `initialize_session_state()`: Initialize Streamlit session variables
- `setup_rag_and_chatbot()`: Initialize RAG system and chatbot
- `@st.cache_data run_analysis(path, branch=None)`: Cached analysis execution
- `run_codebase_info(path)`: Get codebase information
- `create_overview_metrics(results)`: Create metrics dashboard
- `create_severity_chart(issues)`: Create severity distribution chart
- `create_category_chart(issues)`: Create category distribution chart
- `create_file_analysis_table(results)`: Create file analysis table
- `create_chatbot_interface()`: Create chat interface
- `create_rag_stats()`: Create RAG statistics display
- **`setup_page()`**: Configuration and setup page
- `info_page()`: Codebase information page
- `analyze_page()`: Main analysis page with tabs
- `chat_page()`: Enhanced chat page
- `main()`: Main application with navigation
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import asyncio
import sys
import os
from datetime import datetime
from pathlib import Path
import tempfile
import shutil
from typing import Optional, Dict, Any

# Add parent directory to path to import the package
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from code_quality_agent.agent import CodeQualityAgent
    from code_quality_agent.chatbot import CodeQualityChatbot
    from code_quality_agent.rag_system import CodeRAGSystem
    from code_quality_agent.config import Config
    from code_quality_agent.report_generator import ReportGenerator
    from code_quality_agent.utils.file_handler import FileHandler
except ImportError as e:
    st.error(f"Failed to import code_quality_agent package: {e}")
    st.error("Please ensure the package is installed: pip install code-quality-intelligence")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Code Quality Intelligence Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.25rem;
        padding: 0.75rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 0.25rem;
        padding: 0.75rem;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 0.25rem;
        padding: 0.75rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables."""
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = None
    if 'rag_system' not in st.session_state:
        st.session_state.rag_system = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'analysis_history' not in st.session_state:
        st.session_state.analysis_history = []
    if 'setup_complete' not in st.session_state:
        st.session_state.setup_complete = False
    if 'api_key_configured' not in st.session_state:
        st.session_state.api_key_configured = False

def setup_rag_and_chatbot():
    """Initialize RAG system and chatbot."""
    if st.session_state.rag_system is None:
        st.session_state.rag_system = CodeRAGSystem()
    
    if st.session_state.chatbot is None:
        st.session_state.chatbot = CodeQualityChatbot(st.session_state.rag_system)

@st.cache_data
def run_analysis(path: str, branch: Optional[str] = None) -> Dict[str, Any]:
    """Run code analysis with caching."""
    try:
        agent = CodeQualityAgent()
        # Use asyncio in a thread-safe way for Streamlit
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(agent.analyze_codebase(path, branch=branch))
        loop.close()
        return results
    except Exception as e:
        return {"error": str(e)}

def run_codebase_info(path: str) -> Dict[str, Any]:
    """Get codebase information without full analysis."""
    try:
        file_handler = FileHandler()
        files = file_handler.get_code_files(path)
        
        if not files:
            return {"error": "No supported code files found"}
        
        # Language distribution
        language_counts = {}
        total_size = 0
        total_lines = 0
        
        for file_path in files:
            language = file_handler.detect_language(file_path)
            language_counts[language] = language_counts.get(language, 0) + 1
            
            stats = file_handler.get_file_stats(file_path)
            total_size += stats.get('size_bytes', 0)
            total_lines += stats.get('total_lines', 0)
        
        file_handler.cleanup()
        
        return {
            "total_files": len(files),
            "total_size_kb": total_size / 1024,
            "total_lines": total_lines,
            "languages": language_counts,
            "files": files
        }
    except Exception as e:
        return {"error": str(e)}

def create_overview_metrics(results: Dict[str, Any]):
    """Create overview metrics display."""
    if not results or 'error' in results:
        st.error("No analysis results available")
        return
    
    summary = results.get('summary', {})
    issues = results.get('issues', [])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Files Analyzed",
            value=summary.get('total_files', 0)
        )
    
    with col2:
        critical_high = len([i for i in issues if i.get('severity') in ['high', 'critical']])
        st.metric(
            label="Total Issues",
            value=summary.get('total_issues', 0),
            delta=f"{critical_high} critical/high"
        )
    
    with col3:
        complexity_score = summary.get('metrics', {}).get('complexity_score', 0)
        st.metric(
            label="Complexity Score",
            value=f"{complexity_score:.1f}",
            delta="Lower is better"
        )
    
    with col4:
        security_issues = len([i for i in issues if i.get('category') == 'security'])
        st.metric(
            label="Security Issues",
            value=security_issues,
            delta="Critical priority" if security_issues > 0 else "All clear"
        )

def create_severity_chart(issues: list):
    """Create severity distribution chart."""
    if not issues:
        st.info("No issues to display")
        return
    
    severity_counts = {}
    for issue in issues:
        severity = issue.get('severity', 'info').title()
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
    fig = px.pie(
        values=list(severity_counts.values()),
        names=list(severity_counts.keys()),
        title="Issues by Severity",
        color_discrete_map={
            'Critical': '#ff4444',
            'High': '#ff8800',
            'Medium': '#ffbb33',
            'Low': '#00C851',
            'Info': '#33b5e5'
        }
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

def create_category_chart(issues: list):
    """Create category distribution chart."""
    if not issues:
        return
    
    category_counts = {}
    for issue in issues:
        category = issue.get('category', 'unknown').replace('_', ' ').title()
        category_counts[category] = category_counts.get(category, 0) + 1
    
    fig = px.bar(
        x=list(category_counts.values()),
        y=list(category_counts.keys()),
        orientation='h',
        title="Issues by Category",
        color=list(category_counts.values()),
        color_continuous_scale='viridis'
    )
    
    fig.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

def create_file_analysis_table(results: Dict[str, Any]):
    """Create file analysis table."""
    file_analyses = results.get('file_analyses', {})
    if not file_analyses:
        st.info("No file analysis data available")
        return
    
    table_data = []
    for file_path, analysis in file_analyses.items():
        issues = analysis.get('issues', [])
        metrics = analysis.get('metrics', {})
        
        severity_counts = {}
        for issue in issues:
            severity = issue.get('severity', 'info')
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        table_data.append({
            'File': Path(file_path).name,
            'Full Path': file_path,
            'Issues': len(issues),
            'Critical': severity_counts.get('critical', 0),
            'High': severity_counts.get('high', 0),
            'Medium': severity_counts.get('medium', 0),
            'Low': severity_counts.get('low', 0),
            'Complexity': metrics.get('complexity_score', 0),
            'Language': analysis.get('debug', {}).get('language', 'unknown')
        })
    
    if table_data:
        df = pd.DataFrame(table_data)
        
        def highlight_issues(val):
            if val > 5:
                return 'background-color: #ffcccc'
            elif val > 2:
                return 'background-color: #fff2cc'
            return ''
        
        styled_df = df.style.applymap(highlight_issues, subset=['Issues', 'Critical', 'High'])
        st.dataframe(styled_df, use_container_width=True)

def create_chatbot_interface():
    """Create chatbot interface."""
    st.subheader("Chat with Your Codebase")
    
    setup_rag_and_chatbot()
    
    if st.session_state.analysis_results and st.session_state.chatbot:
        st.session_state.chatbot.set_analysis_context(st.session_state.analysis_results)
    
    if st.session_state.chatbot:
        # Display chat history
        for message in st.session_state.chat_history:
            with st.container():
                st.markdown(
                    f'<div class="chat-message user-message"><strong>You:</strong> {message["user"]}</div>',
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="chat-message assistant-message"><strong>Assistant:</strong> {message["assistant"]}</div>',
                    unsafe_allow_html=True
                )
        
        # Chat input
        user_input = st.text_input("Ask about your code:", placeholder="e.g., What security issues did you find?")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Send", type="primary"):
                if user_input:
                    with st.spinner("Thinking..."):
                        response = st.session_state.chatbot.chat(user_input)
                    
                    st.session_state.chat_history.append({
                        "user": user_input,
                        "assistant": response
                    })
                    st.rerun()
        
        with col2:
            if st.button("Clear Chat"):
                st.session_state.chat_history = []
                if st.session_state.chatbot:
                    st.session_state.chatbot.clear_conversation()
                st.rerun()
    else:
        st.warning("Chatbot not available. Please check your API key configuration.")

def create_rag_stats():
    """Create RAG system statistics."""
    if st.session_state.rag_system and st.session_state.rag_system.is_available():
        stats = st.session_state.rag_system.get_collection_stats()
        
        if 'error' not in stats:
            st.subheader("RAG System Status")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Code Chunks Stored", stats.get('total_chunks', 0))
            with col2:
                st.metric("Avg Issues per Chunk", f"{stats.get('avg_issues_per_chunk', 0):.1f}")
            
            if 'languages' in stats:
                lang_df = pd.DataFrame(
                    list(stats['languages'].items()),
                    columns=['Language', 'Chunks']
                )
                fig = px.bar(lang_df, x='Language', y='Chunks', title='Code Chunks by Language')
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("RAG system not available or not initialized")

def setup_page():
    """Setup page for configuration."""
    st.header("Setup & Configuration")
    
    # API Key Configuration
    st.subheader("API Key Setup")
    
    current_key = Config.get_groq_api_key()
    if current_key:
        st.success("Groq API key is configured")
        st.session_state.api_key_configured = True
    else:
        st.warning("No Groq API key found")
    
    new_key = st.text_input("Enter your Groq API key:", type="password", value=current_key or "")
    
    if st.button("Save API Key"):
        if new_key:
            # Save to environment
            os.environ['GROQ_API_KEY'] = new_key
            st.success("API key saved!")
            st.session_state.api_key_configured = True
            st.rerun()
        else:
            st.error("Please enter a valid API key")
    
    # Dependencies Check
    st.subheader("Dependencies Check")
    
    dependencies = {
        "langchain": "LangChain",
        "langchain_groq": "LangChain-Groq", 
        "git": "GitPython",
        "streamlit": "Streamlit"
    }
    
    missing_deps = []
    for module, name in dependencies.items():
        try:
            __import__(module)
            st.success(f"{name}")
        except ImportError:
            missing_deps.append(module)
            st.error(f"{name}")
    
    if missing_deps:
        st.warning(f"Missing dependencies: {', '.join(missing_deps)}")
        st.info("Run: pip install -r requirements.txt")
    else:
        st.success("All dependencies installed!")
        st.session_state.setup_complete = True

def info_page():
    """Codebase information page."""
    st.header("Codebase Information")
    
    st.subheader("Quick Analysis")
    analysis_type = st.radio("Analysis Type", ["Local Path", "GitHub Repository"])
    
    if analysis_type == "Local Path":
        path_input = st.text_input("Local Path", placeholder="./my-project")
        branch_input = None
    else:
        path_input = st.text_input("GitHub URL", placeholder="https://github.com/user/repo")
        branch_input = st.text_input("Branch (optional)", placeholder="main")
    
    if st.button("Get Information", type="primary"):
        if path_input:
            with st.spinner("Analyzing codebase structure..."):
                if analysis_type == "Local Path":
                    info_results = run_codebase_info(path_input)
                else:
                    # For GitHub repos, we need to clone first
                    st.info("GitHub repository analysis requires full analysis. Please use the Analyze page.")
                    return
            
            if 'error' in info_results:
                st.error(f"Error: {info_results['error']}")
            else:
                # Display information
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Total Files", info_results['total_files'])
                with col2:
                    st.metric("Total Size", f"{info_results['total_size_kb']:.1f} KB")
                with col3:
                    st.metric("Total Lines", f"{info_results['total_lines']:,}")
                
                # Language distribution
                st.subheader("Language Distribution")
                lang_df = pd.DataFrame(
                    list(info_results['languages'].items()),
                    columns=['Language', 'Files']
                )
                lang_df['Percentage'] = (lang_df['Files'] / info_results['total_files'] * 100).round(1)
                
                fig = px.pie(lang_df, values='Files', names='Language', title='Files by Language')
                st.plotly_chart(fig, use_container_width=True)
                
                # File list
                st.subheader("Files Found")
                files_df = pd.DataFrame(info_results['files'], columns=['File Path'])
                st.dataframe(files_df, use_container_width=True)
        else:
            st.error("Please enter a path or GitHub URL")

def analyze_page():
    """Main analysis page."""
    st.header("Code Analysis")
    
    # Analysis settings
    col1, col2 = st.columns(2)
    
    with col1:
        analysis_type = st.radio("Analysis Type", ["Local Path", "GitHub Repository"])
        
        if analysis_type == "Local Path":
            path_input = st.text_input("Local Path", placeholder="./my-project")
            branch_input = None
        else:
            path_input = st.text_input("GitHub URL", placeholder="https://github.com/user/repo")
            branch_input = st.text_input("Branch (optional)", placeholder="main")
    
    with col2:
        output_format = st.selectbox("Output Format", ["Console", "JSON", "Markdown"])
        interactive_mode = st.checkbox("Enable Interactive Mode", value=False)
    
    # Analysis button
    if st.button("Analyze Code", type="primary"):
        if path_input:
            with st.spinner("Analyzing code... This may take a few minutes."):
                results = run_analysis(path_input, branch_input)
                st.session_state.analysis_results = results
                
                if 'error' not in results:
                    st.session_state.analysis_history.append({
                        'timestamp': datetime.now(),
                        'path': path_input,
                        'total_issues': results.get('summary', {}).get('total_issues', 0),
                        'total_files': results.get('summary', {}).get('total_files', 0)
                    })
            
            st.rerun()
        else:
            st.error("Please enter a path or GitHub URL")
    
    # Display results
    if st.session_state.analysis_results:
        results = st.session_state.analysis_results
        
        if 'error' in results:
            st.error(f"Analysis failed: {results['error']}")
        else:
            # Tabs for different views
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Charts", "Details", "Chat", "RAG"])
            
            with tab1:
                st.header("Analysis Overview")
                create_overview_metrics(results)
                
                # Recommendations
                recommendations = results.get('recommendations', [])
                if recommendations:
                    st.subheader("Recommendations")
                    for i, rec in enumerate(recommendations, 1):
                        st.markdown(f"{i}. {rec}")
                
                # Quality trends
                if st.session_state.analysis_history:
                    st.subheader("Quality Trends")
                    df = pd.DataFrame(st.session_state.analysis_history)
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                    
                    fig = px.line(
                        df, 
                        x='timestamp', 
                        y='total_issues',
                        title='Code Quality Over Time',
                        markers=True
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            with tab2:
                st.header("Issue Distribution")
                
                col1, col2 = st.columns(2)
                with col1:
                    create_severity_chart(results.get('issues', []))
                with col2:
                    create_category_chart(results.get('issues', []))
            
            with tab3:
                st.header("Detailed Analysis")
                
                st.subheader("File Analysis")
                create_file_analysis_table(results)
                
                st.subheader("Top Issues")
                issues = results.get('issues', [])
                if issues:
                    for i, issue in enumerate(issues[:10], 1):
                        severity_icon = {
                            'critical': '[CRITICAL]', 'high': '[HIGH]', 'medium': '[MEDIUM]', 'low': '[LOW]', 'info': '[INFO]'
                        }.get(issue.get('severity', 'info'), '[UNKNOWN]')
                        
                        with st.expander(f"{severity_icon} {issue.get('title', 'Issue')} - {Path(issue.get('file_path', '')).name}:{issue.get('line_number', 'N/A')}"):
                            st.write(f"**Category:** {issue.get('category', 'unknown').title()}")
                            st.write(f"**Severity:** {issue.get('severity', 'info').title()}")
                            st.write(f"**Description:** {issue.get('description', 'No description available')}")
                            if issue.get('suggestion'):
                                st.write(f"**Suggestion:** {issue.get('suggestion')}")
                            if issue.get('code_snippet'):
                                st.code(issue.get('code_snippet'), language=issue.get('language', 'text'))
                else:
                    st.info("No issues found!")
            
            with tab4:
                create_chatbot_interface()
            
            with tab5:
                create_rag_stats()

def chat_page():
    """Enhanced chat page."""
    st.header("Enhanced Code Quality Chat")
    
    st.info("This version includes RAG and conversational features!")
    
    # Path input
    path_input = st.text_input("Enter path or GitHub URL to analyze", placeholder="https://github.com/user/repo")
    
    if st.button("Start Chat Session", type="primary"):
        if path_input:
            with st.spinner("Analyzing codebase..."):
                results = run_analysis(path_input)
                
                if 'error' in results:
                    st.error(f"Analysis failed: {results['error']}")
                else:
                    st.session_state.analysis_results = results
                    st.session_state.chatbot = None  # Reset chatbot
                    st.success("Analysis complete! You can now chat with your codebase.")
                    st.rerun()
        else:
            st.error("Please enter a path or GitHub URL")
    
    # Chat interface
    if st.session_state.analysis_results:
        create_chatbot_interface()

def main():
    """Main application."""
    initialize_session_state()
    
    st.markdown('<h1 class="main-header">Code Quality Intelligence Agent</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Home", "Setup", "Info", "Analyze", "Chat"]
    )
    
    # Clear results button
    if st.sidebar.button("Clear All Results"):
        st.session_state.analysis_results = None
        st.session_state.chat_history = []
        st.rerun()
    
    # Page routing
    if page == "Home":
        st.markdown("""
        ## Welcome to Code Quality Intelligence Agent
        
        This web application provides comprehensive code quality analysis using AI-powered insights.
        
        ### Features:
        - **Comprehensive Analysis**: Security, performance, complexity, and style issues
        - **GitHub Integration**: Analyze repositories directly from GitHub
        - **Conversational AI**: Chat about your code and get explanations
        - **RAG System**: Semantic search through large codebases
        - **Visual Reports**: Charts and graphs for easy understanding
        - **Multiple Output Formats**: Console, JSON, and Markdown reports
        
        ### Getting Started:
        1. Go to **Setup** to configure your Groq API key (optional for basic analysis)
        2. Use **Info** for quick codebase statistics
        3. Use **Analyze** for comprehensive code quality analysis
        4. Use **Chat** for interactive conversations about your code
        
        ### Supported Languages:
        Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala
        
        ### CLI Commands Available:
        - `analyze` - Full code analysis with multiple output formats
        - `setup` - Configure API keys and dependencies
        - `info` - Quick codebase information
        - `dashboard` - Launch this web interface
        - `chat` - Enhanced interactive chat session
        """)
        
    elif page == "Setup":
        setup_page()
        
    elif page == "Info":
        info_page()
        
    elif page == "Analyze":
        analyze_page()
        
    elif page == "Chat":
        chat_page()

if __name__ == "__main__":
    main()
