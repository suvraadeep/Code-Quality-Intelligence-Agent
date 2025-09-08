"""Demo script for Code Quality Intelligence Agent."""

import asyncio
import os
import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


async def run_demo():
    
    title = Text("Code Quality Intelligence Agent Demo", style="bold blue")
    demo_panel = Panel(
        "🤖 Welcome to the Code Quality Intelligence Agent Demo!\n\n"
        "This demo will show you how to analyze code for quality issues\n"
        "using AI-powered insights and static analysis tools.",
        title=title,
        border_style="blue"
    )
    console.print(demo_panel)
    console.print()
    
    if not os.getenv("GROQ_API_KEY"):
        console.print("[yellow]⚠️ GROQ_API_KEY not found in environment[/yellow]")
        console.print("[blue]💡 For this demo, we'll use a mock API key[/blue]")
        os.environ["GROQ_API_KEY"] = "demo_key_for_testing"
    
    try:
        from code_quality_agent.agent import CodeQualityAgent
        from code_quality_agent.report_generator import ReportGenerator
        
        console.print("[green]✅ All components loaded successfully[/green]")
        
        console.print("\n[bold blue]📊 Demo 1: Analyzing Python Test File[/bold blue]")
        console.print("Analyzing: test_example.py")
        
        console.print("[yellow]Note: This is a demo - actual analysis requires a valid Groq API key[/yellow]")
        
        demo_issues = [
            {
                "category": "security",
                "severity": "high", 
                "title": "Hardcoded API Key",
                "description": "API key found hardcoded in source code",
                "line_number": 8,
                "suggestion": "Move API key to environment variable"
            },
            {
                "category": "security",
                "severity": "critical",
                "title": "SQL Injection Vulnerability", 
                "description": "Direct string formatting in SQL query",
                "line_number": 38,
                "suggestion": "Use parameterized queries"
            },
            {
                "category": "performance",
                "severity": "medium",
                "title": "Inefficient Algorithm",
                "description": "O(n²) nested loop complexity",
                "line_number": 12,
                "suggestion": "Use set operations for better performance"
            },
            {
                "category": "complexity",
                "severity": "high",
                "title": "High Cyclomatic Complexity",
                "description": "Function has too many nested conditions",
                "line_number": 22,
                "suggestion": "Refactor using early returns or lookup table"
            }
        ]
        
        console.print("\n[green]🔍 Sample Analysis Results:[/green]")
        for i, issue in enumerate(demo_issues, 1):
            severity_color = {
                "critical": "red",
                "high": "red", 
                "medium": "yellow",
                "low": "green"
            }.get(issue["severity"], "white")
            
            console.print(f"{i}. [{severity_color}][{issue['severity'].upper()}][/{severity_color}] {issue['title']}")
            console.print(f"   Line {issue['line_number']}: {issue['description']}")
            console.print(f"   💡 {issue['suggestion']}")
            console.print()
        
        console.print("[bold blue]📊 Demo 2: JavaScript Analysis Preview[/bold blue]")
        console.print("Analyzing: test_example.js")
        
        js_issues = [
            "XSS vulnerability in innerHTML usage",
            "Dangerous eval() function call",
            "Use of var instead of let/const",
            "String-based setTimeout security risk"
        ]
        
        console.print("\n[green]🔍 JavaScript Issues Found:[/green]")
        for issue in js_issues:
            console.print(f"• {issue}")
        
        console.print()
        
        console.print("[bold blue]🤖 Demo 3: Interactive Q&A Simulation[/bold blue]")
        
        qa_examples = [
            {
                "question": "What are the most critical security issues?",
                "answer": "The most critical issue is the SQL injection vulnerability in line 38. This allows attackers to manipulate database queries. Also, the hardcoded API key in line 8 should be moved to environment variables."
            },
            {
                "question": "How can I improve the performance?",
                "answer": "The main performance issue is in the slow_function() with O(n²) complexity. You can fix this by using set operations or a more efficient algorithm. Also, avoid string concatenation in loops."
            },
            {
                "question": "What about code maintainability?",
                "answer": "Several functions are too complex or too long. The complex_function() has high cyclomatic complexity - consider using early returns or a lookup table. Also, add docstrings to undocumented functions."
            }
        ]
        
        for qa in qa_examples:
            console.print(f"[bold cyan]Q: {qa['question']}[/bold cyan]")
            console.print(f"[green]A: {qa['answer']}[/green]")
            console.print()
        
        console.print("[bold blue]📋 Demo 4: Available Report Formats[/bold blue]")
        
        formats = [
            ("Console", "Rich, colorful terminal output with tables and panels"),
            ("JSON", "Structured data format for integration with other tools"),
            ("Markdown", "Human-readable format for documentation and sharing")
        ]
        
        for format_name, description in formats:
            console.print(f"• [bold]{format_name}[/bold]: {description}")
        
        console.print()
        
        console.print("[bold green]🚀 Try It Yourself![/bold green]")
        
        examples = [
            "python cli.py analyze test_example.py",
            "python cli.py analyze test_example.js --interactive", 
            "python cli.py analyze . --format json --output report.json",
            "python cli.py analyze https://github.com/user/repo",
            "python cli.py info ."
        ]
        
        console.print("\n[blue]Example commands:[/blue]")
        for example in examples:
            console.print(f"  {example}")
        
        console.print()
        final_panel = Panel(
            "🎉 Demo completed!\n\n"
            "To run actual analysis, make sure you have:\n"
            "1. A valid Groq API key set in GROQ_API_KEY environment variable\n"
            "2. All dependencies installed (pip install -r requirements.txt)\n\n"
            "Start with: python cli.py setup",
            title="🏁 Next Steps",
            border_style="green"
        )
        console.print(final_panel)
        
    except ImportError as e:
        console.print(f"[red]❌ Import error: {e}[/red]")
        console.print("[yellow]💡 Run 'pip install -r requirements.txt' first[/yellow]")
    except Exception as e:
        console.print(f"[red]❌ Demo error: {e}[/red]")


if __name__ == "__main__":
    asyncio.run(run_demo())
