#Print numbers from 1-151.
# for x in range(1, 151):
#     print(x)

# # print the multiples of 5 to 1000.
# for x in range(5,1000,5):
#     print(x)

# # Print integers 1 - 100. if divisible by 5 print 'coding'. if divisble by 10 print ' Coding Dojo'
# for x in range(1,100):
#     if x%10 == 0:
#         print('Coding Dojo')
#     elif x%5 == 0:
#         print('Coding')
#     else:
#         print(x)

# # add odd integers from 0 - 500000, print the final sum
# sum = 0
# for x in range(1,500001):
#     if x%2 == 1:
#         sum += x
#     print(sum)

# # countdown from 2018 in increments of 4 
# for i in range(2018,1,-4):
#     print(i)

# Set High, Low, and mult variable. the loop should iterate from the lownum to the highnum and print the multiples of mult.
lownum = 2
highnum = 28
mult = 7
for x in range(lownum,highnum+1):
    if x%mult == 0:
        print(x)