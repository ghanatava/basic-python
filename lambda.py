lst=[1,2,4,3,5,6]
print(list(map(lambda x:x**3,lst)))
#using with filter()
print(list(filter(lambda x:x%2==0,lst)))
