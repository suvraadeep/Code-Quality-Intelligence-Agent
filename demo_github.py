"""
GitHub Integration Demo Script for Code Quality Intelligence Agent
This script demonstrates the GitHub repository analysis capabilities.
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from code_quality_agent.agent import CodeQualityAgent
from rich.console import Console
from rich.panel import Panel

console = Console()

async def demo_github_analysis():
    
    console.print(Panel(
        "[bold blue]🐙 GitHub Integration Demo[/bold blue]\n"
        "This demo shows how to analyze GitHub repositories with the Code Quality Intelligence Agent.",
        title="Demo",
        border_style="blue"
    ))
    
    demo_repos = [
        {
            "url": "https://github.com/gvanrossum/patma",
            "description": "Small Python pattern matching examples"
        },
        {
            "url": "https://github.com/pallets/flask",
            "description": "Popular Python web framework"
        },
        {
            "url": "https://github.com/psf/requests", 
            "description": "Python HTTP library"
        }
    ]
    
    console.print("\n[bold green]Available Demo Repositories:[/bold green]")
    for i, repo in enumerate(demo_repos, 1):
        console.print(f"  {i}. {repo['url']} - {repo['description']}")
    
    console.print(f"\n[yellow]Analyzing: {demo_repos[0]['url']}[/yellow]")
    
    agent = CodeQualityAgent()
    
    console.print("\n[blue]🚀 Starting analysis...[/blue]")
    results = await agent.analyze_codebase(demo_repos[0]['url'])
    
    if 'error' in results:
        console.print(f"[red]❌ Analysis failed: {results['error']}[/red]")
        return
    
    summary = results.get('summary', {})
    issues = results.get('issues', [])
    
    console.print(Panel(
        f"[bold]Files Analyzed:[/bold] {summary.get('total_files', 0)}\n"
        f"[bold]Total Issues:[/bold] {summary.get('total_issues', 0)}\n"
        f"[bold]Repository:[/bold] {demo_repos[0]['url']}",
        title="✅ Analysis Complete",
        border_style="green"
    ))
    
    if issues:
        console.print("\n[bold yellow]🔍 Top Issues Found:[/bold yellow]")
        for i, issue in enumerate(issues[:3], 1):
            severity = issue.get('severity', 'info').upper()
            title = issue.get('title', 'Issue')
            file_path = issue.get('file_path', 'Unknown file')
            console.print(f"  {i}. [{severity}] {title} - {Path(file_path).name}")
    else:
        console.print("\n[green]🎉 No issues found![/green]")
    
    console.print(Panel(
        "[bold]GitHub Integration Features Demonstrated:[/bold]\n"
        "✅ Automatic repository cloning\n"
        "✅ Multi-file analysis\n"
        "✅ Issue detection and categorization\n"
        "✅ Temporary directory cleanup\n"
        "✅ Rich console output",
        title="🚀 Demo Complete",
        border_style="cyan"
    ))

if __name__ == "__main__":
    try:
        asyncio.run(demo_github_analysis())
    except KeyboardInterrupt:
        console.print("\n[yellow]Demo interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]Demo error: {e}[/red]")
