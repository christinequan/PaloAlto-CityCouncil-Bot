import selenium
import requests
from bs4 import BeautifulSoup
import pprint
import PyPDF2

# GLOBAL VARS
URL = 'http://www.cityofpaloalto.org/gov/agendas/council/2016.asp'

def get_data():

    html = requests.get(URL)
    soup = BeautifulSoup(html.text, 'lxml')
    table = soup.find("tbody")

    for row in table.findAll("tr"):
        col = row.findAll("td")
        date = col[0].text.encode('utf-8')
        if col[3].text.encode('utf-8') == "Transcript":
            print col[3].contents

def main():
    get_data()

main()
