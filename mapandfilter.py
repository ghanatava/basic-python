def cube(n):
    print(n**3)
lst=[1,2,3,4,5,6]
result=list(map(cube,lst))
print(result)
#filter()
def even(n):
    return(n%2==0)
itr=[1,2,3,4,5,6,8,9,20]
out=list(filter(even,itr))
print(out)