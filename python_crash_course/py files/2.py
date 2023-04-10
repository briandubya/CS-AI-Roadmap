name = "Brian"
print(name.title())
print(name.upper())
print(name.lower())

#Adding Whitespae to Strings with Tabs or Newlines
print("Python")
print("\nPython")
print("\tPython")
print("\n\tPython")

#Stripping Whitespace
fav_lang = "python "
print(fav_lang.strip())

#Removing Prefixes
url = "http://www.google.com"
simple_url = url.removeprefix("http://")

print(url)
print(simple_url)

#Exercises
_name = "Brian"
print (f"hello {_name}")
print(_name.title())
print(_name.upper())
print(_name.lower())

filename = "notes.txt"
print(filename.removesuffix('.txt'))

#underscores in numbers
universe_age = 14_000_000_000
print(universe_age)

#Multiple assignment
x, y, z = 0, 0, 0

#Constants.
#always capitalise
MAX_CONNECTIONS = 5000

#Zen of Python
import this