Of course. I can combine all the pieces into a single, comprehensive workbook for you. No other tools are needed.

Here is the complete guide, integrating all the sections we've discussed.

-----

## 🚀 Your First Steps with ChromaDB: A Beginner's Guide

Welcome to your first guide to **ChromaDB**\! Think of ChromaDB as a smart filing cabinet for your information. Instead of just searching for exact words, it understands the *meaning* or *context* behind your text. This is incredibly powerful and is the technology behind many modern AI applications.

In this guide, we'll learn how to use ChromaDB to store and search through a company's travel policy documents, from basic setup to advanced usage.

-----

### 🛠️ Step 1: Installation

First things first, let's get ChromaDB installed. We'll use pip, Python's package installer.

```bash
# Create a virtual environment to keep your project dependencies isolated
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# chromadb_env\Scripts\activate

# Now install ChromaDB in the virtual environment
pip install chromadb
```

-----

### 🗂️ Step 2: Creating Your First "Filing Cabinet" (Collection)

Now that ChromaDB is installed, we need to initialize it and create a **collection**. A collection is like a single drawer in your filing cabinet dedicated to a specific topic—in our case, company travel policies.

```python
import chromadb

# Initialize the ChromaDB client. This creates an in-memory database.
client = chromadb.Client()

# Create a new collection or get it if it already exists.
collection = client.get_or_create_collection(name="travel_policies")
```

-----

### 📄 Step 3: Managing Your Data (CRUD on Data Points)

As policies change, you'll need to **C**reate, **R**ead, **U**pdate, and **D**elete data points. This is the most common workflow in ChromaDB.

#### Create: Adding Documents

Our collection is empty. Let's add our first few travel policy documents. We need to give each document a unique **`id`** and the **`document`** content itself. We can also include **`metadatas`**—extra information that helps us filter our searches later.

ChromaDB will automatically convert these text documents into numerical formats called **embeddings** behind the scenes. This is how it understands the meaning of the text.

```python
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
```

#### Read: Asking Questions (Querying)

This is where the magic happens\! We can now ask a question using natural language. ChromaDB will convert our question into an embedding and find the documents with the most similar meanings.

```python
results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2 # Ask for the top 2 most relevant results
)

print(results)
```

Notice how the flight policy is the top result. It understands the *intent* of our query\! The **`distances`** value in the full output shows how "far" a result is from the query—a lower number means a closer match.

#### Update: Changing a Document

When a policy changes, you can use the **`update`** or **`upsert`** methods.

  * **`update`** modifies an existing entry.
  * **`upsert`** will **update** an entry if the `id` exists, or **insert** a new one if it doesn't.

Let's increase the hotel budget and add a policy for train travel.

```python
collection.upsert(
    ids=["hotel_policy_01", "train_policy_01"],
    documents=[
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
        "Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."
    ],
    metadatas=[
        {"policy_type": "hotels", "max_spend": 300},
        {"policy_type": "train", "last_updated": "2025-10-15"}
    ]
)
```

#### Delete: Removing a Document

If a policy is no longer relevant, you can easily remove it using its `id`.

```python
collection.delete(ids=["train_policy_01"])
```

-----

### 💾 Step 4: Saving Your Work (Persistent Database)

By default, `chromadb.Client()` creates an "in-memory" database, which is erased when your program finishes. To save your data permanently, use the **`PersistentClient`**.

You simply provide a **`path`** to a directory where you want ChromaDB to store its files. If the directory doesn't exist, ChromaDB will create it.

```python
# Use PersistentClient and give it a path to a folder
# This client will save all data to the "./chroma_db" directory
persistent_client = chromadb.PersistentClient(path="./chroma_db")

# Now, creating a collection works the same way, but it will be saved to disk.
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

# Data added to this collection will persist between sessions
p_collection.add(
    ids=["saved_policy_01"],
    documents=["All expense reports must be submitted within 15 days of trip completion."]
)
```

-----

### 🗂️ Step 5: Managing Your Collections (CRUD on Collections)

You can also manage the collections themselves.

#### Read (List All Collections)

To see all collections in the database, use **`list_collections()`**.

```python
all_collections = client.list_collections()

print("Available collections:")
for coll in all_collections:
    print(f"- {coll.name}")
```

#### Update (Modify a Collection)

You can change a collection's name or metadata using the **`modify()`** method.

```python
# First, get the collection object
collection_to_update = client.get_collection(name="travel_policies")

# Now, rename it
collection_to_update.modify(name="legacy_travel_policies")
```

#### Delete a Collection

To permanently remove a collection and all its data, use **`delete_collection()`**. **Be careful**, as this action cannot be undone.

```python
client.delete_collection(name="legacy_travel_policies")
```

-----

### 🧠 Step 6: Advanced - Using OpenAI's Embedding Model

While Chroma's default model is great, you can integrate more powerful models like those from **OpenAI**. Let's use the `text-embedding-3-small` model.

#### Install Libraries & Set Up API Key

We need two new libraries: `openai` to use their models and `tiktoken` to count **tokens** (the pieces of words that models "see" and are used for billing).

```python
%pip install -Uq openai tiktoken
```

You will need an OpenAI API key. It's best practice to set this as an environment variable.

```python
import os
# Set your key, e.g., os.environ['OPENAI_API_KEY'] = 'your-key-here'
```

#### Understanding Tokens with `tiktoken`

It's important to count tokens to manage costs and stay within model limits. The `text-embedding-3-small` model uses the `cl100k_base` encoding.

```python
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")
token_count = len(encoding.encode("This is a sample sentence."))
print(f"Token Count: {token_count}")
```

#### Create a Collection with the OpenAI Model

To use the OpenAI model, you pass it in as the **`embedding_function`** when creating a collection.

```python
from chromadb.utils import embedding_functions

# Create an embedding function using OpenAI's model
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                model_name="text-embedding-3-small"
            )

# Create a new collection and pass in our new embedding function
openai_collection = client.get_or_create_collection(
    name="travel_policies_openai",
    embedding_function=openai_ef
)

# From here, adding and querying data works exactly the same as before!
openai_collection.add(
    ids=["flight_policy_01", "hotel_policy_01"],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
    ]
)

results = openai_collection.query(
    query_texts=["What is the hotel budget?"],
    n_results=1
)

print(results['documents'])
```

Congratulations\! You've now learned the complete fundamentals of ChromaDB.