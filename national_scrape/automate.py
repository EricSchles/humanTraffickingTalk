from subprocess import *
import glob
import os

os.chdir("config")
urls = glob.glob("*.txt")
os.chdir("../")

for url in urls:
#generate the spider
    call(['python', 'generate_craigslist.py',url])
#run the spider
    call(['python', 'link_scrap.py',url])

