'''
Given an array of integer return indices of two numbers such that sum up
to specific number
num = [1,3,5,7,9,8]
target=12
return : [2,3]
First step for the solution is creating dictionary for diff with looping list
12 - 1 = 11 {11:0}
12 - 3 = 9  {11:0,9:1}
12 - 5 = 7  {11:0,9:1,7:1}
12 - 7 = 5  {11:0,9:1,7:1,5:2}
12 - 9 = 3  {11:0,9:1,7:1,5:2,3:3}
12 - 8 = 4  {11:0,9:1,7:1,5:2,3:3,4:4}

After creating dict then check for list have dict element if present return indices of list [dict[num[i],i]
return [2,3]

'''
num = [1,3,5,7,9,8]
target=13
def two_sum(num,target):
    dict = {}
    for i in range(len(num)):
        if num[i] in dict:
            return [dict[num[i]],i]
        else:
            dict[target - num[i] ]=i
print(two_sum(num,target))
