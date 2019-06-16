def swap(array,i ,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def chooseSort_simple(array):
    for i in range(len(array)-1):
        temp = i
        temp_value = array[i]
        for j in range(i+1,len(array)):
            if array[j]<temp_value:
                temp_value=array[j]
                temp=j
        swap(array,i,temp)
array=[3,38,5,44,15,36,26,27,2,44,4,19,46,50,47,16]
chooseSort_simple(array)
print(array)

