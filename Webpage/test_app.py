
"""
Test script for the Code Quality Intelligence Agent Web Interface.
This script performs basic tests to ensure the application works correctly.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import plotly.express as px
        print("✅ Plotly imported successfully")
    except ImportError as e:
        print(f"❌ Plotly import failed: {e}")
        return False
    
    try:
        from code_quality_agent.agent import CodeQualityAgent
        print("✅ CodeQualityAgent imported successfully")
    except ImportError as e:
        print(f"❌ CodeQualityAgent import failed: {e}")
        return False
    
    return True

def test_config():
    """Test configuration loading."""
    print("\nTesting configuration...")
    
    try:
        from config import get_config, SUPPORTED_LANGUAGES, PAGES
        print("✅ Configuration loaded successfully")
        print(f"   Supported languages: {len(SUPPORTED_LANGUAGES)}")
        print(f"   Available pages: {len(PAGES)}")
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_app_structure():
    """Test if the app structure is correct."""
    print("\nTesting app structure...")
    
    base_dir = Path(__file__).parent
    
    required_files = [
        "app.py",
        "requirements.txt", 
        "README.md",
        "launch.py",
        "config.py"
    ]
    
    for file_name in required_files:
        file_path = base_dir / file_name
        if file_path.exists():
            print(f"✅ {file_name} exists")
        else:
            print(f"❌ {file_name} missing")
            return False
    
    return True

def test_launcher():
    """Test the launcher script."""
    print("\nTesting launcher...")
    
    try:
        from launch import check_dependencies
        if check_dependencies():
            print("✅ Launcher dependencies check passed")
            return True
        else:
            print("❌ Launcher dependencies check failed")
            return False
    except Exception as e:
        print(f"❌ Launcher test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Code Quality Intelligence Agent Web Interface")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_config,
        test_app_structure,
        test_launcher
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! The web interface is ready to use.")
        print("\nTo launch the application:")
        print("  python launch.py")
        print("  or")
        print("  streamlit run app.py")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
