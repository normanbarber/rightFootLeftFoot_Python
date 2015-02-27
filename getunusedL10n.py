import mmap
import re
import os

viewKeys = []
L10nKeys = []

input_viewpath = input('Enter path to your view file:')
input_localepath = input('Enter path to your locale file:')

def getKeys(dirpath,keys,matchstr,stringreplace1,stringreplace2):
	path = open(dirpath)
	str = mmap.mmap(path.fileno(), 0, access=mmap.ACCESS_READ)
	items = re.findall(matchstr, str)
	if len(items) > 0:
		for item in items:
			key = item.replace('"',"'").replace(stringreplace1,'').replace(stringreplace2,'')
			keys.append(key)
		return keys

localefiles = {}
stringreplace1 = '\t'
stringreplace2 = ':'
localematch = '(.*:)'
getKeys(input_localepath,L10nKeys,localematch,stringreplace1,stringreplace2)

viewfiles = {}
stringreplace1 = '#{__('
stringreplace2 = ')}'
viewmatch = '(#{.*})'
for (dirpath, dirnames, filenames) in os.walk(input_viewpath):
    for filename in filenames:
        viewfiles[filename] = os.sep.join([dirpath, filename])
        getKeys(viewfiles[filename],viewKeys,viewmatch,stringreplace1,stringreplace2)

intersect = set(viewKeys).intersection(L10nKeys)
print (intersect)

input("Press enter to exit program");