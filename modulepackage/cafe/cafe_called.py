#วิธีที่ 1
from cafe_module import Desserts
from cafe_module import Drink

#วิธีที่ 2
#from cafe_module import Dessert,Drink

desert = Desserts()
print (desert.show_dessert())


drinks = Drink()
print(drinks.show_drink())
drinks.add_drink('smoothie')
print(drinks.show_drink())
drinks.add_drink('juice')
print(drinks.show_drink())