class Car:
    brand = 'Toyota'

    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year 
        self.price = price
        
    def printCarDetail(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Colour: {self.colour}')
        print(f'Year: {self.year}')
        print(f'Price: {self.price:,.2f}')
        
        
    def __del__(self):
        print('objest was destroyed')

if __name__ == '__main__':
    myCar = Car("Supra","Red", 2019, 5000000)
    myCar.printCarDetail()

    bibeCar = Car("Camry","siver", 2021, 3000000)
    bibeCar.printCarDetail()