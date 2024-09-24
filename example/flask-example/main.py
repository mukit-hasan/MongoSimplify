from flask import Flask, jsonify
from db import Product
from serialize import ProductSerializer

app = Flask(__name__)

app.secret_key = 'my_secret_key'


@app.route('/create')
def create():
    """
    Route to create a new product document in the 'product' collection of the MongoDB database.

    How it works:
    - The `Product` class inherits from `Model`, which automatically connects to the MongoDB database.
    - The `create` method inserts the provided data into the associated collection (`product`).

    Returns:
        JSON response containing a success message and the inserted document ID, or an error message.
    """
    try:
        data = {
            "title": 'car',
            "price": 491,
            'img': "#"
        }
        # Use the custom `create` method to insert a new document
        product = Product.create(data)
        return jsonify({"message": 'success', "product": str(product)})
    except Exception as e:
        print(e)
        return jsonify({"message": str(e)})


@app.route('/product/all')
def all_products():
    """
    Route to retrieve all product documents from the 'product' collection.

    How it works:
    - The `all` method fetches all documents from the MongoDB collection associated with the `Product` model.
    - Each document is serialized using `ProductSerializer` before being returned as JSON.

    Returns:
        JSON response containing a list of serialized product documents, or an error message.
    """
    try:
        products = Product.all()  # Use the custom `all` method to retrieve all documents
        result = [ProductSerializer(product).serialize()
                  for product in products]
        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


@app.route('/product/<title>')
def get_product_by_title(title):
    """
    Route to retrieve a single product document based on its title.

    How it works:
    - The `get` method finds a document that matches the provided title in the `product` collection.
    - The document is then serialized using `ProductSerializer` and returned as JSON.

    Args:
        title: The title of the product to retrieve (passed as a URL parameter).

    Returns:
        JSON response containing the serialized product document, or an error message.
    """
    try:
        # Use the custom `get` method to find a document by title
        product = Product.get(title=title)
        if product:
            return jsonify(ProductSerializer(product).serialize())
        else:
            return jsonify({'error': 'Product not found'})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


@app.route('/product/update/<title>')
def update_product(title):
    """
    Route to update an existing product document based on its title.

    How it works:
    - The `update` method finds a document that matches the provided title and updates it with new values.
    - The updated document's ID is returned in the JSON response.

    Args:
        title: The title of the product to update (passed as a URL parameter).

    Returns:
        JSON response containing a success message and the updated document's ID, or an error message.
    """
    try:
        # The query to find the product document by title
        query = {"title": title}
        new_values = {"price": 999}  # The new values to update in the document
        # Use the custom `update` method to modify the document
        result = Product.update(query, new_values)
        return jsonify({"message": 'success', "updated_count": result.matched_count})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


@app.route('/product/delete/<title>')
def delete_product(title):
    """
    Route to delete a product document based on its title.

    How it works:
    - The `delete` method removes a document that matches the provided title from the `product` collection.

    Args:
        title: The title of the product to delete (passed as a URL parameter).

    Returns:
        JSON response containing a success message if deletion was successful, or an error message.
    """
    try:
        # Use the custom `delete` method to remove the document by title
        result = Product.delete(title=title)
        if result.deleted_count > 0:
            return jsonify({"message": 'success', "deleted_count": result.deleted_count})
        else:
            return jsonify({"error": 'Product not found or already deleted'})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
