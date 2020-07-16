def selection_sort(arr):
    for i in range(len(arr)):
        m_value = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < m_value:
                m_value = arr[j]
        m_index = arr.index(m_value,i)
        arr[i], arr[m_index] = arr[m_index], arr[i]
    return arr
arr = [3,5,6,1,-1,9,6,77,-99,191]
print("unsorted list: %s" %arr)
print(selection_sort(arr))