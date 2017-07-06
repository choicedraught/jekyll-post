#!/usr/bin/env python3

# Creates a new file in the current folder and inputs the "Front Matter" info for Jekyll post
# File format:
# ---
# layout: post
# title:  "Welcome to Jekyll!"
# date:   2017-07-05 12:53:46 +0800
# categories: jekyll update
# ---

import argparse
import os.path
from datetime import datetime
import time
def date2iso(thedate): # Some dudes neat little hack to get the TZ Offset - apparently this is easier in Python3
     strdate = thedate.strftime("%Y-%m-%d %H:%M:%S")
     minute = (time.localtime().tm_gmtoff / 60) % 60
     hour = ((time.localtime().tm_gmtoff / 60) - minute) / 60
     utcoffset = "%.2d%.2d" %(hour, minute)
     if utcoffset[0] != '-':
         utcoffset = ' +' + utcoffset
     return strdate + utcoffset

ArgumentParser = argparse.ArgumentParser(description='Give me the title of your Blog post mofo.')
ArgumentParser.add_argument('title', nargs='+', help='Required: The Title of your Blog Post') # This is how you do a positional argument apparently
ArgumentParser.add_argument('--datetime', required=False, dest='datetime',help='Optional: specity a post date that is not today.  Format YYYY-MM-DD HH:MM:SS +/-0000')

args      = ArgumentParser.parse_args()
title     = args.title

if not args.datetime:
  mydate  = datetime.now().strftime("%Y-%m-%d")
  isodate = date2iso(datetime.fromtimestamp(time.time()))
else:
  isodate = args.datetime
  mydate  = isodate.split(" ",2)[0] # We just want the date part for out filename

filetitle = "-".join(title) # Split the title into words and then hyphen them
filename  = mydate+"-"+filetitle+".markdown" # Now create the filename 
output    = "---\nlayout: post\ntitle:  "+" ".join(title)+"\ndate:   "+isodate+"\ncategories: jekyll update\n---\n" # Create the Post conetent as a string

# Debugging
#print(title)
#print(mydate)
#print(isodate)
#print(filetitle)

# Check if the file exists first
if os.path.isfile(filename):
  print("\n")  
  print("Error: File '"+filename+"'"+" exists, exiting.")
  print("\n")  
  quit()
else:
  f = open(filename, 'w')
  f.write(output)

print("\n")  
print("Created new blog post in: '"+filename+"'. You're welcome!\n")
quit()
