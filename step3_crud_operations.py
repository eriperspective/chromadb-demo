# Step 3: Managing Your Data (CRUD Operations)
# ==============================================
# CRUD stands for: Create, Read, Update, Delete
# These are the fundamental operations for working with data in ChromaDB

import chromadb

# Initialize ChromaDB and create our collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="travel_policies")

print("=" * 60)
print("STEP 3: CRUD OPERATIONS ON DATA")
print("=" * 60)

# =============================================================================
# CREATE: Adding Documents to the Collection
# =============================================================================
print("\nCREATE: Adding travel policy documents...")
print("-" * 60)

# The .add() method requires:
# - ids: A unique identifier for each document (like a filing number)
# - documents: The actual text content
# - metadatas: Extra information for filtering (optional but very useful!)

collection.add(
    ids=[
        "flight_policy_01",
        "hotel_policy_01",
        "rental_car_policy_01",
        "flight_policy_02"
    ],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $250 per night in major cities. A list of preferred hotel partners is available.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval. Always select the company's insurance option.",
        "All flights, regardless of destination, must be booked through the official company travel portal, 'Concur'."
    ],
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"},
        {"policy_type": "flights", "requires_portal": "True"}
    ]
)

print(f"Added {collection.count()} documents to the collection!")

# =============================================================================
# READ: Querying Documents (The Smart Search!)
# =============================================================================
print("\nREAD: Asking questions with natural language...")
print("-" * 60)

# This is where ChromaDB shines! We can ask questions in plain English
# ChromaDB converts our question into an "embedding" (a list of numbers)
# and finds documents with similar meanings

query_question = "What is the policy for international flights?"
print(f"\nQuestion: '{query_question}'")

results = collection.query(
    query_texts=[query_question],
    n_results=2  # Get the top 2 most relevant results
)

print("\nTop 2 most relevant policies:")
for i, (doc, distance, metadata) in enumerate(zip(
    results['documents'][0],
    results['distances'][0],
    results['metadatas'][0]
), 1):
    print(f"\n  Result #{i}:")
    print(f"    Document: {doc[:80]}...")  # Show first 80 characters
    print(f"    Metadata: {metadata}")
    print(f"    Distance: {distance:.4f} (lower = more similar)")

# Let's try another query
print("\n" + "-" * 60)
query_question_2 = "How much can I spend on accommodation?"
print(f"\nQuestion: '{query_question_2}'")

results2 = collection.query(
    query_texts=[query_question_2],
    n_results=1
)

print(f"\nMost relevant policy:")
print(f"  {results2['documents'][0][0]}")

# =============================================================================
# UPDATE: Modifying Existing Documents
# =============================================================================
print("\nUPDATE: Modifying policies...")
print("-" * 60)

# The hotel budget has increased! Let's update it.
# We use .upsert() which will:
# - UPDATE the document if the ID exists
# - INSERT (create) a new one if the ID doesn't exist

collection.upsert(
    ids=["hotel_policy_01"],
    documents=["Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners."],
    metadatas=[{"policy_type": "hotels", "max_spend": 300}]
)

print("Updated hotel_policy_01 - increased budget from $250 to $300!")

# Let's add a completely new policy using upsert
collection.upsert(
    ids=["train_policy_01"],
    documents=["Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."],
    metadatas=[{"policy_type": "train", "last_updated": "2025-10-15"}]
)

print("Added new policy: train_policy_01")
print(f"Collection now has {collection.count()} documents")

# Let's verify the update worked
print("\n" + "-" * 60)
print("Verifying the hotel budget update:")
results3 = collection.query(
    query_texts=["hotel spending limit"],
    n_results=1
)
print(f"  {results3['documents'][0][0]}")

# =============================================================================
# DELETE: Removing Documents
# =============================================================================
print("\nDELETE: Removing outdated policies...")
print("-" * 60)

# The train policy was just a test. Let's remove it.
collection.delete(ids=["train_policy_01"])

print("Deleted train_policy_01")
print(f"Collection now has {collection.count()} documents")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

# Get all documents to show final state
all_docs = collection.get()
print(f"\nTotal documents in collection: {collection.count()}")
print("\nAll policy IDs:")
for doc_id in all_docs['ids']:
    print(f"  - {doc_id}")

print("\nStep 3 completed successfully!")
print("You now know how to Create, Read, Update, and Delete documents!")

