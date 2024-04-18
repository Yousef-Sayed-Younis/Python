from time import sleep
from os import listdir
from random import choice
from os.path import abspath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


with open("./number.txt", "r") as numbers_file:
    numbers = numbers_file.read().split("\n")
    if numbers[-1] == "":
        numbers.pop()

with open("./messages.txt", "r", encoding="utf-8") as messages_file:
    messages = messages_file.read().split("\n_____\n")
    if messages[-1] == "":
        messages.pop()

with open("./ext-messages.txt", "r", encoding="utf-8") as ext_messages_file:
    ext_messages = ext_messages_file.read().split("\n_____\n")
    if ext_messages[-1] == "":
        ext_messages.pop()

# images = [f"{abspath('./imgs/' + img)}" for img in listdir("./imgs")]

while True:
    attach_image = input("Attach images? \n Yes: 1 No: 0   -->   ")
    if attach_image == "1" or attach_image == "0":
        attach_image = int(attach_image)
        break
    print("Please enter 1 or 2")


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

for number in numbers:
    counter = 0
    while True:
        try:
            url = "https://web.whatsapp.com/send?phone=" + number
            driver.get(url)
            sleep(5)
            footer = WebDriverWait(driver, timeout=30).until(Ec.presence_of_element_located((By.CLASS_NAME, "_1VZX7")))

            text = choice(messages) + "\n" + choice(ext_messages)
            js_excecution = f"const mainEl = document.querySelector('#main')\n"\
                "const textareaEl = mainEl.querySelector('div[contenteditable=\"true\"]')\n"\
                "if(!textareaEl) {\n"\
                "throw new Error('There is no opened conversation')\n"\
                "}\n"\
                "textareaEl.focus()\n"\
                f"document.execCommand('insertText', false, `{text}`)\n"\
                "textareaEl.dispatchEvent(new Event('change', { bubbles: true }))\n"\
                "setTimeout(() => {\n"\
                "(mainEl.querySelector('[data-testid=\"send\"]') || mainEl.querySelector('[data-icon=\"send\"]')).click()\n"\
                "}, 100)"
            driver.execute_script(js_excecution)
            sleep(2)

            if attach_image:
                driver.execute_script("document.querySelector('[data-testid=\"clip\"]').click()")
                upload_image_icon = WebDriverWait(driver, timeout=30)\
                    .until(Ec.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=\"Photos & Videos\"]")))
                upload_image_button = upload_image_icon.find_element(By.CSS_SELECTOR, "input")
                upload_image_button.send_keys(choice(images))
                send_button = WebDriverWait(driver, timeout=30).\
                    until(Ec.presence_of_element_located((By.CSS_SELECTOR, "[role='button'][aria-label='Send']")))
                send_button.click()

            print("sent successfully to --> " + number)
            sleep(5) if attach_image else sleep(2)
            break

        except Exception:
            counter += 1
            print(f"Unexpected error happened while sending to {number}")
            print(f"Trial number {counter + 1}")
            if counter == 3:
                print(f"Failed sending to {number}")
                break

print("Code Ended")
