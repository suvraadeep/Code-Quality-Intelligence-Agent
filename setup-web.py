"""
Setup script to make the Code Quality Intelligence web interface easily accessible.
This script creates a global command that can be run from anywhere.
"""

import os
import sys
import shutil
from pathlib import Path

def main():
    """Setup the web interface for global access."""
    print("Setting up Code Quality Intelligence Web Interface...")
    
    # Get the current directory (should be the main project directory)
    current_dir = Path.cwd()
    webpage_dir = current_dir / "Webpage"
    
    if not webpage_dir.exists():
        print("Error: Webpage directory not found. Please run this from the main project directory.")
        sys.exit(1)
    
    # Create a simple launcher script in the main directory
    launcher_content = f'''#!/usr/bin/env python3
"""
Code Quality Intelligence Agent - Web Interface Launcher
Run this script to launch the web interface.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Launch the web interface."""
    script_dir = Path(__file__).parent
    webpage_dir = script_dir / "Webpage"
    app_path = webpage_dir / "app.py"
    
    if not app_path.exists():
        print("Error: Web interface not found.")
        sys.exit(1)
    
    print("Launching Code Quality Intelligence Agent Web Interface...")
    print("The application will open in your browser at http://localhost:8501")
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--server.address", "localhost",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\\nWeb interface stopped by user")
    except Exception as e:
        print(f"Error launching application: {{e}}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''
    
    # Write the launcher script
    launcher_path = current_dir / "cqi-web.py"
    with open(launcher_path, 'w') as f:
        f.write(launcher_content)
    
    # Make it executable on Unix systems
    try:
        os.chmod(launcher_path, 0o755)
    except:
        pass  # Windows doesn't support chmod
    
    # Create Windows batch file
    batch_content = f'''@echo off
REM Code Quality Intelligence Agent - Web Interface Launcher
python "%~dp0cqi-web.py"
pause
'''
    
    batch_path = current_dir / "cqi-web.bat"
    with open(batch_path, 'w') as f:
        f.write(batch_content)
    
    print("✓ Web interface setup complete!")
    print()
    print("You can now launch the web interface using:")
    print("  python cqi-web.py")
    print("  or")
    print("  cqi-web.bat (Windows)")
    print()
    print("The web interface will be available at: http://localhost:8501")

if __name__ == "__main__":
    main()
