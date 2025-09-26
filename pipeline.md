## Current Project Pipeline and Task Flow

Understanding how queries and tasks flow through the Code Quality Intelligence Agent is crucial for developers working with or extending the system. The project follows distinct pipelines depending on the type of operation being performed.

### **1. Code Analysis Pipeline**

The core analysis pipeline is the most complex workflow in the system, involving multiple stages of processing, analysis, and result aggregation.

#### **Analysis Flow Description**

When a user initiates code analysis (either through CLI `analyze` command or web interface), the request flows through a carefully orchestrated pipeline that maximizes both accuracy and performance. The process begins with input validation and preprocessing, moves through multi-layered analysis stages, and concludes with comprehensive report generation.

The pipeline is designed to handle various input types (local files, directories, GitHub repositories) and scales from single-file analysis to large repository processing. It employs both static analysis tools and AI-powered insights, combining traditional code quality metrics with modern language model understanding.

#### **Analysis Pipeline Flow**

```
┌─────────────────┐
│   User Input    │ ──── CLI: python cli.py analyze <path>
│                 │ ──── Web: Streamlit interface
│                 │ ──── API: agent.analyze_codebase()
└─────────────────┘
         │
         ▼
┌─────────────────┐
│    cli.py       │ ──── Command parsing and validation
│  _run_analysis  │ ──── Environment setup (API keys, config)
│                 │ ──── Progress tracking initialization
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   config.py     │ ──── Validate configuration settings
│   Config.validate│ ──── Check API key availability
│                 │ ──── Load environment variables
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   agent.py      │ ──── Initialize CodeQualityAgent
│ CodeQualityAgent│ ──── Setup LLM connections (Groq)
│   __init__      │ ──── Initialize analyzers and RAG system
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ file_handler.py │ ──── Determine input type (local/GitHub)
│ get_code_files  │ ──── Clone repository if needed
│                 │ ──── Filter supported file types
│                 │ ──── Apply ignore patterns (.gitignore style)
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   agent.py      │ ──── Iterate through each code file
│analyze_codebase │ ──── Parallel processing for multiple files
│                 │ ──── Aggregate results and metrics
└─────────────────┘
         │
         ▼ (For each file)
┌─────────────────┐
│   agent.py      │ ──── Check file size (chunking if >1MB)
│ _analyze_file   │ ──── Detect programming language
│                 │ ──── Route to appropriate analyzer
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  analyzers.py   │ ──── Python: AST + Bandit + Radon
│ CodeAnalyzer    │ ──── JavaScript: Pattern analysis + Semgrep
│                 │ ──── Other languages: Pattern-based analysis
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   agent.py      │ ──── Send code to Groq LLM
│analysis_runnable│ ──── Parse JSON response
│                 │ ──── Merge static + LLM results
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  rag_system.py  │ ──── Add code chunks to vector database
│ add_codebase    │ ──── Generate embeddings for semantic search
│                 │ ──── Store metadata and analysis results
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   agent.py      │ ──── Aggregate all file results
│analyze_codebase │ ──── Calculate overall metrics
│                 │ ──── Generate recommendations
│                 │ ──── Sort issues by severity
└─────────────────┘
         │
         ▼
┌─────────────────┐
│report_generator │ ──── Format results for output
│     .py         │ ──── Console: Rich tables and panels
│                 │ ──── JSON: Structured data export
│                 │ ──── Markdown: Human-readable report
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Final Output   │ ──── Display results to user
│                 │ ──── Save to file if requested
│                 │ ──── Enable interactive mode if specified
└─────────────────┘
```

### **2. Interactive Chat Pipeline**

The chat functionality provides a conversational interface for discussing code quality findings, leveraging both analysis results and RAG-enhanced context retrieval.

#### **Chat Flow Description**

The interactive chat system creates a sophisticated dialogue experience where users can ask natural language questions about their codebase. The system maintains conversation context, retrieves relevant code snippets through semantic search, and provides informed responses using the analysis results as context.

The chat pipeline integrates multiple AI components: the conversational LLM for dialogue management, the RAG system for context retrieval, and the analysis engine for factual grounding. This multi-layered approach ensures responses are both conversational and technically accurate.

#### **Chat Pipeline Flow**

