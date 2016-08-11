# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(nested_list):
    capitalized_list = []
    for item in nested_list:
        item_type = str(type(item))
        if "list" in item_type:
            capitalized_list .append(capitalize_nested(item))  # Recursively call the function if item is a list
        elif "str" in item_type:                               # Only apply upper() if item is a string
            capitalized_list.append(item.upper())              # Append as is otherwises
        else:
            capitalized_list.append(item)
    return capitalized_list


def main():
    pass
    # print(capitalize_nested(['apple', ['bear'], 'cat']))
    # print(capitalize_nested(['apple', ['bear', 'buffalo'], 'cat', 1, 2, 'a']))


if __name__ == "__main__":
    main()
