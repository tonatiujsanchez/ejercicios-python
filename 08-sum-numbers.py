# Recibe una cantidad infinita de numeros hata recibir "basta",
# luego devolver la suma de todos los números ingresados

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def sum_numbers(num_list):
    result = 0
    for number in num_list:
        result = result + number
    return result


number_list=[]
def get_and_sum_numbers():
    value = input('Ingrese un número ')

    if( value != 'basta' and ( is_int(value) or is_float(value) )):
        if(is_int(value)):
            number_list.append( int(value) )
        else:
            number_list.append( float(value) )
           
        get_and_sum_numbers()
        
    return sum_numbers( number_list )
    

result = get_and_sum_numbers()
print( result )

# NOTA: La plicación tambien termina cuando se ingresa un valor que no es un numero
# NOTA 2: La plicación tambien acepta el ingreso de valores decimales