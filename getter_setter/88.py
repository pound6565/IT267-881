class Area:
    def __init__(self) -> None:
        self.__base = 0
        self.__high = 0


    @property # getter for base
    def base(self):
        return self.__base

    @base.setter #setter for base
    def base(self,value):
        self.__base = value


    @property # getter for high
    def high(self):
        return self.__high

    @high.setter #setter for base
    def high(self,value):
        self.high = value     #self.__high = value 

    def compute_area(self):
        return 0.5 * self.base * self.high     #return 0.5 * self.__base * self.__high



    
    
    