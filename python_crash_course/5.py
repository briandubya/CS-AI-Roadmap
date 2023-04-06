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

if age <=12:
    price = 0
elif age >12 and age <18:
    price = 20
#else:
    #price = 25
#You can ommit the else block and use an elif block instead. Which makes more sense in this case.
elif age >=18:
    price = 25

print (f"Your admission price is ${price}")
print('\n')

