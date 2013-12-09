from subprocess import *
import os
import hashlib
import glob
import time
import datetime
import sqlite3

def main():
    present_dir = os.getcwd()

    config = open("config.txt","r")

    #md5 function comes from http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python/4213255#4213255

    #we strip the trailing newlines with strip() because it causes a formatting error
    #when we try to write to the name_spider.py file  
    name = config.readline()    
    dir_name = name.split('.')
    dir_name = dir_name[1]
    name = name.strip("\n")

    config.close()

    #change directories into the top of the scrapper
    os.chdir(dir_name+'_sample/')
    print "starting the scraper for the desired webpages"

    call(['scrapy', 'crawl', dir_name,"-o","items.csv","-t","csv"])

    csv_file = open("items.csv", "r")
    urls_to_scrape = []
    for i in csv_file:
        line = i.split(",")
        if line[1][0] != "/":
            continue
        urls_to_scrape.append(name+line[1])

    urls_file = open("urls_to_scrape.txt", "w")
    for i in urls_to_scrape:
        urls_file.write(i+"\n")

    call(['mv', './urls_to_scrape.txt', present_dir])
