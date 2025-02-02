def max_of_subtuple(input_tuple, start_index, end_index):
    subtuple = input_tuple[start_index:end_index + 1]
    return max(subtuple)

# Example
input_tuple = (1, 7, 9, 4, 6, 4, 5)
start_index = 1
end_index = 4

max_element = max_of_subtuple(input_tuple, start_index, end_index)
print(max_element)