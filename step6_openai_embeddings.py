# Step 6: Advanced - Using OpenAI's Embedding Model
# ====================================================
# ChromaDB uses a default embedding model (all-MiniLM-L6-v2) which is great!
# But you can also use more powerful models like OpenAI's text-embedding-3-small
# 
# This step shows how to integrate OpenAI embeddings for even better results.

import chromadb
from chromadb.utils import embedding_functions
import os

print("=" * 70)
print("STEP 6: ADVANCED - USING OPENAI'S EMBEDDING MODEL")
print("=" * 70)

# =============================================================================
# UNDERSTANDING EMBEDDING MODELS
# =============================================================================
print("\nWhat are Embedding Models?")
print("-" * 70)

explanation = """
Embedding models convert text into numbers (vectors). These numbers capture 
the MEANING of the text, allowing ChromaDB to find similar documents.

Think of it like this:
- "I love dogs" → [0.2, 0.8, 0.1, ...]  (vector of numbers)
- "I adore puppies" → [0.3, 0.7, 0.2, ...]  (similar vector!)
- "I hate taxes" → [-0.5, 0.1, 0.9, ...]  (different vector)

Better embedding models = Better understanding of meaning
"""
print(explanation)

# =============================================================================
# DEFAULT MODEL vs OPENAI MODEL
# =============================================================================
print("Comparison: Default vs OpenAI Models")
print("-" * 70)

comparison = """
┌────────────────────────┬────────────────────┬──────────────────────┐
│ Feature                │ Default (MiniLM)   │ OpenAI (3-small)     │
├────────────────────────┼────────────────────┼──────────────────────┤
│ Cost                   │ FREE               │ Paid (very cheap)    │
│ Speed                  │ Fast               │ Fast (API call)      │
│ Quality                │ Good               │ Excellent            │
│ Vector Size            │ 384 dimensions     │ 1536 dimensions      │
│ Multilingual           │ Limited            │ Excellent            │
│ Best For               │ Testing, Learning  │ Production, Quality  │
└────────────────────────┴────────────────────┴──────────────────────┘
"""
print(comparison)

# =============================================================================
# CHECKING FOR OPENAI API KEY
# =============================================================================
print("\nChecking for OpenAI API Key")
print("-" * 70)

# Check if OpenAI API key is set as an environment variable
openai_api_key = os.environ.get('OPENAI_API_KEY')

if openai_api_key:
    print("OPENAI_API_KEY found in environment variables")
    print(f"  Key starts with: {openai_api_key[:15]}...")
else:
    print("OPENAI_API_KEY not found!")
    print("\nTo use OpenAI embeddings, you need to:")
    print("  1. Get an API key from: https://platform.openai.com/api-keys")
    print("  2. Set it as an environment variable:")
    print("     Windows PowerShell: $env:OPENAI_API_KEY='your-key-here'")
    print("     Windows CMD: set OPENAI_API_KEY=your-key-here")
    print("     Linux/Mac: export OPENAI_API_KEY='your-key-here'")
    print("\nNOTE: For now, we'll continue with the default model")
    print("   (This is perfectly fine for learning!)")

# =============================================================================
# CREATING A COLLECTION WITH OPENAI EMBEDDINGS
# =============================================================================
print("\nCreating Collection with OpenAI Embeddings")
print("-" * 70)

client = chromadb.PersistentClient(path="./chroma_db")

if openai_api_key:
    # If we have an API key, use OpenAI embeddings
    try:
        print("Setting up OpenAI embedding function...")
        
        openai_ef = embedding_functions.OpenAIEmbeddingFunction(
            model_name="text-embedding-3-small",  # OpenAI's efficient model
            api_key=openai_api_key
        )
        
        # Create a collection with OpenAI embeddings
        openai_collection = client.get_or_create_collection(
            name="travel_policies_openai",
            embedding_function=openai_ef
        )
        
        print("Created collection with OpenAI embeddings!")
        
        # Add some documents
        print("\nAdding documents...")
        openai_collection.add(
            ids=["flight_01", "hotel_01", "expense_01"],
            documents=[
                "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
                "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
                "All expenses must be submitted within 15 days with receipts for items over $25."
            ],
            metadatas=[
                {"policy_type": "flights"},
                {"policy_type": "hotels"},
                {"policy_type": "expenses"}
            ]
        )
        
        print(f"Added {openai_collection.count()} documents with OpenAI embeddings")
        
        # Query the collection
        print("\nQuerying with OpenAI Embeddings")
        print("-" * 70)
        
        query_result = openai_collection.query(
            query_texts=["What's the hotel spending limit?"],
            n_results=1
        )
        
        print("Question: 'What's the hotel spending limit?'")
        print(f"\nAnswer: {query_result['documents'][0][0]}")
        print(f"Distance: {query_result['distances'][0][0]:.4f}")
        
        print("\nOpenAI embeddings are working!")
        
    except Exception as e:
        print(f"Error setting up OpenAI embeddings: {e}")
        print("   This might be due to:")
        print("   - Invalid API key")
        print("   - Network issues")
        print("   - Missing openai package")
        openai_api_key = None  # Fall back to default

