# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

(x[1][0]) = 15

students[0] ["last_name"] = ("Bryant")
sports_directory ["soccer"][0] = ("Andres") 

print(students, sports_directory) 






# Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_Dictionary(students):
    return (students)


x = iterate_Dictionary(students)

print(students[0]) 
print(students[1])
print(students[2])
print(students[3])


# Get Values From a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary1(students):
    print (students[0] ["first_name"])
    print (students[1] ["first_name"])
    print (students[2] ["first_name"])
    print (students[3] ["first_name"])
    
def iterateDictionary2(students):
    print (students[0] ["last_name"])
    print (students[1] ["last_name"])
    print (students[2] ["last_name"])
    print (students[3] ["last_name"])

x = iterateDictionary1( students)
y = iterateDictionary2( students)

# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key, values in dojo.items():
        if key == ("locations"):
            print('7', key)
        elif key == ("instructors"):
            print('8', key)
        if(isinstance(values, list)):
            for value in values:
                print(value)
        else:
            print(value)

x = printInfo(dojo)