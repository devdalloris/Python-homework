with open("grades.csv", "w") as f:
    f.writelines("""Name,Subject,Grade
Alice,Math,85
Bob,Science,78
Carol,Math,92
Dave,History,74""")
with open("grades.csv", "rt") as f:
    l=f.read().splitlines()
    ages=[row.split(",")[2] for row in l[1:]]
    sum_of_grades = list(map(int, ages))
    print(sum(sum_of_grades))
with open("average_grades.csv", "w") as file:
    file.writelines("""Subject,Average Grade
Math,88.5
Science,78
History,74""")


