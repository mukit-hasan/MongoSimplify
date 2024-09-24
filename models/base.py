from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Any, Dict, List, Optional


class Model:
    """
    class Model(models.model):
        host = 'localhost'
        port = 24017
        database = 'databse_name'

    class Product(Model):
        pass

    """
    client: MongoClient = None
    db: Database = None

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        # Default to 'localhost' if not set
        host: str = getattr(cls, 'host', 'localhost')
        # Default to 27017 if not set
        port: int = getattr(cls, 'port', 27017)
        # Default to 'pymongomodel_db'
        database: str = getattr(cls, 'database', 'pymongomodel_db')

        if Model.client is None:
            Model._connect(host, port, database)
        cls.collection: Collection = Model.db[cls.__name__.lower()]

    @staticmethod
    def _connect(host: str, port: int, database: str) -> None:
        """Connect to MongoDB server with specified host, port, and database."""
        try:
            Model.client = MongoClient(host=host, port=port)
            Model.db = Model.client[database]
        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {str(e)}")

    @classmethod
    def get(cls, data: Optional[Dict[str, Any]] = None, **kwargs) -> Optional[Dict[str, Any]]:
        """Retrieve a single document from the database based on a filter."""
        if data is None:
            data = kwargs
        try:
            return cls.collection.find_one(data)
        except Exception as e:
            raise RuntimeError(f"Error retrieving document: {str(e)}")

    @classmethod
    def get_or_create(cls, data: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        """Retrieve a document or create a new one if it doesn't exist."""
        if data is None:
            data = kwargs
        try:
            result = cls.collection.find_one(data)
            if result is None:
                result = cls.collection.insert_one(data)
                return result.inserted_id
            return result
        except Exception as e:
            raise RuntimeError(f"Error getting or creating document: {str(e)}")

    @classmethod
    def all(cls) -> List[Dict[str, Any]]:
        """Retrieve all documents from the collection."""
        try:
            return list(cls.collection.find())
        except Exception as e:
            raise RuntimeError(f"Error retrieving documents: {str(e)}")

    @classmethod
    def create(cls, data: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        """Insert a new document into the collection."""
        if data is None:
            data = kwargs
        try:
            result = cls.collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            raise RuntimeError(f"Error creating document: {str(e)}")

    @classmethod
    def create_many(cls, data: List[Dict[str, Any]]) -> Any:
        """Insert multiple documents into the collection."""
        try:
            return cls.collection.insert_many(data)
        except Exception as e:
            raise RuntimeError(f"Error creating multiple documents: {str(e)}")

    @classmethod
    def create_index(cls, keys: List[tuple]) -> Any:
        """Create an index on specified fields to improve query performance."""
        try:
            return cls.collection.create_index(keys)
        except Exception as e:
            raise RuntimeError(f"Error creating index: {str(e)}")

    @classmethod
    def update(cls, query: Dict[str, Any], new_values: Dict[str, Any]) -> Any:
        """Update documents matching the query with new values."""
        try:
            return cls.collection.update_one(query, {"$set": new_values})
        except Exception as e:
            raise RuntimeError(f"Error updating document: {str(e)}")

    @classmethod
    def delete(cls, data: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        """Delete a document from the collection based on a filter."""
        if data is None:
            data = kwargs
        try:
            return cls.collection.delete_one(data)
        except Exception as e:
            raise RuntimeError(f"Error deleting document: {str(e)}")

    @classmethod
    def count(cls, filter: Optional[Dict[str, Any]] = None) -> int:
        """Count the number of documents that match the filter criteria."""
        try:
            return cls.collection.count_documents(filter or {})
        except Exception as e:
            raise RuntimeError(f"Error counting documents: {str(e)}")

    @classmethod
    def find(cls, filter: Optional[Dict[str, Any]] = None, limit: int = 0) -> List[Dict[str, Any]]:
        """Retrieve multiple documents based on a filter and limit the number of results."""
        try:
            return list(cls.collection.find(filter or {}).limit(limit))
        except Exception as e:
            raise RuntimeError(f"Error finding documents: {str(e)}")

    @classmethod
    def bulk_write(cls, operations: List[Dict[str, Any]]) -> Any:
        """Perform bulk write operations (insert, update, delete) efficiently."""
        try:
            return cls.collection.bulk_write(operations)
        except Exception as e:
            raise RuntimeError(f"Error performing bulk write: {str(e)}")

    @classmethod
    def drop(cls) -> None:
        """Drop the entire collection from the database."""
        try:
            cls.collection.drop()
        except Exception as e:
            raise RuntimeError(f"Error dropping collection: {str(e)}")

    @classmethod
    def replace(cls, query: Dict[str, Any], replacement: Dict[str, Any]) -> Any:
        """Replace a document that matches the query with a new document."""
        try:
            return cls.collection.replace_one(query, replacement)
        except Exception as e:
            raise RuntimeError(f"Error replacing document: {str(e)}")

    @classmethod
    def distinct(cls, field: str) -> List[Any]:
        """Get distinct values for a specified field in the collection."""
        try:
            return cls.collection.distinct(field)
        except Exception as e:
            raise RuntimeError(f"Error getting distinct values: {str(e)}")

    @classmethod
    def create_compound_index(cls, keys: List[str]) -> Any:
        """Create an index on multiple fields to improve query performance."""
        try:
            return cls.collection.create_index(keys)
        except Exception as e:
            raise RuntimeError(f"Error creating compound index: {str(e)}")
