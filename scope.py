#scope of variables
x=100
def func(x):
    x=50
    def cube():
        print(x**3)
    cube()
func(x)
print(x)
'''L: local variable
   E: enclosing function
   G: global
   B: built in'''
