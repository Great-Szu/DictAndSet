import copy
from copy import deepcopy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}
# Perform a shallow copy - creates just another reference to the same object
# things = animals.copy()


# Perform a deep copy - create a literal copy. Another being
things = deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])
print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])