```
┌─────────────────┐
│  User Question  │ ──── "What security issues did you find?"
│                 │ ──── "How can I improve performance?"
│                 │ ──── "Explain this complexity issue"
└─────────────────┘
         │
         ▼
┌─────────────────┐
│    cli.py       │ ──── Interactive mode or chat command
│_interactive_mode│ ──── Input validation and preprocessing
│                 │ ──── Special command handling (exit, help)
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   chatbot.py    │ ──── Receive user message
│CodeQualityChatbot│ ──── Update conversation history
│     chat()      │ ──── Prepare context for LLM
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  rag_system.py  │ ──── Semantic search through code chunks
│get_code_context │ ──── Find relevant code snippets
│                 │ ──── Rank by similarity to question
│                 │ ──── Extract top 3-5 relevant contexts
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   chatbot.py    │ ──── Combine RAG context with analysis results
│_summarize_      │ ──── Format conversation history
│analysis_context │ ──── Prepare comprehensive context prompt
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   chatbot.py    │ ──── Send to Groq LLM with context
│  chat_chain     │ ──── Apply conversational prompt template
│                 │ ──── Generate contextual response
└─────────────────┘
         │
         ▼ (If LLM unavailable)
┌─────────────────┐
│   chatbot.py    │ ──── Pattern-based response generation
│_fallback_response│ ──── Keyword matching for topic detection
│                 │ ──── Template-based answers
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   chatbot.py    │ ──── Update conversation history
│     chat()      │ ──── Maintain context for follow-ups
│                 │ ──── Return formatted response
└─────────────────┘
         │
         ▼
┌─────────────────┐
│    cli.py       │ ──── Display response in Rich panel
│_interactive_mode│ ──── Wait for next user input
│                 │ ──── Handle conversation continuation
└─────────────────┘
```

### **3. Web Interface Pipeline**

The Streamlit web interface provides a comprehensive dashboard for code analysis with real-time interaction and visualization capabilities.

#### **Web Interface Flow Description**

The web interface serves as a user-friendly frontend that wraps all the core functionality in an interactive dashboard. Users can upload code, configure analysis parameters, view results in multiple formats, and interact with the chatbot - all through a modern web interface.

The pipeline manages session state, caches analysis results for performance, and provides real-time updates during long-running operations. The interface supports multiple analysis modes and provides rich visualizations of code quality metrics.

#### **Web Interface Pipeline Flow**

```
┌─────────────────┐
│  User Access    │ ──── Browser → http://localhost:8501
│                 │ ──── Streamlit app initialization
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Load Streamlit configuration
│    main()       │ ──── Initialize session state
│                 │ ──── Setup navigation sidebar
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Route to selected page
│ Page Navigation │ ──── Setup/Info/Analyze/Chat
│                 │ ──── Maintain state across pages
└─────────────────┘
         │
         ▼ (Analysis Page Selected)
┌─────────────────┐
│   app.py        │ ──── Collect user inputs
│ analyze_page()  │ ──── Path, branch, output format
│                 │ ──── Validation and preprocessing
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Cache analysis for performance
│@st.cache_data   │ ──── Create new event loop
│ run_analysis()  │ ──── Call agent.analyze_codebase()
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ [Same as Analysis Pipeline Above] │
│                                   │
│ Full analysis pipeline executes   │
│ with results returned to web UI   │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Process analysis results
│ analyze_page()  │ ──── Update session state
│                 │ ──── Trigger UI refresh
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Create overview metrics
│create_overview_ │ ──── Generate severity charts
│    metrics()    │ ──── Build file analysis tables
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Plotly interactive charts
│create_severity_ │ ──── Pandas data processing
│    chart()      │ ──── Rich HTML formatting
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │ ──── Initialize RAG and chatbot
│setup_rag_and_  │ ──── Set analysis context
│   chatbot()     │ ──── Enable chat interface
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Browser UI     │ ──── Interactive dashboard
│                 │ ──── Real-time chat interface
│                 │ ──── Downloadable reports
└─────────────────┘
```

### **4. RAG System Pipeline**

The RAG (Retrieval-Augmented Generation) system enables semantic search through code and provides enhanced context for AI responses.

#### **RAG Flow Description**

The RAG system transforms code into searchable vector embeddings, enabling semantic similarity search that goes beyond keyword matching. When users ask questions, the system retrieves the most relevant code chunks and provides them as context to the language model, significantly improving response accuracy and relevance.

The pipeline supports multiple RAG backends (ChromaDB, FAISS, Simple keyword-based) with automatic fallback mechanisms, ensuring the system remains functional even when advanced vector databases are unavailable.

#### **RAG Pipeline Flow**

