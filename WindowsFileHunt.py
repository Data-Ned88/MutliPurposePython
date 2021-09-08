#library imports required: os, re for text searches, datetime
import os
import re
import datetime as dt

#user pastes in a folder path from Window File Explorer - Python prepares searchable text string

wd = input('Copy root folder path to search from Windows File Explorer:')
es = []
wdir = [x + '\\' if x == '\\' else x for x in wd]
outdir = ''.join(wdir)


#From root, get all files from all subfolders and the root folder, and add...
#...their names and created dates to 'infolist'

infolist = []
for root, dirs, files in os.walk(outdir):
    for f in files:
        ffp = os.path.join(root, f)
        time_c = os.path.getctime(ffp)
        infolist.append([ffp,dt.datetime.fromtimestamp(time_c)])

#result list variable to be a redacted version of infolist for only the files that match your search criteria        
resultlist = []


#two lists for all permissible file extensions and filename contents

endings = ['\.csv$','\.xlsx$','\.xlsm$'] # path ends with (ie file extension is)
name_searches  = ['analysis','report','analysys'] # path contains
windows = [dt.datetime(2020,1,1),dt.datetime(2021,2,1)] #created date min and max
#compare each file in infolists to your criteria

for fl in infolist:
    fname = fl[0]
    
    include_1 = any([x for x in endings if re.search(x,fname.lower())])
    include_2 = any([x for x in name_searches if re.search(x,fname.lower())])
    include_3 = fl[1] > windows[0] and fl[1] < windows[1]
    
    include_master = all([include_1,include_2,include_3]) # customise this list to include or exclude any you need or dont need
    if include_master:
        resultlist.append(fl)
        
#print your results to the Command Prompt or jupyter notebook cell output    
for res in resultlist:
    print(res[0] + ': Created: ' + dt.datetime.strftime(res[1],'%Y-%m-%d'))