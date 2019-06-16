def swap(array,i ,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubbleSort(array):
    for i in range(len(array)-1):
        flag=0
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                flag = 1
                swap(array,j,j+1)
        if flag==0:
            break
    print(array)


def partition(array,start,end):
    mark_value=array[start]
    storeindex=start
    swap(array,start,end)
    for i in range(start,end):
        if array[i]<mark_value:
            swap(array,storeindex,i)
            storeindex=storeindex+1
    swap(array,storeindex,end)
    return storeindex

def quikSort(array,start,end):
    if start<end:
        mark=partition(array,start,end)
        quikSort(array,start,mark-1)
        quikSort(array,mark+1,end)


array=[3,38,5,44,15,36,26,27,2,44,4,19,46,50,47,16]
#bubbleSort(array)
quikSort(array,0,len(array)-1)
print(array)