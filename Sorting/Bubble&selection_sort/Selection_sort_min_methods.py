list1 = [2,6,9,-1,0,4,44,23,46,442,-33]

print(list1)
def selection_sort_using_min(arr):
    for i in range(len(arr)):
        min_value = min(arr[i:])
        min_index = arr.index(min_value)
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# sort duplicates in list using selection sort
def selection_sort_duplicates(arr):
    """
    method used to sort duplicates in the list
    :param arr:
    :return: sorted list
    """
    for i in range(len(arr)-1):
        min_value = min(arr[i:])
        min_index = arr.index(min_value,i)
        """
        To handle duplicates in list, index value will be plays vital role and hence start position is added as i
        i means that from start index where we need to search index 
        """
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
dup_list = [4,5,6,7,8,-1,-2,5,8,2,11]

print(selection_sort_using_min(list1))

print(selection_sort_duplicates(dup_list))