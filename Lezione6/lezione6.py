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