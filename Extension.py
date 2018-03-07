import os
import operator
import os.path
import platform
from collections import Counter


def shifter(specifier,dektop,documents) :
	for (paths, dirs, files) in os.walk(desktop):
		if (paths == desktop):
		    for file1 in files:
		        if file1 not in NotRemove_files :
		            extsn = file1.split(".")[-1] #Getting extension of file
		            file_list.append(extsn)
		            temp_list.append(extsn)
		            if not os.path.exists(documents + specifier + extsn.upper()):
		                os.makedirs(documents + specifier+ extsn.upper()) #Creating Folder
		            try:
		                os.rename(paths + specifier + file1, documents + specifier + extsn.upper() + specifier + file1)#Moving folder
		                record.append(extsn)
		            except:
		                try:
		                    os.rmdir(documents + specifier + extsn.upper())
		                except:
		                    pass

	unique_record = list(set(record))
	if (unique_record == []):
		print "No files Moved (Maybe files with same name and location already present)"
	else:
		print "Total file types moved -:"
	for count in unique_record:
		print count, Counter(record)[count] # To count how many file types are moved as per the extension



file_list = []
temp_list = []
record = []
NotRemove_files = []

if "Windows" in platform.platform():
    i = 0
    
    #To get the location of Documents,Desktop folder for user login
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents') 
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    #Location of Public Desktop
    public_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']))
    public_desktop = public_desktop.replace(os.getenv('username'), "Public")
    

    for (paths, dirs, files) in os.walk(public_desktop): 
        for file in files:
            if (file.split(".")[-1] == "lnk"):
                NotRemove_files.append(file) 
    #List will comprise of lnk files which should not be removed like My computer,Counterstrike,etc
    
    shifter("\\",desktop,documents)

else:
    #To get the location of Documents,Desktop folder for user login in Linux based OS
    documents = os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    shifter("/",desktop,documents)
