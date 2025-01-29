# Multiplicar dos números sin usar el símbolo de multiplicación

def multiply_two_numbers(num1:int, num2:int):
    result = 0
    i =1
    while i <= num1:
        result+= num2
        i += 1 
    return result

num1 = 7
num2 = 3


result = multiply_two_numbers(num1, num2)
print(result)


