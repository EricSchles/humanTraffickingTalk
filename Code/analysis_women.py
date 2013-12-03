import re
import os
from subprocess import *
import glob

def picture_check(contents):
    pattern = re.compile(".jpg")
    m = pattern.search(contents)
    if m == None:
        return False
    else:
        return True

def number_of_pictures(contents):
    m = re.findall(".jpg",contents)
    return len(m)

def number_of_pictures(contents):
    m = re.findall(".jpg",contents)
    return len(m)

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
