class Persona:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        if not isinstance(self.first_name,str):
            self.first_name=None
            print("Il nome inserito non è una stringa!")
        if not isinstance(self.last_name,str):
            self.last_name=None
            print("Il cognome inserito non è una stringa!")
        if self.first_name and self.last_name:
            self.age=0
        else:
            self.age=None

    def setName(self,first_name):
        if isinstance(self.first_name,str):
            self.first_name=first_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self,last_name):
        if isinstance(self.last_name,str):
            self.last_name=last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self,age):
        if isinstance(self.age,int):
            self.age=age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name
    
    def getAge(self):
        return self.age
    
    def greet(self):
        print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni")
