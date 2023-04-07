cars = ['bmw', 'audi', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Checking for Inequality
requested_topping = 'Pasta'

if requested_topping != 'anchovies':
    print(f'Hold the anchovies')
else:
    print(f'Bring the {requested_topping.title()}')
print('\n')

#Checking Multiple Conditions
requested_topping1, requested_topping2 = 'Pasta', 'Anchovies'

if (requested_topping1 == 'Pasta') and (requested_topping2 == 'Anchovies'):
    print(f'Bring the food!')
else:
    print(f'Bring the {requested_topping.title()}')
print('\n')

#Checking whether a value is in a list
guests = ['alex', 'akki', 'tha', 'ammi', 'jess']
request_guest = 'brian'

if request_guest in guests:
    print (f'Welcome {request_guest.title()}')
else:
    print (f"sorry {request_guest.title()}, you're not invited")

print('\n')
# The If-elif-else Chain
age = 18

if age <= 12:
    price = 0
elif age > 12 and age < 18:
    price = 20
#else:
    #price = 25
#You can ommit the else block and use an elif block instead. Which makes more sense in this case.
elif age >=18:
    price = 25

print (f"Your admission price is ${price}")
print('\n')

#5-3
alien_colour = 'red'

if alien_colour == 'green':
    print('You just earned 5 points')
print('\n')

#5-4
alien_colour = 'red'

if alien_colour == 'green':
    print('You just earned 5 points')
else:
    print ('You just earned 10 points')
print('\n')

#5-6
age = 20

if age < 2:
    person = 'a baby'
elif age >= 2 and age < 4:
    person = 'a toddler'
elif age >= 4 and age < 13:
    person = 'a kid'
elif age >= 13 and age <20:
    person = 'a teenager'
elif age >=20 and age < 65:
    person = 'an adult'
elif age >= 65:
    person = 'an elder'

print (f"You're {person}")
print('\n')

#5-7
fav_Fruits = ['apple', 'banana', 'strawberry', 'kiwifruit']

if 'apple' in fav_Fruits:
    print ('You really like apples')
if 'cheery' in fav_Fruits:
    print ('You really like cherry')
if 'banana' in fav_Fruits:
    print ('You really like bananas')
if 'kiwifruit' in fav_Fruits:
    print ('You really like Kiwifruit')
print('\n')

#Using if statements with Lists
requested_toppings = ['mushrooms', 'capsicum', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'capsicum':
        print(f"Sorry we're out of {requested_topping}")
    else:
        print (requested_topping)
print('\n')

#Checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(requested_topping)
else:
    print("Please add toppings")
print('\n')

#Using Multiple lists
available_toppings = ['mushrooms', 'capsicum', 'extra cheese']
requested_toppings = ['mushrooms', 'bacon', 'capsicum', 'anchovies']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry {requested_topping} is not available")
print('\n')

#5-8 and 5-9
##usernames = ['bdub', 'soldierboy', 'sniperxx420', 'admin', 'trickdaddy']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f"Hello, {username}")
else:
    print('There are no users')
print('\n')

#5-10
current_users = ['bdub', 'soldierboy', 'sniperxx420', 'admin', 'trickdaddy']
new_users = ['BDUB', 'daddyyankee', '50 Cent', 'Ja Rule']

for user in new_users:
    user = user.lower()
    if user in current_users:
        print('Please select a new name')
    else:
        current_users.append(user)
        print(f'Welcome aboard {user}')

print(current_users)
print('\n')