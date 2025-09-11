"""
Code Quality Intelligence Agent

An AI-powered code quality analysis tool that provides comprehensive insights 
into your codebase using advanced language models and static analysis techniques.
"""

__version__ = "1.6.2"
__author__ = "Code Quality Intelligence Team"

from .agent import CodeQualityAgent
from .config import Config

__all__ = ["CodeQualityAgent", "Config"]