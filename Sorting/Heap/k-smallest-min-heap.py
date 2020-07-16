
"""
Find the kth smallest element from the list using min heap
time complexity to find the kth smallest element in list is O(k+nlog(n))
time complexity to heapif O(log(n))
time complicity to create and build heap is O(n),
To find the kth smallest element u have to pop k element from the list
total time complexity is the kth element from the list O(n+Klog(n)
"""
def min_heapify(arr,i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(arr)
    small = i
    if left < length  and arr[i] > arr[left]:
        small = left
    if right < length and arr[small] > arr[right]:
        small = right
    if small != i :
        arr[i], arr[small] = arr[small],arr[i]
        min_heapify(arr,small)
def build_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr,i)
    return arr
def kthsmall(arr,k):
    harry = build_min_heap(arr)
    for i in range(k):
        arr[0],arr[-1] = arr[-1],arr[0]
        item = harry.pop()
        min_heapify(arr, 0)
        if i == k-1:
            return item

a = [1,9,8,2,3,10,14,7,16,4]
k=3
print(kthsmall(a,k))

#print(heapsort(a))
