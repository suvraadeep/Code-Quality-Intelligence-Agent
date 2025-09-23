"""
Purpose: Main entry point script

High-level Overview:
Standalone entry point that allows running the tool with `python cqi.py [commands]` by importing and executing the CLI interface.

Key Components:
- Path setup for package imports
- CLI interface execution

Functions/Classes:
- `Path setup`: Adds package to Python path
- `CLI execution`: Imports and runs the main CLI interface
"""

import sys
from pathlib import Path

# Add package to path
sys.path.insert(0, str(Path(__file__).parent))

from code_quality_agent.cli import cli

if __name__ == '__main__':
    cli()
