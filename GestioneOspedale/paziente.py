from persona import Persona
class Paziente(Persona):
    def __init__(self,first_name,last_name,idCode):
        Persona.__init__(self,first_name,last_name)
        self.idCode=idCode
    
    def setIdCode(self,idCode):
        self.idCode=idCode

    def getIdCode(self):
        return self.idCode
    
    def patientInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name} \nID: {self.idCode}")
        