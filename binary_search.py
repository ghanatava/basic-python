lst=[1,6,2,4,5,3,7,8,9,10]
lst.sort()
def binary_search_iterative(key,lst):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if key==lst[mid]:
            return 'found at index',mid
        elif key<lst[mid]:
            high=mid-1
        else:
            low=mid+1
        return 'not found'
def binary_search_reccursive(key,lst,low,high):
    if low>high:
        return 'not found'
    else:
        mid=(low+high)//2
        if key==lst[mid]:
            return 'found at index',mid
        elif key<lst[mid]:
            return binary_search_reccursive(key, lst, low, mid-1)
        else:
            return binary_search_reccursive(key, lst, mid+1, high)
print(binary_search_reccursive(6, lst,0,len(lst)-1))
print(binary_search_iterative(5,lst))
