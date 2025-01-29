# Ingresar nombre y apellido e imprimirlo al reves

def change_name(name):
    i=len(name)-1
    name_backwards=''
    while( i >= 0  ):
        name_backwards += name[i] 
        i-=1
    return name_backwards


name = change_name('Tonatiuj Sánchez')
print(name)