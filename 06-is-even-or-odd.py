# Escribir una función que evalue si un número es par o impar


def is_even_or_odd(number):
    if(number % 2 == 0):
        return f'{number} is even' #Es par
    else:
        return f'{number} is odd' #Es impar
    

result = is_even_or_odd(26)
print(result)
