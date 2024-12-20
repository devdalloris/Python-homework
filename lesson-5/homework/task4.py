def enrollment_stats(b):
    s1=0
    s2=0
    for i in range(0,7):
        for j in range(0,3):
            if j==1:
                s1=s1+b[i][1]
                s2=s2+b[i][2]
    print(f"Total students: {s1/1000}")
    print(f"Total tuition: $ {s2/1000}")
    
def mean(b):
    return 
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
enrollment_stats(universities)
