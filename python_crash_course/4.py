magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print (magician)
    print (f'{magician.title()}, that was a great trick\n')

print ('Thank you everyone, that was a great magic show\n')

#Ex 4-1
fav_pizzas = ['pepperoni', 'spicy', 'buffalo']
for pizza in fav_pizzas:
    print (f'I like {pizza} pizza!')
print ('\nI fucking love pizza!\n')

# Making Numerical Lists

## Using the range() Function
for value in range(1,5):
    print (value)
print('\n')

for value in range(6):
    print (value)
print('\n')

## Using range() to make a List of Numbers
number_list = list(range(1,6))
print (number_list)
even_numbers = list(range(2,11,2))
print (even_numbers)
print('\n')
### Square number example
square = []
for number in range(1,11):
    squared = number **2
    square.append(squared)
print (square)
print('\n')
##Simple Statistics with a List of NUmbers
digits = list(range(0,10))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
print('\n')
#List Comprehension
###Using the Square number example to write the code in a single line
square = [value**2 for value in range(1,11)]
print(square)
print('\n')
#Ex 4-3 to 4-9
##4-3
list_20 = list(range(1,21))
for value in list_20:
    print(value)
print('\n')
##4-5
million_list = list(range(1, 1_000_001))
print(min(million_list))
print(max(million_list))
print(sum(million_list))
print('\n')
##4-6
odd_list = list(range(1,21,2))
for odd in odd_list:
    print(odd)
print('\n')
##4-7
multi_30 = [value*3 for value in range(3,31)]
for value in multi_30:
    print(value)
print('\n') 
##4-8 & 4-9 Cubes
cube_list = [value**3 for value in range(1,11)]
for value in cube_list:
    print(value)

#Working with a part of a list
## Slicing a List
players = ['charles', 'martin', 'michael', 'brian', 'eli', 'david', 'john']
players_ = [player.title() for player in players]
print(players_)
print(players[0:3])
print(players[:3])
print(players[3:])
print(players[-3:])
print(players[:-3])
print('\n')
## Looping through a slice
for player in players[0:3]:
    print (player.title())
print('\n')
##Copying a List
players_copy = players[:]
print(players)
print(players_copy)
print('\n')

##4-11
players.append('greg')
print(players)
players_copy.append('dick')
print(players_copy)

#Tuples
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
##Looping 
for dimension in dimensions:
    print(dimensions)
print('\n')

##Writing over a tuple
print ('The original dimensions are')
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print (f'The modified dimensions are:')
for dimension in dimensions:
    print(dimension)