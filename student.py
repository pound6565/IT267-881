class Student:

    def __init__(self,id:str,name:str,major='IT') -> None:                  #major default "IT"
        self.id = id
        self.name = name
        self.major = major

    def printdisplay_detail(self):
        print(f'ID: {self.id}')
        print(f'NAME: {self.name}')
        print(f'MAJOR: {self.major}')

    def __del__(self):
        print('objest was destroyed')

if __name__ =="__main__":
    Jessica = Student('111','Jessica','IT')
    Jessica.printdisplay_detail()

    John = Student('112','John','MKT')
    John.printdisplay_detail()

    James = Student('113','James',)
    James.printdisplay_detail()

