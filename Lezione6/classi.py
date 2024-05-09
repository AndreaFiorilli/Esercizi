class Person:
    def __init__(self, name:str, surname:str, birth_date:str, birth_place:str, gender:str) -> None:
        """

        """
        self._name:str=name
        self._surname:str=surname
        self._birth_date:str=birth_date
        self._birth_place:str=birth_place
        self._gender:str=gender
        self._ssn:str=None
        self.compute_ssn()

    def get_ssn(self)->str:
        """
        This function returns the ssn value
        input: none
        return: self._ssn: str, the function returns the ssn
        """
        return self._ssn
    
    def set_ssn(self,ssn:str)->None:
        """
        This function set the attribute ssn
        input: ssn: str, the parameter contains the ssn value
        return: None
        """
        self._ssn=ssn

    def get_name(self):
        """
        This function returns a person's name
        input: none
        return: self._name: str, the function returns the person's name
        """
        return self._name
    
    def set_name(self,name:str)->None:
        """
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        return: None
        """
        self._name=name
        self._ssn=self.compute_ssn()
    
    def compute_ssn(self)->bool:
        """
        Check the ssn's correctness
        """
        vocali="a e i o u A E I O U"
        codCat=""
        conta=0
        numDis=0
        conta1=0
        numPar=0
        for x in range(len(vocali)):
            self._name = self._name.replace(vocali[x], "")
            self._surname = self._surname.replace(vocali[x], "")
        month=self._birth_date[3:5]
        if month=="01":
            month="A"
        elif month=="02":
            month="B"
        elif month=="03":
            month="C"
        elif month=="04":
            month="D"
        elif month=="05":
            month="E"
        elif month=="06":
            month="H"
        elif month=="07":
            month="L"
        elif month=="08":
            month="M"
        elif month=="09":
            month="P"
        elif month=="10":
            month="R"
        elif month=="11":
            month="S"
        elif month=="12":
            month="T"

        if self._birth_place=="Aosta":
            codCat="A326"
        elif self._birth_place=="Torino":
            codCat="L219"
        elif self._birth_place=="Genova":
            codCat="D969"
        elif self._birth_place=="Mlano":
            codCat="F205"
        elif self._birth_place=="Trento":
            codCat="L378"
        elif self._birth_place=="Bolzano":
            codCat="A952"
        elif self._birth_place=="Venezia":
            codCat="L736"
        elif self._birth_place=="Trieste":
            codCat="L424"
        elif self._birth_place=="Bologna":
            codCat="A944"
        elif self._birth_place=="Firenze":
            codCat="D612"
        elif self._birth_place=="Perugia":
            codCat="G478"
        elif self._birth_place=="Ancona":
            codCat="A271"
        elif self._birth_place=="Roma":
            codCat="H501"
        elif self._birth_place=="L'Aquila":
            codCat="A345"
        elif self._birth_place=="Campobasso":
            codCat="B519"
        elif self._birth_place=="Napoli":
            codCat="F839"
        elif self._birth_place=="Bari":
            codCat="A662"
        elif self._birth_place=="Potenza":
            codCat="G942"
        elif self._birth_place=="Catanzaro":
            codCat="C352"
        elif self._birth_place=="Palermo":
            codCat="G273"
        elif self._birth_place=="Cagliari":
            codCat="B354"
        year=self._birth_date[-2:]
        day=self._birth_date[:2]
        first_three_name_char=self._name[-3:]
        last_three_surname_char=self._surname[:3]
        self._ssn1= last_three_surname_char.upper()+first_three_name_char.upper()+year+month+day+codCat
        for p in self._ssn1[0:15:2]:
            if p=="0":
                conta=1
            elif p=="1":
                conta=0
            elif p=="2":
                conta=5
            elif p=="3":
                conta=7
            elif p=="4":
                conta=9
            elif p=="5":
                conta=13
            elif p=="6":
                conta=15
            elif p=="7":
                conta=17
            elif p=="8":
                conta=19
            elif p=="9":
                conta=21
            elif p=="A":
                conta=1
            elif p=="B":
                conta=0
            elif p=="C":
                conta=5
            elif p=="D":
                conta=7
            elif p=="E":
                conta=9
            elif p=="F":
                conta=13
            elif p=="G":
                conta=15
            elif p=="H":
                conta=17
            elif p=="I":
                conta=19
            elif p=="J":
                conta=21
            elif p=="K":
                conta=2
            elif p=="L":
                conta=4
            elif p=="M":
                conta=18
            elif p=="N":
                conta=20
            elif p=="O":
                conta=11
            elif p=="P":
                conta=3
            elif p=="Q":
                conta=6
            elif p=="R":
                conta=8
            elif p=="S":
                conta=12
            elif p=="T":
                conta=14
            elif p=="U":
                conta=16
            elif p=="V":
                conta=10
            elif p=="w":
                conta=22
            elif p=="X":
                conta=25
            elif p=="Y":
                conta=24
            elif p=="Z":
                conta=23
            numDis=numDis+conta
        for p in self._ssn1[1:15:2]:
            if p=="0":
                conta1=0
            elif p=="1":
                conta1=2
            elif p=="2":
                conta1=2
            elif p=="3":
                conta1=3
            elif p=="4":
                conta1=4
            elif p=="5":
                conta1=5
            elif p=="6":
                conta1=6
            elif p=="7":
                conta1=7
            elif p=="8":
                conta1=18
            elif p=="9":
                conta1=9
            elif p=="A":
                conta1=0
            elif p=="B":
                conta1=1
            elif p=="C":
                conta1=2
            elif p=="D":
                conta1=3
            elif p=="E":
                conta1=4
            elif p=="F":
                conta1=5
            elif p=="G":
                conta1=6
            elif p=="H":
                conta1=7
            elif p=="I":
                conta1=8
            elif p=="J":
                conta1=9
            elif p=="K":
                conta1=10
            elif p=="L":
                conta1=11
            elif p=="M":
                conta1=12
            elif p=="N":
                conta1=13
            elif p=="O":
                conta1=14
            elif p=="P":
                conta1=15
            elif p=="Q":
                conta1=16
            elif p=="R":
                conta1=17
            elif p=="S":
                conta1=18
            elif p=="T":
                conta1=19
            elif p=="U":
                conta1=20
            elif p=="V":
                conta1=21
            elif p=="w":
                conta1=22
            elif p=="X":
                conta1=23
            elif p=="Y":
                conta1=24
            elif p=="Z":
                conta1=25
            numPar=numPar+conta1
        num=(numDis+numPar)%26
        if num==0:
            codContr="A"   
        elif num==1:
            codContr="B"
        elif num==2:
            codContr="C"
        elif num==3:
            codContr="D"
        elif num==4:
            codContr="E"
        elif num==5:
            codContr="F"
        elif num==6:
            codContr="G"
        elif num==7:
            codContr="H"
        elif num==8:
            codContr="I"
        elif num==9:
            codContr="J"
        elif num==10:
            codContr="K"
        elif num==11:
            codContr="L"
        elif num==12:
            codContr="M"
        elif num==13:
            codContr="N"
        elif num==14:
            codContr="O"
        elif num==15:
            codContr="P"
        elif num==16:
            codContr="Q"
        elif num==17:
            codContr="R"
        elif num==18:
            codContr="S"
        elif num==19:
            codContr="T"
        elif num==20:
            codContr="U"
        elif num==21:
            codContr="V"
        elif num==22:
            codContr="W"
        elif num==23:
            codContr="X"
        elif num==24:
            codContr="Y"
        elif num==25:
            codContr="Z"
        self._ssn=self._ssn1+codContr
        
    def __str__(self)->str:
        return f"name: {self._name} surname: {self._surname} ssn: {self._ssn}"
    
persona_1:Person=Person(name="Andrea",surname="Fiorilli",birth_date="03/05/2004",birth_place="Roma",gender="male")
#persona_2:Person=Person(name="Valentino", surname="Rossi")

#print(str(persona_1))
#print(str(persona_2))

print(persona_1.get_ssn())
#persona_1.set_ssn(ssn="RTFGHY")
#print(persona_1.get_ssn())

#queue: list[Person]=[persona_1,persona_2]

#for person in queue:
#    print(person.get_ssn())


