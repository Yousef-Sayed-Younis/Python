import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class crwaledArticle():
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Bot:
    def article(self, name):
        count = 1
        page = 1
        pageIncrement = 10
        maxRetrieves = 100

        a = []

        url = "https://www.amazon.com/s?k=" + name + "&page" + str(page)

        options = Options()
        options.headless = False # Open Webprowser when the code is running
        options.add_experimental_option("detach", True)

        browser = webdriver.Chrome(ChromeDriverManager().install, options=options)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(10)
        
        while True:
            try:
                if pageIncrement*page > maxRetrieves: break

                if count > pageIncrement:
                    count = 1
                    page += 1

                # Get title
                xPathTitle = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + str(count) + ']/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
                title = brower.find_element_by_xpath(xPathTitle)
                titleText = title.get_attribute("innerHTML").splitlines()[0]
                title.click()

                xPathPrice = '//*[@id="price_inside_box"]'
                price = brower.find_element_by_xpath(xPathPrice)
                priceText = price.get_attribute("innerHTML")

                url = "https://www.amazon.com/s?k=" + name + "&page" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10)

                info = crwaledArticle(titleText, priceText)
                a.append(info)

                count += 1

            except Exception as e:
                print("Exception", e)
                count += 1
                if pageIncrement*page > maxRetrieves: break

                if count > pageIncrement:
                    count = 1
                    page += 1

                url = "https://www.amazon.com/s?k=" + name + "&page" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10)

        browser.close()

        return a

fetcher = Bot()


article = pd.DataFrame(
    {"title": fetcher.article('laptop'),}
)

article.to_csv("article.csv")

# with open('results.csv', newline=' ', encoding='utf-8') as csvfile:
#     articleWriter = csv.writer(csvfile, delimiter=";", quotecher='"', quoting=csv.QUOTE_MINIMAL)
#     for article in fetcher.article('laptop'):
#         articleWriter.writerow([article.title, article.price])
