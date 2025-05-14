from exercises.challange_deepcopy import coping_deep
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = coping_deep(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(original)
print(copy_1)
print(copy_2)