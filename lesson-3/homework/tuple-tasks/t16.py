a=(1,7,9,4,6,4,5)
def is_sorted_tuple(input_tuple):
    for i in range(len(input_tuple) - 1):
        if input_tuple[i] > input_tuple[i + 1]:
            return False
    return True
print(is_sorted_tuple(a))