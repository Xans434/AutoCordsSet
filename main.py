import pyautogui
import time


class AutoClicker:
    def __init__(self):
        self.x_enterline = (387, 209)
        self.z_enterline = (395, 255)
        self.btn_setcoords = (384, 347)
        self.btn_launch = (395, 392)

    def enter_coord(self, coord, position):
        pyautogui.moveTo(position[0], position[1])
        pyautogui.click()
        pyautogui.write(coord)

    def execute_commands(self):
        pyautogui.moveTo(self.btn_setcoords[0], self.btn_setcoords[1])
        pyautogui.click()
        pyautogui.moveTo(self.btn_launch[0], self.btn_launch[1])
        pyautogui.click()

    def run(self):
        while True:
            coords = input('COORDS - XZ: ').strip()
            if not coords:
                continue

            coords_split = coords.split()
            if len(coords_split) != 2:
                print("Please enter two coordinates separated by a space.")
                continue

            time.sleep(3)
            self.enter_coord(coords_split[0], self.x_enterline)
            self.enter_coord(coords_split[1], self.z_enterline)
            self.execute_commands()


if __name__ == "__main__":
    autoclicker = AutoClicker()
    autoclicker.run()