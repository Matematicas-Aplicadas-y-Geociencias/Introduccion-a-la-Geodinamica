print('¡Hola, mundo!')
mi_nombre = input('¿Cuál es tu nombre?: ')                 # Pregunta por tu nombre
print('Me da mucho gusto conocerte, ' + mi_nombre)
print('La longitud de tu nombre es: ', end = '')
print(len(mi_nombre))
mi_edad = input('¿Cuál es tu edad?: ')                                        # Pregunta por tu edad
print('Tu edad dentro de un año será de: ' + str(int(mi_edad) + 1) + ' años.')