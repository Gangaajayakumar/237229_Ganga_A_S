import json

class Person:
    
    def __init__(self, name, age ,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def get_details(self):
        return f"{self.name},{self.age},{self.gender}"
        #print(f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender}")
    
class Employee(Person):
    
    def __init__(self, name, age, gender,emp_id,department,salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        
    def get_details(self):
        details = super().get_details()
        details += (
            f"{self.emp_id}"
            f"{self.department}"
            f"{self.salary}"
        )
        return details
        
    def is_eligible_for_bonus(self):
        if self.salary < 50000:
            print(True)
        
    def from_string(cls,data_string):
        #return cls(data_string)
        name, age, gender, emp_id, dep, salary = data_string.split(",")
        return cls(name, int(age), gender, emp_id, dep, float(salary))
    
    from_string = classmethod(from_string)
    
    def bonus_policy():
        print("__Bonus Policy__")
        print("If the salary is less than 50000, You are not eligible for bonus policy")
    bonus_policy = staticmethod(bonus_policy)
    
    
class Department:
    
    def __init__(self,name):
        self.name = name
        self.employees = []
        
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            print("Invalid employee!")
        
        
    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)
        
    
    def get_all_emplyees(self):
        return self.employees
 
       
#Data Persistence   
def save_to_json(employees, filename="employees.json"):
    with open(filename, "w") as file:
        json.dump([emp.__dict__ for emp in employees], file, indent=4)
    

def load_from_json(filename="employees.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [
                Employee(
                    name=emp_data['name'],
                    age=emp_data['age'],
                    gender=emp_data['gender'],
                    emp_id=emp_data['emp_id'],
                    department=emp_data['department'],
                    salary=emp_data['salary']
                )
                for emp_data in data
            ]
    except FileNotFoundError:
        print("JSON file is empty.")
        return []
        
        
    
# if __name__ == "__main__":
#     p = Person("Anil",35,"Male")
#     p.get_details()
    
#     e = Employee("Vimal",35,"Male","E101","HR",45000)
#     e.get_details()
#     print(e.is_eligible_for_bonus())
    
#     e1 = Employee.from_string("John,35,Male,E101,HR,45000")
#     e1.get_details()
#     e1.bonus_policy()
    

        
        
        
    
    