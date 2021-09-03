class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,obj):
        self.stack.append(obj)
    def pop(self):
        return self.stack.pop()  #use return or else get a nonetype value
    def display(self):
        print(self.stack)
    def rev_str(self,string):
        for i in string:
            self.push(i)
        string=''
        for i in range(len(self.stack)): #len returns int object which is not iterable
            string+=self.pop()
        print(string)   
stack=Stack()
stack.rev_str('02496')