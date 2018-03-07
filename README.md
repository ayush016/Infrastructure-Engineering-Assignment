# Innovaccer Infrastructure Engineering Assignment 
## Program in PYTHON 2.7 (Compatible for every Operating System)

### Problem Description
1. Find the information of top 10 biggest files from a Directory/whole system.
2. Move the files from a source directory to folders according to their extensions in to destination directory.

### Problem - 1
``` Max_10Size.py ``` will recursively search the drives/directory specified (by default all drives in the windows system and root '/' directory for Linux)

#### Functioning 
###### Search Function:
This take path of the drive/directory/folder as a parameter and stores the path and file sizes in the list (file_list and size_list) using os.walk 
###### Searchig drives location in windows:
This will check if path exists for drive (A to Z) hence finds all the drives name in the windows for user to completely search the system 
###### enumerate() function for fast searching:
It allows user to loop over something and have an automatic counter (i.e adds a counter to an iterable) for searching 10 Max files in the list 
###### os.walk() for recursive tree searching:
Built-in function in the OS module is used to generate the file names in a directory tree by walking the tree in top-down fasion
###### Python Platform module:
It is used to detect the Operating system info (Windows or Linux). In Linux OS information is stored in /sys directory for windows 7 C:\Windows\System32\license.rtf and EULA code for windows 10 

#### Building Max_10Size.py
``` Python 2.x (Python 2.7 preferred)``` 
In Terminal/Command Prompt move to the directory of Max_10Size.py and run the following command.
``` python Max_10Size.py ```

###### Remarks:
1. Currently by defualt for windows all drives and for linux root directory will be searched, User can change the location in the code by removing the commented block as specified inside the Max_10Size.py (It will take approx. 10-15 minutes depending upon the system to search whole computer)
2. Program while running show the folders currently being searched and total files searched at the end.
3. If whole computer is searched /dev/core ( symbolic link to the regular file) in linux and C:\pagefile.sys ( least-used files in RAM are 'paged' out to this file.) in windows may be the largest file because of its enormous size
 
 ### Problem 2
``` Extension.py ``` will sort the files on Desktop on the basis of file extension and move them in separate folders in Documents folder Hence desktop is cleaned but shortcut ("lnk") inside the Public Desktop folder (C:\Users\Public\Public Desktop) is not moved irrespective of the user login as the recuirement was not to remove shortcuts of My Computer, Chrome or even Counter strike like applications. 

#### Functioning 
###### Shifter function:
This function uses the os.walk module to get the names with extensions of files from the desktop and if folder is not created in documents having name as file's extension than it will create that folder.
Along with this in every iteration file will be moved from desktop to document in specific folders.
###### Counter from collection:
```Counter("list name")``` is used for as a container that keeps track of how many times equivalent values are added hence knowing the total files transfered according to its extension type.

#### Building Max_10Size.py
``` Python 2.x (Python 2.7 preferred)``` 
In Terminal/Command Prompt move to the directory of Extension.py and run the following command.
``` Extension.py```

#### Remarks:
Extra function for rmdir is used, if any file have permision to read but cannot be moved i.e the newly made directory is empty than it will remove that directory to avoid the reduntant folder.
Please make a note that "/" is used in linux for path specifier (ex. /Home/) and "\" is used by Windows (C:/User/) but "/" is treated as a character in python scripting so "\\" is used or modified in the code  

#### Contact 15ucc009@lnmiit.ac.in (+918003236561) for any queries  
