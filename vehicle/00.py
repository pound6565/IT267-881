class Vehicle:
    
    def __init__(self,name,wheels,max,vin) -> None:
        self.name = name
        self.wheels = wheels
        self._max_speed = max
        self.__vin = vin 

    def set_vin(self,vin):
        self.__vin = vin
        
    def v_detail():
        print(f'====================================')
        print(f'Name: {self.name}')
        print(f'====================================')
        print(f'Wheels: {self.wheels}')
        print(f'Max Speed: {self.max_speed}')
        print(f'Vin: {self.__vin}')
        
        

