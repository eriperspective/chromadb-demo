# ChromaDB Demo - Complete Tutorial

A comprehensive, step-by-step guide to learning ChromaDB - a powerful vector database for semantic search and AI applications.

## What is ChromaDB?

ChromaDB is a vector database that understands the **meaning** of text, not just exact word matches. It's like having a smart search engine that can find relevant information based on context and semantics.

**Example:** If you ask "What's the hotel budget?", it will find documents about "hotel spending limits" even if those exact words aren't used!

## What You'll Learn

This tutorial covers everything from basics to advanced topics:

1. **Installation** - Setting up ChromaDB with Python 3.12
2. **Creating Collections** - Your first "smart filing cabinet"
3. **CRUD Operations** - Create, Read, Update, Delete documents
4. **Persistent Storage** - Saving data permanently to disk
5. **Managing Collections** - CRUD operations on collections themselves
6. **OpenAI Integration** - Using advanced embedding models

## Prerequisites

- Python 3.12+ (Python 3.11 also works)
- Git
- OpenAI API key (optional, only for Step 6)

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/eriperspective/chromadb-demo.git
cd chromadb-demo
```

### 2. Create and activate virtual environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Tutorial Steps

Each step is a standalone Python script with detailed comments and explanations:

### Step 1: Installation

Already completed when you installed the dependencies!

### Step 2: Create Your First Collection

```bash
python step2_create_collection.py
```

Learn how to:
- Initialize ChromaDB client
- Create a collection (like a filing cabinet drawer)
- Understand in-memory vs persistent storage

### Step 3: CRUD Operations on Documents

```bash
python step3_crud_operations.py
```

Learn how to:
- **Create:** Add documents with metadata
- **Read:** Query using natural language
- **Update:** Modify existing documents
- **Delete:** Remove documents by ID

### Step 4: Persistent Storage

```bash
python step4_persistent_storage.py
```

Learn how to:
- Use `PersistentClient` to save data to disk
- Understand the difference between in-memory and persistent storage
- Work with database files

### Step 5: Managing Collections

```bash
python step5_manage_collections.py
```

Learn how to:
- Create multiple collections
- List and retrieve collections
- Modify collection metadata
- Delete collections safely

### Step 6: OpenAI Embeddings (Advanced)

```bash
# Set your OpenAI API key first
# Windows PowerShell:
$env:OPENAI_API_KEY='your-key-here'

# Then run:
python step6_openai_embeddings.py
```

Learn how to:
- Integrate OpenAI's `text-embedding-3-small` model
- Understand tokens and costs
- Compare default vs OpenAI embeddings

## OpenAI API Key (Optional)

For Step 6, you'll need an OpenAI API key:

1. Get one at: https://platform.openai.com/api-keys
2. Set it as an environment variable:

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY='your-key-here'
```

**Windows CMD:**
```cmd
set OPENAI_API_KEY=your-key-here
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY='your-key-here'
```

## Project Structure

```
chromadb-demo/
├── step2_create_collection.py       # Creating your first collection
├── step3_crud_operations.py         # CRUD on documents
├── step4_persistent_storage.py      # Saving data to disk
├── step5_manage_collections.py      # Managing collections
├── step6_openai_embeddings.py       # Advanced: OpenAI integration
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
├── chroma_db/                       # Persistent database (auto-created)
└── README.md                        # This file!
```

## Key Concepts

### Embeddings
Text converted to numbers (vectors) that capture meaning:
- "I love dogs" → [0.2, 0.8, 0.1, ...]
- "I adore puppies" → [0.3, 0.7, 0.2, ...] (similar!)

### Collections
Like filing cabinet drawers - containers for related documents.

### Metadata
Extra information attached to documents for filtering and organization.

### Semantic Search
Finding documents by meaning, not just exact word matches.

## Use Cases

ChromaDB is perfect for:
- Document search systems
- Chatbot knowledge bases
- Q&A systems
- Semantic search engines
- Research paper organization
- Internal company knowledge bases

## Troubleshooting

### Python Version Issues
This demo requires Python 3.12 (or 3.11). If you have Python 3.14+, you may encounter compatibility issues with some dependencies.

### Virtual Environment Not Activating
Make sure you're using the correct activation command for your OS (see Installation section).

### OpenAI API Errors
- Verify your API key is set correctly
- Check you have credits in your OpenAI account
- Ensure the `openai` package is installed: `pip install openai`

## Cost Information

**Default Model (all-MiniLM-L6-v2):**
- 100% FREE
- Runs locally
- Good quality

**OpenAI Model (text-embedding-3-small):**
- $0.02 per 1 million tokens
- ~$0.00022 for 1,000 documents
- Excellent quality

## Contributing

This is a learning demo, but feel free to:
- Report issues
- Suggest improvements
- Share your own examples

## Resources

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [Vector Databases Explained](https://www.pinecone.io/learn/vector-database/)

## Learning Path

**Beginner:** Run Steps 1-4  
**Intermediate:** Complete Step 5  
**Advanced:** Tackle Step 6 with OpenAI

## License

This is a educational demo project. Feel free to use it for learning!

## Acknowledgments

Built as a teaching tool for junior developers learning vector databases and semantic search.

---

**Made for learning ChromaDB**


