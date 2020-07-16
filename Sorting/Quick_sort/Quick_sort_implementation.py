
"""
We can implement quick sort by using 4 differnt way in selecting the pivot value
1. Araay last element as pivot
2. Array first element as pivot
3. Random element as pivot
4. using median as pivot

Here i'm implementing 1 way choosing last element as pivot
"""
def partition(arr,start,end):
    divider = start
    pivot = end
    for i in range(start,end):
        if arr[i] < arr[pivot]:
            arr[i],arr[divider] = arr[divider],arr[i]
            divider += 1
    arr[pivot],arr[divider] = arr[divider],arr[pivot]
    return divider
def quick_sort(arr,start,end):
    if start < end:
        pos = partition(arr,start,end)
        quick_sort(arr,start,pos-1)
        quick_sort(arr,  pos+1,end)
arr = [10, 7, 8, 9, 1, 5,2,-2,6,4]
n = len(arr)
quick_sort(arr,0,n-1)
print(arr)

