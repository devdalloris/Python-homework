def repeat_elements(input_tuple, repeat_times):
    new_tuple = tuple(element for element in input_tuple for _ in range(repeat_times))
    return new_tuple

# Example
input_tuple = (1, 2, 3)
repeat_times = 3

new_tuple = repeat_elements(input_tuple, repeat_times)
print(new_tuple)