class binarysearch(object):

    def __init__(self, arr, item ):
        self.arr = arr
        self.item = item

    def binary_search(self):

        L = 0
        R = len(self.arr)-1

        while L <= R:
            mid = (L + R)//2
            if self.arr[mid] == self.item:
                print(" {} has found at index {} ".format(self.item,mid))
                return True
            else:
                if self.arr[mid] < self.item:
                    L = mid + 1
                else:
                    R = mid - 1
        return False

    def binary_search_recursive(self, low, high):
        if low > high:
            return False
        else:
            mid = (low + high )// 2
            if self.arr[mid] == self.item:
                print(" {} recursive method has found at index {} ".format(self.item, mid))
                return True
            elif self.arr[mid] < self.item:
                return self.binary_search_recursive(mid+1, high)
            else:
                return self.binary_search_recursive(low, mid-1)




array = [1,5,7,8,9,99,121,134,154,178,199,201,400]
item = 121
obj = binarysearch(array,item)
print(obj.binary_search_recursive(0,len(array)-1))
if obj.binary_search():
    print("found")
else:
    print("Not Found")

