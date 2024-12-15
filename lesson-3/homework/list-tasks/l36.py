numbers=[1,4,5,-4,3,-8,4,3,4,9]
numbers1=numbers
for i in numbers:
    if i<0:
        numbers1.remove(i)
print(sum(numbers1))