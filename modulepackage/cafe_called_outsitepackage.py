#วิธีที่ 1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drink

#วิธีที่ 2
#from cafe import cafe_module

desert = Desserts()
print (desert.show_dessert())


drinks = Drink()
print(drinks.show_drink())

drinks.add_drink('smoothie')    #เพิ่ม Element ได้ทีละ 1    ________#เพิ่ม smoothie
print(drinks.show_drink())

drinks.add_drink('juice')  #เพิ่ม juice
print(drinks.show_drink())

