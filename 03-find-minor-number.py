# Escribir una funcion que encuentre el elemento menor de una lista

elements = [5,6,4,5,8,9,1]

def find_minor_element(list):
    minor_element = list[0]
    
    for element in list:
        if( element < minor_element ):
            minor_element = element
    return minor_element
    

minor_element = find_minor_element(elements)
print(minor_element)
