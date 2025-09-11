<div align="center">

<img src="https://github.com/user-attachments/assets/3fb55c0c-5fd0-471a-9753-6ba384243b2b" alt="Code Quality Intelligence Agent Logo" width="500"/>

<p align="center">
  <a href="https://pypi.org/project/code-quality-intelligence">📦 PyPI Package</a>
  &nbsp;|&nbsp;
  <a href="#-examples">💡 Examples</a>
  &nbsp;|&nbsp;
  <a href="https://github.com/YOUR_USERNAME/YOUR_REPOSITORY">⭐ Star Us</a>
</p>

</div>

## What is Code Quality Intelligence Agent?

Code Quality Intelligence Agent (CQI) is an AI-powered runtime for analyzing and improving code quality across large codebases. It combines static analysis, semantic search, and large language models to provide actionable insights for developers and teams.

With CQI, you can analyze local projects or GitHub repositories in seconds, detect vulnerabilities, measure complexity, and surface hidden patterns in your code. The system integrates Bandit, Radon, and Semgrep for static checks while enhancing results with deep AST parsing and AI-powered reasoning.

In a single command, you can run a full analysis and generate rich reports:

```bash
cqi analyze https://github.com/pallets/flask --format console
```

Or switch to interactive mode for real-time, context-aware AI chat about your codebase:

```bash
cqi analyze sample_code --interactive
```

But the real advantage of CQI is its architecture:

* **AI-Augmented Static Analysis**: Traditional tools enriched with LLM insights for deeper coverage.
* **Enterprise-Ready RAG System**: Semantic search over code with persistent vector databases for fast retrieval.
* **Multi-Format Reports**: Console, JSON, and Markdown outputs for both humans and CI/CD pipelines.
* **Web Dashboard**: A professional Streamlit-based interface with charts, metrics, and interactive visualizations.
* **Privacy First**: Your code never leaves your system—analysis runs locally with your own API key.

For organizations and developers, CQI provides a complete solution: a fast CLI for everyday use, a professional web UI for visualization, and extensibility to plug in new models, embeddings, or workflows.
Unlike conventional static analysis, CQI brings a novel AI-driven architecture: it merges rule-based detection with semantic understanding, giving teams a powerful assistant that doesn’t just detect issues—it explains them.


## Table of Contents

## Table of Contents

