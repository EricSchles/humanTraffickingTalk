from bs4 import BeautifulSoup, SoupStrainer
import os
from subprocess import *
import glob
import re

# config = open("config.txt","r")

# name = config.readline()    #for line is always the name of the scraper
# name = name.split('.')
# domain_name = name[1]+"."+name[2] #domain name
# domain_name = domain_name.strip()
# name = name[1]
# os.chdir(name+'scraper/')

# files_to_scrap = glob.glob('*')
# iterator = 0

# for i in files_to_scrap:
#     if ".cfg" in i:
#         del files_to_scrap[iterator]
#     if os.path.isdir(i):
#         del files_to_scrap[iterator]
#     if ".db" in i:
#         del files_to_scrap[iterator]
#     iterator += 1
    

# for i in files_to_scrap:
#     call(['cp', i, i+'.html'])

files_to_scrape = glob.glob("*.html")

print files_to_scrape

for i in files_to_scrape:
    print i+"\n\n"
    j_file = open(i, "r")
    j_contents = j_file.read()
    #print type(j_contents)
    #call(['cat', i, "|", "grep", "href"]
    m = re.findall('(?<=href=").+(?=")', j_contents)
    for j in m:
        print j
    print "end of file\n\n"
