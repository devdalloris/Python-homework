list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
list=[]
for i in range(3):
        if list1[i]!=list2[i]:
            list.append(list1[i])
for i in range(3):
        if list1[i]!=list2[i]:
            list.append(list2[i])
print(list)