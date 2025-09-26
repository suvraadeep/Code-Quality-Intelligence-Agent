## Sample Run: Complete Execution Trace

To understand how the Code Quality Intelligence Agent works in practice, let's trace a complete analysis run with detailed input/output at each stage.

### **Sample Input**

**Command**: `python cli.py analyze ./sample_code/auth_service.py --interactive --format json --output report.json`

**Target File (`auth_service.py`)**:
```python
import hashlib
import jwt
from datetime import datetime

# Hardcoded secret key - SECURITY ISSUE
SECRET_KEY = "my_secret_123"

class AuthService:
    def __init__(self):
        self.users = {}
        
    def hash_password(self, password):
        # Weak hashing - SECURITY ISSUE
        return hashlib.md5(password.encode()).hexdigest()
    
    def authenticate_user(self, username, password):
        # SQL injection vulnerable - SECURITY ISSUE
        query = f"SELECT * FROM users WHERE username='{username}'"
        
        if username in self.users:
            stored_hash = self.users[username]
            input_hash = self.hash_password(password)
            
            # Complex nested conditions - COMPLEXITY ISSUE
            if input_hash == stored_hash:
                if len(password) > 8:
                    if any(c.isdigit() for c in password):
                        if any(c.isupper() for c in password):
                            if any(c.islower() for c in password):
                                return self.generate_token(username)
                            else:
                                return None
                        else:
                            return None
                    else:
                        return None
                else:
                    return None
            else:
                return None
        return None
    
    def generate_token(self, username):
        payload = {
            'username': username,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
```

### **Detailed Execution Trace**

#### **Stage 1: CLI Entry Point**

**File**: `cli.py`
**Function**: `analyze()`

**Input**:
```
path = "./sample_code/auth_service.py"
output = "report.json"
format = "json"
interactive = True
groq_key = None
branch = None
```

**Processing**:
```python
# cli.py:105-123
def analyze(path, output, format, interactive, groq_key, branch):
    if groq_key:
        os.environ['GROQ_API_KEY'] = groq_key
    
    try:
        Config.validate()  # Calls config.py
    except ValueError as e:
        console.print(f"[red]❌ Configuration Error: {e}[/red]")
        sys.exit(1)
    
    asyncio.run(_run_analysis(path, output, format, interactive, branch))
```

**Output**: Proceeds to `_run_analysis()` with validated configuration

#### **Stage 2: Configuration Validation**

**File**: `config.py`
**Function**: `Config.validate()`

**Input**: Environment variables check
**Processing**:
```python
# config.py:48-53
@classmethod
def validate(cls):
    if not cls.get_groq_api_key():
        raise ValueError("GROQ_API_KEY environment variable is required")
    return True

@classmethod
def get_groq_api_key(cls) -> str:
    load_dotenv(override=True)
    return os.getenv("GROQ_API_KEY", "")
```

**Output**: 
```
✅ Configuration valid
GROQ_API_KEY: "gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" (loaded from environment)
```

#### **Stage 3: Agent Initialization**

**File**: `agent.py`
**Function**: `CodeQualityAgent.__init__()`

**Input**: Configuration from previous stage
**Processing**:
```python
# agent.py:27-51
def __init__(self):
    Config.validate()
    
    self.llm = ChatGroq(
        groq_api_key=Config.get_groq_api_key(),
        model_name="deepseek-r1-distill-llama-70b",
        temperature=0.1,
        max_tokens=4096
    )
    
    self.memory = ConversationBufferMemory(return_messages=True)
    self.analyzer = CodeAnalyzer()  # From analyzers.py
    self.report_generator = ReportGenerator()  # From report_generator.py
    self.file_handler = FileHandler()  # From file_handler.py
    
    # Initialize RAG system
    self.rag_system = CodeRAGSystem()  # From rag_system.py
    self.chatbot = CodeQualityChatbot(self.rag_system)  # From chatbot.py
    
    self._setup_analysis_chain()
    self._setup_qa_chain()
```

