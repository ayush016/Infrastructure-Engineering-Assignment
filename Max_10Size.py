import os
import operator
import platform

def search(folder): #Function will search and store all files path and size in a list

    count = 0
    for (paths, dirs, files) in os.walk(folder):
        for current in dirs :
            print "Searching....",current,"Folder"
        for file in files:
           
            try:
                if "Windows" in platform.platform() :
                	z = paths + '\\' + file
                else :
                	z = paths + '/' + file

                x = z.replace("\\", "\\\\")
                file_list.append(x)
                
                size = os.stat(x).st_size / float(1048576) #Coversion of bytes to Mb
                size_list.append(size)

                count=count+1

            except:
                size_list.append(-1)
                count = count + 1
    return count


if "2.7" in platform.python_version() :
    if "Windows" in platform.platform() : #Checking for windows operating system

        print "Please wait"
        file_list = []
        size_list = []
        L = []
        count=0
        for i in range(ord('a'), ord('z') + 1): #Checking for drives name in windows
            drive = chr(i)
            if (os.path.exists(drive + ":\\")):
                L.append(drive)
                
        for disk in L :
            count = count + search(disk.upper()+':\\') #Search all drives one by one
            
            #Remove the below comment to hardcore the directory or drive location
            '''
            file_list = []
            count=0
            count = search("specify location here")
            '''

    else : #For linux based Operating systems like Ubuntu,RedHat,CentOs,Kali,etc
    
    	file_list = []
        size_list = []
	count=search("/") #User can change the path (by defalt it is root direc)
	
	#The below program search 10 max files in stored list
    print ""
    for i in range (1 , 11) :
        index, value = max(enumerate(size_list), key=operator.itemgetter(1)) #Fast Searching in a list
        if "Windows" in platform.platform() :
        	final=file_list[index].replace("\\\\","\\")
        else :
        	final=file_list[index].replace("\\\\","/")
        
        
        print i," |" , final, value, "MB"
        print"-------------------------------------------------"
        size_list[index]=-1
    print "Total files searched = ", count
    print "Done"

