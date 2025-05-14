animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

def coping_deep(your_dict: dict) -> dict:

    your_dict_deepcopy = {}

    for key, value in your_dict.items():
        your_dict_deepcopy[key] = list(value)

    return your_dict_deepcopy



copied_list = coping_deep(animals)

animals["teddy"].append("toy")

print(copied_list)