**Output**:
```
✅ LLM initialized: ChatGroq(model="deepseek-r1-distill-llama-70b")
✅ Analyzers initialized: Bandit, Radon, Semgrep available
✅ RAG system initialized: ChromaDB backend
✅ Analysis chains configured
```

#### **Stage 4: File Handler Processing**

**File**: `file_handler.py`
**Function**: `get_code_files()`

**Input**: `path = "./sample_code/auth_service.py"`
**Processing**:
```python
# file_handler.py:24-29
def get_code_files(self, path: str, branch: Optional[str] = None) -> List[Path]:
    if self._is_github_url(path):
        return self._get_files_from_github(path, branch=branch)
    else:
        return self._get_files_from_local(path)

# file_handler.py:115-140
def _get_files_from_local(self, path: str) -> List[Path]:
    path_obj = Path(path)
    
    if not path_obj.exists():
        return []
    
    code_files = []
    
    if path_obj.is_file():
        if self._is_supported_file(path_obj):
            code_files.append(path_obj)
```

**Output**:
```
✅ File type: Local file
✅ Path exists: ./sample_code/auth_service.py
✅ Supported extension: .py
✅ File size: 1,247 bytes (within limits)
Files to analyze: [Path('./sample_code/auth_service.py')]
```

#### **Stage 5: Language Detection**

**File**: `file_handler.py`
**Function**: `detect_language()`

**Input**: `Path('./sample_code/auth_service.py')`
**Processing**:
```python
# file_handler.py:173-196
def detect_language(self, file_path: Path) -> str:
    extension_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'typescript',
        # ... more mappings
    }
    
    return extension_map.get(file_path.suffix.lower(), 'unknown')
```

**Output**: `language = "python"`

#### **Stage 6: Static Analysis**

**File**: `analyzers.py`
**Function**: `analyze_python_file()`

**Input**: 
```
file_path = Path('./sample_code/auth_service.py')
content = [file contents as shown above]
```

**Processing**:

**6a. AST Analysis**:
```python
# analyzers.py:66-70
try:
    tree = ast.parse(content)
    results.update(self._analyze_python_ast(tree, content))
except SyntaxError as e:
    results['syntax_errors'] = [str(e)]
```

**AST Analysis Output**:
```python
{
    'complexity_issues': [
        {
            'line': 18,
            'type': 'high_complexity',
            'message': 'Function "authenticate_user" has high complexity (12)',
            'severity': 'medium'
        }
    ],
    'style_issues': [
        {
            'line': 8,
            'type': 'missing_docstring',
            'message': 'Class "AuthService" missing docstring',
            'severity': 'low'
        }
    ]
}
```

**6b. Bandit Security Analysis**:
```python
# analyzers.py:73-76
if self.available_tools['bandit']:
    results['security_issues'].extend(
        self._run_bandit_analysis(file_path)
    )
```

**Bandit Output**:
```python
[
    {
        'line': 6,
        'type': 'security',
        'test_id': 'B105',
        'message': 'Hardcoded password string',
        'severity': 'medium',
        'confidence': 'medium',
        'code': 'SECRET_KEY = "my_secret_123"'
    },
    {
        'line': 12,
        'type': 'security', 
        'test_id': 'B303',
        'message': 'Use of insecure MD5 hash function',
        'severity': 'medium',
        'confidence': 'high',
        'code': 'return hashlib.md5(password.encode()).hexdigest()'
    }
]
```

**6c. Radon Complexity Analysis**:
```python
# analyzers.py:78-82
if self.available_tools['radon']:
    results['metrics'].update(
        self._run_radon_analysis(content)
    )
```

**Radon Output**:
```python
{
    'cyclomatic_complexity': [
        {
            'name': 'authenticate_user',
            'complexity': 12,
            'lineno': 15
        }
    ],
    'maintainability_index': 65.2,
    'halstead': {
        'difficulty': 8.5,
        'effort': 1250.3,
        'volume': 147.1
    }
}
```

