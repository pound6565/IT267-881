from geographic import Geographic
from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation_density(self):
        return self.population / self.area

    def showdetail(self):
        #ชื่อประเทศ
        print(f'Country name: {self.name}')
        
        #สถานที่ตั้ง
        print(self.getcordinate())

        #แสดงขนาดพื้นที่, จำนวนประชากร และความหนาแน่นของประชากร
        print(f'Area: {self.area}')
        print(f'Population: {self.population} Million')
        print(f'Density: {self.getpopulation_density()}')

        #Time Zone, Climate, Temperature, Weather
        print(f'Timezone: {self.gettimezone()}')
        print(f'climate: {self.getclimate()}')
        print(f'Timeperature(C): {self.celsius}')
        print(f'Timeperature(F): {self.getfarenheit()}')
        print(f'Weather: {self.getweather()}')
        print()


