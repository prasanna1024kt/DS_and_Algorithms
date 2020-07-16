'''
Given array of n integer are there element a,b and c in array such that a+b+c=0?
Find the all unique triplet in the array which gives sum of zero

num = [-1, 0, 1, 2, -1, -4]
sorted_num = [-4, -1, -1, 0, 1, 2]
code algorithm:
1. Sort array
2. starts iterating through list, create 2 pointer namely left and right.
Left is next number of array and right last element of the array
3. [-4, -1, -1, 0, 1, 2] i=-4 , l=i+1 =-1 and r=2 sum i+l+r =0 -4-1+2 <0 then move left to next element l = l+1
if l == l+1 then drop l+1 and move to next element ( unique triplet elements from list)
4. if sum <0 is not found then increase i = i+1 and remaining as step 3
5. if in case i, l and r sum >0 then decrease r = r-1
6. if sum = 0 then l = l+1 and r=r-1
7. if sumtotal is 0 then append i,l,r into empty array

'''
def three_sum(num):
    res =[]
    num = sorted(num)
    for i in range(len(num)-2):
        #checking i element uniqueness
        if i>0 and num[i] == num[i-1]: # edge incase 3 zero as input and eleminate duplicates
            continue
        left = i + 1
        rgt = len(num) - 1
        while left < rgt:
            sumt = num[i] + num[left] + num[rgt]
            # step 3
            if sumt < 0 :
                left = left + 1
            # step 4
            elif sumt > 0 :
                rgt = rgt - 1
            else:
                res.append([num[i],num[left],num[rgt]])
                while left < rgt and num[left] == num[left + 1]: # check duplicates for left and next element
                    left = left + 1
                while left < rgt and num[rgt] == num[rgt-1]:# check duplicates for right and prev element
                    rgt = rgt - 1
                left = left + 1
                rgt  = rgt - 1
    return  res

num = [-1, 0, 1, 2, -1, -4]

print(three_sum(num))