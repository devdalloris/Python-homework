tuple1 = (1, 2, 3, 4, 5)
tuple2 = ()
if tuple1:
    last_element_tuple1 = tuple1[0]
    print("Last element of tuple1:", last_element_tuple1)
else:
    print("Tuple1 is empty.")
last_element_tuple2 = tuple2[-1] if tuple2 else "Tuple2 is empty"
print("Last element of tuple2:", last_element_tuple2)