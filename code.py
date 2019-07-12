# CircuitPython demo - I2C scan
import adafruit_ssd1306
from adafruit_circuitplayground.express import cpx
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
oled.fill(0)
oled.show()
cpx.pixels[7] = (0, 255, 0)
cpx.pixels[6] = (0, 255, 0)

class Heart:
    def __init__(self, center_x, center_y, size=5):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size

    def drawSelf(self):
        draw_Heart(self.center_x, self.center_y, self.size)

def draw_Heart(xpos0, ypos0, height, col=1):
    oled.pixel(xpos0, ypos0, col)
    for i in range(height):
        oled.pixel(xpos0-i, ypos0-i, col)
        oled.pixel(xpos0+i, ypos0-i, col)
    oled.pixel(xpos0, ypos0-height, col)
    oled.pixel(xpos0+4, ypos0-height, col)
    oled.pixel(xpos0-4, ypos0-height, col)
    oled.pixel(xpos0+3, ypos0-height-1, col)
    oled.pixel(xpos0-3, ypos0-height-1, col)
    oled.pixel(xpos0+2, ypos0-height-1, col)
    oled.pixel(xpos0-2, ypos0-height-1, col)

hearts = [Heart(10, 10), Heart(20, 10), Heart(30, 10)]

class Pet:
    def __init__(self, petName, petType, petAge):
        self.petName = petName
        self.petType = petType
        self.petAge = petAge
        self.petHunger = 100
        self.petHappy = 100
        self.center_x = 50
        self.center_y = 30
        self.inc = 3

    def drawSelf(self):
        draw_Pet(self.center_x, self.center_y, self.petType)
        oled.text(self.petName, self.center_x-10, self.center_y+10, 'blue')

    def wanderSelf(self):
        if self.center_x >= oled.width-10:
            self.inc = -self.inc
        elif self.center_x < 0:
            self.inc = -self.inc
        self.center_x = self.center_x+self.inc


def draw_Pet(center_x, center_y, petType):
    oled.rect(center_x, center_y, 10, 10, 'blue')
    oled.pixel(center_x+2, center_y+2, 1)
    oled.pixel(center_x+6, center_y+2, 1)
testPet = Pet('Kiwi', 'type1', 0)
myPlaces = ["Home", "Store", "Games", "Food"]
selected = myPlaces[1]
currentPlace = myPlaces[0]
def menu_Next(selected):
    print(selected)

def draw_Ui():
    oled.text(' Smol Fren', 40, 5, 'blue')
    oled.text("Store", 0, oled.height-10, 'blue')
    oled.text("Games", 40, oled.height-10, 'blue')
    oled.text("Food", 80, oled.height-10, 'blue')
    hearts[0].drawSelf()
    hearts[1].drawSelf()
    hearts[2].drawSelf()
    myString = "At: "+currentPlace
    oled.text(myString, 0, 20, 'blue')

    if selected == myPlaces[1]:
        myX = 0
    elif selected == myPlaces[2]:
        myX = 40
    else:
        myX = 80
    oled.rect(myX, oled.height-1, 20, 1, 'blue')
buttonA = cpx.button_a
buttonB = cpx.button_b
while True:
    oled.fill(0)

    testPet.drawSelf()
    testPet.wanderSelf()
    if cpx.button_a:
        menu_Next(selected)
    draw_Ui()
    oled.show()