from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# pyautogui.displayMousePosition()

def click(x, y):
    win32api.SetCursorPos((x, y)) # Set the mouse in this Position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(1340, 450)[0] == 0: # Click When the Red value = 0
        click(1340, 450)
    if pyautogui.pixel(1425, 450)[0] == 0:
        click(1425, 450)
    if pyautogui.pixel(1500, 450)[0] == 0:
        click(1500, 450)
    if pyautogui.pixel(1590, 450)[0] == 0:
        click(1590, 450)

