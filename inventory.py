from data.inventory_data import inventory


def get_all_items():
    """
    Return all inventory items.
    """
    return inventory


def get_item_by_id(item_id):
    """
    Return one inventory item by its ID.
    If the item does not exist, return None.
    """
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def add_item(new_item):
    """
    Add a new item to the inventory.

    Automatically generates the next available ID.
    """

    if inventory:
        new_id = inventory[-1]["id"] + 1
    else:
        new_id = 1

    new_item["id"] = new_id

    inventory.append(new_item)

    return new_item


def update_item(item_id, updates):
    """
    Update an existing inventory item.

    Returns the updated item.
    Returns None if the item is not found.
    """

    item = get_item_by_id(item_id)

    if item is None:
        return None

    for key, value in updates.items():
        if key in item:
            item[key] = value

    if "product" in updates:
        item["product"].update(updates["product"])

    return item


def delete_item(item_id):
    """
    Delete an inventory item.

    Returns True if deleted.
    Returns False if the item is not found.
    """

    item = get_item_by_id(item_id)

    if item is None:
        return False

    inventory.remove(item)

    return True