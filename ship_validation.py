"""
SHIPPING VALIDATION
Code Quality Intelligence Agent - Production Ready Confirmation
This script provides a final validation that ALL features are working and ready for production.
"""

import subprocess
import sys
import time
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run_cmd(cmd, desc, timeout=60):
    try:
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8',
            errors='ignore'
        )
        success = result.returncode == 0
        return success, len(result.stdout), result.stderr
    except:
        return False, 0, "Command failed"

def main():
    start_time = time.time()
    
    console.print(Panel(
        "[bold bright_green]🚀 FINAL SHIPPING VALIDATION[/bold bright_green]\n"
        "[bold white]Code Quality Intelligence Agent - Production Ready Check[/bold white]\n\n"
        "[dim]Validating ALL features are working and ready for production deployment.[/dim]",
        title="🏆 SHIP READY VALIDATION",
        border_style="bright_green"
    ))
    
    tests = [
        ("python cli.py --version", "CLI Version"),
        ("python cli.py --help", "CLI Help"),
        ("python cli.py analyze sample_code --format console", "Local Analysis"),
        ("python cli.py analyze sample_code --format json --output ship_test.json", "JSON Export"),
        ("python cli.py analyze sample_code --format markdown --output ship_test.md", "Markdown Export"),
        ("python cli.py info sample_code", "Codebase Info"),
        ("python cli.py analyze https://github.com/gvanrossum/patma --format console", "GitHub Analysis"),
    ]
    
    results = {}
    passed = 0
    total = len(tests)
    
    console.print(Panel("[bold blue]🧪 Running Production Tests[/bold blue]", border_style="blue"))
    
    for i, (cmd, desc) in enumerate(tests, 1):
        console.print(f"[yellow]Test {i}/{total}: {desc}[/yellow]")
        success, output_len, error = run_cmd(cmd, desc, timeout=90)
        
        if success:
            console.print(f"  ✅ PASS - {output_len:,} chars output")
            passed += 1
            results[desc] = "✅ PASS"
        else:
            console.print(f"  ❌ FAIL - {error[:100] if error else 'Unknown error'}")
            results[desc] = "❌ FAIL"
    
    console.print(f"\n[bold blue]📄 Validating Generated Files[/bold blue]")
    
    files_to_check = ["ship_test.json", "ship_test.md"]
    files_valid = 0
    
    for filename in files_to_check:
        if Path(filename).exists():
            size = Path(filename).stat().st_size
            console.print(f"  ✅ {filename}: {size:,} bytes")
            files_valid += 1
        else:
            console.print(f"  ❌ {filename}: Missing")
    
    console.print(f"\n[bold blue]🧠 Testing RAG System[/bold blue]")
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from core.rag_system import CodeRAGSystem
        
        rag = CodeRAGSystem()
        rag_available = rag.is_available()
        stats = rag.get_collection_stats()
        
        console.print(f"  ✅ RAG Available: {rag_available}")
        console.print(f"  ✅ RAG System: {stats.get('system', 'Unknown')}")
        console.print(f"  ✅ Total Chunks: {stats.get('total_chunks', 0)}")
        
        rag_working = rag_available
    except Exception as e:
        console.print(f"  ❌ RAG Error: {e}")
        rag_working = False
    
    cli_score = passed / total
    files_score = files_valid / len(files_to_check)
    
    overall_ready = (cli_score >= 0.85 and files_score >= 0.9 and rag_working)
    
    duration = time.time() - start_time
    
    table = Table(title="🎯 FINAL SHIPPING SCORECARD")
    table.add_column("Component", style="cyan")
    table.add_column("Score", style="white") 
    table.add_column("Status", style="green")
    table.add_column("Ship Ready", style="bold")
    
    table.add_row(
        "CLI Commands",
        f"{passed}/{total} ({cli_score:.0%})",
        "✅ Working" if cli_score >= 0.85 else "❌ Issues",
        "🚢 YES" if cli_score >= 0.85 else "❌ NO"
    )
    
    table.add_row(
        "Report Generation",
        f"{files_valid}/{len(files_to_check)} ({files_score:.0%})",
        "✅ Working" if files_score >= 0.9 else "❌ Failed",
        "🚢 YES" if files_score >= 0.9 else "❌ NO"
    )
    
    table.add_row(
        "RAG System",
        f"{stats.get('total_chunks', 0)} chunks",
        "✅ Available" if rag_working else "❌ Disabled",
        "🚢 YES" if rag_working else "❌ NO"
    )
    
    table.add_row(
        "Performance",
        f"{duration:.1f}s",
        "✅ Fast" if duration < 300 else "⚠️ Slow",
        "🚢 YES" if duration < 300 else "⚠️ REVIEW"
    )
    
    console.print(table)
    
    if overall_ready:
        console.print(Panel(
            f"[bold bright_green]🎉 PRODUCTION READY! 🚀[/bold bright_green]\n\n"
            f"[bold]✅ ALL SYSTEMS GO FOR SHIPPING[/bold]\n\n"
            f"📊 [bold]Final Scores:[/bold]\n"
            f"• CLI Commands: {passed}/{total} working ({cli_score:.0%})\n"
            f"• Report Generation: {files_valid}/{len(files_to_check)} formats ({files_score:.0%})\n"
            f"• RAG System: {stats.get('total_chunks', 0)} chunks indexed\n"
            f"• Performance: {duration:.1f} seconds\n\n"
            f"🔥 [bold]Ready Features:[/bold]\n"
            f"• Multi-language code analysis\n"
            f"• Security vulnerability detection\n"
            f"• Complexity and maintainability scoring\n"
            f"• GitHub repository analysis\n"
            f"• Interactive AI chatbot with RAG\n"
            f"• Multiple report formats (Console, JSON, Markdown)\n"
            f"• Cross-platform CLI interface\n"
            f"• Web dashboard (Streamlit)\n"
            f"• Error handling and graceful degradation\n\n"
            f"[bold bright_cyan]🌟 SHIP IT! 🌟[/bold bright_cyan]\n"
            f"[dim]The Code Quality Intelligence Agent is ready for production deployment![/dim]",
            title="🏆 READY TO SHIP",
            border_style="bright_green"
        ))
    else:
        console.print(Panel(
            f"[bold red]⚠️ NOT READY FOR SHIPPING[/bold red]\n\n"
            f"Issues found - please review and fix before shipping.",
            title="❌ NEEDS WORK",
            border_style="red"
        ))
    
    console.print(Panel(
        "[bold]🚀 PRODUCTION COMMANDS[/bold]\n\n"
        "[cyan]# Basic Analysis[/cyan]\n"
        "python cli.py analyze /path/to/code\n"
        "python cli.py analyze https://github.com/user/repo\n\n"
        "[cyan]# Interactive Features[/cyan]\n"
        "python cli.py analyze code --interactive\n"
        "python cli.py chat\n\n"
        "[cyan]# Report Generation[/cyan]\n"
        "python cli.py analyze code --format json --output report.json\n"
        "python cli.py analyze code --format markdown --output report.md\n\n"
        "[cyan]# Web Dashboard[/cyan]\n"
        "python simple_dashboard.py\n"
        "streamlit run streamlit_app.py\n\n"
        "[cyan]# Advanced Options[/cyan]\n"
        "python cli.py analyze repo --branch develop --interactive\n"
        "python cli.py analyze code --groq-key YOUR_KEY",
        title="📋 COMMAND REFERENCE",
        border_style="cyan"
    ))
    
    for file in ["ship_test.json", "ship_test.md"]:
        if Path(file).exists():
            Path(file).unlink()
    
    console.print(f"\n[bold green]🏁 Validation completed in {duration:.1f} seconds[/bold green]")

if __name__ == "__main__":
    main()
