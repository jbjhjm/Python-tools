import glob
import os
import json
from typing import List, AnyStr, Dict

def load_source_files(files='source/*.TXT') -> List[AnyStr]:
	files = glob.glob('source/*.TXT')
	return files


# TODO: current anaconda ships with python 3.7 which does not support Literal.
# class FileInfo(TypedDict):
#     fullName: str
#     name: str
#     ext: str

def getFileinfo(filePath) -> Dict:
	fullName = os.path.basename(filePath)
	parts = os.path.splitext(fullName) # splitext returns [name, extension]
	info = {'fullName':fullName,'name':parts[0],'ext':parts[1]}
	return info

def writeToJson(filePath:AnyStr,data:any):
	file = open(filePath, "w")
	json.dump(data, file, indent=4, sort_keys=True)
	file.close()

def readJson(filePath:AnyStr):
	file = open(filePath, "r")
	data = json.load(file)
	file.close()
	return data