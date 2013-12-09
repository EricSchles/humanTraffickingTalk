"""
This script creates a file that has the domain name and the starting urls for a new scrapper class.  These urls are line seperated.
"""
import os
from subprocess import *


if not os.path.exists("config"):
    os.mkdir("config")

os.chdir("config")
call(['cp', '../national_links.txt', 'national_links.txt'])

urls = open("national_links.txt", "r")

for url in urls:
    
    full_line = url.split(",")
    name = full_line[1].rstrip().lstrip()
    name = name.replace("/","")
    name = name.replace("(","")
    name = name.replace(")","")
    name = name.replace("-","")
    name = name.replace(" ","_")
    
    url = full_line[0].rstrip().lstrip()
    config = open(name+"_config.txt","w")
    base = url
    start = url+"/cas/"

    to_append = start
    url_list = []
    url_list.append(base)
    url_list.append(start)

    for i in xrange(1,1000):
        to_append += "index"+str(i)+"00.html"
        url_list.append(to_append)
        to_append = start

    for i in url_list:
        config.write(i + "\n")
    
    config.close()


urls.close()
