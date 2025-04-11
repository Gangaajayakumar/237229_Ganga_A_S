from employee import Employee

class EmployeeManager(object):
    
    def __init__(self):
        self.employees =[]
        
    #add employee
    def add_employee(self,name,department,designation,gross_salary,tax,bonus):
        employee = Employee(name,department,designation,gross_salary,tax,bonus)
        self.employees.append(employee)
        return employee
    
    #view all employee
    def view_employee(self):
        return self.employees
    
    #search employee
    def search_employee(self,id):
        for emp in self.employees:
            if emp.id == id:
                return emp
            return None
        
        
    #delete an employee
    def delete_employee(self,id):
        for emp in self.employees:
            if emp.id == id:
                self.employees.remove(emp)
                return True
            return False
        
    #load employee details
    def load_employee(self,employee_dict):
        self.employees = [Employee.from_dict(td) for td in employee_dict]
        
    #list of employee in dictionary fromat
    def to_dict_list(self):
        return [employee.to_dict() for employee in self.employees]
            
        