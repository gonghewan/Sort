class Heap():
    def __init__(self):
        # make sure the father node's index = son node's index / 2
        self.data_list = [None]

    def size(self):
        return len(self.data_list)

    def left(self,father):
        return father * 2

    def right(self,father):
        return father * 2 + 1

    def father(self,son):
        # // represents integer division
        return son // 2

    # adjust heap to a maxHeap
    def heapify(self,root,limit_size):
        left_node=self.left(root)
        right_node=self.right(root)
        largest=root
        if left_node<limit_size:
            if self.data_list[left_node]>self.data_list[largest]:
                largest=left_node
        if right_node<limit_size:
            if self.data_list[right_node]>self.data_list[largest]:
                largest=right_node
        if largest!=root:
            self.data_list[largest],self.data_list[root]=self.data_list[root],self.data_list[largest]
            self.heapify(largest,limit_size)

    # insert one element into maxHeap
    def insert(self,data):
        if self.size() == 1:
            self.data_list.append(data)
            return
        self.data_list.append(data)
        new_index=self.size()-1
        fnode=self.father(new_index)
        while new_index!=1 and self.data_list[new_index]>self.data_list[fnode]:
            self.data_list[fnode],self.data_list[new_index]=self.data_list[new_index],self.data_list[fnode]
            new_index=fnode
            fnode=self.father(fnode)


def heapSort(array):
    heap=Heap()
    for i in range(0,len(array)):
        heap.insert(array[i])
    for i in range(len(array),0,-1):
        print(i)
        heap.data_list[1],heap.data_list[i]=heap.data_list[i],heap.data_list[1]
        heap.heapify(1,i-1)
    print(heap.data_list)


array=[3, 38, 5, 44, 15, 36, 26, 27, 2, 44, 4, 19, 46, 50, 47, 16]
heapSort(array)
