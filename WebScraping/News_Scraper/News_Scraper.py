from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import requests
import time
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
def createTxt(title, article, directory):
    title = title.replace(':', '')
    title = title.replace("?", '')
    title = title.replace(' ', '_')
    title = title.replace('|', '')
    title = title.replace('/', '')

    if article != "":
        path = directory + '/' + title + '.txt'

        with open(path, "w", encoding="utf-8") as newsTxt:
            newsTxt.write(article)
    

def getLinks(url):

    r = requests.get(url).text #@@ Working For Most 
    soup = BeautifulSoup(r, 'lxml')
    
    links = []


    if 'bbc' in url:
        if 'sport' in url: #@@
            directory = 'Sports'
            headLins = soup.find_all("div", class_='gs-c-promo-body gs-u-mt@m gel-1/2@xs gel-1/1@m')
            for href in headLins:
                if ("http" not in href.a['href']) and ('av' not in href.a['href']) and ('live' not in href.a['href']) and ('golf' not in href.a['href']):
                    links.append("https://www.bbc.com" + href.a['href'])

        elif 'health' in url: #@@
            directory = 'Health'
            for num in range(1, 51):

                nextPage = f'https://www.bbc.com/news/live/health-47160630/page/{num}'
                
                r = requests.get(nextPage).text
                soup = BeautifulSoup(r, 'lxml')
                
                headLins = soup.find_all("h3", class_='lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-')
                for href in headLins:
                    try:
                        if "http" not in href.a['href']:
                            links.append("https://www.bbc.com" + href.a['href']) 
                    except:
                        pass

        elif 'world' in url: #@@
            directory = 'World'
            for num in range(1, 51):

                nextPage = f'https://www.bbc.com/news/live/world-47639450/page/{num}'

                r = requests.get(nextPage).text
                soup = BeautifulSoup(r, 'lxml')

                headLins = soup.find_all("h3", class_='lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-')
                for href in headLins:
                    try:
                        if "http" not in href.a['href']:
                            links.append("https://www.bbc.com" + href.a['href'])
                    except:
                        pass
                
        elif 'business' in url: #@@
            directory = 'Business'
            for num in range(1, 51):

                nextPage = f'https://www.bbc.com/news/live/business-47737521/page/{num}'

                r = requests.get(nextPage).text
                soup = BeautifulSoup(r, 'lxml')

                headLins = soup.find_all("h3", class_='lx-stream-post__header-title gel-great-primer-bold qa-post-title gs-u-mt0 gs-u-mb-')
                for href in headLins:
                    try:
                        if "http" not in href.a['href']:
                            links.append("https://www.bbc.com" + href.a['href'])
                    except:
                        pass


    if 'cnn' in url:
        if 'politics' in url: #@@
            directory = 'Politics'
            driver = webdriver.Chrome()
            driver.minimize_window()
            driver.get(url)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"lxml")
            time.sleep(1)

            headLins = soup.find_all('h3', class_='cd__headline')

            for h3_tag in headLins:
                if "http" not in h3_tag.a['href']:
                    links.append("https://www.cnn.com" + h3_tag.a['href'])

            driver.quit()

        elif 'health' in url: # @@
            directory = 'Health'
            headLins = soup.find_all("h3", class_='cd__headline')
            for href in headLins:
                try:
                    if 'http' not in href.a['href']:
                        links.append('https://us.cnn.com' + href.a['href'])
                except:
                    pass
        
        elif 'entertainment' in url: # @@
            directory = 'Entertainment'
            headLins = soup.find_all("h3", class_='cd__headline')
            for href in headLins:
                try:
                    if 'http' not in href.a['href']:
                        links.append('https://us.cnn.com' + href.a['href'])
                except:
                    pass

        elif 'business' in url: # @@
            directory = 'Business'
            headLins = soup.find_all("h3", class_='cd__headline')
            for href in headLins[:13]:
                if 'http' not in href.a['href']:
                    links.append('https://us.cnn.com' + href.a['href'])   


    if 'fox' in url:
        if 'business' in url: #@@
            directory = 'Business'
            headLins = soup.find_all("h3", class_='title title-color-default')
            for href in headLins:
                links.append(href.a['href'])
        
        else: #@@
            if 'health' in url:
                directory = 'Health'
            elif 'world' in url:
                directory = 'World'
            elif 'sports' in url:
                directory = 'Sports'
            elif 'politics' in url:
                directory = 'Politics'
            elif 'entertainment' in url:
                directory = 'Entertainment'

            browser = webdriver.Chrome()
            browser.minimize_window()
            browser.get(url)
            showMore = browser.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div/main/section[2]/footer/div')

            for x in range(100):
                
                Showmore = browser.find_element_by_link_text("Show More")
                Showmore.click()

                try:
                    element = WebDriverWait(browser, 10).until(
                        EC.presence_of_all_elements_located((By.LINK_TEXT, "Show More"))
                    )
                    element.click()
                except:
                    pass
                
            browser.implicitly_wait(5)

            content = browser.page_source.encode('utf-8').strip()

            soup = BeautifulSoup(content, 'lxml')

            headLins = soup.find_all("h4", class_='title')
            for href in headLins:
                try:
                    if 'http' not in href.a['href'] and (("https://www.foxnews.com" + href.a['href']) not in links):
                        links.append("https://www.foxnews.com" + href.a['href'])
                except:
                    pass
            
            print(links)
            


    if 'abc' in url: #@@
        if 'Health' in url:
            directory = 'Health'
        elif 'Business' in url:
            directory = 'Business'
        elif 'Sports' in url:
            directory = 'Sports'
        elif 'Politics' in url:
            directory = 'Politics'
        elif 'Entertainment' in url:
            directory = 'Entertainment'

        headLins = soup.find_all("div", class_='ContentRoll__Headline')
        for href in headLins:
            if 'video' not in href.a['href']:
                links.append(href.a['href'])  
        

    if 'politico' in url:
        directory = 'Politics'
        for num in range(1, 5514):

            nextPage = f'https://www.politico.com/politics/{num}'

            r = requests.get(nextPage).text
            soup = BeautifulSoup(r, 'lxml')

            headLins = soup.find_all("div", class_='summary')
            for href in headLins:
                try:
                    links.append(href.a['href'])
                except:
                    pass


    for new in links: # Getting title and article from all the news
            
        articles = []

        r = requests.get(new)
        soup = BeautifulSoup(r.text, 'lxml')


        if 'bbc' in new: #@@
            if 'sport' in new: 
                title = soup.title.text
                container = soup.find_all('div', class_='qa-story-body story-body gel-pica gel-10/12@m gel-7/8@l gs-u-ml0@l gs-u-pb++')

                for text in container:
                    articles.append(text.text)

                article = ''.join(articles)

                # Creating Txt Files:
                createFolder(directory)
                createTxt(title, article, directory)

            else:
                title = soup.title.text
                container = soup.find_all('div', class_='ssrcss-uf6wea-RichTextComponentWrapper e1xue1i83')
                for text in container:
                    articles.append(text.text)

                article = ''.join(articles)

                createFolder(directory)
                createTxt(title, article, directory)

        if 'cnn' in new: #@@ Working
            title = soup.title.text
            article = soup.find_all('div', class_='l-container')[3].text

            createFolder(directory)
            createTxt(title, article, directory)
            

        if 'fox' in new: #@@
            try:
                title = soup.title.text
                ignore = soup.find('div', class_='featured featured-video video-ct')
                container = ignore.find_next_siblings()
                for text in container:
                    articles.append(text.text)
            except:
                pass

            article = ''.join(articles)

            createFolder(directory)
            createTxt(title, article, directory)


        if 'abc' in new: #@@
            title = soup.title.text
            container = soup.find_all('section', class_='Article__Content story')
            for text in container:
                articles.append(text.text)

            article = ''.join(articles)

            createFolder(directory)
            createTxt(title, article, directory)


        if 'politico' in new: #@@
            title = soup.title.text
            container = soup.find_all('div', class_='story-text')

            for div in container: 
                try:    
                    children = div.findChildren('p')
                    for child in children:
                        articles.append(child.text)
                except:
                    pass

            article = ''.join(articles)

            createFolder(directory)
            createTxt(title, article, directory)
 


Links = {
        1 : 'https://www.bbc.com/news/health', 
        2 : 'https://us.cnn.com/health',
        3 : 'https://www.foxnews.com/health',
        4 : 'https://abcnews.go.com/Health',

        5 : 'https://www.bbc.com/news/world',
        6 : 'https://www.foxnews.com/world',

        7 : 'https://us.cnn.com/business',
        8 : 'https://www.bbc.com/news/business',
        9 : 'https://www.foxbusiness.com/',
        10 : 'https://abcnews.go.com/Business',

        11 : 'https://www.bbc.com/sport',
        12 : 'https://www.foxnews.com/sports',
        13 : 'https://abcnews.go.com/Sports',

        14 : 'https://us.cnn.com/politics',
        15 : 'https://www.foxnews.com/politics',
        16 : 'https://www.politico.com/politics',
        17 : 'https://abcnews.go.com/Politics',
    
        18 : 'https://abcnews.go.com/Entertainment',
        19 : 'https://us.cnn.com/entertainment',
        20 : 'https://www.foxnews.com/entertainment',
}


for Link in Links:
    print(str(Link) + ' ' + Links[Link])

Number = int(input("Enter The Number Of Link: "))
url = Links[Number]

getLinks(url)