# MongoDB Model Library for Python

MongoSimplify is a simple yet powerful library designed for seamless interaction with MongoDB using Python. It provides an intuitive interface for performing common MongoDB operations, making it easy to execute CRUD operations and more. This library is highly versatile and can be integrated into any Python framework, such as Django or Flask, allowing developers to efficiently manage MongoDB interactions with minimal effort.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Connecting to the Database](#connecting-to-the-database)
  - [CRUD Operations](#crud-operations)
  - [Additional Operations](#additional-operations)
- [Examples](#examples)
- [License](#license)

## Installation

You can install the library via pip. Ensure you have MongoDB and pymongo installed in your Python environment.

```bash
pip install MongoSimplify
```


# Usage
Connecting to the Database
To use the library, define a subclass of Model to specify your database connection details.

```py
from MongoSimplify.models import models

# setting up host port and database
class Model(Model):
    host = 'localhost'  # or your MongoDB server IP
    port = 27017
    database = 'my_database'

class Product(Mydb): # collection name
    pass

```

# CRUD Operations
## Create a Document
```py
# Create a new document
my_doc = {'name': 'Alice', 'age': 30}
new_id = Product.create(my_doc)
print(f"Document created with ID: {new_id}")
```
## Retrieve a Document
```python
# Get a single document
doc = Product.get({'name': 'Alice'})
print(doc)
```

## Update a Document

```python
# Update the document
updated_doc = Product.update({'name': 'Alice'}, {'age': 31})
print(f"Updated documents: {updated_doc.modified_count}")
```
## Delete a Document
```python
# Delete a document
deleted_doc = Prsoduct.delete({'name': 'Alice'})
print(f"Deleted documents: {deleted_doc.deleted_count}")
Additional Operations
```
## Count Documents
```python
# Count documents
count = Product.count()
print(f"Total documents: {count}")
```
## Find Multiple Documents
```python
# Find documents with a limit
docs = Product.find(limit=5)
for doc in docs:
    print(doc)
```

## Bulk Write Operations

```python
# Perform bulk operations
operations = [
    InsertOne({'name': 'Bob', 'age': 25}),
    UpdateOne({'name': 'Alice'}, {'$set': {'age': 32}}),
    DeleteOne({'name': 'Charlie'})
]
result = Product.bulk_write(operations)
print(f"Bulk operation result: {result.bulk_api_result}")
```

## Create Indexes
```python
# Create an index on a field
index_name = Product.create_index([('name', 1)])  # 1 for ascending
print(f"Index created: {index_name}")
```

# Contributing
Contributions to MongoSimplify are welcome! Whether you're fixing bugs, improving documentation, or adding new features, your help is greatly appreciated. 

# License
This library is licensed under the MIT License. See the LICENSE file for more details.
