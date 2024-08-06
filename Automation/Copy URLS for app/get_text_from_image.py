import keyboard
# import webbrowser
# from time import sleep
import pyautogui as auto

def quotes():
    auto.keyDown("shift")
    auto.press("'")
    auto.keyUp("shift")

def paste():
    auto.hotkey("ctrl", "v")
    auto.press("right")
    auto.press(",")
    auto.press("enter")

def copy():
    auto.hotkey("shift", "home")
    auto.hotkey("ctrl", "c")

while True:
    if keyboard.is_pressed("shift"):
        copy()

    if keyboard.is_pressed("capslock"):
        quotes()

    if keyboard.is_pressed("ctrl"):
        paste()
    