**6d. Pattern-based Analysis**:
```python
# analyzers.py:88-89
results = self._augment_python_with_patterns(content, results)
```

**Pattern Analysis Output**:
```python
{
    'security_issues': [
        {
            'line': 16,
            'type': 'pattern',
            'message': 'Possible SQL string formatting in query (f-string)',
            'severity': 'high',
            'code': 'query = f"SELECT * FROM users WHERE username=\'{username}\'"'
        }
    ]
}
```

**Combined Static Analysis Output**:
```python
{
    'security_issues': [
        {'line': 6, 'type': 'security', 'message': 'Hardcoded password string', 'severity': 'medium'},
        {'line': 12, 'type': 'security', 'message': 'Use of insecure MD5 hash function', 'severity': 'medium'},
        {'line': 16, 'type': 'pattern', 'message': 'Possible SQL string formatting', 'severity': 'high'}
    ],
    'complexity_issues': [
        {'line': 18, 'type': 'high_complexity', 'message': 'Function has high complexity (12)', 'severity': 'medium'}
    ],
    'style_issues': [
        {'line': 8, 'type': 'missing_docstring', 'message': 'Class missing docstring', 'severity': 'low'}
    ],
    'metrics': {
        'cyclomatic_complexity': [{'name': 'authenticate_user', 'complexity': 12, 'lineno': 15}],
        'maintainability_index': 65.2
    }
}
```

#### **Stage 7: LLM Analysis with LangChain**

**File**: `agent.py`
**Function**: `_analyze_file()` → `analysis_runnable.ainvoke()`

**Input to LLM**:
```python
# agent.py:218-225
response = await self.analysis_runnable.ainvoke({
    "code": content,
    "language": "python", 
    "filename": "auth_service.py"
})
```

**LangChain Chain Configuration**:
```python
# agent.py:53-67
def _setup_analysis_chain(self):
    analysis_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert code quality analyst. Return STRICT JSON only, no prose."),
        ("human",
         "Analyze the following {language} code from file {filename} and identify quality issues.\n\n"
         "Focus on: security, performance, complexity, duplication, testing, documentation, maintainability, best_practices.\n\n"
         "Code to analyze:\n```{language}\n{code}\n```\n\n"
         "Respond with a JSON object with keys: issues (array), metrics (object), summary (string).")
    ])

    self.analysis_runnable = analysis_prompt | self.llm | StrOutputParser()
```

