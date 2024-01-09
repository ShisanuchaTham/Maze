class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size = self._size - 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size = self._size + 1

class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link

if __name__ == '__main__':
    x = Stack()
    x.push(1)
    x.push(2)
    x.push(3)
    x.push(1)
    # if x.peek == 1:
    #     print("T1")
    # if x._top == 1:
    #     print("T2")
    # if x._top.item == 1:
    #     print("T3")
    a = x._top.next.item
    print(a)
