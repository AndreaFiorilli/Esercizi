# Fiorilli Andrea
# 16/05/2024

#ES1. Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). 
# The numbers should be stored in a list and returned as output.

def Es1()->list:
    num: list = [lista for lista in range(2000,3201)]
    num1:list=[]
    for a in num:
        if a%7 == 0:
            if a%5 != 0:
                num1.append(a)
    return num1

print(Es1())

#ES2. Write a function to calculate the factorial of a number given as input. The number should be returned as output. 
# For example:
#    Input: 8
#    Output: 40320

def Es2(n: int)->int:
    f=1
    for i in range(n, 0, -1):
        f=f*i
    return f
n=8
print(Es2(n))

#ES3. Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. 
#The list is given as input to the function. All factorials should be returned as output.
# For example:
#    Input: [2, 5, 8, 10]
#    Output: [2, 120, 40320, 3628800]

def Es3()->list:
    a=input("Inserisci il numero di elementi: ")
    i=int(a)
    b=0
    lista:list=[]
    lista2:list=[]
    while b!=i:
        b=b+1
        c=input(f"Inserisci il {b}° numero: ")
        num=int(c)
        lista.append(num)
    for z in lista:
        f=1
        lista1:list = [lista1 for lista1 in range(1,z+1)]
        for j in lista1:
            f=f*j
        lista2.append(f)
    return lista2
print(Es3())

#ES4. Given an integer n as input, write a function to generate a dictionary that contains (i, i*i)
# as (key, value) pairs such that i is an integer between 1 and n (both included). 
# The function should return the dictionary as output. 
# For example:
#    Input: 8
#    Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def Es4(n:int)->dict:
    a:dict={}
    b=0
    i=1
    for i in range(1, n+1):
        b=i*i
        a[i]=b
    return a
n=8
print(Es4(n))

#ES5. Write a function that accepts a string with a comma-separated sequence of words as input and 
# prints the words as a comma-separated sequence after sorting them alphabetically.
# For example:
#    Input: without,hello,bag,world
#    Output: bag,hello,without,world

def Es5()->str:
    string:str=("without,hello,bag,world")
    a=string.replace(","," ")
    string1=a.split()
    lista=list(string1)
    lista.sort()
    delim=","
    frase=delim.join(lista)
    return frase
print(Es5())

#ES6. Write a function that accepts a list of sentences (string) as input and 
# returns each line as output after capitalising all sentence characters. For example:
#    Input: Practice makes perfect
#    Output: PRACTICE MAKES PERFECT
def Es6()->str:
    string:str=("Practice makes perfect")
    return string.upper()
print(Es6())





def transform(x: int) -> int:
    if x%2==0:
        return x/2
    else:
        return (x*3)-1
    

def calcola_stipendio(ore_lavorate: int) -> float:
    ore_extra=0
    ore_standard=0
    if ore_lavorate <= 40:
        return ore_lavorate*10
    else:
        ore_extra=ore_lavorate-40
        ore_standard=ore_lavorate-ore_extra
        return ore_extra*(10*1.50)+ore_standard*10


def print_seq(): 
    
    print("Sequenza a):")
    lista=[1,2,3,4,5,6,7]
    for a in lista:
        print(a)
    print()

    print("Sequenza b):")
    lista=[3, 8, 13, 18, 23]
    for a in lista:
        print(a)
    print()

    print("Sequenza c):")
    lista=[20, 14, 8, 2, -4, -10]
    for a in lista:
        print(a)
    print()
    
    print("Sequenza d):")
    lista=[19, 27, 35, 43, 51]
    for a in lista:
        print(a)


def integerPower(base:int,esponente:int)->int:
    if esponente > 0:
        return base**esponente
    

def hypotenuse(cateto1:float,cateto2:float)->float:
    ipotenusa=0.0
    ipotenusa=cateto1**2+cateto2**2
    return ipotenusa**(1/2)


def check_parentheses(expression: str) -> bool:
    conta=0
    for i in expression:
        if i== '(':
            conta=conta+1
        else:
            conta=conta-1
            if conta<0:
                break

    if conta==0:
        return True
    else:
        return False
    





	

