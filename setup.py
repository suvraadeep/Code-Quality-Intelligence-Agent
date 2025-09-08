"""Setup script for Code Quality Intelligence Agent."""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True


def install_dependencies():
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False


def setup_environment():
    env_file = Path(".env")
    
    if env_file.exists():
        print("✅ .env file already exists")
        return True
    
    print("🔧 Setting up environment...")
    
    if os.getenv("GROQ_API_KEY"):
        print("✅ GROQ_API_KEY found in environment")
        return True
    
    print("\n🔑 Groq API Key Setup")
    print("You need a Groq API key to use this tool.")
    print("Get one at: https://console.groq.com/")
    
    api_key = input("Enter your Groq API key (or press Enter to skip): ").strip()
    
    if api_key:
        try:
            with open(".env", "w") as f:
                f.write(f"GROQ_API_KEY={api_key}\n")
            print("✅ API key saved to .env file")
            return True
        except Exception as e:
            print(f"❌ Failed to save API key: {e}")
            return False
    else:
        print("⚠️ Skipped API key setup. Set GROQ_API_KEY environment variable later.")
        return True


def verify_setup():
    print("\n🧪 Verifying setup...")
    
    try:
        import langchain
        import langchain_groq
        import click
        import rich
        import git
        print("✅ All required packages imported successfully")
        
        result = subprocess.run([sys.executable, "cli.py", "--help"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ CLI interface working")
            return True
        else:
            print("❌ CLI interface test failed")
            return False
    
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Setup verification failed: {e}")
        return False


def main():
    print("🚀 Code Quality Intelligence Agent Setup")
    print("=" * 50)
    
    if not check_python_version():
        sys.exit(1)
    
    if not install_dependencies():
        print("\n💡 Try installing dependencies manually:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    if not setup_environment():
        print("\n💡 You can set up the API key later by:")
        print("   export GROQ_API_KEY=your_key_here")
        print("   or create a .env file with GROQ_API_KEY=your_key_here")
    
    if verify_setup():
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Test the installation:")
        print("   python cli.py info test_example.py")
        print("2. Run a full analysis:")
        print("   python cli.py analyze test_example.py")
        print("3. Try interactive mode:")
        print("   python cli.py analyze test_example.py --interactive")
        print("\nFor help: python cli.py --help")
    else:
        print("\n⚠️ Setup completed with warnings. Check the messages above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
