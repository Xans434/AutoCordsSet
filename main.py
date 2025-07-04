import pyautogui
import time


t = time
g = pyautogui


x_enterline = [387, 209]
z_enterline = [395, 255]
btn_setcoords = [384, 347]
btn_launch = [395, 392]


def dx_enterline():
    g.moveTo(x_enterline[0], x_enterline[1])
    g.leftClick()
    g.typewrite(coords_split[0])

def dz_enterline():
    g.moveTo(z_enterline[0], z_enterline[1])
    g.leftClick()
    g.typewrite(coords_split[1])


def dstart_up():
    g.moveTo(btn_setcoords[0], btn_setcoords[1])
    g.leftClick()
    g.moveTo(btn_launch[0], btn_launch[1])
    g.leftClick()


while True:
    coords = str(input('COORDS - XZ: '))
    coords_split = coords.split()

    t.sleep(3)

    dx_enterline()
    dz_enterline()
    dstart_up()

    print(coords_split, x_enterline, z_enterline)