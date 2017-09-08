
from queue import PriorityQueue

class BinaryNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

        # self.freq = None
        self.symbol = None
        self.number = None

    def delete_left(self):
        self.left = None

    def delete_right(self):
        self.right = None

    def delete_me_from_parent(self):
        if self.parent.left is self:
            self.parent.delete_left()
        elif self.parent.right is self:
            self.parent.delete_right()

    def has_children(self):
        return self.has_left() or self.has_right()

    def get_child(self):
        if self.has_left():
            return self.left
        elif self.has_right():
            return self.right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def __le__(self, *args, **kwargs):
        return True

    def __gt__(self, *args, **kwargs):
        return False

    def __ge__(self, *args, **kwargs):
        return True

    def __eq__(self, *args, **kwargs):
        return True

    def __lt__(self, *args, **kwargs):
        return False

    def __ne__(self, *args, **kwargs):
        return False


class MyBinaryTree:
    def __init__(self, q : PriorityQueue):
        """

        :param q: expects  queue with tuples (frequency, symbol)
        """
        # symbol may be a node or a actual symbol
        while q.qsize() > 1:
            f = q.get()
            s = q.get()

            if not isinstance(f[1], BinaryNode):
                f_node = BinaryNode()
                f_node.symbol = f[1]
                f_node.number = '0'
            else:
                f_node = f[1]
                f_node.number = '0'


            if not isinstance(s[1], BinaryNode):
                s_node = BinaryNode()
                s_node.symbol = s[1]
                s_node.number = '1'
            else:
                s_node = s[1]
                s_node.number = '1'



            p_node = BinaryNode()

            f_node.parent = p_node
            s_node.parent = p_node

            p_node.left = f_node
            p_node.right = s_node


            t = tuple((f[0] + s[0], p_node))
            q.put(t)

        self.tree = q.get()[1]
        assert q.empty()

    def get_symbols_with_codes(self):
        symbols_with_codes = dict()

        node = self.tree

        code = str()
        while self.tree.has_children():

            while node is not None and node.has_children():
                node = node.get_child()
                code += node.number

            if isinstance(node.symbol, str):
                symbols_with_codes[node.symbol] = code
                node.delete_me_from_parent()
                code = code[:-1]
                node = node.parent
            else:
                node.delete_me_from_parent()
                code = code[:-1]
                node = node.parent

        return symbols_with_codes


def get_symbols_with_frequencies(line):
    unique_symbols = set(line)
    symbols_with_frequensies = PriorityQueue(maxsize=1000)

    for s in unique_symbols:
        counter = 0
        for l in line:
            if l == s:
                counter += 1
        symbols_with_frequensies.put((counter, s))
    return symbols_with_frequensies


line = str(input())
# line = 'cccc'
symbols_with_frequensies = get_symbols_with_frequencies(line)
if (symbols_with_frequensies.qsize() == 1):
    symbols_with_codes = dict()
    symbols_with_codes[symbols_with_frequensies.get()[1]] = '0'
else:
    tree = MyBinaryTree(symbols_with_frequensies)
    symbols_with_codes = tree.get_symbols_with_codes()

# кодирование
coded_line = str()
for l in line:
    coded_l = symbols_with_codes[l]
    coded_line += str(coded_l)


unique_symbols = set(line)
print(str(len(unique_symbols)) + ' ' + str(len(coded_line)))

for s in dict(symbols_with_codes).keys():
    print(str(s) + ':' + ' ' + str(symbols_with_codes[s]))

print(coded_line)