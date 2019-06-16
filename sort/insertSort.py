def simply_insert(array):
    for i in range(1,len(array)):
        for j in range(0,i):
            if(array[i-j]<array[i]):
                temp=array[i]
                for k in range(i,i-j+1,-1):
                    array[i]=array[i-1]
                array[i-j+1]=temp

def swap(array,i ,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def shellSort(array):
    gap=len(array)/2
    while gap>0:
        temp = 0
        while temp+gap<len(array):
            if array[temp]>array[temp+gap]:
                swap(array,temp,temp-gap)
            temp=temp+1
        gap=gap/2



array=[3,38,5,44,15,36,26,27,2,44,4,19,46,50,47,16]
#simply_insert(array)
shellSort(array)
print(array)