**LLM Request to Groq**:
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an expert code quality analyst. Return STRICT JSON only, no prose."
    },
    {
      "role": "human", 
      "content": "Analyze the following python code from file auth_service.py and identify quality issues.\n\nFocus on: security, performance, complexity, duplication, testing, documentation, maintainability, best_practices.\n\nCode to analyze:\n```python\n[full code content]\n```\n\nRespond with a JSON object with keys: issues (array), metrics (object), summary (string)."
    }
  ],
  "model": "deepseek-r1-distill-llama-70b",
  "temperature": 0.1,
  "max_tokens": 4096
}
```

**LLM Response from Groq**:
```json
{
  "issues": [
    {
      "category": "security",
      "severity": "critical",
      "line_number": 6,
      "title": "Hardcoded Secret Key",
      "description": "Secret key is hardcoded in source code, making it accessible to anyone with code access",
      "suggestion": "Move secret key to environment variables or secure configuration",
      "code_snippet": "SECRET_KEY = \"my_secret_123\""
    },
    {
      "category": "security", 
      "severity": "high",
      "line_number": 12,
      "title": "Weak Password Hashing",
      "description": "MD5 is cryptographically broken and unsuitable for password hashing",
      "suggestion": "Use bcrypt, scrypt, or Argon2 for secure password hashing",
      "code_snippet": "return hashlib.md5(password.encode()).hexdigest()"
    },
    {
      "category": "security",
      "severity": "critical", 
      "line_number": 16,
      "title": "SQL Injection Vulnerability",
      "description": "Direct string interpolation in SQL query allows SQL injection attacks",
      "suggestion": "Use parameterized queries or ORM to prevent SQL injection",
      "code_snippet": "query = f\"SELECT * FROM users WHERE username='{username}'\""
    },
    {
      "category": "complexity",
      "severity": "high",
      "line_number": 18,
      "title": "Excessive Cyclomatic Complexity",
      "description": "authenticate_user function has deeply nested conditions making it hard to maintain",
      "suggestion": "Refactor using early returns and extract validation logic into separate methods",
      "code_snippet": "if input_hash == stored_hash:\n    if len(password) > 8:\n        if any(c.isdigit()..."
    },
    {
      "category": "maintainability",
      "severity": "medium",
      "line_number": 8,
      "title": "Missing Class Documentation", 
      "description": "AuthService class lacks docstring explaining its purpose and usage",
      "suggestion": "Add comprehensive docstring describing class responsibilities",
      "code_snippet": "class AuthService:"
    },
    {
      "category": "best_practices",
      "severity": "medium",
      "line_number": 15,
      "title": "Missing Error Handling",
      "description": "No exception handling for potential JWT encoding errors or database operations",
      "suggestion": "Add try-catch blocks for external operations and provide meaningful error messages",
      "code_snippet": "def authenticate_user(self, username, password):"
    }
  ],
  "metrics": {
    "complexity_score": 12.0,
    "maintainability_score": 45.0,
    "security_score": 25.0,
    "overall_score": 35.0
  },
  "summary": "This authentication service has critical security vulnerabilities including hardcoded secrets, weak password hashing, and SQL injection risks. The code also suffers from high complexity and poor maintainability due to deeply nested conditions."
}
```

#### **Stage 8: Result Merging**

**File**: `agent.py`
**Function**: `_analyze_file()` - Result merging logic

**Input**: Static analysis results + LLM analysis results
**Processing**:
```python
# agent.py:235-253
# Normalize and merge issues
merged_issues = []
for issue in llm_analysis.get("issues", []):
    issue["file_path"] = str(file_path)
    merged_issues.append(issue)

# Map static findings into common issue format
def add_static(group, items, category, default_severity="medium"):
    for it in items:
        merged_issues.append({
            "category": category,
            "severity": it.get("severity", default_severity),
            "line_number": it.get("line", 0),
            "title": it.get("type", group),
            "description": it.get("message", "Static analysis finding"),
            "suggestion": "",
            "code_snippet": it.get("code", ""),
            "file_path": str(file_path)
        })

add_static("security_issues", static_results.get("security_issues", []), "security")
add_static("complexity_issues", static_results.get("complexity_issues", []), "complexity")
add_static("style_issues", static_results.get("style_issues", []), "maintainability", "low")
```

**Merged Output**:
```python
{
    "issues": [
        # LLM issues (6 items) + Static issues (5 items) = 11 total issues
        # Duplicates removed, severity-sorted
    ],
    "metrics": {
        "complexity_score": 12.0,  # From LLM
        "maintainability_score": 45.0,  # From LLM  
        "security_score": 25.0,  # From LLM
        "overall_score": 35.0  # From LLM
    },
    "summary": "Combined analysis summary...",
    "debug": {
        "language": "python",
        "static_counts": {"security": 3, "complexity": 1, "style": 1},
        "merged_issue_count": 11
    }
}
```

#### **Stage 9: RAG System Integration**

**File**: `rag_system.py`
**Function**: `add_codebase()`

**Input**: 
```
files = [Path('./sample_code/auth_service.py')]
analysis_results = [merged analysis from Stage 8]
```

**Processing**:
```python
# rag_system.py:189-258
def add_codebase(self, files: List[Path], analysis_results: Dict[str, Any]) -> bool:
    documents = []
    metadatas = []
    ids = []
    
    for file_path in files:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        chunks = self.text_splitter.split_text(content)
        
        file_analysis = analysis_results.get('file_analyses', {}).get(str(file_path), {})
        issues = file_analysis.get('issues', [])
        
        for i, chunk in enumerate(chunks):
            chunk_id = hashlib.md5(f"{file_path}_{i}_{chunk[:100]}".encode()).hexdigest()
            
            metadata = {
                "file_path": str(file_path),
                "file_name": file_path.name,
                "language": "python",
                "chunk_index": i,
                "has_issues": len(issues) > 0,
                "issue_count": len(issues),
                "complexity_score": 12.0
            }
            
            documents.append(chunk)
            metadatas.append(metadata) 
            ids.append(chunk_id)
    
    self.collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
