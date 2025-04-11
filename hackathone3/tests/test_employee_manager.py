import unittest
from employee_manager import EmployeeManager

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        self.tm = EmployeeManager()
        
    def test_add_and_get_employee(self):
        self.tm.add_employee("Alice","Human Resources","HR Manager",80000,10,5000)
        self.tm.add_employee("Johnson","Human Resources","HR Manager",80000,10,5000)
        std = self.tm.view_employee()
        self.assertEqual(len(std),2)
       
    def test_search_ID(self):
        emp1 = self.tm.add_employee("Alice","Human Resources","HR Manager",80000,10,5000)
        result = self.tm.search_employee(emp1.id)
        self.assertTrue(result)
       
       
       
    def test_delete_employee(self):
        emp1 = self.tm.add_employee("Alice","Human Resources","HR Manager",80000,10,5000)
        result = self.tm.delete_employee(emp1.id)
        self.assertTrue(result)
        self.assertEqual(len(self.tm.view_employee()),0)
       
    def tearDown(self):
        return None