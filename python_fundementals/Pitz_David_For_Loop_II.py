# def bigsize(nums):
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             nums[i] = 'big'
#     return nums

# li=[1,-9,-2,6,2,-1]
# print(bigsize(li))
# ------------------------------------

# def countpos(nums):
#     count=0
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             count+=1
#     nums[len(nums)-1] = count
#     return nums

# li=[1,9,-2,6,2,-1,11,22,-2]
# print(countpos(li))

# -------------------------------------

def sumtotal(nums):
    sum=0
    for i in range(len(nums)):
        sum += nums[i]
    return sum
li=[1,9,-3,6,2,10]
# print(sumtotal(li))
# -------------------------------------

def average(nums):
    sum=0
    for i in range(len(nums)):
        sum += nums[i]
    avg = sum/len(nums)
    return avg
li=[1,2,3,4,100,-99]
# print(average(li))
# -------------------------------------

def length(nums):
    length = len(nums)
    return length
li=[]
# print(length(li))
# -------------------------------------

def minimum(nums):
    min = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min
li=[-11111,-9,-2,-100,2,-2000]
# print(minimum(li))
# ---------------------------------------

def maximum(nums):
    max = nums[0]
    for i in range(len(nums)):
        if max < nums[i]:
            max = nums[i]
    return max
li=[1,2,333,4,100,-99,10000]
# print(maximum(li))
# ---------------------------------------

def ultanalysis(nums):
    thisdict = {
        'Total Sum':0,
        'Average':0,
        'Minimum':nums[0],
        'Maximum':nums[0],
        'Length':0
    }
    thisdict['Total Sum'] = sumtotal(nums)
    thisdict['Average'] = average(nums)
    thisdict['Minimum'] = minimum(nums)
    thisdict['Maximum'] = maximum(nums)
    thisdict["Length"] = len(nums)

    return thisdict
li=[1,2,3,4,100,22,-2,100000]
print(ultanalysis(li))
# -------------------------------------------

# def reverse(nums):
#     length = len(nums)/2 
#     length = round(length)
#     last = len(nums)-1
#     for i in range(length):
#         temp = nums[i]
#         nums[i] = nums[last-i]
#         nums[last-i] = temp
#     return nums
# li=[1,2,3,4,100,-99,2]
# print(reverse(li))
