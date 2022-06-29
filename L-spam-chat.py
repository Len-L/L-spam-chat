

import pyautogui
import time

pesan = input("Enter Message-> ")
time.sleep(2)
print("Example '4' ")
n = int(input("how many messages-> "))
print("move to screen chat")

time.sleep(5)

for i in range(n):
    pyautogui.typewrite(pesan)
    pyautogui.press("enter")


