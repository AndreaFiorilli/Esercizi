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
        first_three_name_char=self._name[:3]
        last_three_surname_char=self._surname[-3:]
        self._ssn= first_three_name_char+last_three_surname_char

    def __str__(self)->str:
        return f"name: {self._name} surname: {self._surname} ssn: {self._ssn}"
    
persona_1:Person=Person(name="Andrea",surname="Fiorilli",birth_date="03/05/2004",birth_place="Rome",gender="male")
#persona_2:Person=Person(name="Valentino", surname="Rossi")

#print(str(persona_1))
#print(str(persona_2))

print(persona_1.get_ssn())
#persona_1.set_ssn(ssn="RTFGHY")
#print(persona_1.get_ssn())

#queue: list[Person]=[persona_1,persona_2]

#for person in queue:
#    print(person.get_ssn())


