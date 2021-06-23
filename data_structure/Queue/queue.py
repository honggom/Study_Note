class Queue():

    # 초기화
    def __init__(self):
        self.queue = []

    # 큐 개수 가져오기
    def getSize(self):
        return len(self.queue)

    # 데이터 삽입
    def enqueue(self, data):
        self.queue.append(data)

    # 데이터 삭제 및 리턴
    def dequeue(self):
        if self.isEmpty() == 0:
            return 'empty..'
        return self.queue.pop(0)

    # 큐가 비어있는지 확인
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    # 데이터 확인
    def printQ(self):
        print(self.queue)


a = Queue()
a.enqueue(1)
print(a.isEmpty())
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# print(q.dequeue())
# q.printQ()
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.getSize())
