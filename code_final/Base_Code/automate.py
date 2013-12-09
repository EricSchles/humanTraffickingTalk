# import generate_craigslist
# import link_scrap
from subprocess import *

#generate the spider
call(['python','generate_craigslist.py'])
#generate_craigslist.main()

#run the spider
call(['python', 'link_scrap.py'])
#link_scrap.main()
