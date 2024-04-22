# Andrea Fiorilli
# 19/04/2024

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, 
# and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, 
# instead of printing just the name of the pizza. 
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, 
# that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

a: list = ["Margherita","Diavola","Boscaiola"]
for sentence in a:
    print (f"I like pizza {sentence}")
print ("I really like pizza")

# 4-2. Animals: Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, 
# and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, 
# such as A dog would make a great pet.
# • Add a line at the end of your program, 
# stating what these animals have in common. 
# You could print a sentence, such as Any of these animals would make a great pet!

animals: list = ["Dog", "Cat", "Turtle"]
for a in animals:
    print (f"The {a} is a good animal")
print (f"All this animals can be pet")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for a in range(1,21):
    print(a)

# 4-4. One Million: Make a list of the numbers from one to one million, 
# and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

num: list = range(1,1000001)
#for a in num:
# print(a)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, 
# and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million numbers.

print(min(num))
print(max(num))
print(sum(num))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
# Use a for loop to print each number.

for a in range(1,20,2):
    print(a)

# 4-7. Threes: Make a list of the multiples of 3, 
# from 3 to 30. Use a for loop to print the numbers in your list.

num: list = range(3,31, 3)
for a in num:
    print(a)

# 4-8. Cubes: A number raised to the third power is called a cube. 
# For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
# and use a for loop to print out the value of each cube.


num: list = range(1,11)
for a in num:
    b=a**3
    print(b)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

lista: list = [lista ** 3 for lista in range(1,11)]
print(lista)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

num: list = [lista for lista in range(1,11)]
for a in num:
    print(a)
print (f"The first three items in the list are: {num[:3]}")
print (f"Three items from the middle of the list are: {num[3:6]}")
print (f"The first three items in the list are: {num[7:]}")

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

a: list = ["Margherita","Diavola","Boscaiola"]
for sentence in a:
    print (f"I like pizza {sentence}")
print ("I really like pizza")
z: str = ""
y: str = ""

friend_pizzas: list = a.copy() 
a.append("Bianca")
friend_pizzas.append("Rossa")
for sentence in a:
    z=z+", "+sentence
print (f"My favorite pizzas are:{z}")
for sentence1 in friend_pizzas:
    y=y+", "+sentence1
print (f"My friend’s favorite pizzas are:{y}")

# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi') 
