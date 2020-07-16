def min_heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(arr)
    small = i
    if length < left and arr[i] > arr[left]:
        small = left
    if length < right and arr[small] > arr[right]:
        small = right
    if small != i :
        arr[i], arr[small] == arr[small], arr[i]
        min_heapify(arr, small)
def build_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr, i)
    return arr

def kthlargest(arr, k):
    n = len(arr)
    build_heap(arr)
    print(arr)
    #print(n)
    k_element = (n-k)+1
    print(k_element)
    for i in range(k_element):
        print(i)
        # arr[0],arr[-1] = arr[-1], arr[0]
        # item = arr.pop()
        # #print(item)
        # min_heapify(arr,0)
        # if i == k_element-1:
        #     return item
a = [1,9,8,2,3,10,14,7,16,4]
k=3
print(kthlargest(a,k))