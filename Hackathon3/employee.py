import uuid

class Employee:
    
    def __init__(self,name:str,department:str,designation:str,gross_salary,tax,bonus,id=None):
        self.id = id if id else str(uuid.uuid4())
        self.name =name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_Salary = self.net_salary()
        
    def net_salary(self): 
        tax_amount = self.gross_salary * (self.tax / 100)
        self.net_Salary = self.gross_salary - tax_amount + self.bonus
        return self.net_Salary
        
    def to_dict(self):
        return {
            "id" : self.id,
            "name": self.name,
            "department":self.department,
            "designation": self.designation,
            "gross_salary":self.gross_salary,
            "tax":self.tax,
            "bonus":self.bonus,
            "net_salary":self.net_Salary
        }
        
    @staticmethod
    def from_dict(data):
        return Employee(
            name = data["name"],
            department= data["department"],
            designation= data["designation"],
            gross_salary= data["gross_salary"],
            tax=data["tax"],
            bonus=data["bonus"],
            #net_salary=data["net_salary"],
            id = data["id"]
            
        )
        
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Department: {self.department}, "
            f"Designation: {self.designation}, Gross Salary: {self.gross_salary}, "
            f"Tax: {self.tax}, Bonus: {self.bonus}, Net Salary: {self.net_Salary}")
        