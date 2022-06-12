class Person:
    def __init__(self,name:str,gender:str,profession:str,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours):
        self.study = hours
    
    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study:{self.study}')

#person_1
jessa = Person('Jessa','Female','Software Engineer',10)
jessa.work()
jessa.show()

#person_2
jon = Person('Jon','Male','Doctor',15)
jon.work()
jon.show()

#lisa
lisa = Person('Lisa','Male','Korean Singer',10)
lisa.work()
lisa.show()

