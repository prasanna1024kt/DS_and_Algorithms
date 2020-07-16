'''
find the kth largest element from the list,
you can use any heap properties like min-heap and max-heap
Here i'm using max heap to find the kth largest element from the list
Time complexuty to find the kth largest element is:
time complexity to find the kth largest element in list is O(k+nlog(n))
time complexity to heapif O(log(n))
time complicity to create and build heap is O(n),
To find the kth largest element u have to pop k element from the list
total time complexity is the kth largest element from the list O(n+Klog(n)

'''

def max_heapify(arr, i ):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(arr)
    largest = i

    if length > left and arr[largest] < arr[left]:
        largest = left
    if length > right and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i] , arr[largest] = arr[largest], arr[i]
        max_heapify(arr,largest)
def build_max_heap(arr):
    for i in reversed(range(len(arr)//2)):
        max_heapify(arr,i)
    return arr
def kthlargest(arr, k):
    build_max_heap(arr)
    print(arr)
    for i in range(k):
        arr[0], arr[-1] = arr[-1], arr[0]
        item = arr.pop()
        max_heapify(arr,0)
        if i == k-1:
            return item
a = [1,9,8,2,3,10,14,7,16,4]
k=3
print(kthlargest(a,k))