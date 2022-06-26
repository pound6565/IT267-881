# วิธีที่ 1
from measure import Measure

if __name__ == '__main__':
    modj = Measure()
    #ให้ user เลือกได้ว่าต้องการแปลงค่า inch หรือ cm
    #รับค่า ตัวเลขจาก user ได้
    
    choice = input('Choose menu to convert (1:inch),(2:cm):')

    if choice == '1':
        user_input = float(input('Enter Number: '))
        print(f'{user_input} inch. = {modj.inch_cm(user_input):.2f} cm.')
            
    elif choice == '2':
        user_input = float(input('Enter Number: '))
        print(f'{user_input} cm. = {modj.cm_inch(user_input):.2f} inch.')
    else:
        print('Choose wrong menu')

            
    #print(f'5 cm = {modj.cm_inch(5):.2f} inch') #1.97
    #print(f'18.5 inch = {modj.inch_cm(18.5):.2f} cm') #46.99



