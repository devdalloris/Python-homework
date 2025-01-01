def add_new():
    employee_id = input("Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    new_record = f"{employee_id}, {name}, {position}, {salary}\n"
    return new_record

def view_all_employee_records():
    with open('employees.txt', 'r') as file:
        all_employees = file.read()
    return all_employees

def search_by_ID():
    ID = input("Enter ID to search: ")
    with open('employees.txt', 'r') as file:
        for i in file:
            if i[:4] == ID:
                return i
        return "ID not found"

def update_list_all_employee():
    with open("employees.txt", 'r') as file:
        return file.read()

def start():
    print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete all employee records
6. Exit""")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        with open('employees.txt', 'a') as file:
            file.write(add_new())
        print("Employee record added.")
        start()
        
    elif choice == 2:
        print("A list of all employees: ")
        print(view_all_employee_records())
        start()
        
    elif choice == 3:
        print(search_by_ID())
        start()
        
    elif choice == 4:
        print(update_list_all_employee())
        start()
        
    elif choice == 5:
        with open('employees.txt', 'w') as file:
            pass
        print("All employee records deleted.")
        start()
        
    else:
        print("Goodbye!")
        exit(0)

start()