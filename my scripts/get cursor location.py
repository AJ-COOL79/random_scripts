import pyautogui, time
from os import system

while True:
    x, y = pyautogui.position()
    pos_str = "x: " + str(x).rjust(2) + " y: " + str(y).rjust(2)
    print(pos_str)
    system("cls")