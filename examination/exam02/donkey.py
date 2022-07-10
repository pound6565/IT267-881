class Donkey:
    def __init__(self, age:int, weight:float):
        self.age = age
        self.weight = weight

    def sound(self):
        return f'Donky makes eeyore sound'

    def show_info(self):
        return f'Age:{self.age}-year-old /nWeight: {self.weight}kg'


