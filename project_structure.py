"""Display the project structure for the Code Quality Intelligence Agent."""

from pathlib import Path
from rich.console import Console
from rich.tree import Tree
from rich.panel import Panel

console = Console()

def create_project_tree():
    
    tree = Tree("📁 [bold blue]Code Quality Intelligence Agent[/bold blue]")
    
    core_branch = tree.add("📦 [bold green]Core Components[/bold green]")
    core_branch.add("🤖 [cyan]cli.py[/cyan] - Main CLI interface")
    core_branch.add("⚙️ [cyan]config.py[/cyan] - Configuration settings")
    
    core_pkg = core_branch.add("📁 [yellow]core/[/yellow]")
    core_pkg.add("🧠 [cyan]agent.py[/cyan] - LangChain agent with Groq")
    core_pkg.add("🔍 [cyan]analyzers.py[/cyan] - Code analysis engines")
    core_pkg.add("📊 [cyan]report_generator.py[/cyan] - Rich reporting system")
    
    utils_pkg = core_branch.add("📁 [yellow]utils/[/yellow]")
    utils_pkg.add("📂 [cyan]file_handler.py[/cyan] - File & GitHub operations")
    
    setup_branch = tree.add("📦 [bold magenta]Setup & Dependencies[/bold magenta]")
    setup_branch.add("📋 [cyan]requirements.txt[/cyan] - Python dependencies")
    setup_branch.add("🔧 [cyan]setup.py[/cyan] - Automated setup script")
    setup_branch.add("🌍 [cyan]env_example.txt[/cyan] - Environment template")
    
    docs_branch = tree.add("📚 [bold yellow]Documentation[/bold yellow]")
    docs_branch.add("📖 [cyan]README.md[/cyan] - Complete documentation")
    docs_branch.add("🚀 [cyan]QUICKSTART.md[/cyan] - 5-minute setup guide")
    
    examples_branch = tree.add("🧪 [bold red]Examples & Testing[/bold red]")
    examples_branch.add("🐍 [cyan]test_example.py[/cyan] - Python code with issues")
    examples_branch.add("🟨 [cyan]test_example.js[/cyan] - JavaScript code with issues")
    examples_branch.add("🎬 [cyan]demo.py[/cyan] - Interactive demo")
    examples_branch.add("▶️ [cyan]run_example.py[/cyan] - Example runner")
    
    return tree

def show_architecture():
    
    arch_content = """
🔄 [bold]Analysis Pipeline[/bold]
┌─ Input Processing (Files/GitHub URLs)
├─ Language Detection & File Discovery  
├─ Multi-layered Analysis:
│  ├─ 🔍 AST Parsing (Python)
│  ├─ 🛡️ Security Analysis (Bandit, Semgrep)
│  ├─ 📊 Complexity Metrics (Radon)
│  └─ 🤖 AI Analysis (LangChain + Groq)
├─ Issue Aggregation & Prioritization
├─ 📋 Report Generation (Console/JSON/MD)
└─ 🤖 Interactive Q&A

🧠 [bold]AI Components[/bold]
├─ LangChain Framework
├─ Groq LLM Integration (llama3-8b-8192)
├─ Conversation Memory
└─ Prompt Engineering for Code Analysis

🔧 [bold]Analysis Categories[/bold]
├─ 🔒 Security (Vulnerabilities, Secrets)
├─ ⚡ Performance (Bottlenecks, Complexity)
├─ 🧩 Code Quality (Duplication, Smells)
├─ 🧪 Testing (Coverage, Gaps)
├─ 📚 Documentation (Missing, Outdated)
└─ ✨ Best Practices (Style, Patterns)
"""
    
    return Panel(arch_content, title="🏗️ System Architecture", border_style="blue")

def show_features():
    
    features_content = """
✨ [bold]Core Features[/bold]
├─ 🌍 Multi-language support (Python, JS, TS, Java, C++, etc.)
├─ 🐙 GitHub repository analysis
├─ 🤖 AI-powered insights with LangChain + Groq
├─ 🎨 Beautiful rich console output
├─ 💬 Interactive Q&A about your codebase
├─ 📊 Multiple report formats (Console/JSON/Markdown)
└─ 🔧 Easy CLI interface

🚀 [bold]Advanced Capabilities[/bold]
├─ 🧠 Semantic code understanding
├─ 📈 Severity-based issue prioritization
├─ 🔄 Continuous integration ready
├─ 🎯 Actionable recommendations
├─ 📝 Comprehensive documentation
└─ 🛡️ Security-first analysis approach

🎨 [bold]User Experience[/bold]
├─ ⚡ Fast setup (5 minutes)
├─ 🎯 Developer-friendly reports
├─ 💡 Practical suggestions
├─ 🔍 Deep codebase insights
└─ 📱 Cross-platform compatibility
"""
    
    return Panel(features_content, title="✨ Key Features", border_style="green")

def main():
    
    
    # Header
    header = Panel(
        "[bold blue]Code Quality Intelligence Agent[/bold blue]\n"
        "AI-powered code analysis with LangChain, MCP, and Groq\n\n"
        "[dim]Built for developers who care about code quality[/dim]",
        border_style="blue"
    )
    
    console.print(header)
    console.print()
    
    
    console.print(create_project_tree())
    console.print()
    
    
    console.print(show_architecture())
    console.print()
    
    
    console.print(show_features())
    console.print()
    
    
    quick_start = Panel(
        "🚀 [bold]Quick Start[/bold]\n\n"
        "1. [cyan]pip install -r requirements.txt[/cyan]\n"
        "2. [cyan]export GROQ_API_KEY=your_key_here[/cyan]\n"
        "3. [cyan]python cli.py analyze test_example.py[/cyan]\n\n"
        "📚 Full guide: [cyan]python cli.py setup[/cyan] or see QUICKSTART.md",
        title="🎯 Get Started",
        border_style="yellow"
    )
    
    console.print(quick_start)

if __name__ == "__main__":
    main()
