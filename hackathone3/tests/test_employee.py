import unittest
import uuid
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def test_employee_creation(self):
        emp_id = str(uuid.uuid4())
        emp = Employee("Anil","Finance","HR",30000,2,200,id = emp_id)
        
        self.assertEqual(emp.name, "Anil")
        self.assertEqual(emp.department, "Finance")
        self.assertEqual(emp.designation, "HR")
        self.assertEqual(emp.gross_salary, 30000)
        self.assertEqual(emp.tax, 2)
        self.assertEqual(emp.bonus, 200)
        self.assertEqual(emp.id, emp_id)
        
        
        tax_amount = 30000 * (2 / 100)
        expected_net_salary = 30000 - tax_amount + 200
        self.assertEqual(emp.net_salary(), expected_net_salary)
        
    def test_to_dict(self):
        t = Employee(name="Alice", department="Human Resources", designation="HR Manager",gross_salary=80000,tax=10,bonus=5000)
        d = t.to_dict()
        self.assertEqual(d['name'], "Alice")
        self.assertEqual(d['department'], "Human Resources")
        self.assertEqual(d['designation'], "HR Manager")
        self.assertEqual(d['gross_salary'],80000)
        self.assertEqual(d['tax'],10)
        self.assertEqual(d['bonus'],5000)
        self.assertEqual(d['id'], t.id)
        
    def test_from_dict(self):
        data = {
            'id': '1234-5678',
            'name': 'Alice',
            'department': 'Human Resources',
            'designation': 'HR Manager',
            'gross_salary':80000,
            'tax':10,
            'bonus':5000
            
        }
        t = Employee.from_dict(data)
        self.assertEqual(t.id, '1234-5678')
        self.assertEqual(t.name, 'Alice')
        self.assertEqual(t.department, "Human Resources")
        self.assertEqual(t.designation,"HR Manager")
        self.assertEqual(t.gross_salary, 80000)
        self.assertEqual(t.tax,10)
        self.assertEqual(t.bonus,5000)
        
if __name__ == "__main__":
    
    unittest.main()
        
        