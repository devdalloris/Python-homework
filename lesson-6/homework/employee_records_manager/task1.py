def add_new():
    employee_id = input("Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    new_record = f"{employee_id}, {name}, {position}, {salary}\n"
    
    with open('employees.txt', 'a') as file:
        file.write(new_record)
        
    print("Employee record added.")

def view_all_employee_records():
    with open('employees.txt', 'r') as file:
        all_employees = file.read()
    print("A list of all employees:")
    print(all_employees)

def search_by_ID():
    ID = input("Enter ID to search: ")
    with open('employees.txt', 'r') as file:
        for line in file:
            if line.startswith(ID):
                print("Employee details:")
                print(line.strip())
                return
        print("Employee ID not found.")

def update_employee_info():
    ID = input("Enter ID to update: ")
    updated_info = input("Enter updated information (name, position, salary): ")
    updated_info = updated_info.split(", ")
    
    with open('employees.txt', 'r') as file:
        lines = file.readlines()
    
    found = False
    with open('employees.txt', 'w') as file:
        for line in lines:
            if line.startswith(ID):
                file.write(", ".join([ID] + updated_info) + "\n")
                print("Employee information updated.")
                found = True
            else:
                file.write(line)
    
    if not found:
        print("Employee ID not found.")

def delete_employee_record():
    ID = input("Enter ID to delete: ")
    
    with open('employees.txt', 'r') as file:
        lines = file.readlines()
    
    found = False
    with open('employees.txt', 'w') as file:
        for line in lines:
            if not line.startswith(ID):
                file.write(line)
            else:
                found = True
    
    if found:
        print("Employee record deleted.")
    else:
        print("Employee ID not found.")

def start():
    while True:
        print("\nChoose an option:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Your choice is: ")

        if choice == '1':
            add_new()
        elif choice == '2':
            view_all_employee_records()
        elif choice == '3':
            search_by_ID()
        elif choice == '4':
            update_employee_info()
        elif choice == '5':
            delete_employee_record()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Inorrect option, please try later again!")

start()