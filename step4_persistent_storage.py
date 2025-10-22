# Step 4: Persistent Storage
# ============================
# So far, we've used chromadb.Client() which stores data in memory (RAM).
# This means data disappears when the program ends!
# 
# PersistentClient saves data to disk, so it persists between program runs.

import chromadb
import os

print("=" * 60)
print("STEP 4: PERSISTENT STORAGE")
print("=" * 60)

# =============================================================================
# THE PROBLEM: In-Memory Storage
# =============================================================================
print("\nTHE PROBLEM: In-Memory Storage")
print("-" * 60)
print("When using chromadb.Client(), data lives in RAM:")
print("  - Fast and great for testing")
print("  - Data disappears when program ends")
print("  - Can't share data between program runs")

# =============================================================================
# THE SOLUTION: PersistentClient
# =============================================================================
print("\nTHE SOLUTION: PersistentClient")
print("-" * 60)

# Create a PersistentClient that saves data to a folder
# The "path" parameter tells ChromaDB where to store the database files
# If the folder doesn't exist, ChromaDB will create it for you!

persistent_client = chromadb.PersistentClient(path="./chroma_db")

print("Created PersistentClient")
print(f"Database files will be saved in: {os.path.abspath('./chroma_db')}")

# =============================================================================
# WORKING WITH PERSISTENT COLLECTIONS
# =============================================================================
print("\nCreating a Persistent Collection")
print("-" * 60)

# Everything else works exactly the same as before!
# The only difference is that now the data is saved to disk

p_collection = persistent_client.get_or_create_collection(name="saved_policies")

print(f"Collection '{p_collection.name}' created (or retrieved if it existed)")
print(f"Current document count: {p_collection.count()}")

# =============================================================================
# ADDING DATA THAT PERSISTS
# =============================================================================
print("\nAdding Data That Will Persist")
print("-" * 60)

# Let's check if we already have data from a previous run
if p_collection.count() > 0:
    print("Collection already has data from a previous run!")
    print("   This proves persistence is working!")
    print(f"   Documents in collection: {p_collection.count()}")
else:
    # First time running - let's add some data
    print("First time running - adding initial data...")
    
    p_collection.add(
        ids=["saved_policy_01", "saved_policy_02", "saved_policy_03"],
        documents=[
            "All expense reports must be submitted within 15 days of trip completion.",
            "Travel insurance is mandatory for all international trips exceeding 7 days.",
            "Receipts must be provided for all expenses over $25."
        ],
        metadatas=[
            {"policy_type": "expenses", "category": "reporting"},
            {"policy_type": "insurance", "category": "international"},
            {"policy_type": "expenses", "category": "documentation"}
        ]
    )
    
    print(f"Added {p_collection.count()} documents")
    print("Data is now saved to disk!")

# =============================================================================
# QUERYING PERSISTENT DATA
# =============================================================================
print("\nQuerying the Persistent Data")
print("-" * 60)

query_result = p_collection.query(
    query_texts=["When do I need to submit expenses?"],
    n_results=1
)

print("Question: 'When do I need to submit expenses?'")
print(f"\nAnswer: {query_result['documents'][0][0]}")
print(f"Metadata: {query_result['metadatas'][0][0]}")

# =============================================================================
# DEMONSTRATING PERSISTENCE
# =============================================================================
print("\nTesting Persistence")
print("-" * 60)
print("Try this:")
print("  1. Run this script again")
print("  2. Notice that the data is still there!")
print("  3. Check the './chroma_db' folder - you'll see database files")
print("")
print("This is the power of PersistentClient - your data survives!")

# =============================================================================
# VIEWING ALL STORED DATA
# =============================================================================
print("\nAll Stored Policies")
print("-" * 60)

all_data = p_collection.get()
print(f"Total documents: {len(all_data['ids'])}")
print("\nStored policy IDs:")
for policy_id in all_data['ids']:
    print(f"  - {policy_id}")

# =============================================================================
# COMPARING: In-Memory vs Persistent
# =============================================================================
print("\n" + "=" * 60)
print("COMPARISON: In-Memory vs Persistent")
print("=" * 60)

comparison = """
┌─────────────────────┬──────────────────┬────────────────────┐
│ Feature             │ Client()         │ PersistentClient() │
├─────────────────────┼──────────────────┼────────────────────┤
│ Speed               │ Very Fast        │ Slightly Slower    │
│ Data Persists?      │ No (RAM only)    │ Yes (Saved to disk)│
│ Good for Testing?   │ Yes              │ Yes                │
│ Good for Production?│ No               │ Yes                │
│ Survives Restart?   │ No               │ Yes                │
└─────────────────────┴──────────────────┴────────────────────┘

NOTE: Use Client() for quick tests and experiments
NOTE: Use PersistentClient() when you need to save your data!
"""

print(comparison)

print("\nStep 4 completed successfully!")
print("Your data is now safely stored on disk!")

