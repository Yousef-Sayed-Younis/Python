import pyautogui as auto
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://docs.google.com/spreadsheets/d/1xe3HdySFkg4qaUekiswadSkLmUZbNanOUsylPPxvOpI/edit?usp=sharing")
driver.maximize_window()

copyPos = []
for i in copyPos:
    auto.click(304, 381)
    auto.hotkey('ctrl', 'c')
    auto.hotkey('ctrl', 't')
    auto.hotkey('ctrl', 'v')
# auto.displayMousePosition()
# 304, 381
# 496, 377
# 662, 379
# email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "input[autocomplete='username']")))
# email.clear()
# email.send_keys("zxwr.gm@gmail.com")

# next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "button[type='button']"))).click()
