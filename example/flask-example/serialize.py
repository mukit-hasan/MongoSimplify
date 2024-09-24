class ProductSerializer:
    """
    The ProductSerializer class is responsible for converting MongoDB documents into a format 
    that can be easily returned as JSON in API responses.

    MongoDB documents contain ObjectId instances, which are not natively JSON serializable.
    To handle this, the serializer converts the ObjectId into a string and retrieves the necessary
    fields from the document to create a JSON-serializable dictionary.

    Attributes:
        product (dict): The MongoDB document to be serialized.
    """

    def __init__(self, product):
        """
        Initializes the ProductSerializer with a MongoDB document.

        Args:
            product (dict): A MongoDB document representing a product.
        """
        self.product = product

    def serialize(self):
        """
        Serializes the MongoDB document into a JSON-serializable dictionary.

        This method extracts relevant fields from the MongoDB document and converts
        the ObjectId into a string format so that it can be safely returned in a JSON response.

        Returns:
            dict: A dictionary containing the serialized data of the product.
        """
        return {
            # Convert the MongoDB ObjectId to a string
            "_id": str(self.product["_id"]),
            # Get the 'title' field from the product document
            "title": self.product.get("title"),
            # Get the 'price' field from the product document
            "price": self.product.get("price"),
            # Get the 'img' field from the product document
            "img": self.product.get("img")
        }
