def merge_sort_ascneding(arr):
    if len(arr)>1: # divide the list into sublist untill having single element in the list
        mid = len(arr) //2 # getting middle element spliting array into left and right
        left = arr[:mid] # splited left array
        right = arr[mid:] # splited right array
        merge_sort_ascneding(left) # recurssively calling merge sort algorithm for splitted left list
        merge_sort_ascneding(right) # recurssively calling merge sort algorithm for splitted right list
        i=j=k=0 # initialing 3 variables i is index left list , j is index right list , K is for position in input array and added to sorted value in iterate way
        while i < len(left) and j < len(right): # looping through left and right list
            if left[i] < right[j]: # checks for left ith index value less than right jth index value
                arr[k] = left[i] # if above condition satisfy , left ith index value will add to input array in kth position
                i +=1 # incrementing i if above condition is true
                k +=1 # incrementing k if above condition is true
            else:
                arr[k] = right[j] # if above condition satisfy , right jth index value will add to input array in kth position
                j +=1 # incrementing j if above condition is true
                k +=1 # incrementing k if above condition is true
        while i < len(left): # after above step any value leftout in left sublist
            arr[k] = left[i]
            i +=1
            k +=1
        while j < len(right):# after above step any value leftout in right sublist
            arr[k] = right[j]
            j +=1
            k +=1
    return arr

def merge_sort_descending(arr):
    if len(arr)>1: # divide the list into sublist untill having single element in the list
        mid = len(arr) //2 # getting middle element spliting array into left and right
        left = arr[:mid] # splited left array
        right = arr[mid:] # splited right array
        merge_sort_descending(left) # recurssively calling merge sort algorithm for splitted left list
        merge_sort_descending(right) # recurssively calling merge sort algorithm for splitted right list
        i=j=k=0 # initialing 3 variables i is index left list , j is index right list , K is for position in input array and added to sorted value in iterate way
        while i < len(left) and j < len(right): # looping through left and right list
            if left[i] > right[j]: # checks for left ith index value less than right jth index value
                arr[k] = left[i] # if above condition satisfy , left ith index value will add to input array in kth position
                i +=1 # incrementing i if above condition is true
                k +=1 # incrementing k if above condition is true
            else:
                arr[k] = right[j] # if above condition satisfy , right jth index value will add to input array in kth position
                j +=1 # incrementing j if above condition is true
                k +=1 # incrementing k if above condition is true
        while i < len(left): # after above step any value leftout in left sublist
            arr[k] = left[i]
            i +=1
            k +=1
        while j < len(right):# after above step any value leftout in right sublist
            arr[k] = right[j]
            j +=1
            k +=1
    return arr

arr = [9,12,11,13,5,6,7,10]
print("sorted array in ascending order")
print(merge_sort_ascneding(arr))
print("sorted array in descending order")
print(merge_sort_descending(arr))

