import unittest
from persona import Persona
class  TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona=Persona("Nome","Cognome")
    
    