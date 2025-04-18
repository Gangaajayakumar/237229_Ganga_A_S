from employee_manager import EmployeeManager
from storage import Storage

def display_emploee(employees: list) -> None:
    if not employees:
        print("No employee details to display")
    else:
        for employee in employees:
            print(f'{employee.id},{employee.name},{employee.department},{employee.designation},{employee.gross_salary},{employee.tax},{employee.bonus},{employee.net_Salary}')
            
def main():
    
    manager = EmployeeManager()
    store =Storage()
    
    saved_data = store.load()
    manager.load_employee(saved_data)
    
    while True:
        
        print("Employee Management CLI App")
        print("\n1.Add Employee \n2.View all employee \n3.Search employee by ID \n4.Delete Employee \n5.Exit\n")  
        choice = input("Enter the choice->")
        
        if choice == '1':
            name = input("Enter a name: ")
            department = input("Enter the department: ")
            designation = input("Enter the designation: ")
            gross_salary = float(input("Enter the gross salary:"))
            tax = float(input("Enter the tax rate:"))
            bonus = float(input("Enter the bonus:"))
            employees = manager.add_employee(name,department,designation,gross_salary,tax,bonus)
            store.save(manager.to_dict_list())
            print(f"Employee added with ID: {employees.id}")
            
        elif choice == '2':
                display_emploee(manager.view_employee())
                
        elif choice == '3':
            tid = input("Enter the ID to search: ")
            result = manager.search_employee(tid)
            if (result):
                print(result)
                store.save(manager.to_dict_list())
                print("Search data")
            else:
                print("Student ID not found")
                
        elif choice == '4':
            tid = input("Enter the ID to delete: ")
            if manager.delete_employee(tid):
                store.save(manager.to_dict_list())
                print("employee details deleted")
            else:
                print("employee ID not found")
                
        elif choice == '5':
            print("Goodbye !")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":

    main()
     
    
    