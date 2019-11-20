#! python3

#This is a simple script I made out of pure boredom.  It simply grabs all the urls from a user-defined site.
#More features to be added?

import requests
from bs4 import BeautifulSoup

def main():
    url = input('Please type a url: ')
    url = url.lower()

    if url.startswith('https://www.')  or url.startswith('http://www.'):
        source = requests.get(url)
        soup = BeautifulSoup(source.text, features='html.parser')

        for link in soup.findAll('a'):
            href_raw = link.get('href')

            print(href_raw)

    else:
        print("That's not a url!  Please make sure you format it like this: 'https://www.YOURSITE.com'")
        main()

main()
