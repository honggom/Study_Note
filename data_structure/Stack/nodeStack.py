class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)

        # 현재 head를 지금 들어오는 node의 next로 지정 다음 push일 때 옮기기 위함
        node.next = self.head
        self.head = node

    def pop(self):
        if self.isEmpty():
            return 'empty..'

        # 현재 head의 data를 return 그 후 head를 현재 head의 next로 할당
        data = self.head.data
        self.head = self.head.next
        return data

    def isEmpty(self):
        if self.head:
            return False
        return True

    def peek(self):
        if self.isEmpty():
            return False
        return self.head.data


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
