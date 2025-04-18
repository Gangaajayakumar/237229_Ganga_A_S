import unittest
import os
from storage import Storage

class testStorage(unittest.TestCase):
    
    def setUp(self):
        self.filepath = 'employee.pkl'
        self.storage = Storage(self.filepath)
        
    def test_save_and_load(self):
        emp_list = [
            {'id':"1", "name" : "Ganga", "department":'Human Resources',"designation":"HR Manager","gross_salary":80000,"tax":10,"bonus":5000,"net_salary":77000},
            {'id':"2", "name" : "Ganga", "department":'Human Resources',"designation":"HR Manager","gross_salary":80000,"tax":10,"bonus":5000,"net_salary":77000}
        ]
        self.storage.save(emp_list)
        loaded = self.storage.load()
        self.assertEqual(len(loaded),2)
        self.assertEqual(loaded[0]['id'],"1")
        self.assertEqual(loaded[1]['id'],'2')
        self.assertEqual(loaded[0]['name'],"Ganga")
        self.assertEqual(loaded[0]['department'],"Human Resources")
        self.assertEqual(loaded[0]['designation'],"HR Manager")
        self.assertEqual(loaded[0]['department'],"Human Resources")
        self.assertEqual(loaded[0]['gross_salary'],80000)
        self.assertEqual(loaded[0]['tax'],10)      
        self.assertEqual(loaded[0]['bonus'],5000) 
        self.assertEqual(loaded[0]['net_salary'],77000)   
          
        
        
    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        