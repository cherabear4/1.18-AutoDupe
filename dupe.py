import time
import pyautogui
import keyboard
import sys

def main():
    time.sleep(3)
    pyautogui.rightClick()
    time.sleep(0.3)
    pyautogui.rightClick()
    time.sleep(0.3)
    pyautogui.click(900, 220)
    pyautogui.click()
    pyautogui._mouseMoveDrag
    time.sleep(0.5)

while True:
    #you have to spam equal to stop the program because idk its kinda broken
    if keyboard.is_pressed('='):
        print('Exiting')
        sys.exit()
        
    main()
