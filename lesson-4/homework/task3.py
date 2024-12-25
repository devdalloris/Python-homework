txt='assalom'
x=''
list1=['a','e','i','o','u']
for i in range(len(txt)):
    x=x+txt[i]
    if (i+1)%3==0:
        if txt[i] in list1: 
            continue
        else:
            x=x+'_'
print(x)