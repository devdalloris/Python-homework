numbers=[8, 3, 15, 11, 45, 11, 34, 67]
if(len(numbers)%2==1):
    print(numbers[int(len(numbers)/2)])
else:
    print(numbers[int(len(numbers)/2-1):int(len(numbers)/2)+1])