```

**Output**:
```
✅ Added 3 code chunks to ChromaDB
✅ Generated embeddings using SentenceTransformer
✅ Stored metadata with issue counts and complexity scores
```

#### **Stage 10: Final Result Aggregation**

**File**: `agent.py`
**Function**: `analyze_codebase()` - Final aggregation

**Input**: Individual file analysis results
**Processing**:
```python
# agent.py:169-191
# Sort issues by severity
all_issues.sort(key=lambda x: Config.SEVERITY_LEVELS.get(x.get("severity", "info"), 0), reverse=True)

results = {
    "summary": {
        "total_files": len(files),
        "total_issues": len(all_issues), 
        "metrics": overall_metrics
    },
    "issues": all_issues,
    "file_analyses": file_analyses,
    "recommendations": self._generate_recommendations(all_issues)
}
```

**Final Analysis Output**:
```python
{
    "summary": {
        "total_files": 1,
        "total_issues": 11,
        "metrics": {
            "complexity_score": 12.0,
            "maintainability_score": 45.0,
            "security_score": 25.0,
            "overall_score": 35.0
        }
    },
    "issues": [
        {
            "category": "security",
            "severity": "critical",
            "line_number": 6,
            "title": "Hardcoded Secret Key",
            "description": "Secret key is hardcoded in source code",
            "suggestion": "Move secret key to environment variables",
            "file_path": "./sample_code/auth_service.py"
        },
        {
            "category": "security", 
            "severity": "critical",
            "line_number": 16,
            "title": "SQL Injection Vulnerability",
            "description": "Direct string interpolation in SQL query allows attacks",
            "suggestion": "Use parameterized queries",
            "file_path": "./sample_code/auth_service.py"
        }
        // ... 9 more issues
    ],
    "recommendations": [
        "🚨 Address critical security and performance issues immediately",
        "🔒 Consider implementing a security review process", 
        "🧩 Refactor complex functions to improve maintainability"
    ]
}
```

#### **Stage 11: Report Generation**

**File**: `report_generator.py`
**Function**: `generate_json_report()`

**Input**: Final analysis results
**Processing**:
```python
# report_generator.py:272-291
def generate_json_report(self, analysis_results: Dict[str, Any], output_path: str) -> None:
    try:
        report_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'version': '1.0.0',
                'tool': 'Code Quality Intelligence Agent'
            },
            'analysis': analysis_results
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
```

**Final JSON Report (`report.json`)**:
```json
{
  "metadata": {
    "generated_at": "2024-01-15T14:30:45.123456",
    "version": "1.0.0", 
    "tool": "Code Quality Intelligence Agent"
  },
  "analysis": {
    "summary": {
      "total_files": 1,
      "total_issues": 11,
      "metrics": {
        "complexity_score": 12.0,
        "maintainability_score": 45.0,
        "security_score": 25.0,
        "overall_score": 35.0
      }
    },
    "issues": [
      {
        "category": "security",
        "severity": "critical",
        "line_number": 6,
        "title": "Hardcoded Secret Key",
        "description": "Secret key is hardcoded in source code, making it accessible to anyone with code access",
        "suggestion": "Move secret key to environment variables or secure configuration",
        "code_snippet": "SECRET_KEY = \"my_secret_123\"",
        "file_path": "./sample_code/auth_service.py"
      }
      // ... complete issue list
    ],
    "recommendations": [
      "🚨 Address critical security and performance issues immediately",
      "🔒 Consider implementing a security review process",
      "🧩 Refactor complex functions to improve maintainability"
    ]
  }
}
```

#### **Stage 12: Interactive Chat Mode**

**File**: `cli.py` → `chatbot.py`
**Function**: Interactive Q&A session

**User Question**: "What are the most critical security issues?"

**Processing Flow**:

**12a. Question Processing**:
```python
# chatbot.py:102-144
def chat(self, message: str) -> str:
    # Get RAG context
    rag_context = ""
    if self.rag_system and self.rag_system.is_available():
        rag_context = self.rag_system.get_code_context(message, self.analysis_context)
    
    # Prepare conversation history
    history_text = self._format_conversation_history()
    analysis_summary = self._summarize_analysis_context()
