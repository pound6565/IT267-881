class CoffeeOder:
    menu_type = 'coffee'
    total = 0

    def __init__(self,customer_name:str,menu:str,num = 1,size = 'R') -> None:
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        self.price = 0

    