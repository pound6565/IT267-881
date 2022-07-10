class Horse:
    max_height = 200
    def __init__(self,max : float,name : str,color : str):
        self.max_height = max
        self.name = name
        self.color = color

    def run(self):
        return f'{self.name} is runnig'

    def show_name(self):
        return f'Name : {self.name}'

    def show_info(self):
        return f'Name: {self.name} /nColor: {self.color} /nMax Height: {self.max_height}cm'

