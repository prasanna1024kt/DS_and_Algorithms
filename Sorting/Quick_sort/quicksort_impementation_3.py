"""
quick sort using random pivot value
"""
import random

def random_pivot(arr,start,end):
    rpivot = random.randrange(start,end)
    arr[start],arr[rpivot] = arr[rpivot],arr[start]
    return partition(arr,start,end)
def partition(arr,start,end):
    divider =start + 1
    pivot = start
    for i in range(start+1,end+1):
        if arr[i]<arr[pivot]:
            arr[i],arr[divider] = arr[divider],arr[i]
            divider = divider +1
    arr[start],arr[divider-1] = arr[divider-1], arr[start]
    return divider-1

def random_quicksort(arr,start,end):
    if start<end:
        pos = random_pivot(arr,start,end)
        random_quicksort(arr,start,pos-1)
        random_quicksort(arr,pos+1,end)
arr = [10, 7, 8, 9, 1, 5,2,-2,6,4]
n = len(arr)
random_quicksort(arr,0,n-1)
print(arr)
array = [10, 7, 8, 9, 1, 5]
random_quicksort(array, 0, len(array) - 1)
print(array)
# arr.clear()

