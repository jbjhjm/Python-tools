import glob
from lib.helpers_file import getFileinfo, writeToJson

files = glob.glob('source/*.TXT')

nameList = []

for path in files:
	fileInfo = getFileinfo(path)
	nameList.append(fileInfo['name'])

writeToJson('filelist.json', nameList)