import os
import sys
import time
# the during of file's life before deleting
DAYS= 0.0001

# folders where we will find old files
FOLDERS =[
    "/home/kali/Documents/rubbish/Telegram Desktop"
    
]

# variables for statistics
TOTAL_DELETED_SIZE=0
TOTAL_DELETED_FILES=0
TOTAL_DELETED_FOLDERS=0

nowTime=time.time()

# convert days in seconds
days_in_secs=DAYS*24*60*60

# замеряем время? которое живёт система без X DAYS
ageTime=nowTime-days_in_secs

def deleting_old_files(folder):
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE

    # path ---> path to directory
    # folder_name ---> only name of dir
    # files ---> ls of dir
    
    for path,folder_name,files in os.walk(folder):

        # check for every file
        for file in files:

            # create the whole path to file include filename
            fileName=os.path.join(path,file)

            # get modification time
            fileTime=os.path.getmtime(fileName)

            # check if fileTime younger than замеряем время? которое живёт система без X DAYS
            if fileTime<ageTime:

                # get size of file
                fileSize=os.path.getsize(fileName)

                # statistics stuff
                TOTAL_DELETED_SIZE+=fileSize
                TOTAL_DELETED_FILES+=1
                print("Deleting file: ",str(fileName))

                # remove
                os.remove(fileName)
            
def deleting_empty_dirs(folder):
    global TOTAL_DELETED_FOLDERS
    empy_folders_counter=0
    # path ---> path to directory
    # folder_name ---> only name of dir
    # files ---> ls of dir
    for path,folder_name,files in os.walk(folder):
        # check if there are files or dirs in folder
        if (not folder_name) and (not files):

            # statistics
            TOTAL_DELETED_FOLDERS+=1
            empy_folders_counter+=1
            print("deleting empty dir: ", path)

            # remove
            os.rmdir(path)

    if empy_folders_counter>0:
        deleting_empty_dirs(folder)



# --------------------------------------Main-------------------------

startime=time.asctime()
print(startime)


for folder in FOLDERS:
    # funct to delete files
    deleting_old_files(folder)

    # funct to delete empty dirs
    deleting_empty_dirs(folder)
print(os.walk(folder))
finishtime=time.asctime()

print("------------------------------------------")
print("------------------------------------------")

print("start time: ", str(startime))
print("finish time: ", str(finishtime))

print("TOTAL DELETED FILES ",str(TOTAL_DELETED_FILES))
print("TOTAL DELETED FOLDERS ",str(TOTAL_DELETED_FOLDERS))
print("TOTAL CLEANING SIZE ",str(TOTAL_DELETED_SIZE/1024)," Kb")