```
┌─────────────────┐
│  Code Analysis  │ ──── Analysis results with code chunks
│   Complete      │ ──── File metadata and issues
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ rag_system.py   │ ──── Detect available RAG backends
│ _setup_rag_     │ ──── ChromaDB → FAISS → Simple RAG
│   system()      │ ──── Initialize chosen backend
└─────────────────┘
         │
         ▼ (ChromaDB Available)
┌─────────────────┐
│ rag_system.py   │ ──── Initialize ChromaDB client
│_setup_chromadb()│ ──── Create/load collection
│                 │ ──── Setup SentenceTransformer
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ rag_system.py   │ ──── Split code into semantic chunks
│ add_codebase()  │ ──── Generate embeddings for each chunk
│                 │ ──── Store with metadata (language, issues)
└─────────────────┘
         │
         ▼ (Alternative: FAISS Backend)
┌─────────────────┐
│embedding_rag.py │ ──── Custom feature extraction
│_extract_code_   │ ──── Pattern-based embeddings
│  features()     │ ──── FAISS index creation
└─────────────────┘
         │
         ▼ (Alternative: Simple Backend)
┌─────────────────┐
│ simple_rag.py   │ ──── Keyword extraction and indexing
│_index_keywords()│ ──── Function/class/variable mapping
│                 │ ──── Simple text-based search
└─────────────────┘
         │
         ▼ (Query Time)
┌─────────────────┐
│   User Query    │ ──── "Show me security issues in auth"
│                 │ ──── "Find complex functions"
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ rag_system.py   │ ──── Convert query to embeddings
│get_code_context │ ──── Similarity search in vector DB
│                 │ ──── Retrieve top K relevant chunks
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ rag_system.py   │ ──── Format retrieved chunks
│get_code_context │ ──── Add file context and metadata
│                 │ ──── Return structured context string
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   chatbot.py    │ ──── Combine RAG context with query
│     chat()      │ ──── Send enhanced prompt to LLM
│                 │ ──── Generate contextual response
└─────────────────┘
```

### **5. GitHub Integration Pipeline**

The GitHub integration enables direct analysis of remote repositories with branch support and temporary workspace management.

#### **GitHub Flow Description**

When users provide a GitHub URL, the system automatically clones the repository to a temporary directory, analyzes the code, and cleans up afterwards. This process supports branch specification, handles authentication if needed, and manages large repositories efficiently.

The pipeline includes error handling for network issues, repository access problems, and cleanup procedures to ensure no temporary files are left behind.

#### **GitHub Integration Pipeline Flow**

```
┌─────────────────┐
│ GitHub URL Input│ ──── https://github.com/user/repo
│                 │ ──── Optional branch specification
└─────────────────┘
         │
         ▼
┌─────────────────┐
│file_handler.py  │ ──── Parse GitHub URL components
│_parse_github_url│ ──── Extract owner, repo, branch
│                 │ ──── Validate URL format
└─────────────────┘
         │
         ▼
┌─────────────────┐
│file_handler.py  │ ──── Create temporary directory
│_get_files_from_ │ ──── Initialize Git client
│   github()      │ ──── Setup clone parameters
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   GitPython     │ ──── Execute git clone command
│  Repo.clone_    │ ──── Handle authentication if needed
│    from()       │ ──── Switch to specified branch
└─────────────────┘
         │
         ▼
┌─────────────────┐
│file_handler.py  │ ──── Scan cloned repository
│_get_files_from_ │ ──── Apply file filters and ignore patterns
│   local()       │ ──── Collect supported code files
└─────────────────┘
         │
         ▼
┌─────────────────┐
│ [Standard Analysis Pipeline] │
│                               │
│ Files processed through       │
│ normal analysis workflow      │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│file_handler.py  │ ──── Remove temporary directory
│   cleanup()     │ ──── Clean up cloned repository
│                 │ ──── Free system resources
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Analysis       │ ──── Return results to user
│  Results        │ ──── No local files remain
└─────────────────┘
```

### **Pipeline Characteristics**

#### **Error Handling**
Each pipeline includes comprehensive error handling:
- **Network failures**: Retry mechanisms and graceful degradation
- **API limits**: Rate limiting and fallback strategies  
- **File system errors**: Permission handling and cleanup procedures
- **Memory constraints**: Chunking for large files and streaming processing

#### **Performance Optimization**
- **Caching**: Analysis results cached in web interface
- **Parallel processing**: Multiple files analyzed concurrently
- **Lazy loading**: RAG systems initialized only when needed
- **Resource management**: Automatic cleanup of temporary resources

#### **Scalability Features**
- **Chunked analysis**: Large files processed in segments
- **Streaming responses**: Real-time progress updates
- **Modular architecture**: Easy to add new analysis tools
- **Configurable limits**: File size and count restrictions

This pipeline architecture ensures robust, scalable, and maintainable code quality analysis across all supported interfaces and use cases.
