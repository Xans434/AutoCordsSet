import pyautogui
import time

t = time
g = pyautogui

x_enterline = [387, 209]
z_enterline = [395, 255]


while True:
    coords = str(input('pls input COORDS - XZ: '))
    coords_split = coords.split()

    t.sleep(3)

    g.moveTo(x_enterline[0], x_enterline[1])
    g.leftClick()
    g.typewrite(coords_split[0])
    t.sleep(0.1)
    g.moveTo(z_enterline[0], z_enterline[1])
    g.leftClick()
    g.typewrite(coords_split[1])


    print(coords_split, x_enterline, z_enterline)