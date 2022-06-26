class Item:

    def __init__(self,name:str,price:float,quantity = 1) -> None:
        #ตรวจสอบ price, quantity ว่าต้อง > 0    #โดยใช้ assert 
        assert price > 0,f'Price {price} must greater than 0'
        assert quantity > 0,f'Quantity {quantity} must greater than 0'

        self.name = name                                 
        self.price = price
        self.quantity = quantity

    #instance method ต้องมีคำว่า (self)เสมอ
    #จะเรียกใช้ method นี้ได้จะต้องมีการสร้าง object 
    def total_price(self):                                  
        return self.price * self.quantity

    def __del__(self):
        print('object was destroyed')

if __name__ =='__main__':
     item1 = Item('monitor',5600,1)
     item2 = Item('mouse',1500,2)
     print('===Total Price===')
     print(f'{item1.name} : {item1.total_price():,.2f}')
     print(f'{item2.name} = {item2.quantity} : {item2.total_price():,.2f}')
     print(f'Total: {item1.total_price() + item2.total_price():,.2f}') 

