a="hello"
print(a[4])
#string slicing
print(a[::2])
#string method
b=len(a)
print(b)
print(a.upper())
print(a.swapcase())
c=a.isalpha()
print(c)
print(a.isalnum())
print(a.isnumeric())
c=a.replace('llo','avo')
print(c)
print(a.index('lo'))
d=" fuck,you "
print(d.strip())
#lstrip() for left space and rstrip() for right space removal
e=d.split(',')
print(e)
