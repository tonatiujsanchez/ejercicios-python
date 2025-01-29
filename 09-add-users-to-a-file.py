# Escribir una función que reciba nombre y apellido de usuarios y los vaya agregando a un archivo

def add_new_user():
    first_name = input('Ingrese el nombre: ')
    last_name = input('Ingrese el apellido: ')
    full_name = f'\n{first_name} {last_name}'
    
    c = open('09-user-list.txt', 'a')
    c.write(full_name)
    c.close()

    print('Usuario agregado correctamente')
    countinue = input('¿Agregar otro usuario? (si/no) ')

    if(countinue == 'si'):
        add_new_user()

    c = open('09-user-list.txt')
    print(c.read())

add_new_user()
    