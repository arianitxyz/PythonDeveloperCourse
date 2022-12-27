from contents import recipes


def dcopy(given_dict: dict) -> dict:
    copied_dict = {}

    for item, value in given_dict.items():
        copied_dict[item] = value.copy()
    return copied_dict


new_dict = dcopy(recipes)
new_dict["Butter chicken"]["ginger"] = 300
print(id(new_dict["Butter chicken"]["ginger"]), new_dict["Butter chicken"]["ginger"])
print(id(recipes["Butter chicken"]["ginger"]), recipes["Butter chicken"]["ginger"])