```

**12b. RAG Context Retrieval**:
```python
# rag_system.py:316-344
def get_code_context(self, question: str, analysis_results: Dict[str, Any]) -> str:
    relevant_chunks = self.search_similar_code(question, n_results=3)
    
    context_parts = []
    for chunk in relevant_chunks:
        metadata = chunk['metadata']
        content = chunk['content']
        
        context_part = f"""
File: {metadata['file_name']} ({metadata['language']})
Issues: {metadata['issue_count']} | Complexity: {metadata.get('complexity_score', 0)}

Code:
```{metadata['language']}
{content[:500]}
```
"""
        context_parts.append(context_part)
    
    return "\n---\n".join(context_parts)
```

**RAG Context Output**:
```
File: auth_service.py (python)
Issues: 11 | Complexity: 12.0

Code:
```python
# Hardcoded secret key - SECURITY ISSUE  
SECRET_KEY = "my_secret_123"

class AuthService:
    def __init__(self):
        self.users = {}
        
    def hash_password(self, password):
        # Weak hashing - SECURITY ISSUE
        return hashlib.md5(password.encode()).hexdigest()
```
```

**12c. LLM Chat Response**:
```python
# chatbot.py:116-123
response = self.chat_chain.invoke({
    "analysis_context": analysis_summary,
    "rag_context": rag_context,
    "conversation_history": history_text,
    "question": message
})
```

**Chat LLM Request**:
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an expert code quality assistant with a friendly, conversational personality..."
    },
    {
      "role": "human",
      "content": "Analysis Context:\nFiles analyzed: 1 | Total issues: 11 | Complexity score: 12.0 | Issues by severity: critical: 2, high: 2, medium: 4, low: 3\n\nRAG Context:\n[code context from above]\n\nUser Question: What are the most critical security issues?"
    }
  ]
}
```

**Chat Response**:
```
The most critical security issues in your authentication service are:

🚨 **Critical Issues:**

1. **Hardcoded Secret Key** (Line 6)
   - Your JWT secret key "my_secret_123" is hardcoded directly in the source code
   - This means anyone with access to your code can forge JWT tokens
   - **Fix**: Move this to an environment variable: `SECRET_KEY = os.getenv('JWT_SECRET_KEY')`

2. **SQL Injection Vulnerability** (Line 16)
   - You're using f-string formatting directly in your SQL query
   - An attacker could inject malicious SQL: `username="'; DROP TABLE users; --"`
   - **Fix**: Use parameterized queries: `cursor.execute("SELECT * FROM users WHERE username=?", (username,))`

🔴 **High Priority Issue:**

3. **Weak Password Hashing** (Line 12)
   - MD5 is cryptographically broken and unsuitable for passwords
   - It's fast and vulnerable to rainbow table attacks
   - **Fix**: Use bcrypt: `import bcrypt; bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())`

These three issues could lead to complete system compromise. I'd recommend fixing them immediately before deploying to production. Would you like me to show you specific code examples for the fixes?
```
