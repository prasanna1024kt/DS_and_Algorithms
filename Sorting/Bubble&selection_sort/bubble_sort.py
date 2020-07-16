def bubble_sort(arr):

    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):#-j  used to ignore already swapped element from previous iteration
            if arr[i] > arr[i+1]: # For ascending order used > (greter than ), For descending order use < (lessthan) in constrant
                arr[i],arr[i+1] = arr[i+1],arr[i]
                #print(arr) # return list for each iteration
            else:
                print(arr)
        print("              ")
    return arr
arr = [3,5,-1,6,2,1]
bubble_sort(arr)