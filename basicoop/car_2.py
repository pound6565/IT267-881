class Car:
    brand = 'Toyota'

    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year 
        self.price = price
    #inatance method
    def printCarDetail(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Colour: {self.colour}')
        print(f'Year: {self.year}')
        print(f'Price: {self.price:,.2f}')

    #staticmethod ไม่มีคำว่า (self)    
    @staticmethod
    def get_static_method():
        text = 'static'
        print(f'In {text} method')
        # ตัวแปร text ใช้ได้ในแต่เฉพาะ get_static_method() เท่านั้น

    #class method ต้องมี cls
    @classmethod
    def get_class_method(cls):
        my_text = 'Class'
        print(f'This is {my_text} method')


    def __del__(self):
        print('objest was destroyed')

if __name__ == '__main__':
    myCar = Car("Supra","Red", 2019, 5000000)
    myCar.printCarDetail()

    #bibeCar = Car("Camry","siver", 2021, 3000000)
    #bibeCar.printCarDetail()

    #call static method
    Car.get_static_method() #เรียกผ่าน class
    myCar.get_static_method() #เรียกผ่าน instance/object

    #call class method
    Car.get_class_method() #เรียกผ่าน class 
    myCar.get_class_method() #เรียกผ่าน instance/object