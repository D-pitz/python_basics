# def countdown(num):
#     result=[]
#     for i in range (num, -1, -1):
#         result.append(i)
#     return result

# print(countdown(7))
# ----------------------------------------------------

# def printandreturn(x,y):
#     print(x)
#     return(y)

# print(printandreturn(80,567))
# ---------------------------------------------------

# def firstpluslength(ints):
#     sum=0
#     sum += ints[0] + len(ints) 
#     return sum

# nums=[10,2,3,6,7,4,3]
# print(firstpluslength(nums))
# ----------------------------------------------

# def valuesgreaterthansecond(mylist):
#     if len(mylist)<2:
#         return "False"
#     count=0
#     newlist=[]
#     for i in range(len(mylist)):
#         if mylist[i] > mylist[1]:
#             newlist.append(mylist[i])
#             count += 1
#     print(count)
#     return newlist

# li=[6,10,4,2,6,3,100,22,33,3,55]
# print(valuesgreaterthansecond(li))

def lengthandvalue(length,value):
    newlist=[]
    for i in range(length):
        newlist.append(value)
    return newlist
print(lengthandvalue(22,100))
