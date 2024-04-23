# Andrea Fiorilli
# 23/04/2024

# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

def display_message() -> None:
    a: str="Im learning functons"
    print(a)

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.

def favorite_function(title):
    print(f"One of my favorite books is {title}")
favorite_function("Alice in Wonderland")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size,text):
    print(f"The shirt's size is {size} and the text is {text}")
make_shirt("small","Hello world!")

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.
#

def describe_city(city: str, country: str = "Italy") -> None:
    message: str = f"{city} is in {country}"
    print(message)
describe_city("Rome")

#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
#     The function should return a string formatted like this: "Santiago, Chile". 
#     Call your function with at least three city-country pairs, and print the values that are returned.
#

def city_country(city: str, country: str) -> str:
    message: str = f"{city}, {country}"
    return message
print(city_country("Rome","Italy"))

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
#Make at least one new function call that includes the number of songs on an album.

def make_album(artist: str, title: str) -> dict:
    album: dict = {"artist" : artist, "album" : title}
    return album
print(make_album("A","B"))

#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_message(message: list=["A","B","C"]) -> None:
    for t in message:
        print(t)
show_message()

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. ######
#After calling the function, print both of your lists to make sure the messages were moved correctly.
#

def send_message(message: list) -> list:
    sent_message: list = [] 
    for t in message:
        print(t)
        sent_message.append(t)
        message.remove(t)    
    return sent_message

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, 
#and it should print a summary of the sandwich that’s being ordered.
# # Call the function three times, using a different number of arguments each time.
#

def sandwich(*args) -> None:
    print("Elenco ingredienti panino: ")
    for i in args:
        print(i)
sandwich("lattuce","ham")
sandwich("Ham")


#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
#

def build_profiler(first_name: str, last_name: str, age: int, weight: int) -> str:
    message: str = f"{first_name} {last_name}, age:{age}, weight: {weight}"
    return message
print(build_profiler("name","lastname",34,70))

#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly. 


def make_car(manufacturer: str, model: str, color: str = None) -> dict:
    car = {"manufacturer" : manufacturer,
           "model" : model,
           "color" : color,}
    return car
print(make_car("manuf","model","color"))
