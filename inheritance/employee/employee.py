class Employee:
    def __init__(self,id,name,salary) -> None:
        self.id = id
        self.name = name
        self._salary = salary    # เห็นข้างหน้าเป็น # ให่ใส่ _

    def emp_detail(self):
        print(f'\nid: {self.id}')
        print(f'name: {self.name}')
        

    def _emp_salary(self):    # เห็นข้างหน้าเป็น # ให่ใส่ _ 
        print(f'salary: {self._salary}\n')                  
        
        
        
        
        
         # เห็นข้างหน้าเป็น - ให่ใส่ __ 