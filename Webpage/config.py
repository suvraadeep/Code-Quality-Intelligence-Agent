"""
Configuration file for the Code Quality Intelligence Agent Web Interface.
"""

import os
from pathlib import Path

# Application settings
APP_TITLE = "Code Quality Intelligence Agent"
APP_ICON = "🔍"
APP_LAYOUT = "wide"

# Server settings
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8501

# File paths
BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
PAGES_DIR = BASE_DIR / "pages"
COMPONENTS_DIR = BASE_DIR / "components"

# Analysis settings
SUPPORTED_LANGUAGES = [
    "python", "javascript", "typescript", "java", "cpp", "csharp",
    "go", "rust", "php", "ruby", "swift", "kotlin", "scala"
]

# Output formats
OUTPUT_FORMATS = ["Console", "JSON", "Markdown"]

# Analysis types
ANALYSIS_TYPES = ["Local Path", "GitHub Repository"]

# Chart colors
SEVERITY_COLORS = {
    'Critical': '#ff4444',
    'High': '#ff8800', 
    'Medium': '#ffbb33',
    'Low': '#00C851',
    'Info': '#33b5e5'
}

# Page configuration
PAGES = [
    {"name": "Home", "key": "home"},
    {"name": "Setup", "key": "setup"},
    {"name": "Info", "key": "info"},
    {"name": "Analyze", "key": "analyze"},
    {"name": "Chat", "key": "chat"}
]

# Default settings
DEFAULT_SETTINGS = {
    "analysis_type": "Local Path",
    "output_format": "Console",
    "interactive_mode": False,
    "enable_rag": True,
    "enable_chat": True
}

# API configuration
API_CONFIG = {
    "groq_key_env": "GROQ_API_KEY",
    "timeout": 30,
    "max_retries": 3
}

# File size limits
MAX_FILE_SIZE_MB = 10
MAX_TOTAL_SIZE_MB = 100

# Cache settings
CACHE_TTL = 3600  # 1 hour in seconds
ENABLE_CACHING = True

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def get_config(key: str, default=None):
    """Get configuration value."""
    return globals().get(key.upper(), default)

def set_config(key: str, value):
    """Set configuration value."""
    globals()[key.upper()] = value

def get_env_config(key: str, default=None):
    """Get configuration from environment variable."""
    return os.environ.get(key, default)
