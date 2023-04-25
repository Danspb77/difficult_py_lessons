# !/bin/python3

# the first string to linux get the script

# lib for get file sixe and check if file exist
import os

# for frguments of comand string
import sys

# ibrary for COPY
import shutil 

# check need arguments
while True:
    if len(sys.argv)==4:
        break
    if len(sys.argv)<4:
        print("Missing arguments")
        break
    if len(sys.argv)>4:
        print("Too many arguments")
        break
# take argvs from comand line
file_name=sys.argv[1]
limitsize=int(sys.argv[2])
logsnumber=int(sys.argv[3])

# check if file exist
if os.path.isfile(file_name)==True:
    # get the size in bytes
    logfile_size=os.stat(file_name).st_size
    # convert size into Kbytes
    logfile_size=logfile_size//1024

    if logfile_size>=limitsize:
        print("logsnumber >0aaaaaaaaaaaaaaaaaaaaaaaaa")
        if logsnumber >0:
            print("logsnumber >0")
            for  current_file_num in range(logsnumber,1,-1):
                src=file_name+"_"+str(current_file_num-1)
                dst=file_name+"_"+str(current_file_num)
                print(src)
                if os.path.isfile(src)==True:
                    shutil.copyfile(src,dst)
                    print("copied from "+src+"  to " + dst)

            shutil.copyfile(file_name,file_name+"_1")
            print("copy from  " + file_name+"  to "+file_name+"_1")
        
        myfile=open(file_name,'w')
        myfile.close()
