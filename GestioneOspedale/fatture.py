from dottore import Dottore
from paziente import Paziente
class Fattura(Dottore):
    def __init__(self,patient,doctor:Dottore):
        self.patient=[]
        self.doctor=doctor
        self.fatture=0
        self.salary=0
        if doctor.isAValidDoctor() is True:
            self.fatture=len(self.patient)
            self.salary=0
        else:
            self.patient=None
            self.doctor=None
            self.fatture=None
            self.salary=None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        return self.doctor.getParcel()*len(self.patient)
    
    def getFatture(self):
        return self.fatture
    
    def addPatient(self,newPatient):
        self.patient.append(newPatient)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del dottor {self.doctor.last_name} è stato aggiunto il paziente {newPatient.getIdCode()}")

    def removePatient(self,idCode):
        for i in self.patient:
            if idCode == i.getIdCode():
                self.patient.remove(i)
        self.getSalary()
        self.getFatture()
        print(f"Alla lista del dottor {self.doctor.last_name} è stato rimosse il paziente {idCode}")

    