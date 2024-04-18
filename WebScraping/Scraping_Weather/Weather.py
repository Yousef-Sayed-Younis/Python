import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.09969000000007&lon=-118.33512999999999#.YAbuI-jXJPY")
soup = BeautifulSoup(page.content, "html.parser") # Give me all page
# print(soup.find_all("a")) # Find all tags of a

week = soup.find(id="seven-day-forecast-body")
# print(week)

items = week.find_all(class_="tombstone-container")
# print(items[0])

# print(items[1].find(class_="period-name").get_text()) # Get the text 
# print(items[1].find(class_="short-desc").get_text())
# print(items[1].find(class_="temp").get_text())

period_names = [item.find(class_="period-name").get_text() for item in items[1:]] # List Coprehension
short_descriptions = [item.find(class_="short-desc").get_text() for item in items[1:]] # List Coprehension
temperatures = [item.find(class_="temp").get_text() for item in items[1:]] # List Coprehension

# print(period_names)
# print(short_descriptions)
# print(temperatures)

weather = pd.DataFrame( # Make Columns and Rows
    {"period": period_names,
    "descriptions": short_descriptions,
    "temperatures": temperatures,
    }
)

print(weather)

weather.to_csv('weather.csv')