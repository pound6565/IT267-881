#สร้างพนักงาน IT
from empit import EmpIT
mike = EmpIT('001','make',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#สร้างพนักงาน MKT
from empmkt import EmpMKT
anna = EmpMKT('002','anna',35000)
#anna.add_location()
#anna.add_commision()
anna.emp_detail()
anna.mkt_salary()

#สร้าง jess 003 เงินเดือน 45000 ทำงานอยู่เชียงใหม่ ได้คอมมิชชั่น 35%
jess = EmpMKT('003','Jess',45000)
jess.add_location('CNX')
jess.add_commision(35)
jess.emp_detail()
jess.mkt_salary()