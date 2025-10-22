# Step 2: Creating Your First Collection
# =======================================
# A collection is like a filing cabinet drawer dedicated to a specific topic.
# In our case, we're creating one for company travel policies.

import chromadb

# Initialize the ChromaDB client
# This creates an in-memory database (data will be lost when the program ends)
# Think of this as opening your filing cabinet
client = chromadb.Client()

# Create a new collection or get it if it already exists
# The collection name is like a label on the drawer: "travel_policies"
collection = client.get_or_create_collection(name="travel_policies")

# Let's verify it was created successfully
print("Collection created successfully!")
print(f"Collection name: {collection.name}")
print(f"Collection ID: {collection.id}")

# Let's also check how many items are in the collection (should be 0 for now)
print(f"Number of documents in collection: {collection.count()}")

