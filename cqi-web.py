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
        print("\nWeb interface stopped by user")
    except Exception as e:
        print(f"Error launching application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
