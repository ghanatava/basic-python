class Quadilateral:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print('Quadilateral is created')
    def get_type(self):
        return "Quadilateral"
class Rectangle(Quadilateral):
    def __init__(self,length,breadth):
        Quadilateral.__init__(self,length,breadth)
        print('rectangle is created')
    def area(self):
        return self.length*self.breadth
    #function overriding
    def get_type(self):
        return 'Rectangle'
class Square(Rectangle):  #or Square(Rectangle,Quadilateral)
    def __init__(self,length,breadth):       
        Quadilateral.__init__(self,length,breadth)
        self.length=self.breadth
        print('square is created')
    def get_type(self):
        print()

rectangle=Rectangle(100,50)
area=rectangle.area()
print(area)
print(rectangle.get_type())
square=Square(100,100)
sqarea=square.area()
print(sqarea)
