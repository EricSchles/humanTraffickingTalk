import os
import glob
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

def time_posted(contents):
    offset = contents.find("Posted: <time datetime=")
    date = contents[offset+23:offset+49] 
    #this is a based on the conventions within craigslist
    #date format: year-month-dayTHour:minute:second-timezone (based on gmt)
    return date

def picture_check(contents):
    pattern = re.compile(".jpg")
    m = pattern.search(contents)
    if m == None:
        return False
    else:
        return True

def find_all_pictures(contents):
    page = BeautifulSoup(urllib2.urlopen(contents))
    pictures = page.findAll('img')
    return pictures


#getting the original link if pictures exist:

print "checking results in prostitutes..."
present_dir = "results/results_women/prostitutes"
os.chdir(present_dir)    
files_to_check = glob.glob("*.html")
has_pictures = []
files_to_check = glob.glob("*.html")
for i_file in files_to_check:
    
    j_file = open(i_file,"r")
    html_offset = i_file.find(".html")
    folder_name = i_file[:html_offset]
    j_contents = j_file.read()
    picture_exists = picture_check(j_contents)
    if picture_exists: #download all the picture
        os.chdir("../../../recursive_top_level/"+folder_name)
        config = open("config.txt","r")
        page = config.read()
        page = page.lstrip().rstrip()
        config.close()
        os.chdir("../../")
        has_pictures.append(page+"\n")
        os.chdir(present_dir)


os.chdir("../../../")
print "writing to picture_links.csv..."


if not os.path.exists("pictures"):
    os.mkdir("pictures")

print "downloading pictures to pictures folder..."
os.chdir("pictures")

results = open("picture_links.csv","w")
for i_file in has_pictures:
    i_file = i_file.strip("\n")
    pictures_uncleaned = find_all_pictures(i_file)
    for picture in pictures_uncleaned:
        picture = picture["src"]
        start = picture.find("http")
        pic = picture[start:]
        name = pic.split("/")[-1]
        
        results.write(i_file+","+name+"\n")
        
        f = open(name,'wb')
        f.write(urllib.urlopen(pic).read())
        f.close()

results.close()
