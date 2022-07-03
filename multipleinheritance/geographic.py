#geographic.py
class Geographic:
    def setcordinate(self,lat,long):
        self.latitude = lat
        self.longitude = long
    
    def getcordinate(self):
        return f'Latitude: {self.latitude}\nLongitude: {self.longitude}'

    def gettimezone(self):
        timezone = round(self.longitude/12 - 1)     #round เพื่อให้ได้เลข กลมๆ
        if timezone > 0:
            return f'Timezone +{timezone}'  #Timezone+7
        else:
            return f'Timezone{timezone}' #Timezone-12

    def getclimate(self):
        if self.latitude <= -66.5 or self.latitude >= 66.5:
            return 'Polar Zone'
        elif self.latitude <= -23.5 or self.latitude >= 23.5:
            return 'Temperate Zone'
        else:
            return 'Tropical Zone'

 