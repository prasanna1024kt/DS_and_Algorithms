def max_heapify(arr,i):
    left = 2 *i + 1
    right = 2 * i + 2
    length = len(arr)
    largest = i
    if length > left and arr[largest] < arr[left]:
        largest = left
    if length > right and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        max_heapify(arr,largest)
def build_max_heap(arr):
    for i in reversed(range(len(arr)//2)):
        max_heapify(arr,i)
    return arr
def heapmaxsort(array):
    sorted_array=[]
    build_max_heap(array)
    for _ in range(len(array)):
        array[0],array[-1] = array[-1],array[0]
        sorted_array.append(array.pop())
        max_heapify(array,0)
    return sorted_array
arr = [1,12,9,5,6,10]
print(build_max_heap(arr))
print(heapmaxsort(arr))
a = [1,9,8,2,3,10,14,7,16,4]
print(heapmaxsort(a))