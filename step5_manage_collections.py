# Step 5: Managing Collections (CRUD on Collections)
# ====================================================
# In Step 3, we learned CRUD on DOCUMENTS (the data inside collections)
# Now we'll learn CRUD on COLLECTIONS themselves (the containers)

import chromadb

print("=" * 60)
print("STEP 5: CRUD OPERATIONS ON COLLECTIONS")
print("=" * 60)

# Let's use PersistentClient so our collections persist
client = chromadb.PersistentClient(path="./chroma_db")

# =============================================================================
# CREATE: Creating Multiple Collections
# =============================================================================
print("\nCREATE: Creating Multiple Collections")
print("-" * 60)

# Let's create several collections for different purposes
# Think of these as different filing cabinet drawers

travel_collection = client.get_or_create_collection(
    name="travel_policies",
    metadata={"department": "HR", "category": "policies"}
)

hr_collection = client.get_or_create_collection(
    name="hr_policies", 
    metadata={"department": "HR", "category": "employment"}
)

it_collection = client.get_or_create_collection(
    name="it_policies",
    metadata={"department": "IT", "category": "security"}
)

print("Created/Retrieved 3 collections:")
print(f"  - {travel_collection.name}")
print(f"  - {hr_collection.name}")
print(f"  - {it_collection.name}")

# =============================================================================
# READ: Listing All Collections
# =============================================================================
print("\nREAD: Listing All Collections")
print("-" * 60)

# Get all collections in the database
all_collections = client.list_collections()

print(f"Total collections in database: {len(all_collections)}")
print("\nCollection Details:")

for coll in all_collections:
    print(f"\n  Collection: {coll.name}")
    print(f"    ID: {coll.id}")
    print(f"    Metadata: {coll.metadata}")
    print(f"    Document Count: {coll.count()}")

# =============================================================================
# Retrieving a Specific Collection
# =============================================================================
print("\nRetrieving a Specific Collection")
print("-" * 60)

# You can get a collection by name (it must exist, or it will raise an error)
try:
    retrieved_collection = client.get_collection(name="travel_policies")
    print(f"Successfully retrieved: {retrieved_collection.name}")
    print(f"  Documents in collection: {retrieved_collection.count()}")
except Exception as e:
    print(f"Error: {e}")

# Trying to get a collection that doesn't exist will raise an error
try:
    fake_collection = client.get_collection(name="nonexistent_collection")
except Exception as e:
    print(f"\nAs expected, trying to get a non-existent collection fails:")
    print(f"  Error: {type(e).__name__}")

# =============================================================================
# UPDATE: Modifying Collection Metadata
# =============================================================================
print("\nUPDATE: Modifying Collection Metadata")
print("-" * 60)

# You can update a collection's name or metadata
# Let's rename the IT collection and update its metadata

it_collection.modify(
    name="it_security_policies",  # Rename it
    metadata={"department": "IT", "category": "security", "updated": "2025-10-21"}
)

print("Modified collection:")
print(f"  Old name: it_policies")
print(f"  New name: it_security_policies")
print(f"  New metadata: {it_collection.metadata}")

# Let's verify by listing collections again
print("\nUpdated Collection List:")
updated_collections = client.list_collections()
for coll in updated_collections:
    print(f"  - {coll.name} (metadata: {coll.metadata})")

# =============================================================================
# DELETE: Removing Collections
# =============================================================================
print("\nDELETE: Removing Collections")
print("-" * 60)

print(f"Collections before deletion: {len(client.list_collections())}")

# Let's delete the HR policies collection
# WARNING: This will permanently delete the collection AND all its data!
client.delete_collection(name="hr_policies")

print("Deleted 'hr_policies' collection")
print(f"Collections after deletion: {len(client.list_collections())}")

# List remaining collections
print("\nRemaining Collections:")
for coll in client.list_collections():
    print(f"  - {coll.name}")

# =============================================================================
# BEST PRACTICES
# =============================================================================
print("\n" + "=" * 60)
print("BEST PRACTICES FOR MANAGING COLLECTIONS")
print("=" * 60)

best_practices = """
1. **Naming Conventions:**
   - Use descriptive, lowercase names with underscores
   - Examples: "travel_policies", "user_documents", "product_catalog"

2. **Metadata:**
   - Use metadata to organize collections
   - Add creation date, department, purpose, etc.
   - Makes it easier to manage many collections

3. **get_or_create_collection() vs get_collection():**
   - get_or_create_collection(): Safe, won't error if exists/doesn't exist
   - get_collection(): Strict, errors if collection doesn't exist
   - Use get_or_create_collection() for flexibility

4. **Deletion Safety:**
   - Deleting a collection is PERMANENT
   - Always verify before deleting
   - Consider archiving instead of deleting

5. **Organization:**
   - Group related data in the same collection
   - Don't create too many tiny collections
   - But also don't put unrelated data in one collection
"""

print(best_practices)

# =============================================================================
# PRACTICAL EXAMPLE: Collection Management Workflow
# =============================================================================
print("=" * 60)
print("PRACTICAL WORKFLOW EXAMPLE")
print("=" * 60)

# 1. Check if collection exists
collection_name = "temporary_test_collection"
existing_collections = [c.name for c in client.list_collections()]

if collection_name in existing_collections:
    print(f"Collection '{collection_name}' already exists")
    test_coll = client.get_collection(collection_name)
else:
    print(f"Creating new collection '{collection_name}'")
    test_coll = client.create_collection(
        name=collection_name,
        metadata={"purpose": "testing", "temporary": True}
    )

# 2. Add some data
test_coll.add(
    ids=["test1"],
    documents=["This is a test document"]
)

print(f"Added document to '{collection_name}'")
print(f"  Document count: {test_coll.count()}")

# 3. Clean up - delete the temporary collection
client.delete_collection(name=collection_name)
print(f"Cleaned up: deleted '{collection_name}'")

print("\nStep 5 completed successfully!")
print("You now know how to manage collections in ChromaDB!")

