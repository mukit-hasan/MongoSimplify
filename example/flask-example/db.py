from models import Model as models
import sys
import os

"""This Import is only for this example in your project you will import it
    as from PymongoModel import models
    and in the Model calss 
    class Model(models.Model) 
    """
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '...', '...')))


class Model(models):
    """
    The Model class is inherited from the imported Model class, and it is used to establish a connection to the MongoDB database.

    Attributes:
        host (str): The hostname or IP address of the MongoDB server (default is 'localhost').
        port (int): The port number on which the MongoDB server is listening (default is 27017).
        database (str): The name of the MongoDB database to connect to (default is 'test').
    """
    host = 'localhost'
    port = 27017
    database = 'test'


class Product(Model):
    """
    The Product class represents a MongoDB collection. This class inherits from the Model class and automatically
    links to a collection in the MongoDB database, where the collection name is derived from the class name (in this case, 'product').

    This means that instances of the Product class correspond to documents in the 'product' collection of the specified database.
    """
    pass
