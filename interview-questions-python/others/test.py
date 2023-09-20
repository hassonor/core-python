# A dictionary to maintain parent-child relationships and names.
hash_map_of_parent_and_child = {}


def func_a(id, pId, name):
    # Check if the current node (with the provided ID) is already in the dictionary.
    # If not, add it.
    if id not in hash_map_of_parent_and_child:
        hash_map_of_parent_and_child[id] = {'children': [], 'name': name}
    else:
        hash_map_of_parent_and_child[id]['name'] = name  # Update name if it's already present.

    # Handle parent ID and its children
    if pId in hash_map_of_parent_and_child:
        hash_map_of_parent_and_child[pId]['children'].append(id)
    else:
        hash_map_of_parent_and_child[pId] = {'children': [id], 'name': None}

    return hash_map_of_parent_and_child


# Testing the function
print(funcA(1, 3, "a"))
print(funcA(2, 3, "b"))
print(funcA(3, 4, "c"))
print(funcA(4, 6, "d"))
print(funcA(5, 3, "e"))
