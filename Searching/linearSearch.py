class linearsearch(object):
    '''
    Linear search Algorithm inspect each item in a list one by one from one end to the other,
    to find a match for what you are searching for.
    We can achieve algorithm by simple for loop or by using recursive way
    '''

    def __init__(self, search_array, search_item ):
        self.search_array = search_array
        self.search_item = search_item

    def LinearSearch(self):
        print(self.search_array)
        for item in range(len(self.search_array)):

            if self.search_array[item] == self.search_item:
                print("{} exists at {} index in array ".format(self.search_item, item))
                return item
        return -1

    def LinearSearchRecursive(self, index):

        if index >= len(self.search_array):
            return -1
        if self.search_array[index] == self.search_item:
            print("{} exists at {} index in array ".format(self.search_item, index))
            return index
        return self.LinearSearchRecursive(index+1)


list1 = [3,4,8,12,10,24,26]
search = 24
linear = linearsearch(list1, search)
print(linear.LinearSearch())
print(linear.LinearSearchRecursive(0))






