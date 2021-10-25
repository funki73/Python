num1 = 42 # variable and value
num2 = 2.3 # variable and value
boolean = True = # Type check 
string = 'Hello World' #type check
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable with Array's - Strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable with Array's - Strings
fruit = ('blueberry', 'strawberry', 'banana') #argument
print(type(fruit)) #log statement -> type -> argument
print(pizza_toppings[1]) #log state -> argument -> array
pizza_toppings.append('Mushrooms') #
print(person['name']) #log state -> argument -> array
person['name'] = 'George' 
person['eye_color'] = 'blue'
print(fruit[2]) # return 

if num1 > 45: # if statement
    print("It's greater") # return
else: # else
    print("It's lower") # return

if len(string) < 5: # if statement
    print("It's a short word!") # return
elif len(string) > 15: # else if statement
    print("It's a long word!") # return
else: # else
    print("Just right!") # return

for x in range(5): # 
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() 
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)