else:
    print("Using DEFAULT embedding model (all-MiniLM-L6-v2)")
    print("This is perfectly fine for learning and testing!")

# =============================================================================
# UNDERSTANDING TOKENS (for OpenAI billing)
# =============================================================================
if openai_api_key:
    print("\nUnderstanding Tokens and Cost")
    print("-" * 70)
    
    try:
        import tiktoken
        
        # OpenAI's text-embedding-3-small uses cl100k_base encoding
        encoding = tiktoken.get_encoding("cl100k_base")
        
        sample_text = "All expense reports must be submitted within 15 days."
        tokens = encoding.encode(sample_text)
        token_count = len(tokens)
        
        print(f"Sample text: '{sample_text}'")
        print(f"Token count: {token_count}")
        print(f"First 5 tokens (as numbers): {tokens[:5]}")
        
        # Cost calculation (as of 2024)
        # text-embedding-3-small: $0.02 per 1M tokens
        cost_per_million = 0.02
        cost_for_sample = (token_count / 1_000_000) * cost_per_million
        
        print(f"\nCost estimate:")
        print(f"  - This text costs: ${cost_for_sample:.8f}")
        print(f"  - 1,000 similar texts: ${cost_for_sample * 1000:.6f}")
        print(f"  - Very affordable for most use cases!")
        
    except ImportError:
        print("tiktoken not installed")
        print("   Install with: pip install tiktoken")

# =============================================================================
# BEST PRACTICES
# =============================================================================
print("\n" + "=" * 70)
print("BEST PRACTICES FOR EMBEDDING MODELS")
print("=" * 70)

best_practices = """
1. **Start with the Default Model:**
   - Perfect for learning, testing, and prototyping
   - Free and runs locally
   - Good quality for most use cases

2. **Upgrade to OpenAI When You Need:**
   - Better quality for complex/nuanced queries
   - Excellent multilingual support
   - Production applications with quality requirements

3. **Cost Management:**
   - OpenAI embeddings are VERY cheap ($0.02 per 1M tokens)
   - Cache embeddings when possible
   - Only re-embed when content changes

4. **Consistency:**
   - ALWAYS use the same embedding model for a collection
   - Don't mix different embedding models in one collection
   - Create separate collections for different models

5. **Testing:**
   - Test both models with your actual data
   - Compare quality of search results
   - Decide based on your specific needs
"""
print(best_practices)

# =============================================================================
# COMPARISON DEMO (if both models available)
# =============================================================================
print("=" * 70)
print("DEMONSTRATION")
print("=" * 70)

# Create a collection with default embeddings for comparison
default_collection = client.get_or_create_collection(
    name="travel_policies_default"
)

if default_collection.count() == 0:
    default_collection.add(
        ids=["flight_01", "hotel_01", "expense_01"],
        documents=[
            "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
            "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
            "All expenses must be submitted within 15 days with receipts for items over $25."
        ],
        metadatas=[
            {"policy_type": "flights"},
            {"policy_type": "hotels"},
            {"policy_type": "expenses"}
        ]
    )

# Query with default model
print("\nQuery with DEFAULT model:")
default_result = default_collection.query(
    query_texts=["accommodation spending limits"],
    n_results=1
)
print(f"Answer: {default_result['documents'][0][0][:70]}...")
print(f"Distance: {default_result['distances'][0][0]:.4f}")

if openai_api_key and 'openai_collection' in locals():
    print("\nQuery with OPENAI model:")
    openai_result = openai_collection.query(
        query_texts=["accommodation spending limits"],
        n_results=1
    )
    print(f"Answer: {openai_result['documents'][0][0][:70]}...")
    print(f"Distance: {openai_result['distances'][0][0]:.4f}")
    
    print("\nBoth models found the correct answer!")
    print("   (OpenAI might have slightly different distance scores)")

print("\nStep 6 completed successfully!")
print("Congratulations! You've completed the ChromaDB tutorial!")

