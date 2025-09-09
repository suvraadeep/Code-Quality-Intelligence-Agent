"""
Entry point script for Code Quality Intelligence Agent package.
This allows users to run the tool with: python cqi.py [commands]
"""

import sys
from pathlib import Path

# Add package to path
sys.path.insert(0, str(Path(__file__).parent))

from code_quality_agent.cli import cli

if __name__ == '__main__':
    cli()
