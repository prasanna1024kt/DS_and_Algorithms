"""
Quick sort implemented using first element as pivot
"""

def partition(arr, start, end):
    divider = start + 1
    pivot = start
    for i in range(start+1,end+1):
        if  arr[i] < arr[pivot]:
            arr[i],arr[divider] = arr[divider],arr[i]
            divider +=1
    arr[start],arr[divider-1] = arr[divider-1],arr[start]
    return divider-1

def quick_sort(arr, start, end):
    if start < end:
        pos = partition(arr,start,end)
        quick_sort(arr,start,pos-1)
        quick_sort(arr, pos+1,end)
arr = [10, 7, 8, 9, 1, 5,2,-2,6,4]
n = len(arr)
quick_sort(arr,0,n-1)
print(arr)
