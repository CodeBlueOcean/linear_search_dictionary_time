def linear_search_dictionary(my_dictionary, target_value):
    for key, value in my_dictionary.items():
        if value == target_value:
            print(f"Found at is {key}.")
            return key
    print(f"Target {target_value} is not in the dictionary")
            


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)


