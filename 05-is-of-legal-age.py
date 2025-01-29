# Escribir una función que evalue si el usuario es mayor de edad

def is_of_legal_age(age):
    if(age >= 18):
        return True
    else:
        return False 

user_is_of_legal_age = is_of_legal_age(30)
print(user_is_of_legal_age)
