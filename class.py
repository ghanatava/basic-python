class Rectangle:
    type='Quadilateral'
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def update_length(self,new_length):
        self.length=new_length
    def update_breadth(self,new_breadth):
        self.breadth=new_breadth

rect=Rectangle(20,10)
area=rect.area()
perimeter=rect.perimeter()
print(perimeter)
print(area)
rect.update_length(100)
rect.update_breadth(20)
print(rect.length,rect.breadth)
print(rect.type)
