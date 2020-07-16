def fibonacci_number(n):

    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)


def fibonacci_search(arr, item):
    mid = 0
    while fibonacci_number(mid) < len(arr):
        mid = mid + 1
    offset = -1

    while fibonacci_number(mid) >1:
        i = min (offset + fibonacci_number(mid -2), len(arr)-1)
        print("current element %s" % arr[i])
        print("offset value %s" % offset)
        if item > arr[i]:
            mid = mid - 1
            offset = i
        elif item < arr[i]:
            mid = mid - 2
        else:
            return i

    while (fibonacci_number(mid -1) and arr[offset + 1] == item):
        return offset + 1


list_1 = [10, 20, 30, 35, 40, 51, 55, 61, 67, 68, 70, 75]
print(list_1)
print(fibonacci_search(list_1, 68))
list_2 = [10, 22, 30, 31, 44, 55, 57, 60, 71, 76, 78, 89, 91, 94, 95]
print(list_2)
print(fibonacci_search(list_2, 71))


