import re
import os
from subprocess import *
import glob

#terminal nodes
def w4m_check(contents):
    pattern = re.compile("w4m")
    m = pattern.search(contents)
    if m == None:
        return False
    else:
        return True

def picture_check(contents):
    pattern = re.compile(".jpg")
    m = pattern.search(contents)
    if m == None:
        return False
    else:
        return True

#none terminal nodes
def number_of_pictures(contents):
    m = re.findall(".jpg",contents)
    return len(m)

def time_posted(contents):
    offset = contents.find("Posted: <time datetime=")
    date = contents[offset+23:offset+49] 
    #this is a based on the conventions within craigslist
    #date format: year-month-dayTHour:minute:second-timezone (based on gmt)
    return date


#it's not clear how to do this yet.
# def hourly_rate(contents):
    
def digit_grab(body):
    #there are a few distinct obfuscation patterns:
    #one: numbers interlaced in the text
    phone_number = []
    for i in body:
        if i.isdigit():
            phone_number.append(i)
    if len(phone_number) == 9 or len(phone_number) == 10:
        
        return ''.join(phone_number)
    else:
        return None



#three: special characters interlaced with text - this may not matter

def word_to_digit(text):
    text = text.replace("ONE","1")
    text = text.replace("TWO","2")
    text = text.replace("THREE","3")
    text = text.replace("FOUR","4")
    text = text.replace("FIVE","5")
    text = text.replace("SIX","6")
    text = text.replace("SEVEN","7")
    text = text.replace("EIGHT","8")
    text = text.replace("NINE","9")
    text = text.replace("ZERO","0")
    return text

def year_old(contents):
    year_old = contents.find("year old")
    
    if year_old != -1:
        age_final = contents[year_old-3:year_old-1]
        return age_final
    else:
        return None

def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()



#generate a list of phone numbers, check for duplicates between postings.
#This may inform possible collusion and may lead to trafficking rings.


#implement other checks as functions, call all of them on the contents
#based on the results from each function check, create an entry in the database,
#these entries determine the overall likelihood of a given posting being what you expect




if not os.path.exists("cleaned_results"):
    os.mkdir("cleaned_results")

files_to_check = glob.glob("*.html")
for i_file in files_to_check:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    w4m = w4m_check(j_contents)
    picture_exists = picture_check(j_contents)
    #with women seeking men and picture we are able to conclusively determine
    #whether a given posting is not a prostitute
    if w4m and picture_exists:
        call(['mv', "./"+i_file, "cleaned_results/"])
        

os.chdir("cleaned_results")    
files_to_check = glob.glob("*.html")
initial = []
w_translate = []
for i_file in files_to_check:
    j_file = open(i_file,"r")
    j_contents = j_file.read()
    start_offset = j_contents.find('<section id="postingbody">')
    end_offset = j_contents.find('</section>',start_offset)
    post_body = j_contents[start_offset:end_offset]

    #determine phone numbers
    translated_body = post_body.upper()
    translated_body = word_to_digit(translated_body)
    phone_number = digit_grab(post_body)
    phone_translated = digit_grab(translated_body)
    #time posted
    date = time_posted(post_body)
    if phone_number != None:
        initial.append([phone_number,i_file,date])
    if phone_translated != None:
        w_translate.append([phone_translated,i_file,date])

    #determine age
    age = year_old(post_body)

    
    

for init_index,init_elem in enumerate(initial):
    for w_index,w_elem in enumerate(w_translate):
        if init_elem[1] == w_elem[1]:
            w_translate.pop(w_index)

in_duplicates = {}
for init_index,init_elem in enumerate(initial):
    for in_index,in_elem in enumerate(initial):
        if init_elem[0] == in_elem[0] and init_elem[1] != in_elem[1]:
            in_duplicates[init_elem[0]] = [init_elem[1],in_elem[1]]

w_duplicates = {}
for w_index,w_elem in enumerate(w_translate):
    for wt_index,wt_elem in enumerate(w_translate):
        if w_elem[0] == wt_elem[0] and w_elem[1] != wt_elem[1]:
            w_duplicates[w_elem[0]] = [w_elem[1],wt_elem[1]]


phone_results = open("numbers.csv","w")
phone_results.write("webpage,time/date,phone number,obfuscated,number in multiple posts\n")
    
for results in initial:
    try:
        in_match = in_duplicates[results[0]]
        phone_results.write(results[1]+","+results[2]+","+results[0]+",no,"+str(in_match)+"\n")
    except KeyError:
        phone_results.write(results[1]+","+results[2]+","+","+results[0]+",no\n")

for results in w_translate:
    try:
        w_match = w_duplicates[results[0]]
        phone_results.write(results[1]+","+results[2]+","+","+results[0]+",yes,"+str(w_match)+"\n")
    except KeyError:
        phone_results.write(results[1]+","+results[2]+","+","+results[0]+",yes\n")

    
phone_results.close()    

keyword_results = open("keywords.csv","w")

text_results = open("text.csv","w")

    

