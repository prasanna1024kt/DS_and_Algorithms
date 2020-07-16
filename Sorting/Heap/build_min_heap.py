def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        #print(array)
        min_heapify(array, smallest)
    #print(array)
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
    return array
#a = [21,1,45,78,3,5]
a = [1,9,8,2,3,10,14,7,16,4]
print(build_min_heap(a))