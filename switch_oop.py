class Switch():
    def __init__(self) -> None:
        self.switch_status = False

    def turn_on(self):
        self.switch_status = True

    def turn_off(self):
        self.switch_status = False

    def show_status(self):
        if (self.switch_status):
            print(f"{'light on'} :)")
        else:
            print(f"{'light off'} :(")

#สร้าง object
sobj = Switch()

if __name__ == "__main__":
    
    sobj.show_status()
    sobj.turn_on()
    sobj.show_status()
    sobj.turn_off()
    sobj.show_status()
    sobj.turn_off()
    sobj.show_status()
    sobj.turn_off()
    sobj.show_status()