"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    inventory = {}
    for item in items:
        value = inventory.setdefault(item, 0)
        inventory[item] = value + 1
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    inventory_items = create_inventory(items)
    for key in inventory_items:
        inventory[key] = inventory.get(key, 0) + inventory_items[key]
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """

    inventory_items = create_inventory(items)
    for key in inventory_items:
        if key not in inventory:
            continue
        inventory[key] = inventory.get(key, 0) - inventory_items[key]
        if inventory[key] < 0:
            inventory[key] = 0
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    try:
        inventory.pop(item)
    except KeyError:
        pass
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    items_tuples = []
    for key, value in inventory.items():
        if value == 0:
            continue
        items_tuples.append((key, value))
    return items_tuples
