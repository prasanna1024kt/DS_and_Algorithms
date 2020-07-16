import math

def jump_search(arr, item):
    N = len(arr)
    B = math.sqrt(N)
    left = 0
    # find block in which element is present
    while arr[int(min(B,N)-1)]< item:
        left = int(B)
        B += math.sqrt(N)
        if left > N:
            return -1
    # in block do linear search for element
    while arr[int(left)] < item:
        left = int(left) + 1
        if left == min(B,N):
            return -1
    # if item found return index of an element
    if arr[left] == item:
        return left
    return -1


arr = [3,6,8,9,11,12,16,18,21,26,28,31,35,45,55,66,67,88,89]
print(arr)
print(jump_search(arr,45))