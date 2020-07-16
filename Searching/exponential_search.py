def exponential_search(arr, item):
    N = len(arr)
    if arr[0] == item:
        return 0
    index = 1
    while (index < N) and (arr[index] <= item):
        index = index * 2
    binary_search(arr, item, index // 2, min(index, N))


def binary_search(arr, item_x, left, right):
    if left >= right:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == item_x:
            print("item found at %s " % mid)
            return mid
        else:
            if arr[mid] < item_x:
                left = mid + 1
            else:
                right = mid - 1
    return False


list1 = [10, 22, 30, 31, 44, 55, 57, 60, 71, 76, 78, 89, 91, 94, 95]
item = 89
exponential_search(list1, item)

