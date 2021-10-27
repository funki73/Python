import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')

# def be_cheerful(name="Mr Nibbles",repeat=10):
#     print(f"Good Morning {name}\n" * repeat)

# be_cheerful("Randy")
# be_cheerful()
# be_cheerful(repeat=4, name="Joe Mama")