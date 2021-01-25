class MinHeap:
    def __init__(self):


        self.size=0
        self.heap=[0]


    def shift_up(self,pos):
       
        while pos//2 >0:
            if self.heap[pos//2]>self.heap[pos]:
                self.heap[pos], self.heap[pos//2]=self.heap[pos//2], self.heap[pos]
            pos=pos//2       
        
    def insert(self, value):

        self.heap.append(value)
        self.size+=1
        self.shift_up(self.size)

    def min_child(self,pos):

        left_child_index = 2 * pos
        right_child_index = 2 * pos + 1

       
        if right_child_index > self.size:
            return left_child_index
        else:
            if self.heap[left_child_index]<self.heap[right_child_index]:
                return left_child_index
            else:
                return right_child_index


    def shift_down(self,pos):

        while 2*pos <= self.size:

            min_child_index=self.min_child(pos)
            self.heap[min_child_index], self.heap[pos]=self.heap[pos], self.heap[min_child_index]

            pos=min_child_index


    def delete_min(self):

        root=self.heap[1]
        self.heap[1]=self.heap[-1]
        self.heap.pop()
        self.size-=1
        self.shift_down(1)

        
minheap=MinHeap()
minheap.insert(5)
minheap.insert(2)
minheap.insert(10)
minheap.insert(1)
