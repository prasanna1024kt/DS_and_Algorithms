def min_heapify(arr,i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(arr)-1
    small = i
    if left <= length and arr[i]>arr[left]:
        small = left
    if right <= length and arr[small] > arr[right]:
        small = right
    if small != i:
        arr[i], arr[small] = arr[small] , arr[i]
        min_heapify(arr,small)
def build_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr,i)
    return arr

def heapsort(arr):

    build_min_heap(arr)
    arr_sorted =[]
    for _ in range(len(arr)):
        arr[0],arr[-1] = arr[-1],arr[0]
        arr_sorted.append(arr.pop())
        min_heapify(arr,0)
    return arr_sorted

a = [-1,9,8,-2,-13,10,14,7,16,4]
arr = ["banana", "orange", "apple","pineapple", "berries", "lichi"]
print(heapsort(a))
print(heapsort(arr))
