"""
dictionary
__________
* Associative array, index can be each value(e.g. string).
* Built by key-value pairs
* Mutable

Methods
__________
* clear() - Deletes the contents of the dictionary
* copy() - Create a copy of the contents of the dictionary
* fromkeys() - Creates a new dictionary with a set of keys and a given value
* get() - Return the value that related to a specific key
* items() - Create a list of tuples from the type key-value
* keys() - Return a list of all keys of the dictionary
* values() - Return a list of all values of the dictionary
* pop() - Delete in the dictionary the entry with the given key
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["year"])

thisdict["year"] = 1980

print(thisdict["year"])
