from bank.account import Account
from bank.customer import Customer


#สร้าง obj ของ customer เพื่อเปิด บัญชี paul
#ข้อมูลลูกค้า paul,nontaburi,012-345-6789
paul = Customer()
paul.new_customer()

#สร้าง obj ของ account 
#ข้อมูลการเปิดบัญชี Siving, '0123-4578',500
paul_acc = Account()
paul_acc.open_account(paul.name,'Saving','0123-4578',500)


#แสดงข้อมูลของ customer Paul
print(paul.cus_info())

#แสดงข้อมูล balance ของบัญชี
print(paul_acc.display_balance())


