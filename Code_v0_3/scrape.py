import glob
import os
from subprocess import *

to_fix_places = glob.glob("*")

places = []
for i in to_fix_places:
    if not ".py" in i:
        if not ".txt" in i:
            places.append(i)


for place in places:
    os.chdir(place)
    os.getcwd()
    call(['python','recursive_scrape.py'])
    os.getcwd()
    os.chdir("../")

