class MinBinaryHeap:
    def __init__(self, values=None):
        self.values = values if values else []
        self.size = len(self.values)
        if self.values:
            self.heapify(self.values)

    def heapify(self, values):
        n = len(values)
        for i in range(n // 2, -1, -1):
            self._sift_down(cur_index=i)

    def is_empty(self) -> bool:
        return self.size == 0

    def _sift_up(self):
        cur_index = self.size - 1
        parent_index = (cur_index - 1) // 2
        while cur_index != 0 and self.values[cur_index] < self.values[parent_index]:
            self.values[cur_index], self.values[parent_index] = self.values[parent_index], self.values[cur_index]
            cur_index = parent_index
            parent_index = (cur_index - 1) // 2

    def _sift_down(self, cur_index=0):
        while 2 * cur_index + 1 < self.size:
            left_index, right_index = 2 * cur_index + 1, 2 * cur_index + 2
            swap_index = left_index
            if right_index < self.size and self.values[right_index] < self.values[left_index]:
                swap_index = right_index

            if self.values[cur_index] <= self.values[swap_index]:
                break

            self.values[cur_index], self.values[swap_index] = self.values[swap_index], self.values[cur_index]
            cur_index = swap_index

    def push(self, val):
        if self.size < len(self.values):
            self.values[self.size] = val
        else:
            self.values.append(val)
        self.size += 1
        self._sift_up()

    def pop(self):
        if self.size == 0:
            raise Exception('Cannot pop element from an empty heap.')

        root_value = self.values[0]
        # swap root element with the last
        self.values[self.size - 1], self.values[0] = self.values[0], self.values[self.size - 1]
        self.size -= 1
        self._sift_down()
        return root_value


heap = MinBinaryHeap([5, 8, 3, 12, 1, -4])
while not heap.is_empty():
    print(heap.pop(), end=" ")
