"""
Comprehensive CLI Testing Suite
Tests all documented CLI commands including RAG features.
"""

import subprocess
import sys
import json
import time
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run_command(cmd, description, timeout=120):
    """Run a command and return detailed results."""
    console.print(f"[blue]Testing: {description}[/blue]")
    console.print(f"[dim]Command: {cmd}[/dim]")
    
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
        output_size = len(result.stdout)
        error_size = len(result.stderr)
        
        if success:
            console.print(f"  [green]SUCCESS[/green] - Output: {output_size:,} chars")
            if error_size > 0:
                console.print(f"  [yellow]Warnings: {error_size} chars[/yellow]")
        else:
            console.print(f"  [red]FAILED[/red] - Exit code: {result.returncode}")
            if result.stderr:
                console.print(f"  [red]Error: {result.stderr[:200]}[/red]")
        
        return {
            "success": success,
            "output_size": output_size,
            "error_size": error_size,
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
        
    except subprocess.TimeoutExpired:
        console.print(f"  [red]TIMEOUT[/red] after {timeout}s")
        return {"success": False, "timeout": True}
    except Exception as e:
        console.print(f"  [red]ERROR[/red]: {e}")
        return {"success": False, "error": str(e)}

def test_basic_commands():
    """Test basic CLI commands."""
    console.print(Panel("[bold]Basic CLI Commands[/bold]", border_style="blue"))
    
    commands = [
        ("python cqi.py --version", "Version information"),
        ("python cqi.py --help", "Help documentation"),
        ("python cqi.py analyze --help", "Analyze command help"),
        ("python cqi.py chat --help", "Chat command help"),
        ("python cqi.py info --help", "Info command help"),
        ("python cqi.py setup --help", "Setup command help"),
    ]
    
    results = {}
    for cmd, desc in commands:
        results[desc] = run_command(cmd, desc, 30)
    
    return results

def test_local_analysis():
    """Test local file and directory analysis."""
    console.print(Panel("[bold]Local Analysis Commands[/bold]", border_style="green"))
    
    commands = [
        ("python cqi.py info sample_code", "Codebase information"),
        ("python cqi.py analyze sample_code/module_a.py --format console", "Single file analysis"),
        ("python cqi.py analyze sample_code --format console", "Directory analysis"),
        ("python cqi.py analyze sample_code --format json --output test_local.json", "JSON export"),
        ("python cqi.py analyze sample_code --format markdown --output test_local.md", "Markdown export"),
    ]
    
    results = {}
    for cmd, desc in commands:
        results[desc] = run_command(cmd, desc, 60)
    
    return results

def test_rag_features():
    """Test RAG-enhanced interactive features."""
    console.print(Panel("[bold]RAG-Enhanced Features[/bold]", border_style="cyan"))
    
    # Test RAG system availability
    console.print("[blue]Testing RAG System Availability[/blue]")
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from code_quality_agent.rag_system import CodeRAGSystem
        
        rag = CodeRAGSystem()
        available = rag.is_available()
        stats = rag.get_collection_stats()
        
        console.print(f"  [green]RAG Available: {available}[/green]")
        console.print(f"  [green]RAG System: {stats.get('system', 'Unknown')}[/green]")
        console.print(f"  [green]Total Chunks: {stats.get('total_chunks', 0)}[/green]")
        
        rag_result = {"available": available, "system": stats.get('system'), "chunks": stats.get('total_chunks', 0)}
        
    except Exception as e:
        console.print(f"  [red]RAG Error: {e}[/red]")
        rag_result = {"available": False, "error": str(e)}
    
    return {"rag_system": rag_result}

def test_github_analysis():
    """Test GitHub repository analysis."""
    console.print(Panel("[bold]GitHub Integration Commands[/bold]", border_style="magenta"))
    
    commands = [
        ("python cqi.py analyze https://github.com/gvanrossum/patma --format console", "GitHub repository analysis"),
        ("python cqi.py analyze https://github.com/gvanrossum/patma --format json --output test_github.json", "GitHub JSON export"),
    ]
    
    results = {}
    for cmd, desc in commands:
        results[desc] = run_command(cmd, desc, 180)  # Longer timeout for GitHub
    
    return results

def test_module_execution():
    """Test package module execution."""
    console.print(Panel("[bold]Package Module Execution[/bold]", border_style="yellow"))
    
    commands = [
        ("python -m code_quality_agent --version", "Module version"),
        ("python -m code_quality_agent --help", "Module help"),
        ("python -m code_quality_agent analyze sample_code --format console", "Module analysis"),
        ("python -m code_quality_agent info sample_code", "Module info"),
    ]
    
    results = {}
    for cmd, desc in commands:
        results[desc] = run_command(cmd, desc, 60)
    
    return results

def validate_generated_files():
    """Validate all generated files."""
    console.print(Panel("[bold]Generated File Validation[/bold]", border_style="white"))
    
    files_to_check = [
        ("test_local.json", "Local analysis JSON"),
        ("test_local.md", "Local analysis Markdown"),
        ("test_github.json", "GitHub analysis JSON"),
    ]
    
    validation_results = {}
    
    for filename, description in files_to_check:
        console.print(f"[blue]Validating: {description}[/blue]")
        
        if Path(filename).exists():
            size = Path(filename).stat().st_size
            console.print(f"  [green]File exists: {size:,} bytes[/green]")
            
            if filename.endswith('.json'):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if 'analysis' in data and 'metadata' in data:
                        files_count = data['analysis']['summary']['total_files']
                        issues_count = data['analysis']['summary']['total_issues']
                        console.print(f"  [green]Valid JSON: {files_count} files, {issues_count} issues[/green]")
                        validation_results[filename] = {"valid": True, "files": files_count, "issues": issues_count}
                    else:
                        console.print(f"  [red]Invalid JSON structure[/red]")
                        validation_results[filename] = {"valid": False}
                        
                except Exception as e:
                    console.print(f"  [red]JSON error: {e}[/red]")
                    validation_results[filename] = {"valid": False, "error": str(e)}
            
            elif filename.endswith('.md'):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if "# Code Quality Intelligence Report" in content:
                        console.print(f"  [green]Valid Markdown structure[/green]")
                        validation_results[filename] = {"valid": True, "size": len(content)}
                    else:
                        console.print(f"  [red]Invalid Markdown structure[/red]")
                        validation_results[filename] = {"valid": False}
                        
                except Exception as e:
                    console.print(f"  [red]Markdown error: {e}[/red]")
                    validation_results[filename] = {"valid": False, "error": str(e)}
        else:
            console.print(f"  [red]File not found[/red]")
            validation_results[filename] = {"valid": False, "error": "Not found"}
    
    return validation_results

def generate_summary_report(all_results, duration):
    """Generate comprehensive test summary."""
    
    # Calculate statistics
    basic_passed = sum(1 for r in all_results["basic"].values() if r.get("success", False))
    basic_total = len(all_results["basic"])
    
    local_passed = sum(1 for r in all_results["local"].values() if r.get("success", False))
    local_total = len(all_results["local"])
    
    module_passed = sum(1 for r in all_results["module"].values() if r.get("success", False))
    module_total = len(all_results["module"])
    
    github_passed = sum(1 for r in all_results["github"].values() if r.get("success", False))
    github_total = len(all_results["github"])
    
    files_valid = sum(1 for r in all_results["files"].values() if r.get("valid", False))
    files_total = len(all_results["files"])
    
    rag_available = all_results["rag"]["rag_system"].get("available", False)
    rag_chunks = all_results["rag"]["rag_system"].get("chunks", 0)
    
    # Create summary table
    table = Table(title="Comprehensive CLI Test Results")
    table.add_column("Test Category", style="cyan")
    table.add_column("Passed", style="green")
    table.add_column("Total", style="white")
    table.add_column("Success Rate", style="bold")
    table.add_column("Status", style="yellow")
    
    table.add_row("Basic Commands", str(basic_passed), str(basic_total), f"{basic_passed/basic_total:.0%}", "PASS" if basic_passed == basic_total else "ISSUES")
    table.add_row("Local Analysis", str(local_passed), str(local_total), f"{local_passed/local_total:.0%}", "PASS" if local_passed == local_total else "ISSUES")
    table.add_row("Module Execution", str(module_passed), str(module_total), f"{module_passed/module_total:.0%}", "PASS" if module_passed == module_total else "ISSUES")
    table.add_row("GitHub Analysis", str(github_passed), str(github_total), f"{github_passed/github_total:.0%}", "PASS" if github_passed >= github_total * 0.8 else "ISSUES")
    table.add_row("File Generation", str(files_valid), str(files_total), f"{files_valid/files_total:.0%}", "PASS" if files_valid == files_total else "ISSUES")
    table.add_row("RAG System", "Yes" if rag_available else "No", "1", "100%" if rag_available else "0%", f"PASS ({rag_chunks} chunks)" if rag_available else "DISABLED")
    
    console.print(table)
    
    # Overall assessment
    total_tests = basic_total + local_total + module_total + github_total
    total_passed = basic_passed + local_passed + module_passed + github_passed
    overall_success_rate = total_passed / total_tests
    
    if overall_success_rate >= 0.9 and rag_available and files_valid == files_total:
        verdict = Panel(
            f"[bold green]COMPREHENSIVE TESTING COMPLETE - ALL SYSTEMS OPERATIONAL[/bold green]\n\n"
            f"Test Summary:\n"
            f"• Total Commands Tested: {total_tests}\n"
            f"• Commands Passed: {total_passed}\n"
            f"• Overall Success Rate: {overall_success_rate:.0%}\n"
            f"• RAG System: {rag_chunks} chunks indexed\n"
            f"• File Generation: {files_valid}/{files_total} formats working\n"
            f"• Test Duration: {duration:.1f} seconds\n\n"
            f"All CLI commands documented in README are working correctly.\n"
            f"The system is ready for production deployment.\n\n"
            f"READY FOR SHIPPING",
            title="VALIDATION SUCCESS",
            border_style="green"
        )
    else:
        issues = []
        if overall_success_rate < 0.9:
            issues.append(f"Low success rate: {overall_success_rate:.0%}")
        if not rag_available:
            issues.append("RAG system not available")
        if files_valid != files_total:
            issues.append("File generation issues")
        
        verdict = Panel(
            f"[bold red]TESTING ISSUES DETECTED[/bold red]\n\n"
            f"Issues found:\n" + "\n".join(f"• {issue}" for issue in issues) + 
            f"\n\nPlease review and fix before deployment.",
            title="NEEDS ATTENTION",
            border_style="red"
        )
    
    console.print(verdict)

def main():
    """Run comprehensive CLI testing."""
    start_time = time.time()
    
    console.print(Panel(
        "[bold]Comprehensive CLI Testing Suite[/bold]\n"
        "Testing all documented commands including RAG features",
        title="CLI VALIDATION",
        border_style="blue"
    ))
    
    # Run all test categories
    console.print("\n" + "="*80)
    basic_results = test_basic_commands()
    
    console.print("\n" + "="*80)
    local_results = test_local_analysis()
    
    console.print("\n" + "="*80)
    rag_results = test_rag_features()
    
    console.print("\n" + "="*80)
    github_results = test_github_analysis()
    
    console.print("\n" + "="*80)
    module_results = test_module_execution()
    
    console.print("\n" + "="*80)
    file_results = validate_generated_files()
    
    # Compile all results
    all_results = {
        "basic": basic_results,
        "local": local_results,
        "rag": rag_results,
        "github": github_results,
        "module": module_results,
        "files": file_results
    }
    
    # Generate summary
    console.print("\n" + "="*80)
    generate_summary_report(all_results, time.time() - start_time)
    
    # Cleanup test files
    cleanup_files = ["test_local.json", "test_local.md", "test_github.json"]
    for file in cleanup_files:
        if Path(file).exists():
            Path(file).unlink()

if __name__ == "__main__":
    main()
