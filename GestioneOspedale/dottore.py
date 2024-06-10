from persona import Persona
class Dottore(Persona):
    def __init__(self,first_name,last_name,specialization,parcel):
        Persona.__init__(self,first_name,last_name)
        self.specialization=specialization
        self.parcel=parcel
        if not isinstance(self.specialization,str):
            self.specialization=None
            print("La specializzazione iniserita non è una stringa!")
        if not isinstance(self.parcel,float):
            self.parcel=None
            print("La parcella inserita non è un float!")
    
    def setSpecialization(self,specialization):
        if isinstance(self.specialization,str):
            self.specialization=specialization
        else:
            print("La specializzazione iniserita non è una stringa!")

    def setParcel(self,parcel):
        if isinstance(self.parcel,str):
            self.parcel=parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self):
        if self.age>30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
            return True
        else:
            print(f"Doctor {self.first_name} {self.last_name} isn't valid!")
            return False

    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.specialization}")
