# name = "Zen"
# print("My name is", name)

# name = "Zen"
# print("My name is " + name)

# print("Hello" + 42)			# output: TypeError
# print("Hello" + str(42))		# output: Hello 42

# name = "Noelle"
# print(name)	# with a comma
# print(name + "" )	# with a +

# name = 42
# print(name)	# with a comma
# # print(name +)	# with a +	-- this one should give us an error!

# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"


# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# sum2 = add(1,4)
# sum3 = sum1 + sum2

# print(sum1)
# print(sum2)

#  ! Update Values in Dictionaries and Lists

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


# TODO: Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# TODO: Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = "Bryant"
print(students)
# TODO: In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print( sports_directory['soccer'])
# TODO: Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


# ! Iterate Through a List of Dictionaries
# TODO: Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_dictionary(students)
    
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# * first_name - Michael, last_name - Jordan
# * first_name - John, last_name - Rosales
# * first_name - Mark, last_name - Guillen
# * first_name - KB, last_name - Tonel



# ! Get Values From a List of Dictionaries
# TODO: Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# * Michael
# * John
# * Mark
# * KB
def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)
# TODO: And iterateDictionary2('last_name', students) should output:
# * Jordan
# * Rosales
# * Guillen
# * Tonel


# ! Iterate Through a Dictionary with List Values
# TODO: Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    for key,val in dict.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)
# * output:
# * 7 LOCATIONS
# * San Jose
# * Seattle
# * Dallas
# * Chicago
# * Tulsa
# * DC
# * Burbank
    
# * 8 INSTRUCTORS
# * Michael
# * Amy
# * Eduardo
# * Josh
# * Graham
# * Patrick
# * Minh
# * Devon