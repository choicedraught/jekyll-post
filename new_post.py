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
from datetime import datetime, timedelta, timezone

ArgumentParser = argparse.ArgumentParser(description='Give me the title of your Blog post mofo.')
ArgumentParser.add_argument('title', nargs='+', help='Required: The Title of your Post') # This is how you do a positional argument apparently
ArgumentParser.add_argument('categories', nargs='+', help='Required: The Categories for your Post')
ArgumentParser.add_argument('--datetime', required=False, dest='datetime',help='Optional: specity a post date that is not today.  Format YYYY-MM-DD HH:MM:SS +/-0000')

date         = datetime.now(timezone.utc).astimezone()
args         = ArgumentParser.parse_args()
title        = args.title
categories   = " ".join(args.categories)

if not args.datetime:
  shortdate  = date.strftime("%Y-%m-%d")
  isodate    = date.strftime('%Y-%m-%d %H:%M:%S %z')
else:
  isodate    = args.datetime
  shortdate  = isodate.split(" ",2)[0] # We just want the date part for out filename

filetitle    = "-".join(title) # Split the title into words and then hyphen them
posttitle    = " ".join(title)
filename     = shortdate+"-"+filetitle+".markdown" # Now create the filename 
output       = "---\nlayout: post\ntitle:  "+posttitle+"\ndate:   "+isodate+"\ncategories: "+categories+"\n---\n" # Create the Post conetent as a string

# Check if the file exists first
if os.path.isfile(filename):
  print("\n")  
  print("Error: File '"+filename+"'"+" exists, exiting.")
  print("\n") 
  #print(output) 
  quit()
else:
  #print(output)
  f = open(filename, 'w')
  f.write(output)

print("\n")  
print("Created new blog post in: '"+filename+"'.\n")
quit()
