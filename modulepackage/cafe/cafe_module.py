class Desserts:
    def __init__(self) -> None:
        self.dessert = ['ข้าวเหนียวมะม่วง','ข้าวเหนียวทุเรียน','ไอศครีม']
    
    def show_dessert(self):
        return f'Dessert Mene: {self.dessert}'

class Drink:
    def __init__(self) -> None:
        self.drink = ['coffee','tea','soda','wine']

    def add_drink(self,new_drink):
        self.drink.append(new_drink)

    def show_drink(self):
        return f'Drink Menu: {self.drink}'
        