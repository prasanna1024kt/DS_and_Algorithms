'''
Find the common elements from the two lists
to achieve this we can use 2 methods
1.Normal method using iteration
2.use dictionary
'''

# method 1

def common_element(list1,list2):
    cmn=[]
    cnt = 0
    for i in list1: # time complexity m
        for j in list2: #time complexity n
            if i == j:
                cmn.append(i)
                cnt = cnt + 1
    print("common elment count is %s" %cnt)
    # total time complexity will be t(m*n)
    print(cmn)
l = [1,3,4,5,7,8]
k = [3,5,9,6,2]

common_element(l,k)

def common_element_dict(list1,list2):
    cnt = 0
    d = {}
    # loading list 2 item into dictionary with list items into dict key and value for key as 1
    for element in list2:
        d[element] = 1
    # checking list 1 items in dict key it will search 0(1) and returns the data as well
    for item in list1:
        if d.get(item) != None:
            print(item)
            cnt = cnt + 1
    print("common elment count is %s" % cnt)

common_element_dict(l,k)
