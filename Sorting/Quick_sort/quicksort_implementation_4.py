"""
quick sort using median as pivot
"""

def partition(arr,start,end):
    median = (end-1-start)/2
    print("input array %s" %arr)
    print(" input start %s and end %s" %(start,end))
    median = int(median+ start)
    print("median %s"%median)
    print((arr[median] - arr[end-1]) * (arr[start]-arr[end-1]))
    print((arr[start] - arr[end-1]) * (arr[median]-arr[end-1]))
    if (arr[median]-arr[end-1]) * (arr[start]-arr[end-1]) >=0:
        arr[start],arr[median] = arr[median],arr[start]
    elif (arr[start]- arr[end-1]) * (arr[median]-arr[end-1]) >=0:
        arr[start],arr[end-1] = arr[end-1],arr[start]
    #print(arr[start])
    print("after swaping %s" %arr)
    divider = start + 1
    pivot = start
    for i in range(start,end+1):
        if arr[i] < arr[pivot]:
            arr[i], arr[divider] = arr[divider], arr[i]
            divider = divider + 1
    arr[start], arr[divider-1] = arr[divider-1], arr[start]
    print("after iteration of swaping %s" %arr)
    return divider-1
def quick_sort(arr, start, end):
    if start < end:
        pos = partition(arr, start, end)
        quick_sort(arr,start,pos)
        quick_sort(arr,pos+1, end)
arr = [10, 7, 8, 9, 1, 5,2,-2,6,4]
print(arr)
n = len(arr)

#partition(arr,0,n-1)
quick_sort(arr,0,n-1)
print(arr)