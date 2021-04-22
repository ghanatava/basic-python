#not recommended for compex projects
x=100
def func():
    #changing a global variable in local functions
    global x 
    x=200
    def cube():
        print(x**3)
    cube()
func()
print(x)
#a better method
x=100
def func(x):
    x=50
    return x
a=func(x)
print(a)