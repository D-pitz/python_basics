# x = [ [5,2,3], [15,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# def changex(li):
#     li[1][0] = 15
#     return li
# print(changex(x))

# def changedict(stud):
#     stud[0]['last_name'] = 'Bryant'
#     return stud
# print(changedict(students))

# def changesport(sport):
#     sport['soccer'][0] = 'Andres'
#     return sport
# print(changesport(sports_directory))

# def changez(z):
#     z[0]['y']= 30
#     return z
# print(changez(z))
# -------------------------------------------------

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students): 
    
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    # first_name - Michael, last_name - Jordan
    # first_name - John, last_name - Rosales
    # first_name - Mark, last_name - Guillen
    # first_name - KB, last_name - Tonel
    for eachdict in students:
        # print(eachdict)
        displaystring = ''
        for currentkey in eachdict.keys():
            # print(currentkey)
            displaystring += f'{currentkey} - {eachdict[currentkey]} '
        print(displaystring)
iterateDictionary(students)
# --------------------------------------------------------

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(key_name, some_list):
#     for currentdict in some_list:
#         for name in currentdict.keys():
#             if (key_name == name):
#                 print(currentdict[key_name])

# iterateDictionary2('last_name', students)
# -----------------------------------------------------------

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for key in some_dict:
#         print(len(some_dict[key]),key)
#         for val in range(len(some_dict[key])):
#             print(some_dict[key][val])
# printInfo(dojo)
