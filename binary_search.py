my_list=[10,12,13,15,20,24,27,33,42,51,57,68,70,77,79,81]

def binary_search(mylist,target,start,stop):
    # when start will be bigger than stop return away
    if stop<start:
        return False
    else:
        mid=(start+stop)//2
        if my_list[mid]==target:
            return mid
        else:
            #  target @@@@@@@@ mid
            if my_list[mid]> target:
                return binary_search(my_list,target,start,mid-1)
            # mid @@@@@@ target
            else:
                return binary_search(my_list,target,mid+1,stop)

target=21
x=(binary_search(my_list,target,0,len(my_list)-1))

if x==False:
    print("item ", target,"isn't founded")
else:
    print("item " , target, "was founded in index ", x)