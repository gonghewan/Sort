def mergesort(array):
    lenth = len(array)
    if lenth <= 1:
        return array
    temp1 = mergesort(array[:lenth//2])
    temp2 = mergesort(array[lenth//2:lenth])
    if len(temp1) > len(temp2):
        min_num = len(temp2)
    else:
        min_num = len(temp1)
    i, j = 0, 0
    temp3 = []
    while i < min_num and j < min_num:
        if temp1[i] < temp2[j]:
            temp3.append(temp1[i])
            i = i + 1
        else:
            temp3.append(temp2[j])
            j = j + 1
    if i < len(temp1):
        while i < len(temp1):
            temp3.append(temp1[i])
            i = i + 1
    elif j < len(temp2):
        while j < len(temp2):
            temp3.append(temp2[j])
            j = j + 1
    return temp3


array = [3, 38, 5, 44, 15, 36, 26, 27, 2, 44, 4, 19, 46, 50, 47, 16]
array = mergesort(array)
print(array)
