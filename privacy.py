#just add __ before any variable,method or class it will be private
class Private:
    def __init__(self,a,b):
        self.__a=a
        self.__b=b
    def sum(self):
        return(self.__a+self.__b)

priv=Private(20,49)
print(priv.sum())
print(priv.__a)#a is now private.
print(priv._Private__a)
