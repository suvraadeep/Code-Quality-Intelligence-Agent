"""
Launcher script for Code Quality Intelligence Agent Web Interface.
This script provides an easy way to launch the web application.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import pandas
        import plotly
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return False

def launch_app():
    """Launch the Streamlit application."""
    app_path = Path(__file__).parent / "app.py"
    
    if not app_path.exists():
        print(f"Error: {app_path} not found")
        return False
    
    print("🚀 Launching Code Quality Intelligence Agent Web Interface...")
    print("📱 The application will open in your browser at http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    print()
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--server.address", "localhost",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Web interface stopped by user")
    except Exception as e:
        print(f"❌ Error launching application: {e}")
        return False
    
    return True

def main():
    """Main launcher function."""
    print("🤖 Code Quality Intelligence Agent - Web Interface")
    print("=" * 50)
    
    if not check_dependencies():
        sys.exit(1)
    
    if not launch_app():
        sys.exit(1)

if __name__ == "__main__":
    main()
