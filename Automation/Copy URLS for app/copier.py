import webbrowser
from time import sleep
import pyautogui as auto

first_url = input("Enter First URL: ")

webbrowser.open(first_url)

num = 0

while True:
    sleep(3)
    auto.hotkey("ctrl", "l")

    auto.hotkey("ctrl", "c")

    if num == 0:
        auto.keyDown("alt")

        auto.press("tab")

        auto.press("tab")

        auto.keyUp("alt")

        num += 1

    else:
        auto.hotkey("alt", "tab")

    auto.press("enter")

    auto.hotkey("shift", "'")

    auto.hotkey("ctrl", "v")

    auto.hotkey("shift", "'")

    auto.press("ctrlright")

    auto.press(",")

    auto.hotkey("alt", "tab")

    auto.press("esc")

    sleep(3)

    auto.hotkey("shift", "n")
