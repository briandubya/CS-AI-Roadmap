#3. Introducing Lists

#Simple example of a list containing a few kinds of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[1].title())
print(bicycles[-1])

#using a list object inside an f string
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

#Modifying Elements in a List
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
motorcycles[0] = 'Ducati'
print(motorcycles)

#Appending
motorcycles.append('Honda')
print(motorcycles)

#Inserting
motorcycles.insert(0, 'harley'.title())
print(motorcycles)

#Removing Elements from a List
##Using Del
del motorcycles[0]
print(motorcycles)
##Using Pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles.append(popped_motorcycle)
print(motorcycles)
first_motorcycle = motorcycles.pop(0)
print(first_motorcycle)
print(motorcycles)
##Remove method
too_expensive = 'yamaha'
motorcycles.remove(too_expensive.title())
print(motorcycles)


#Exercise 1
##3-4
guest_list = ['Thierry Henry', 'Carl Lewis', 'Mike Tyson']
for g in guest_list:
    print(f"Hello, {g}, you're invited to my dinner party")
##3-5
cannot_attend = guest_list.pop(2)
print (f"Unfortunately, {cannot_attend} cannot make it")
guest_list.insert(2, 'Robert Moses')
print(guest_list)
##3-6
guest_list.insert(0, 'David Goggins')
print(guest_list)
print(len(guest_list))
guest_list.insert((len(guest_list)//2), 'Brian')
print(guest_list)
guest_list.append('Jess')
print(guest_list)

#Organising a List
##Sorting a List Permanently 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
##Sorting temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
##Reversing a List
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)
##Finding the length of a list
print(len(cars))