import unittest
from PymongoModel.models import Model


class TestModel(Model):
    host = 'localhost'  # Update with your MongoDB server IP if needed
    port = 27017
    database = 'test_database'


class TestPymongoModel(unittest.TestCase):

    def setUp(self):
        """Set up a test database and collection before each test."""
        self.test_data = {'name': 'Alice', 'age': 30}
        self.test_data2 = {'name': 'Bob', 'age': 25}

    def test_create(self):
        """Test creating a document."""
        result_id = TestModel.create(self.test_data)
        self.assertIsNotNone(result_id, "Document ID should not be None")

    def test_get(self):
        """Test retrieving a document."""
        TestModel.create(self.test_data)
        result = TestModel.get({'name': 'Alice'})
        self.assertIsNotNone(result, "Document should be retrieved")
        self.assertEqual(result['name'], 'Alice')

    def test_update(self):
        """Test updating a document."""
        TestModel.create(self.test_data)
        TestModel.update({'name': 'Alice'}, {'age': 31})
        result = TestModel.get({'name': 'Alice'})
        self.assertEqual(result['age'], 31, "Age should be updated to 31")

    def test_delete(self):
        """Test deleting a document."""
        TestModel.create(self.test_data)
        TestModel.delete({'name': 'Alice'})
        result = TestModel.get({'name': 'Alice'})
        self.assertIsNone(result, "Document should be deleted")

    def tearDown(self):
        """Clean up the test database after each test."""
        TestModel.collection.delete_many({})  # Clear the collection


if __name__ == '__main__':
    unittest.main()
