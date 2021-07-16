# Scrapes random Urban Dictionary definitions
# Made by Timo Kats on 16/07/2021

import requests
from bs4 import BeautifulSoup

def only_letters(input):
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789')
    return ''.join(filter(whitelist.__contains__, input))

def export_csv(word,meaning,links):
    output = open('data.csv', 'a', encoding='utf-8')
    output.write(only_letters(word) + ';' + links + ';' + only_letters(meaning) + '\n')
    output.close()

def scrape():
    index = 1
    source = ""

    while index < 1000:
        url = 'https://www.urbandictionary.com/random.php?page=' + str(index)
        request = requests.get(url)
        if request.status_code == 200:
            source = request.text
            soup = BeautifulSoup(source, 'html.parser').find('div', class_='def-panel')

            # the seperate parts of urban dictionary
            word = soup.find('a', class_='word').text.lower()
            meaning = soup.find('div', class_='meaning').text.lower()
            links = []

            for elem in soup.findAll("a", {"class": "autolink"}):
                links.append(elem.text.lower())

        export_csv(word, meaning, str(links))
        index += 1

if __name__=='__main__':
    export_csv('word', 'meaning', 'links')
    scrape()