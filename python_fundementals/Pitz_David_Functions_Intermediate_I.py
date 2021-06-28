# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.
import random
def randint(min=0,max=0):
    if (min==0) and (max==0):
        num = random.random() * 100
        num = round(num)
        return num
    elif min==0:
        num = random.random() * max
        num = round(num)
        return num
    elif max==0:
        num = random.random() * (100-min) + min
        num = round(num)
        return num
    else:
        num = random.random() * (max-min) + min 
        num = round(num)
        return num
print(randint())
print(randint(max=100000))
print(randint(min=1))
print(randint(min=1100, max=2000))