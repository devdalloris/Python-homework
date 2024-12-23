file=open('employees.txt', 'a')
employee_id=input("Employee ID: ")
name = input("Enter Name: ")
position = input("Enter Position: ")
salary = input("Enter Salary: ")
record = f"{employee_id}, {name}, {position}, {salary}\n"
file.write(record)
print("Employee record added.")
file.close()
