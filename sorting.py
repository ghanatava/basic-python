data=[1,34,5,6,78]
def bubble_sort(lst):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
bubble_sort(data)
print(data)
lst=[1,34,5,6,78]
#selection sort
def selection_sort(lst):
    for i in range(len(lst)-1):
        min=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min]:
                min=j
        if min != i:
            lst[min],lst[i]=lst[i],lst[min]
    return lst    
print(selection_sort(lst))
#insertion sort
array=[1,34,5,6,78]
def insertion_sort(array):
    for i in range(1,len(array)):
        value_to_sort=array[i]
        while array[i-1]>array[i] and i>0:
            array[i-1],array[i]=array[i],array[i-1]
            i=i-1
    return array
print(insertion_sort(array))
    
