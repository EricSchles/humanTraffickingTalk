from subprocess import *
import os
import hashlib
import glob
import time
import datetime
import sqlite3


present_dir = os.getcwd()

config = open("config.txt","r")

#md5 function comes from http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python/4213255#4213255

#we strip the trailing newlines with strip() because it causes a formatting error
#when we try to write to the name_spider.py file  
name = config.readline()    
name = name.split('.')
name = name[1]

config.close()
        
def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()



#change directories into the top of the scrapper
os.chdir(name+'scraper/')
print "starting the scraper for the desired webpages"

call(['scrapy', 'crawl', name])

files_to_hash = glob.glob('*') 
iterator = 0
#cleaning unwanted files
for i in files_to_hash:
    if ".cfg" in i:
        del files_to_hash[iterator]
    if os.path.isdir(i):
        del files_to_hash[iterator]
    iterator += 1


md5list = {}

for i in files_to_hash:
    md5list[i] = md5sum(i)



ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#format: year-month-day hour:minute:second

#update the database

if not name+'_md5_list.db' in glob.glob('*'):
    conn_md5 = sqlite3.connect(name+'_md5_list.db')
    conn_md5.text_factory = str
    c_md5 = conn_md5.cursor()
    c_md5.execute('''CREATE TABLE md5
                  (files, md5, timestamp)''')

    conn_md5.commit()
else:
    conn_md5 = sqlite3.connect(name+'_md5_list.db')
    conn_md5.text_factory = str
    c_md5 = conn_md5.cursor()
    

for files in files_to_hash:
    c_md5.execute("INSERT INTO md5 VALUES ('%s', '%s', '%s')" % (files, md5list[files], st) ) 
    conn_md5.commit()

conn_md5.close()
#hashing works, now time stamp needs to be added and then the data base needs to be generated / updated

#change back to the toplevel directory
os.chdir(present_dir)


