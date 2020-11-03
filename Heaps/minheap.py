# Implementing Min Heap
import random

class MinHeap:
    def __init__(self):
        self.values = [0]
        self.size = 0

    def insert(self, val):
        self.values.append(val)
        self.size += 1
        self.move_up(self.size)

    def get_min_child(self, index):

        # Check if there is only one child
        if (2 * index) + 1 > self.size - 1:
            return 2 * index

        else:

            if self.values[2 * index] > self.values[2 * index + 1]:
                return (2 * index) + 1
            else:
                return 2 * index

    def move_up(self, index):

        while index // 2 > 0:

            if self.values[index] < self.values[index // 2]:
                self.values[index], self.values[index // 2] = self.values[index // 2], self.values[index]
                # Swapping the child node with parent, if val of child is smaller than parent

            index = index // 2

    def move_down(self, index):

        # Check if the given index has a child
        while (2 * index) <= self.size:
            # retrieve index of the child with min value
            min = self.get_min_child(index)

            if self.values[index] > self.values[min]:
                self.values[index], self.values[min] = self.values[min], self.values[index]

            index = min

    def delete_minimum(self):

        # Check size of heap
        if self.size == 1:
            return 'Heap is Empty'

        root = self.values[1]

        self.values[1] = self.values[self.size]
        self.values.pop()

        self.size = self.size - 1
        self.move_down(1)
        return root


heap = MinHeap()
for i in range(10):
    num = random.randint(1, 100)
    heap.insert(num)
    print("Inserted:", num)

print(heap.values)
len=len(heap.values)

sorted=[]
while ( len != 1):
    sorted.append(heap.delete_minimum())
    len=len-1

print("Sorted List of values from heap:",sorted)

