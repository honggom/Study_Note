class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if not self.head:
            return True
        return False

    def enqueue(self, data):
        node = Node(data)

        if self.isEmpty():
            self.head = node
            self.tail = node
            return

        # 현재 tail의 next가 지금 들어온 node를 가르키고..
        self.tail.next = node

        # tail의 위치를 지금 현재 들어온 node를 가르키게 한다..
        self.tail = self.tail.next

    def dequeue(self):
        if self.isEmpty():
            return 'empty..'

        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.isEmpty():
            return 'empty..'
        return self.head.data


q = Queue()
q.enqueue(3)
q.enqueue(2)
q.enqueue(123)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
