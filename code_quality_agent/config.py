"""
Purpose: Configuration settings and API key management

High-level Overview:
Centralized configuration management with support for environment variables, file analysis settings, and quality assessment parameters.

Key Components:
- Environment variable management
- File analysis configuration
- Quality category definitions
- Severity level mappings

Functions/Classes:
- `class Config`: Configuration class with class methods
  - Class Variables:
    - `DEFAULT_MODEL`: LLM model name ("deepseek-r1-distill-llama-70b")
    - `TEMPERATURE`: LLM temperature setting (0.1)
    - `MAX_TOKENS`: Maximum LLM tokens (4096)
    - `MAX_FILE_SIZE`: Maximum file size for analysis (1MB)
    - `SUPPORTED_EXTENSIONS`: Set of supported file extensions
    - `QUALITY_CATEGORIES`: List of quality analysis categories
    - `SEVERITY_LEVELS`: Dictionary mapping severity levels to numeric values
  - `@classmethod validate(cls)`: Validate configuration settings
  - `@classmethod has_groq_api_key(cls)`: Check if API key is available
  - `@classmethod get_groq_api_key(cls)`: Get API key from environment
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the agent."""
    
    # API Keys (fetched dynamically via get_groq_api_key)
    
    # Model settings
    DEFAULT_MODEL = "deepseek-r1-distill-llama-70b"
    TEMPERATURE = 0.1
    MAX_TOKENS = 4096
    
    # File analysis settings
    MAX_FILE_SIZE = 1024 * 1024  # 1MB
    SUPPORTED_EXTENSIONS = {
        '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cpp', '.c', '.h',
        '.cs', '.go', '.rs', '.php', '.rb', '.swift', '.kt', '.scala', '.ipynb'
    }
    
    # Analysis categories
    QUALITY_CATEGORIES = [
        "security",
        "performance", 
        "complexity",
        "code_duplication",
        "testing_gaps",
        "documentation",
        "maintainability",
        "best_practices"
    ]
    
    # Severity levels
    SEVERITY_LEVELS = {
        "critical": 4,
        "high": 3,
        "medium": 2,
        "low": 1,
        "info": 0
    }
    
    @classmethod
    def validate(cls):
        """Validate configuration."""
        if not cls.get_groq_api_key():
            raise ValueError("GROQ_API_KEY environment variable is required")
        return True

    @classmethod
    def has_groq_api_key(cls) -> bool:
        """Check if GROQ API key is available."""
        return bool(cls.get_groq_api_key().strip())

    @classmethod
    def get_groq_api_key(cls) -> str:
        """Get GROQ API key from environment each time (supports runtime overrides)."""
        # Reload .env in case it's created during runtime
        load_dotenv(override=True)
        return os.getenv("GROQ_API_KEY", "")
