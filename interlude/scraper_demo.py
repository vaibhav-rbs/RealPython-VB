#!/usr/local/bin/python3

from urllib.request import urlopen

my_address = "https://realpython.com/practice/aphrodite.html"

html_page = urlopen(my_address)

html_text = html_page.read().decode('utf8')

print (html_text)


