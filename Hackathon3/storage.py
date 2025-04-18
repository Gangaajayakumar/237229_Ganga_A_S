import pickle
import os

class Storage(object):
    
    def __init__(self,path = 'employee.pkl'):
        self.path = path
        
    def save(self,employee_list):
        with open(self.path,'wb') as f:
            pickle.dump(employee_list,f)
            
    def load(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, "rb") as f:
            return pickle.load(f)