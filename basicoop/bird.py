class Bird:
    global bird_type #global variable
        #ถ้าไม่ใส่คำว่า global จะกลายเป็น class variable
    bird_type = 'parrot'
    bird_name = 'Lori'  #class variable

    def __init__(self,colour) -> None:
        self.colour = colour #instance_variable
        name = 'Peter'    
        print(f'{name} in init')

if __name__ =='__main__':
    my_bird = Bird('Green,Blue')


    #call instance variable     #ชื่อวัตถุ.inatance_variable
    print(my_bird.colour)

    #call class variable         #ชื่อคลาส.class_variable
    print(Bird.bird_name)

    #call global.variable  #เรียกชื่อตัวแปลได้เลย
    print(bird_type)

    #error
    #พยายามเรียก local variable
    #print(name)#NameError: name 'name' is not defined
    #พยายามเรียก global variable ผ่าน class
    #print(Bird.bird_type)
    #print object 'Bird' has not attribute 'bird_type'