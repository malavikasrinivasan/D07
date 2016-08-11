# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def is_sorted(list_to_check):
    len_list = len(list_to_check)
    if  len_list == 0:
        return "No items in list"
    if len_list == 1:
        return True
    try:
        for index in range(0, len_list-1):
            if list_to_check[index] > list_to_check[index+1]:
                return False
        return True
    except:
        return "Indeterminable as the list has types that cannot be compared"


def main():
    pass
    # print(is_sorted([29, 2, 4, 3]))
    # print(is_sorted(['a', "Hello", 'b']))
    # print(is_sorted(['a', 'b', 'cat']))
    # print(is_sorted([1, 2, "Hi"]))


if __name__ == "__main__":
    main()           