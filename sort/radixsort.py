def radixsort(array):
    max = array[0]
    for i in array:
        if i > max:
            max = i
    c = 0
    while max != 0:
        max = max // 10
        c += 1
    for i in range(1, c+1):
        list0 = []
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list9 = []
        list8 = []
        list7 = []
        list6 = []
        buckets = [list0, list1, list2, list3, list4, list5, list6, list7, list8, list9]
        for j in array:
            buckets[(j % (pow(10, i)))//pow(10, i-1)].append(j)
            array = []
        for b in buckets:
            for t in b:
                array.append(t)
    return array


array = [3, 38, 5, 44, 15, 36, 26, 27, 2, 44, 4, 19, 46, 50, 47, 16]
array = radixsort(array)
print(array)
