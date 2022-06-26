switch_status = False #สถานะปิด

def turn_on():  #ฟังก์ชันเปิดไฟ
    global switch_status
    switch_status = True 
    print("light on")

def turn_off(): #ฟังก์ชันปิดไฟ
    global switch_status
    switch_status = False
    print("light off")

if __name__ == "__main__":
    print(f'สถานะไฟ: {switch_status}')
    turn_on()
    turn_off()
    turn_off()
    turn_off()
