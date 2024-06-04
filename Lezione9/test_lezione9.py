import unittest
from lezione9 import anagram
class  Test_lezione9(unittest.TestCase):
    def test_anagram(self):
        reader = open ('Lezione9/test.txt')
        s=reader.readline()
        t=reader.readline()
        reader.close()
        self.assertTrue(anagram(s,t))

if __name__=="__main__":
    unittest.main()