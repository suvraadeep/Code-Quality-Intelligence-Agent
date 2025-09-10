# Code Quality Intelligence Agent - Web Interface

A comprehensive Streamlit web application that provides all CLI functionality for analyzing code quality in local files and GitHub repositories.

## Features

### Complete CLI Functionality
- **Analyze**: Full code analysis with multiple output formats (Console, JSON, Markdown)
- **Setup**: Configure API keys and check dependencies
- **Info**: Quick codebase statistics and language distribution
- **Chat**: Enhanced interactive chat with RAG capabilities
- **Dashboard**: Visual reports with charts and graphs

### Analysis Capabilities
- **Security Analysis**: Detect vulnerabilities and security issues
- **Performance Analysis**: Identify performance bottlenecks
- **Code Quality**: Complexity, maintainability, and style analysis
- **Best Practices**: Suggest improvements and optimizations

### Web Interface
- **Multi-page Navigation**: Easy access to all features
- **Real-time Analysis**: Live progress updates and results
- **Interactive Charts**: Visual representation of analysis results
- **Chat Interface**: Conversational AI for code discussions
- **RAG System**: Semantic search through large codebases

## Installation

1. Install the package:
```bash
pip install code-quality-intelligence
```

2. Install web interface dependencies:
```bash
cd Webpage
pip install -r requirements.txt
```

## Usage

### Launch the Web Interface
```bash
cd Webpage
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Available Pages

#### Home
- Welcome page with feature overview
- Getting started guide
- Supported languages list

#### Setup
- Configure Groq API key
- Check dependencies
- System status

#### Info
- Quick codebase statistics
- Language distribution
- File count and size analysis

#### Analyze
- Full code quality analysis
- Multiple output formats
- Interactive mode
- Visual reports and charts

#### Chat
- Enhanced conversational AI
- RAG-powered code discussions
- Context-aware responses

## Configuration

### API Key Setup
1. Go to the **Setup** page
2. Enter your Groq API key (optional for basic analysis)
3. Click "Save API Key"

### Analysis Types
- **Local Path**: Analyze local files and directories
- **GitHub Repository**: Analyze repositories directly from GitHub

## Supported Languages

- Python
- JavaScript
- TypeScript
- Java
- C++
- C#
- Go
- Rust
- PHP
- Ruby
- Swift
- Kotlin
- Scala

## CLI Commands Available

All CLI functionality is available through the web interface:

- `analyze` - Full code analysis with multiple output formats
- `setup` - Configure API keys and dependencies
- `info` - Quick codebase information
- `dashboard` - Launch this web interface
- `chat` - Enhanced interactive chat session

## Features Comparison

| Feature | CLI | Web Interface |
|---------|-----|---------------|
| Code Analysis | ✅ | ✅ |
| GitHub Integration | ✅ | ✅ |
| Multiple Output Formats | ✅ | ✅ |
| Interactive Chat | ✅ | ✅ |
| RAG System | ✅ | ✅ |
| Visual Reports | ❌ | ✅ |
| Real-time Progress | ❌ | ✅ |
| Multi-page Navigation | ❌ | ✅ |
| Dependency Check | ✅ | ✅ |
| API Key Management | ✅ | ✅ |

## Troubleshooting

### Common Issues

1. **Import Error**: Ensure the package is installed
   ```bash
   pip install code-quality-intelligence
   ```

2. **Missing Dependencies**: Install requirements
   ```bash
   pip install -r requirements.txt
   ```

3. **API Key Issues**: Check the Setup page for configuration

4. **Analysis Errors**: Check file paths and permissions

### Getting Help

- Check the Setup page for dependency status
- Use the Info page for quick diagnostics
- Review error messages in the analysis results

## Development

### Running in Development Mode
```bash
cd Webpage
streamlit run app.py --server.runOnSave true
```

### Adding New Features
The web interface is modular and can be extended by:
- Adding new pages to the navigation
- Creating new components in the `components/` folder
- Extending the analysis capabilities

## License

This project is licensed under the same terms as the main Code Quality Intelligence Agent package.
