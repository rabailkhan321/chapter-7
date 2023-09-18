"""
import requests
from bs4 import BeautifulSoup

timeanddate_url = "https://www.timeanddate.com/on-this-day/march/24"
response_timeanddate = requests.get(timeanddate_url)

soup_timeanddate = BeautifulSoup(response_timeanddate.content, 'lxml')

shared_birthday = soup_timeanddate.find("h3", class_="otd-life__title").text.strip()

# Find the parent <ul> element containing the names (assuming they are in a list)
ul_element = soup_timeanddate.find("ul", class_="list--big")

if ul_element:
    # Extract and print all the names within <li> elements that contain an <h3> with class "otd-title"
    list_items = ul_element.find_all("li")
    print("Shared Birthday Information:")
    print(shared_birthday)
    print("Names of People:")
    for item in list_items:
        h3_element = item.find("h3", class_="otd-title")
        if h3_element:
            item_text = h3_element.text.strip()
            print(item_text)
            
else:
    print("No shared birthday information found on this date.")
"""
# Date:18/09/2023
# CSC461 – Assignment1 – Web Scraping
#Name:Rabail Salman
# Registration : FA21-BSE-036
# brief description: From the ‘timeanddate’ website (https://www.timeanddate.com/on-this-day/march/24), I found out who you share birthdate with me(24 March).
#Then I have written the information that I have extracted in text file shared_birthday_info.txt

import requests
from bs4 import BeautifulSoup


timeanddate_url = "https://www.timeanddate.com/on-this-day/march/24"


response_timeanddate = requests.get(timeanddate_url)


soup_timeanddate = BeautifulSoup(response_timeanddate.content, 'lxml')


shared_birthday = soup_timeanddate.find("h3", class_="otd-life__title").text.strip()


ul_element = soup_timeanddate.find("ul", class_="list--big")


names = []


if ul_element:
    
    list_items = ul_element.find_all("li")
    for item in list_items:
        h3_element = item.find("h3", class_="otd-title")
        if h3_element:
            item_text = h3_element.text.strip()
            names.append(item_text)


file_path = "shared_birthday_info.txt"


with open(file_path, "w", encoding="utf-8") as file:
    file.write("Shared Birthday Information:\n")
    file.write(shared_birthday + "\n\n")
    file.write("Names of People:\n")
    for name in names:
        file.write(name + "\n")

print("Data has been written to 'shared_birthday_info.txt'")
