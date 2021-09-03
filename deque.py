class Deque:
    def __init__(self):
        self.deque=[]
    def INSERT_FRONT(self,obj):
        self.deque.insert(0,obj)
    def INSERT_REAR(self,obj):
        self.deque.append(obj)
    def DELETE_FRONT(self):
        self.deque.pop(0)
    def DELETE_REAR(self):
        self.deque.pop()
    def GET_DEQUE(self):
        print(self.deque)
deque=Deque()
deque.INSERT_FRONT(1)
deque.INSERT_FRONT(2)
deque.GET_DEQUE()
deque.INSERT_REAR(3)
deque.INSERT_REAR(4)
deque.GET_DEQUE()
deque.DELETE_FRONT()
deque.DELETE_REAR()
deque.GET_DEQUE()
