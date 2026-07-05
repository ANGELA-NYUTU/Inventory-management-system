from flask import Flask, jsonify, request

from inventory import (
    get_all_items,
    get_item_by_id,
    add_item,
    update_item,
    delete_item
)

app = Flask(__name__)


# GET ALL INVENTORY ITEMS

@app.route("/inventory", methods=["GET"])
def fetch_all_items():
    return jsonify(get_all_items()), 200



# GET SINGLE ITEM BY ID

@app.route("/inventory/<int:item_id>", methods=["GET"])
def fetch_single_item(item_id):
    item = get_item_by_id(item_id)

    if item:
        return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404



# CREATE NEW ITEM

@app.route("/inventory", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    new_item = add_item(data)

    return jsonify(new_item), 201


# UPDATE ITEM (PATCH)
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_existing_item(item_id):
    data = request.get_json()

    updated_item = update_item(item_id, data)

    if updated_item:
        return jsonify(updated_item), 200

    return jsonify({"error": "Item not found"}), 404


# DELETE ITEM
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_item(item_id):

    success = delete_item(item_id)

    if success:
        return jsonify({"message": "Item deleted successfully"}), 200

    return jsonify({"error": "Item not found"}), 404


# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)