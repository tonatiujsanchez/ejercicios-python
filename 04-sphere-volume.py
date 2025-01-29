# Escrubir una funcion que devuelva el volumen de una esfera por su radio
# formula: 4/3 * pi * r ** 3
from math import pi

def get_sphere_volume(ratio):
    volume = (4/3) * pi * (ratio ** 3)
    return round(volume, 2)

volume = get_sphere_volume(2)
print(volume)
