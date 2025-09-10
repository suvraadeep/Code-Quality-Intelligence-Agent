# Quick Start Guide - Code Quality Intelligence Agent Web Interface

## Quick Launch

### Option 1: Using the launcher script
```bash
cd Webpage
python launch.py
```

### Option 2: Direct Streamlit command
```bash
cd Webpage
streamlit run app.py
```

### Option 3: Using batch file (Windows)
```bash
cd Webpage
launch.bat
```

## 📋 Prerequisites

1. **Install the main package:**
   ```bash
   pip install code-quality-intelligence
   ```

2. **Install web dependencies:**
   ```bash
   cd Webpage
   pip install streamlit pandas plotly
   ```

## Access the Web Interface

Once launched, the application will be available at:
- **URL:** http://localhost:8501
- **Port:** 8501 (default)

## Available Features

### Home Page
- Welcome screen with feature overview
- Getting started guide
- Supported languages list

### Setup Page
- Configure Groq API key (optional)
- Check system dependencies
- View system status

### Info Page
- Quick codebase statistics
- Language distribution analysis
- File count and size information

### Analyze Page
- Full code quality analysis
- Multiple output formats (Console, JSON, Markdown)
- Interactive mode
- Visual reports and charts
- Support for local files and GitHub repositories

### Chat Page
- Enhanced conversational AI
- RAG-powered code discussions
- Context-aware responses

## Supported File Types

- **Local Analysis:** Files and directories on your system
- **GitHub Analysis:** Public repositories via URL
- **Languages:** Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, Scala

## Configuration

### API Key Setup (Optional)
1. Go to the **Setup** page
2. Enter your Groq API key
3. Click "Save API Key"

*Note: The application works without an API key for basic analysis, but requires it for advanced AI features.*

## Troubleshooting

### Common Issues

1. **Import Error:**
   ```bash
   pip install code-quality-intelligence
   ```

2. **Missing Dependencies:**
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Port Already in Use:**
   - Change port: `streamlit run app.py --server.port 8502`

4. **Analysis Errors:**
   - Check file paths and permissions
   - Ensure the target directory contains supported code files

### Getting Help

- Check the **Setup** page for dependency status
- Use the **Info** page for quick diagnostics
- Review error messages in the analysis results

## Example Usage

1. **Analyze Local Code:**
   - Go to **Analyze** page
   - Select "Local Path"
   - Enter path: `./my-project`
   - Click "Analyze Code"

2. **Analyze GitHub Repository:**
   - Go to **Analyze** page
   - Select "GitHub Repository"
   - Enter URL: `https://github.com/user/repo`
   - Click "Analyze Code"

3. **Chat with Your Code:**
   - Go to **Chat** page
   - Enter path or GitHub URL
   - Start asking questions about your code

