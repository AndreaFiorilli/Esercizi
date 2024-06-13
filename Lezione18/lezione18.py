import math
def safe_sqrt(number):
    try:
        return math.sqrt(number)
    except:
        print("Error: number is less than 0")
        return number

print(safe_sqrt(-9))

class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    b=["!","*","_","-","?",",",".","#"]
    conta=0
    conta1=0
    for i in password:
        if i in a:
            conta +=1
        if i in b:
            conta1 +=1
    if len(password)<20:
            raise InvalidPasswordError("Password is too short")
    elif conta<3:
            raise InvalidPasswordError("Password hasn't enough uppercase characters")
    elif conta1<4:
            raise InvalidPasswordError("Password hasn't enough special characters")

    try:
        return "Password si valid"
    except InvalidPasswordError as error:
        return error
        
print(validate_password("AndreaFiorilli!!!2004Daje"))
    