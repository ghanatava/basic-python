class Queue:
    def __init__(self):
        self.queue=[]
    def ENQUEUE(self,obj):
        self.queue.append(obj)
    def DEQUEUE(self):
        self.queue.pop(0)
    def PEEK(self):
        print(self.queue[0])
    def GET_QUEUE(self):
        print(self.queue)
    def IS_EMPTY(self):
        if len(self.queue) == 0:
            print(True)
        else:
            print(False)
queue=Queue()
for i in range(1,11):
    queue.ENQUEUE(i)
queue.GET_QUEUE()
queue.DEQUEUE()
queue.GET_QUEUE()