- [Project Overview and Architecture](#project-overview-and-architecture)
  - [Core Components and Their Interactions](#core-components-and-their-interactions)
    - [CodeQualityAgent - The Central Orchestrator](#1-codequalityagent---the-central-orchestrator)
    - [CodeAnalyzer - Multi-Language Static Analysis Engine](#2-codeanalyzer---multi-language-static-analysis-engine)
    - [CodeRAGSystem - Semantic Search and Context Retrieval](#3-coderagsystem---semantic-search-and-context-retrieval)
    - [CodeQualityChatbot - Conversational AI Interface](#4-codequalitychatbot---conversational-ai-interface)
    - [FileHandler - Repository and File Management](#5-filehandler---repository-and-file-management)
    - [ReportGenerator - Multi-Format Output System](#6-reportgenerator---multi-format-output-system)
    - [Web Interface - Professional Dashboard](#7-web-interface---professional-dashboard)
  - [Analysis Pipeline and Workflow](#analysis-pipeline-and-workflow)
  - [AI Integration and Language Model Usage](#ai-integration-and-language-model-usage)
  - [RAG System Implementation Details](#rag-system-implementation-details)
  - [Chunking Strategy for Large Files](#chunking-strategy-for-large-files)
  - [Error Handling and Resilience](#error-handling-and-resilience)
  - [Performance Optimization and Scalability](#performance-optimization-and-scalability)
  - [Integration Capabilities and Extensibility](#integration-capabilities-and-extensibility)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands Reference](#commands-reference)
- [Web Interface](#web-interface)
- [API Reference](#api-reference)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)



## Project Overview and Architecture

The Code Quality Intelligence Agent is a sophisticated software analysis system that combines traditional static analysis techniques with modern artificial intelligence capabilities to provide comprehensive code quality assessment. This enterprise-grade tool represents a convergence of multiple technologies including language models, vector databases, static analysis tools, and web interfaces to create a unified platform for code quality evaluation.

The project architecture follows a modular design pattern with clear separation of concerns, allowing each component to operate independently while contributing to the overall analysis pipeline. At its core, the system operates on a multi-stage analysis process that begins with file discovery and language detection, progresses through static analysis and AI-powered evaluation, and culminates in comprehensive reporting and interactive discussion capabilities.

## Core Components and Their Interactions

### 1. CodeQualityAgent - The Central Orchestrator

The CodeQualityAgent class serves as the primary coordinator for the entire analysis pipeline. This component initializes and manages all other subsystems, including the language model interface, static analysis tools, RAG system, and report generation capabilities. The agent implements an asynchronous analysis workflow that can handle both individual files and entire codebases, including remote GitHub repositories.

The agent's initialization process involves several critical steps: first, it validates the configuration to ensure all necessary API keys and dependencies are available; second, it establishes connections to the Groq API for language model inference using the deepseek-r1-distill-llama-70b model; third, it initializes the conversation memory system for maintaining context across interactions; and finally, it sets up the analysis and question-answering chains using LangChain's prompt templates and output parsers.

The analysis workflow implemented by the agent follows a sophisticated pipeline that begins with input validation and file discovery, progresses through language detection and content extraction, continues with both static and AI-powered analysis, and concludes with result aggregation and report generation. For large codebases, the agent implements an intelligent chunking mechanism that divides large files into manageable segments while preserving code structure and context boundaries.

### 2. CodeAnalyzer - Multi-Language Static Analysis Engine

The CodeAnalyzer component represents the traditional static analysis foundation of the system. This component integrates multiple industry-standard tools including Bandit for security analysis, Radon for complexity metrics, and Semgrep for pattern matching. The analyzer supports thirteen programming languages and implements language-specific analysis strategies to ensure accurate and relevant findings.

The analyzer's architecture includes several specialized analysis methods for different language categories. For Python files, it performs AST parsing to understand code structure, runs Bandit security scans to identify potential vulnerabilities, calculates complexity metrics using Radon, and applies pattern-based rules through Semgrep. JavaScript and TypeScript files undergo similar analysis with language-appropriate tools and techniques, while other supported languages receive pattern-based analysis and heuristic evaluation.

The analyzer also implements a sophisticated duplication detection system that creates fingerprints of code blocks to identify potential duplication across files. This system uses hash-based comparison of normalized code structures to identify similar patterns while accounting for minor variations in formatting and naming conventions.

### 3. CodeRAGSystem - Semantic Search and Context Retrieval

The RAG (Retrieval-Augmented Generation) system represents one of the most sophisticated components of the project, implementing a multi-tiered approach to semantic code search and context retrieval. The system supports three different implementation strategies with automatic fallback capabilities: ChromaDB with sentence transformers for full vector database functionality, FAISS with custom embeddings for efficient similarity search, and a simple keyword-based system for basic context retrieval.

The primary RAG implementation using ChromaDB leverages sentence transformers to create high-quality embeddings of code chunks, storing them in a persistent vector database that supports efficient similarity search and retrieval. When ChromaDB is unavailable due to system constraints or missing dependencies, the system automatically falls back to a FAISS-based implementation that uses custom feature extraction optimized specifically for code analysis.

The custom embedding strategy implemented in the FAISS fallback creates 512-dimensional feature vectors that capture code-specific patterns including function and class definitions, import statements, security-related patterns, complexity indicators, and vocabulary-based semantic features. This approach ensures that even without full transformer-based embeddings, the system can still provide meaningful semantic search capabilities.

The RAG system implements intelligent chunking strategies that respect code structure boundaries, ensuring that functions, classes, and other logical units remain intact within chunks. The chunking process uses recursive character splitting with code-aware separators and implements overlap between chunks to maintain context continuity.

### 4. CodeQualityChatbot - Conversational AI Interface

The chatbot component provides an enhanced conversational interface that supports natural language interactions about code quality findings. This component maintains conversation history and context awareness, enabling users to ask follow-up questions and engage in detailed discussions about their codebase.

The chatbot integrates closely with the RAG system to provide context-aware responses that reference specific code examples and analysis results. It maintains a conversation buffer that preserves the last ten exchanges, ensuring continuity across interactions while managing memory usage effectively. The chatbot's personality is designed to be friendly and approachable while maintaining technical accuracy and providing actionable advice.

The conversation management system implements sophisticated prompt engineering that includes system prompts for personality and behavior, context injection for analysis results and RAG-retrieved information, and conversation history integration for maintaining dialogue continuity. The chatbot can explain technical concepts in accessible language, provide step-by-step solutions, and suggest best practices based on industry standards.

### 5. FileHandler - Repository and File Management

The FileHandler component manages all file operations including local file discovery, GitHub repository cloning, and language detection. This component implements sophisticated logic for handling different input types, from individual files to entire directory structures to remote GitHub repositories with branch support.

The GitHub integration capability allows the system to analyze remote repositories by cloning them to temporary directories and extracting supported code files. The handler supports branch-specific analysis and implements intelligent cleanup mechanisms to manage temporary files and directories created during the analysis process.

Language detection is performed through a combination of file extension analysis and content inspection, ensuring accurate identification of programming languages even in cases where file extensions might be ambiguous or non-standard. The handler maintains a comprehensive mapping of file extensions to programming languages and implements fallback strategies for edge cases.

### 6. ReportGenerator - Multi-Format Output System

The report generation system supports three distinct output formats: rich console output with color coding and formatted tables, structured JSON for integration with other tools and systems, and human-readable Markdown for documentation purposes. Each format is optimized for its intended use case while maintaining consistency in the underlying data structure.

The console output leverages the Rich library to create visually appealing terminal reports with color-coded severity indicators, formatted tables for issue listings, and structured sections for different analysis categories. The JSON output provides a complete data structure that includes all analysis results, metrics, and metadata in a format suitable for programmatic consumption. The Markdown output creates readable documentation that can be integrated into project repositories or shared with team members.

### 7. Web Interface - Professional Dashboard

The web interface represents a comprehensive Streamlit-based dashboard that provides all CLI functionality through a professional, enterprise-suitable web application. The interface is designed without emojis to maintain a professional appearance suitable for corporate environments while providing rich visualizations and interactive features.

The web application implements a multi-page navigation structure with five distinct pages: Home for feature overview and getting started information, Setup for API key configuration and system validation, Info for quick codebase statistics, Analyze for full code quality analysis with visual reports, and Chat for enhanced conversational AI interactions.

The interface includes sophisticated caching mechanisms to optimize performance, real-time progress updates during analysis operations, and interactive visualizations using Plotly for charts and graphs. The application supports both local file analysis and GitHub repository analysis with the same functionality available through the command-line interface.

## Analysis Pipeline and Workflow

The analysis pipeline represents the core workflow that transforms raw code input into comprehensive quality assessments and actionable insights. This pipeline operates through several distinct phases, each building upon the results of previous stages to create a complete picture of code quality.

The pipeline begins with input validation and preprocessing, where the system determines the input type (local file, directory, or GitHub repository), validates accessibility and permissions, and prepares the working environment. For GitHub repositories, this phase includes cloning operations with branch-specific checkout and temporary directory management.

File discovery and language detection follow, where the system recursively searches for supported code files, applies file size and type filters, and performs language identification for each discovered file. This phase creates the inventory of files that will undergo analysis and establishes the language-specific analysis strategies that will be applied.

The core analysis phase operates on each file individually, applying both static analysis tools and AI-powered evaluation. Static analysis includes security scanning with Bandit, complexity measurement with Radon, pattern matching with Semgrep, and AST-based structural analysis. AI analysis involves content preparation and prompt engineering, language model inference through the Groq API, response parsing and validation, and result normalization and integration.

For large files that exceed the configured size limit, the system implements an intelligent chunking mechanism that divides the content into manageable segments while preserving code structure boundaries. Each chunk undergoes individual analysis, and the results are merged using additional language model calls to create comprehensive summaries and eliminate duplicate findings.

Result aggregation and processing combine findings from all analyzed files, identify cross-file patterns and duplication, calculate overall metrics and scores, and generate high-level recommendations based on the discovered patterns. The aggregation process also prepares data structures for different output formats and initializes the RAG system with analysis results for enhanced question-answering capabilities.

## AI Integration and Language Model Usage

The system's AI integration centers around the Groq API and the deepseek-r1-distill-llama-70b model, chosen for its balance of performance, accuracy, and cost-effectiveness for code analysis tasks. The integration implements sophisticated prompt engineering strategies that guide the language model to produce structured, consistent outputs suitable for programmatic processing.

The analysis prompt template instructs the model to act as an expert code quality analyst and return strict JSON responses containing issues arrays with detailed information including category, severity, line numbers, descriptions, and suggestions. The prompt also requests metrics objects with complexity, maintainability, security, and overall scores, along with summary strings that provide human-readable analysis overviews.

The question-answering prompt template creates a helpful code quality assistant personality that provides conversational responses referencing specific analysis findings and context information retrieved through the RAG system. This dual-prompt strategy enables the system to maintain consistency in analysis while providing flexible, natural language interaction capabilities.

Error handling and fallback mechanisms ensure robust operation even when the AI service is unavailable or returns unexpected responses. The system implements retry logic for transient failures, response validation and parsing with graceful degradation, and heuristic-based responses when AI analysis is completely unavailable.

## RAG System Implementation Details

The RAG system implementation represents one of the most technically sophisticated aspects of the project, providing semantic search capabilities that enhance both analysis quality and user interaction experiences. The system's multi-tiered architecture ensures broad compatibility while optimizing performance based on available resources and dependencies.

The primary ChromaDB implementation leverages sentence transformers to create high-quality vector embeddings of code chunks. The system uses the all-MiniLM-L6-v2 model for embedding generation, chosen for its balance of quality and computational efficiency. Code chunks are processed through recursive character splitting with code-aware separators that respect function and class boundaries, ensuring that semantic units remain intact within individual chunks.

The FAISS fallback implementation creates custom 512-dimensional feature vectors through a sophisticated feature extraction process. This process identifies function and class definition patterns using regular expressions, analyzes import statements and dependencies, detects security-related patterns including dangerous function calls, measures complexity indicators through loop and conditional counting, and builds vocabulary-based features using term frequency analysis.

The simple RAG fallback provides basic keyword-based search capabilities when neither ChromaDB nor FAISS is available, ensuring that the system maintains some level of context retrieval functionality regardless of the deployment environment. This implementation uses text similarity metrics and keyword matching to identify relevant code chunks based on user queries.

Persistence mechanisms ensure that vector databases are saved and reloaded efficiently, reducing initialization time for subsequent analysis operations on the same codebase. The system implements intelligent cache invalidation based on file modification times and content hashes to ensure that outdated embeddings are refreshed when code changes.

## Chunking Strategy for Large Files

The chunking implementation addresses one of the significant challenges in code analysis: handling large files that exceed memory or processing limits while maintaining code structure integrity and analysis quality. The system implements a sophisticated chunking strategy that considers both technical constraints and code semantics.

The chunking process begins with size calculation and boundary determination, where the system calculates appropriate chunk sizes based on configured limits, determines overlap requirements to maintain context continuity, and identifies natural breaking points in the code structure. For Python files, the system looks for function and class boundaries, while JavaScript and TypeScript files are split at function and object boundaries.

Chunk creation involves content division with structure preservation, line number tracking for accurate issue reporting, and overlap management to ensure context continuity between adjacent chunks. Each chunk maintains metadata including its position within the original file, size information, and relationship to other chunks.

Individual chunk analysis applies the same analysis pipeline used for regular files, with modifications to handle the chunk context and adjust line numbers appropriately. Each chunk receives both static analysis (where applicable) and AI-powered evaluation, with results tagged to indicate their chunk origin.

The merging process represents a sophisticated application of language model capabilities, where the system uses AI to synthesize chunk-level findings into comprehensive file-level summaries. The merging prompt instructs the model to analyze chunk summaries, identify patterns and relationships across chunks, eliminate duplicate findings, and create cohesive overall assessments that maintain accuracy while providing actionable insights.

## Error Handling and Resilience

The system implements comprehensive error handling and resilience mechanisms to ensure reliable operation across diverse environments and conditions. These mechanisms operate at multiple levels, from individual component failures to system-wide service outages.

Component-level error handling includes API failure recovery with retry logic and exponential backoff, dependency missing graceful degradation to alternative implementations, file access error management with clear user feedback, and parsing error recovery with fallback to heuristic analysis.

System-level resilience mechanisms include configuration validation with helpful error messages, resource management with automatic cleanup of temporary files, memory usage optimization to prevent system overload, and network connectivity handling for GitHub repository access and API calls.

The fallback hierarchy ensures that the system remains functional even when preferred components are unavailable. For RAG functionality, the system falls back from ChromaDB to FAISS to simple keyword search. For AI analysis, the system falls back from full LLM analysis to static analysis only. For web interface functionality, the system provides alternative launch methods and clear troubleshooting guidance.

## Performance Optimization and Scalability

Performance optimization permeates every aspect of the system design, from efficient file processing to intelligent caching strategies. The system implements several key optimization strategies that ensure responsive performance across different scales of analysis.

File processing optimization includes intelligent file filtering to skip unsupported or oversized files, parallel processing capabilities for analyzing multiple files concurrently, and memory management strategies that prevent resource exhaustion during large codebase analysis.

Caching mechanisms operate at multiple levels: RAG embeddings are cached and reused across analysis sessions, analysis results are cached to avoid redundant processing, and web interface components implement session-based caching for improved user experience.

The chunking mechanism itself serves as a scalability feature, enabling analysis of arbitrarily large files by dividing them into manageable segments. This approach ensures that the system can handle enterprise-scale codebases without running into memory or processing limitations.

Network optimization includes efficient GitHub repository cloning with shallow clone options where appropriate, API request batching to minimize network overhead, and intelligent retry mechanisms that balance reliability with performance.

## Integration Capabilities and Extensibility

The system is designed with integration and extensibility as core principles, enabling seamless incorporation into existing development workflows and easy extension with additional analysis capabilities. The modular architecture facilitates both horizontal and vertical scaling of functionality.

CLI integration supports standard Unix pipeline operations, exit codes for CI/CD integration, and multiple output formats for different consumption scenarios. The JSON output format provides complete analysis results in a structured format suitable for processing by other tools, while the Markdown format enables integration into documentation workflows.

The web interface provides REST-like functionality through Streamlit's architecture, enabling programmatic access to analysis capabilities through web requests. Session management capabilities support concurrent users and persistent analysis sessions.

API integration capabilities include webhook support for automated analysis triggers, configuration management for different environments, and authentication mechanisms for secure access in enterprise environments.

Extension points throughout the system enable addition of new language analyzers, custom analysis rules, alternative AI model integrations, and additional output formats. The plugin architecture supports dynamic loading of extensions without requiring core system modifications.

This comprehensive architecture creates a robust, scalable, and extensible platform for code quality analysis that combines the best aspects of traditional static analysis with modern AI capabilities, wrapped in user-friendly interfaces suitable for both individual developers and enterprise teams.


### Key Capabilities

- Multi-language code analysis (13+ programming languages)
- AI-powered insights using Groq's high-performance LLM inference
- RAG (Retrieval-Augmented Generation) system for semantic code search
- GitHub repository analysis with branch support
- Interactive conversational AI chatbot
- Multiple output formats (Console, JSON, Markdown)
- Professional web interface with Streamlit
- Comprehensive static analysis integration

## Features

### Analysis Engine
- **Multi-language Support**: Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala
- **Static Analysis Integration**: Bandit for security, Radon for complexity, Semgrep for patterns
- **AST Parsing**: Deep structural analysis of code syntax and semantics
- **Pattern Recognition**: Security vulnerabilities, performance bottlenecks, maintainability issues

### AI Integration
- **Language Model**: Groq API integration with LangChain framework
- **Model Used**: deepseek-r1-distill-llama-70b for code analysis and conversation
- **Conversation Management**: Context-aware dialogue with memory persistence
- **Fallback System**: Heuristic responses when API unavailable

### RAG System Implementation
- **Vector Database**: FAISS for efficient similarity search with ChromaDB fallback
- **Embedding Strategy**: Custom feature extraction optimized for code analysis
- **Feature Dimensions**: 512-dimensional vectors capturing code patterns and semantics
- **Code-Specific Features**:
  - Function and class detection patterns
  - Import statement analysis
  - Security pattern recognition (eval, pickle, SQL injection)
  - Complexity indicators (loops, conditionals, nesting)
  - Vocabulary-based semantic features
- **Text Chunking**: Recursive character splitting optimized for code structure
- **Persistence**: Automatic index saving and loading for performance

### Report Generation
- **Console Output**: Rich formatted terminal reports with color coding and tables
- **JSON Export**: Structured data format for integration with other tools
- **Markdown Export**: Human-readable reports for documentation
- **Interactive Mode**: Real-time Q&A interface with code context

## Architecture

### Core Components

1. **CodeQualityAgent**: Main orchestrator that coordinates analysis pipeline
2. **CodeAnalyzer**: Multi-language static analysis engine with tool integration
3. **CodeRAGSystem**: Semantic search and context retrieval system
4. **CodeQualityChatbot**: Conversational AI interface with memory
5. **ReportGenerator**: Multi-format report generation engine
6. **FileHandler**: File operations and GitHub repository management
7. **Web Interface**: Professional Streamlit-based dashboard

### Analysis Pipeline

1. **Input Validation**: Path verification and file type detection
2. **Language Detection**: Automatic programming language identification
3. **Content Extraction**: UTF-8 encoding with error handling
4. **Static Analysis**: Integration with Bandit, Radon, and Semgrep
5. **AI Enhancement**: LLM-powered analysis with RAG context
6. **Report Generation**: Multi-format output with rich formatting

## Installation

### Prerequisites

- Python 3.8 or higher
- Git (for GitHub repository analysis)
- Groq API key (obtain from console.groq.com)

### Quick Installation

```bash
# Install the package
pip install code-quality-intelligence

# Install with all optional dependencies
pip install code-quality-intelligence[full,rag]
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/suvraadeep/Code-Quality-Intelligence-Agent.git
cd Code-Quality-Intelligence-Agent

# Install core dependencies
pip install -r requirements.txt

# Install as editable package
pip install -e .

# Build and install package
python setup.py sdist bdist_wheel
pip install dist/code_quality_intelligence-1.6.1-py3-none-any.whl
```

### Optional Dependencies

```bash
# For web interface
pip install streamlit==1.31.0 pandas==2.2.0 plotly==5.19.0

# For advanced RAG features
pip install chromadb==0.4.22 sentence-transformers==2.2.2 faiss-cpu==1.8.0

# For development
pip install pytest black flake8 mypy
```

## Configuration

### API Key Setup

#### Method 1: Environment Variable
```bash
export GROQ_API_KEY=your_api_key_here
```

#### Method 2: .env File
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

#### Method 3: CLI Parameter
```bash
cqi analyze /path/to/code --groq-key your_api_key_here
```

#### Method 4: Setup Wizard
```bash
cqi setup
```

### System Validation

```bash
# Validate complete system functionality
python validation.py

# Test RAG system specifically
python -c "from code_quality_agent.rag_system import CodeRAGSystem; rag = CodeRAGSystem(); print('RAG Available:', rag.is_available())"
```

## Usage

### Basic Analysis

#### Local File Analysis
```bash
# Analyze single file
cqi analyze sample_code/module_a.py --format console

# Analyze directory
cqi analyze sample_code --format console

# Get codebase statistics
cqi info sample_code
```

#### GitHub Repository Analysis
```bash
# Analyze public repository
cqi analyze https://github.com/pallets/flask --format console

# Analyze specific branch
cqi analyze https://github.com/user/repo --branch develop

# Analyze with interactive chat
cqi analyze https://github.com/user/repo --interactive
```

### Report Generation

#### Export Formats
```bash
# Generate JSON report
cqi analyze sample_code --format json --output analysis_report.json

# Generate Markdown report
cqi analyze sample_code --format markdown --output analysis_report.md

# Console output (default)
cqi analyze sample_code --format console
```

### Interactive Features

#### AI-Powered Chat
```bash
# Interactive analysis with RAG-enhanced responses
cqi analyze sample_code --interactive

# Dedicated chat session
cqi chat

# Chat with GitHub repository context
cqi analyze https://github.com/user/repo --interactive
```

### Web Interface

#### Launch Web Dashboard
```bash
# Quick launch (recommended)
cqi --web

# Alternative launch methods
python cqi-web.py
python Webpage/launch.py
cd Webpage && streamlit run app.py
```

### Advanced Options

#### Customization
```bash
# Override API key
python cqi.py analyze code --groq-key custom_api_key

# Branch-specific analysis
python cqi.py analyze https://github.com/user/repo --branch feature-branch

# Combined options
python cqi.py analyze https://github.com/user/repo --format json --output github_analysis.json --interactive --branch main
```

### Package Execution Methods

#### As Python Module
```bash
# Version information
python -m code_quality_agent --version

# Help documentation
python -m code_quality_agent --help

# Analysis execution
python -m code_quality_agent analyze sample_code --format console

# Interactive mode
python -m code_quality_agent analyze sample_code --interactive
```

#### As Entry Point Script
```bash
# Version information
python cqi.py --version

# Help documentation
python cqi.py --help

# Analysis execution
python cqi.py analyze sample_code --format console

# Interactive mode
python cqi.py analyze sample_code --interactive
```

### Web Interfaces

#### Dashboard Access
```bash
# Simple HTML dashboard (no dependencies)
python simple_dashboard.py
# Access at: http://localhost:8080

# Advanced Streamlit dashboard
streamlit run streamlit_app.py
# Access at: http://localhost:8501

# Launch via CLI
python cqi.py dashboard
```

#### Professional Web Interface
```bash
# Quick launch - single command from anywhere
python cqi-web.py

# Windows batch file
cqi-web.bat

# Direct Streamlit launch
cd Webpage && streamlit run app.py
# Access at: http://localhost:8501
```

**Web Interface Architecture:**
- **Main Application**: `Webpage/app.py` - Complete Streamlit web application
- **Configuration**: `Webpage/config.py` - Centralized settings and constants
- **Launcher Scripts**: Multiple launch options for different platforms
- **Testing Suite**: `Webpage/test_app.py` - Comprehensive functionality tests
- **Dependencies**: `Webpage/requirements.txt` - All required packages

**Core Features:**
- **Professional UI**: Clean, emoji-free interface suitable for enterprise use
- **Complete CLI Parity**: All command-line functionality accessible through web interface
- **Real-time Analysis**: Live progress updates with visual feedback
- **Interactive Visualizations**: Charts, graphs, and data tables using Plotly
- **Multi-page Navigation**: 5 distinct pages (Home, Setup, Info, Analyze, Chat)
- **RAG System Integration**: AI-powered code discussions with semantic search
- **GitHub Integration**: Direct repository analysis and cloning
- **Local File Support**: Comprehensive local codebase analysis

**Page-Specific Functionality:**

**Home Page:**
- Welcome screen with feature overview
- Getting started guide and supported languages
- CLI commands reference and feature comparison

**Setup Page:**
- Groq API key configuration and validation
- System dependency checking and status
- Environment setup and troubleshooting

**Info Page:**
- Quick codebase statistics without full analysis
- Language distribution analysis and file counts
- File size and structure information

**Analyze Page:**
- Full code quality analysis with multiple output formats
- Interactive mode with real-time progress
- Visual reports with severity and category charts
- File analysis table with highlighting
- Support for both local paths and GitHub repositories

**Chat Page:**
- Enhanced conversational AI with RAG capabilities
- Context-aware responses based on codebase analysis
- Interactive chat interface with conversation history
- Code-specific question answering

**Technical Implementation:**
- **Session Management**: Persistent state across page navigation
- **Caching System**: Optimized performance with result caching
- **Error Handling**: Graceful error management with user feedback
- **Responsive Design**: Wide layout optimized for data visualization
- **Modular Architecture**: Separate functions for each component
- **Configuration Management**: Centralized settings and constants

**Supported Analysis Types:**
- Local file and directory analysis
- GitHub repository analysis with branch support
- Multiple output formats (Console, JSON, Markdown)
- Interactive chat sessions
- RAG-enhanced code discussions

**Dependencies:**
- Core: `code-quality-intelligence>=1.0.1`
- Web Framework: `streamlit>=1.31.0`, `streamlit-chat>=0.1.1`
- Data Processing: `pandas>=2.2.0`, `plotly>=5.19.0`, `numpy>=1.24.0`
- AI/ML: `langchain>=0.2.16`, `sentence-transformers>=2.2.2`, `chromadb>=0.4.22`
- Visualization: `matplotlib>=3.8.4`, `seaborn>=0.13.2`, `altair>=5.2.0`
- Code Analysis: `bandit>=1.7.5`, `radon>=6.0.1`, `semgrep>=1.45.0`

**Web Interface File Structure:**
```
Webpage/
├── app.py                 # Main Streamlit application (689 lines)
├── config.py              # Configuration and constants
├── requirements.txt        # Web interface dependencies
├── launch.py              # Local launcher with dependency checking
├── test_app.py            # Comprehensive functionality tests
├── README.md              # Web interface documentation
├── QUICK_START.md         # Quick start guide
├── cqi-web                # Unix launcher script
├── cqi-web.bat            # Windows batch launcher
├── launch.bat             # Windows batch file
├── launch.sh              # Unix shell script
├── components/            # Reusable UI components (empty)
├── pages/                 # Additional pages (empty)
├── static/                # Static assets (empty)
└── simple_embeddings_db/  # RAG system database
```

**Key Functions in app.py:**
- `initialize_session_state()` - Session management
- `run_analysis()` - Core analysis execution with caching
- `run_codebase_info()` - Quick statistics without full analysis
- `create_overview_metrics()` - Metrics display with professional styling
- `create_severity_chart()` - Issue severity visualization
- `create_category_chart()` - Issue category distribution
- `create_file_analysis_table()` - Detailed file analysis with highlighting
- `create_chatbot_interface()` - AI chat functionality
- `create_rag_stats()` - RAG system statistics and management
- `setup_page()` - Configuration and dependency checking
- `info_page()` - Quick codebase information
- `analyze_page()` - Full analysis interface
- `chat_page()` - Enhanced chat interface

**Configuration Options (config.py):**
- **Application Settings**: Title, icon, layout configuration
- **Server Settings**: Host, port, and network configuration
- **Supported Languages**: 13 programming languages with detection
- **Output Formats**: Console, JSON, Markdown support
- **Analysis Types**: Local Path and GitHub Repository
- **Chart Colors**: Professional color scheme for severity levels
- **Page Configuration**: Navigation structure and page definitions
- **Default Settings**: Analysis type, output format, interactive mode
- **API Configuration**: Groq API key environment variable and timeouts
- **File Limits**: Maximum file size and total size constraints
- **Cache Settings**: TTL and caching enablement
- **Logging**: Log level and format configuration

**Professional Design Features:**
- **Emoji-Free Interface**: Clean, enterprise-suitable design
- **Text-Based Severity Indicators**: [CRITICAL], [HIGH], [MEDIUM], [LOW], [INFO]
- **Professional Color Scheme**: Consistent color coding for severity levels
- **Responsive Layout**: Wide layout optimized for data visualization
- **Custom CSS Styling**: Professional header, metric cards, and chat messages
- **Clean Navigation**: Simple page names without emoji clutter

**Web Interface Troubleshooting:**

**Common Issues and Solutions:**
1. **Import Errors**: Ensure main package is installed
   ```bash
   pip install code-quality-intelligence
   ```

2. **Missing Dependencies**: Install web interface requirements
   ```bash
   cd Webpage && pip install -r requirements.txt
   ```

3. **Port Conflicts**: Change port if 8501 is occupied
   ```bash
   streamlit run app.py --server.port 8502
   ```

4. **Analysis Failures**: Check file paths and permissions
   - Verify target directory contains supported code files
   - Ensure proper read permissions for local files
   - Check GitHub repository URL format

5. **API Key Issues**: Configure through Setup page
   - Go to Setup page in web interface
   - Enter valid Groq API key
   - Check environment variable configuration

6. **RAG System Problems**: Check database and dependencies
   - Verify ChromaDB installation
   - Check sentence-transformers availability
   - Review RAG statistics in Chat page

**Testing and Validation:**
```bash
# Test web interface functionality
cd Webpage && python test_app.py

# Check specific components
cd Webpage && python -c "from app import *; print('All imports successful')"

# Validate configuration
cd Webpage && python -c "from config import *; print('Configuration loaded')"
```

**Performance Optimization:**
- **Caching**: Results are cached for 1 hour by default
- **File Limits**: Maximum 10MB per file, 100MB total
- **Session Management**: State persists across page navigation
- **Lazy Loading**: Components load only when needed

## Technical Implementation

### RAG System Details

The Retrieval-Augmented Generation system implements semantic search capabilities for enhanced code analysis and conversational AI responses.

#### Embedding Implementation
- **Vector Database**: FAISS IndexFlatIP for cosine similarity search
- **Feature Extraction**: Custom 512-dimensional feature vectors
- **Code Patterns**: Function definitions, class structures, import statements
- **Security Patterns**: eval usage, pickle operations, SQL injection indicators
- **Vocabulary Building**: Dynamic term frequency analysis
- **Chunking Strategy**: Recursive character splitting with code-aware separators

#### Fallback Hierarchy
1. **ChromaDB**: Full vector database with sentence transformers (requires C++ build tools)
2. **Simple Embedding RAG**: FAISS-based semantic search with custom features
3. **Simple RAG**: Keyword-based matching and text search
4. **No RAG**: Basic analysis without enhanced context

### Analysis Pipeline

#### File Processing
1. **Input Validation**: Path verification and file type detection
2. **Language Detection**: Automatic programming language identification
3. **Content Extraction**: UTF-8 encoding with error handling
4. **Chunking**: Code-aware text splitting for optimal analysis

#### Quality Assessment
1. **Security Analysis**: Bandit integration for vulnerability detection
2. **Complexity Metrics**: Radon integration for cyclomatic complexity
3. **Pattern Matching**: Semgrep rules for best practice violations
4. **Duplication Detection**: Cross-file similarity analysis

#### AI Enhancement
1. **Context Preparation**: RAG system provides relevant code chunks
2. **LLM Processing**: Groq API analysis with conversation memory
3. **Response Generation**: Contextual insights with actionable recommendations
4. **Follow-up Support**: Conversation continuation with maintained context

## Supported Analysis Categories

### Security Assessment
- SQL injection vulnerabilities
- Cross-site scripting risks
- Unsafe deserialization patterns
- Hardcoded credentials detection
- Command injection vulnerabilities

### Performance Analysis
- Algorithmic complexity assessment
- Memory usage patterns
- Database query optimization
- Loop efficiency analysis
- Resource leak detection

### Code Quality Metrics
- Cyclomatic complexity measurement
- Maintainability index calculation
- Code duplication identification
- Documentation coverage assessment
- Naming convention compliance

### Best Practice Validation
- Error handling patterns
- Design pattern implementation
- Testing coverage gaps
- API design principles
- Security best practices

## Integration Examples

### CI/CD Pipeline Integration
```yaml
name: Code Quality Assessment
on: [push, pull_request]

jobs:
  quality_check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Code Quality Agent
        run: pip install code-quality-intelligence
      - name: Run Analysis
        run: cqi analyze . --format json --output quality_report.json
        env:
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: quality-report
          path: quality_report.json
```

### Pre-commit Hook
```bash
#!/bin/bash
# .git/hooks/pre-commit
python cqi.py analyze $(git diff --cached --name-only --diff-filter=ACM)
```

## Performance Characteristics

### Execution Metrics
- **Local Analysis**: Instant results for codebases under 100 files
- **GitHub Analysis**: 2-3 minutes for repositories with 100+ files
- **RAG Indexing**: 0.5-2 seconds per code chunk
- **Embedding Generation**: 50-100ms per code chunk
- **AI Response Time**: 2-5 seconds (depending on API latency)

### Scalability
- **File Limit**: Automatically handles up to 100 files per analysis
- **Size Limit**: Files larger than 1MB are skipped for performance
- **Memory Usage**: Optimized for systems with 4GB+ RAM
- **Concurrent Processing**: Parallel analysis of multiple files

## Error Handling

### Graceful Degradation
- **API Unavailable**: Falls back to heuristic responses
- **RAG Disabled**: Continues with basic analysis
- **Network Issues**: Local analysis remains functional
- **Invalid Paths**: Clear error messages with suggestions

### Troubleshooting

#### Common Issues
**"GROQ_API_KEY not found"**
- Solution: Set environment variable or use --groq-key parameter
- Command: `python cqi.py setup`

**"No supported files found"**
- Solution: Verify file extensions and path correctness
- Command: `python cqi.py info /path/to/code`

**"RAG system not available"**
- Solution: Install optional dependencies or use without RAG
- Command: `pip install faiss-cpu sentence-transformers`

**"GitHub cloning failed"**
- Solution: Verify Git installation and repository access
- Command: Ensure Git is in system PATH

## Development and Customization

### Extending Analysis Rules
The system supports custom analysis rules through the LangChain integration:

```python
# Custom analyzer implementation
from code_quality_agent.analyzers import CodeAnalyzer

class CustomAnalyzer(CodeAnalyzer):
    def analyze_custom_patterns(self, content: str) -> List[Dict]:
        # Implement custom analysis logic
        pass
```

### Adding Language Support
```python
# Language-specific analyzer
def analyze_rust_file(self, file_path: Path) -> Dict[str, Any]:
    # Implement Rust-specific analysis
    return {
        'language': 'rust',
        'issues': [],
        'complexity': {}
    }
```

## API Reference

### Core Classes
- `CodeQualityAgent`: Main analysis orchestrator
- `CodeAnalyzer`: Multi-language static analysis engine
- `CodeRAGSystem`: Semantic search and context retrieval
- `CodeQualityChatbot`: Conversational AI interface
- `ReportGenerator`: Multi-format report generation

### Configuration
- `Config.DEFAULT_MODEL`: LLM model selection
- `Config.MAX_FILE_SIZE`: File size limit (1MB default)
- `Config.SUPPORTED_EXTENSIONS`: Supported file types
- `Config.QUALITY_CATEGORIES`: Analysis categories

## Testing and Validation

### Comprehensive Test Suite
```bash
# Complete system validation
python ship_validation.py

# Feature-specific testing
python test_all_features.py

# Package functionality testing
python -m code_quality_agent analyze sample_code
python cqi.py analyze sample_code --interactive
```

### Expected Results
- **Local Analysis**: 11 issues detected in sample code (3 high-severity security issues)
- **GitHub Analysis**: 136+ issues detected in test repositories
- **RAG System**: 200+ code chunks indexed with semantic search
- **Performance**: Complete validation in under 3 minutes

## License and Attribution

### License
MIT License - see LICENSE file for details

### Dependencies
- **LangChain**: Agent framework and LLM integration
- **Groq**: High-performance LLM inference
- **FAISS**: Efficient similarity search and clustering
- **Rich**: Terminal formatting and user interface
- **Click**: Command-line interface framework
- **GitPython**: Git repository operations
- **Bandit**: Python security analysis
- **Radon**: Code complexity metrics


## Support and Contributing

### Bug Reports
Report issues through the GitHub issue tracker with detailed reproduction steps and environment information.

### Feature Requests
Submit enhancement proposals with clear use cases and implementation suggestions.

### Contributing Guidelines
1. Fork the repository
2. Create feature branch with descriptive name
3. Implement changes with appropriate test coverage
4. Submit pull request with detailed description
5. Ensure all validation tests pass





