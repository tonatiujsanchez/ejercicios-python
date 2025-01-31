# Escribe un programa que determine si una palabra o frase ingresada por el usuario
# es un palíndromo (se lee igual al derecho y al revés).

def is_palindrome():
    value = input('Ingrese una palabra: ')

    clean_value = ''
    for char in value:
        if char != ' ' :
            clean_value += char
    
    back_value = clean_value[::-1].lower()

    if back_value == clean_value.lower():
        print(f'"{ value }" SI es un palindromo')
    else: 
        print(f'"{ value }" NO es un palindromo')

is_palindrome()