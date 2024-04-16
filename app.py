# # Variables in python
# first_name = "Sam"
# intro = "This are my first lines of python code!!"
# age = 28
# price_per_hour = 16.50
# is_online = True
# print(intro)

# ...input/string concatenation/print ...

# Note the int issue when working with floats and how to deal with it:
# The value from the input is in form of a string data type.
# First example will work with integers but not floats.

# first_number = input("First_number ")
# second_number = input("Second_number ")
# total_sum = int(first_number) + int(second_number)
# To solve the issue use float instead of int
# total_sum = float(first_number) + float(second_number)
# print(str(total_sum) + " Please don't cheat again.""You are a grown up!!!")
# shorter code
# first_number = float(input("First_number "))
# second_number = float(input("Second_number "))
# total_sum = first_number + second_number

#  If statement

# age = 2024 - int(birth_year)
# print("Your are: " + str(age) + " years of age!!!")
# if age > 35:
#     print("Look for an advanced test!!")
# elif age >30:
#     print("Are you serious you want to cheat??")
# elif age > 18:
#     print("Come on! You are an adult now!!!")
# elif age > 10:
#     print("Sure! Lets work on it together.")
# else:
#     print("No tests for you here!!")


# .....Practice Exercise....."
# name = input("What is your name? ")
# print("Hello " + name)
# weight = input("Enter your weight ")
# units = input("Want to convert to Kgs or Lbs? ")
# if units.upper() == 'K':
#     converted = float(weight) * 0.45
#     print("Your are: " + str(converted) + "Lbs.")
# else:
#     converted = float(weight) / 0.45
#     print("Your are: " + str(converted) + "Kgs.")
# loops
# x = 1
# while x <= 10:
#     print(x * '*')
#     x = x + 1

# Lists
# fruits = ["Mango", "Banana", "apple", "Jack"]
# fruits[3] = "Jack Fruit"
# print(fruits)
# print(fruits[0:3])
# list methods
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(0,0)
# print(numbers)
# print(1 in numbers)
# print(7 in numbers)
# print(len(numbers))
# fruits = ["Mango", "Banana", "apple", "Jack"]
# for f in fruits:
#     print(f)
#
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print((n * 2) + 1900)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1
numbers = range(5)
for n in numbers:
    print(n)
for n in range(10):
    print(n)


