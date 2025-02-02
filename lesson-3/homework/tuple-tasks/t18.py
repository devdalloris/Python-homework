def remove_first_occurrence(input_tuple, element):
    if element in input_tuple:
        index_to_remove = input_tuple.index(element)
        new_tuple = input_tuple[:index_to_remove] + input_tuple[index_to_remove + 1:]
        return tuple(new_tuple)
    else:
        return input_tuple

# Example
input_tuple = (1, 7, 9, 4, 6, 4, 5)
element_to_remove = 4

new_tuple = remove_first_occurrence(input_tuple, element_to_remove)
print(new_tuple)