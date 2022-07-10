
from horse import Horse
from donkey import Donkey
    
class Mule(Horse,Donkey):

     
    def run(self):
        return (f'{self.show_name} is runnig')

    def show_info(self):
        print(f'***** Munu Info *****')
        print(f'Name: {self.show_name()}')
        print(f'Color: {self.color}')
        print(f'Max Height: {self.max_height}')
        print(f'Age: {self.age}')
        print(f'Weight: {self.weight}')
        

    
# obj
if __name__ == "__main__":
   
    mule1 = Mule(200,'Munu','Blue-eyed cream',3,200)
    mule1.show_info

    
    mule2 = Mule(200,'Meme','Palomino',1,120.7)
    mule2.sound
    mule2.show_info

    
    

    
#200,'Munu','Blue-eyed cream',3,200
    