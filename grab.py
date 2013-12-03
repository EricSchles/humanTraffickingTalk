from bs4 import BeautifulSoup
from sys import argv
html = argv[1]
 
soup = BeautifulSoup(html)
print soup

for link in soup.find_all('a'):
    print link

