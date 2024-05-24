#ES1
class Person:
    def __init__(self,name:str,age:int)->None:
        self.name=name
        self.age=age

alice:Person=Person("Alice W.",45)
bob:Person=Person("Bob M.",36)

#Es1
print(bob.age)
persons:Person=[alice,bob]
for p in persons:
    print(p.age)

#Es2
if alice.age>bob.age:
    print(alice.age)
else:
    print(bob.age)



#ES2
class Student:
    def __init__(self,name:str,studyProgram:str,age:int,gender:str)->None:
        self.name=name
        self.studyProgram=studyProgram
        self.age=age
        self.gender=gender

    def printInfo(self)->None:
        print(self.name,self.studyProgram,self.age,self.gender)

me:Student=Student("Andrea","Python",20,"male")
left_neigh:Student=Student("Bob","Python",20,"male")
right_neigh:Student=Student("Alice","Python",18,"female")

me.printInfo()
left_neigh.printInfo()
right_neigh.printInfo()



#ES3
class Animal:
    def __init__(self,name:str,legs:int)->None:
        self.name=name
        self.legs=legs

    def get_legs(self):
        """
        This function returns the animal's legs number
        input: none
        return: self.legs: str, the function returns the animal's legs number
        """
        return self.legs
    
    def set_legs(self,legs:int)->None:
        """
        This function set the attribute legs
        input: legs: input, the parameter contains the animal's legs number
        return: None
        """
        self.legs=legs
    
    def printInfo(self)->None:
        print(self.name,self.legs)

dog:Animal=Animal("dog",0)
cat:Animal=Animal("cat",4)

dog.legs=4
print(dog.legs)

dog.set_legs(3)
print(dog.legs)

print(cat.get_legs())

dog.printInfo()
cat.printInfo()



#ES4
class Food:
    def __init__(self,name:str,price:int,description:str)->None:
        self.name=name
        self.price=price
        self.description=description

class Menu:
    def __init__(self,lista:list=[])->None:
        self.lista=lista

    def add_food(self, food: Food)->None:
        self.lista.append(food)

    def remove_food(self, food: Food)->None:
        self.lista.append(food)

    def getAvaragePrice(self)->float:
        conta=0
        avaragePrice=0
        for p in self.lista:
            conta=conta+1
            avaragePrice=avaragePrice+p.price
        return avaragePrice/conta
    
    def printPrices(self)->str:
        for p in self.lista:
            print(f"{p.name} {p.price}$ description: {p.description}")

food1:Food=Food("Meat",5,"Cow meat")
food2:Food=Food("Fish",6,"Tuna")
food3:Food=Food("Fruit",2,"Apple")

menu: Menu = Menu()
menu.add_food(food1)
menu.add_food(food2)
menu.add_food(food3)

menu.printPrices()
print(menu.getAvaragePrice())


#9-1. Restaurant: Make a class called Restaurant. 
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant()
# that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant:
    def __init__(self,restaurant_name:str, cuisine_type:str)->None:
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self)->None:
        print(self.restaurant_name,self.cuisine_type)

    def opened_restaurant(self,)->None:
        print("The restaurant is open")

restaurant:Restaurant=Restaurant("Name","Type")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.opened_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1.
# Create three different instances from the class, and call describe_restaurant() for each instance.

restaurant1:Restaurant=Restaurant("Name1","Type1")
restaurant2:Restaurant=Restaurant("Name2","Type2")
restaurant3:Restaurant=Restaurant("Name3","Type3")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users: Make a class called User.
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self,first_name:str, last_name:str, age:int, date_birth:str, gender:str)->None:
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.date_birth=date_birth
        self.gender=gender

    def describe_user(self)->None:
        print(self.first_name,self.last_name,self.age,self.date_birth,self.gender)

    def greet_user(self,)->None:
        print(f"Hi {self.first_name,self.last_name}, nice to meet you")

user1:User=User("User","1","18","17/4/06","male")
user2:User=User("User","2","19","17/4/05","female")
user3:User=User("User","3","20","17/4/04","male")
user4:User=User("User","4","21","17/4/03","female")

user1.describe_user()
user1.greet_user

user2.describe_user()
user2.greet_user

user3.describe_user()
user3.greet_user

user4.describe_user()
user4.greet_user

# 9-4. Number Served: Start with your program from Exercise 9-1.
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant:
    def __init__(self,restaurant_name:str, cuisine_type:str, number_served:int=0)->None:
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served

    def describe_restaurant(self)->None:
        print(self.restaurant_name,self.cuisine_type)

    def opened_restaurant(self,)->None:
        print("The restaurant is open")

    def set_number_served(self,number_served:int)->None:
        self.number_served=number_served

    def increment_number_served(self,number_increased:int)->None:
        self.number_increased=number_increased
        self.number_served+=self.number_increased

restaurant:Restaurant=Restaurant("Name","Type")
print(restaurant.number_served)
restaurant.set_number_served(1)
print(restaurant.number_served)
restaurant.increment_number_served(3)
print(restaurant.number_served)

#  9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3.
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.

class User:
    def __init__(self,first_name:str, last_name:str, age:int, date_birth:str, gender:str, login_attemps:int=0)->None:
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.date_birth=date_birth
        self.gender=gender
        self.login_attemps=login_attemps

    def describe_user(self)->None:
        print(self.first_name,self.last_name,self.age,self.date_birth,self.gender)

    def greet_user(self,)->None:
        print(f"Hi {self.first_name,self.last_name}, nice to meet you")

    def increment_login_attemps(self,)->None:
        self.login_attemps+=1

    def reset_login_attemps(self,)->None:
        self.login_attemps=0

user:User=User("User","1","18","17/4/06","male")
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
user.increment_login_attemps()
print(user.login_attemps)
user.reset_login_attemps()
print(user.login_attemps)    

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4.
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method. 

class IceCreamStand(Restaurant):
    def __init__(self,flavors:list, restaurant_name:str, cuisine_type:str, number_served:int=0)->None:
        Restaurant.__init__(self,restaurant_name,cuisine_type,number_served)
        self.flavors={"chocolate","vanilla","banana"}

    def flavors_display(self)->None:
        for i in self.flavors:
            print(i)

icecreamstand:IceCreamStand=IceCreamStand("","Name","Type")
icecreamstand.flavors_display()

# 9-7. Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5.
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method. 

class Admin(User):
    def __init__(self,privileges:list, first_name:str, last_name:str, age:int, date_birth:str, gender:str, login_attemps:int=0)->None:
        User.__init__(self,first_name,last_name,age,date_birth,gender,login_attemps)
        self.privileges=privileges

    def show_privileges(self):
        for i in self.privileges:
            print(i)

admin:Admin=Admin(["can add post","can delete post","can ban user"],"A","B",20,"22/09/04","male")
admin.show_privileges()

# 9-8. Privileges: Write a separate Privileges class.
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.


class Privileges:
    def __init__(self,privileges:list)->None:
        self.privileges=privileges
    def show_privileges(self):
        for i in self.privileges:
            print(i)


class Admin2(User):
    def __init__(self,privileges: Privileges, first_name:str, last_name:str, age:int, date_birth:str, gender:str, login_attemps:int=0)->None:
        User.__init__(self,first_name,last_name,age,date_birth,gender,login_attemps)
        self.privileges=privileges

    def show_privileges(self):
        self.privileges.show_privileges()

privileges:Privileges=Privileges(["can add post","can delete post","can ban user"])
admin2:Admin2=Admin2(privileges,"A","B",20,"22/09/04","male")
admin2.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 65 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once,
# and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant.
# Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

