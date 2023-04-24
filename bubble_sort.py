old_list=[10,75,4,3,43,25,-4,27]
def bubble_sort(list):
    last_item=len(list)-1
    for z in range(0,last_item):
        #  -z because the last part has already sorrted
        for x in range(0,last_item-z):
            if list[x]>list[x+1]:
                list[x],list[x+1]=list[x+1],list[x]
    return list
print(bubble_sort(old_list))