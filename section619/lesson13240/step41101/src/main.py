from array import array


class HeapMax:

    def __init__(self):
        self.arr = array('I')
        self.last_idx = -1

    def fix_heap_after_add(self, last_idx):
        # function assumes that we just add a new element to the end of array and it has las_idx index
        parent_idx = (last_idx - 1) // 2
        elem_idx = last_idx

        while self.arr[parent_idx] < self.arr[elem_idx]:
            self.arr[parent_idx], self.arr[elem_idx] = self.arr[elem_idx], self.arr[parent_idx]

            if parent_idx == 0:
                break

            elem_idx = parent_idx
            parent_idx = (parent_idx - 1) // 2

    def fix_heap_after_get_max(self):

        # function assumes that there are at least 2 elements at least

        elem_idx = 0

        f_child_idx = 1
        s_child_idx = 2

        if s_child_idx > self.last_idx:
            s_child_idx = f_child_idx

        max_child = None
        max_child_idx = None

        if self.arr[f_child_idx] > self.arr[s_child_idx]:
                max_child = self.arr[f_child_idx]
                max_child_idx = f_child_idx
        else:
                max_child = self.arr[s_child_idx]
                max_child_idx = s_child_idx

        while max_child > self.arr[elem_idx]:

            self.arr[elem_idx], self.arr[max_child_idx] = self.arr[max_child_idx], self.arr[elem_idx]

            elem_idx = max_child_idx

            f_child_idx = elem_idx * 2 + 1
            s_child_idx = elem_idx * 2 + 2

            if f_child_idx > self.last_idx:
                break

            if s_child_idx > self.last_idx:
                s_child_idx = f_child_idx

            if self.arr[f_child_idx] > self.arr[s_child_idx]:
                max_child = self.arr[f_child_idx]
                max_child_idx = f_child_idx
            else:
                max_child = self.arr[s_child_idx]
                max_child_idx = s_child_idx

    def add(self, elem):

        if len(self.arr) == 0:
            self.arr.append(elem)
            self.last_idx = 0
            return

        self.arr.append(elem)
        self.last_idx += 1
        self.fix_heap_after_add(self.last_idx)

    def extract_max(self):
        max = self.arr[0]

        self.arr[0] = self.arr[self.last_idx]
        self.arr.pop(self.last_idx)
        self.last_idx -= 1

        if self.last_idx > 0:
            self.fix_heap_after_get_max()

        return max

heap_max = HeapMax()

n = int(input())
# n = 8
lines = ['Insert 200', 'Insert 10', 'ExtractMax','Insert 5', 'Insert 500', 'Insert 600', 'ExtractMax',
         'ExtractMax']
for i in range(n):
    line = input().split(' ')
    # line = lines[i].split(' ')
    command = line[0]

    if command == 'ExtractMax':
        print(heap_max.extract_max())
    elif command == 'Insert':
        new_element = int(line[1])
        heap_max.add(new_element)

