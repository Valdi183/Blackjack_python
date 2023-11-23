"""
Dedicado al corrector Luis/Rubén:
Este juego no es un blackjack realmente, ya que no simula una partida de esta,
sino que es una implementación de un juego de cartas, que trata de imitar un blackjack.
Aún así, he implementado algunas funciones, como elegir dos cartas al azar para el jugador,
o un mensaje de si has ganado o perdido...
"""
from random import sample
"""Esto importa una función (sample) dentro del módulo random,
que es una función que permite generar una muestra de un conjunto de valores.
(La utilizaré para que el juego se asemeje más a un black jack)
"""

#Empiezo definiendo con un diccionario todas las cartas del juego y sus respectivos valores

cartas = {     
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
}
"""
La función obtener_valor_carta calcula la puntuación total de un conjunto de carta,
se busca cada carta en el diccionario cartas, y sus valores se suman para obtener
el valor total. (La función la invocaré más tarde)
"""
def obtener_valor_carta(cartas_jugador):
    return sum(cartas[carta] for carta in cartas_jugador)

"""
A continuación, con estos prints, se muestra en pantalla todas las cartas y sus puntos.
Con el primero las cartas (el .join une todas las claves en una cadena de caracteres, separados
por espacios). en el segundo, se muestra la puntuación, combirtiendo los valores de las cartas en una lista
"""
print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))
"""
Este bucle for simplemente, "recorre" todo el diccionario, y muestra en pantalla la carta y su valor
para cada carta de este diccionario
"""
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

"""
Aquí entra en juego la función sample, que basicamente escogerá cartas aleatoriamente (2 en este caso
como en el blacjack ) Para el jugador.Y para la puntuación, entra en juego la función definida anteriormente. 
Los prinst posteriores muestran las cartas asignadas y la puntuacón del jugador
"""

main_jugador = sample(list(cartas), 2)
score_jugador = obtener_valor_carta(main_jugador)

print("Ha seleccionado:", end=" ")
for carta in main_jugador:
    print(carta, end=" ")
print(" >> su score es", score_jugador)

#Esta parte del código Hace lo mismo que la anterior pero para el crupier

main_crupier = sample(list(cartas), 2)
score_crupier = obtener_valor_carta(main_crupier)

print("La banca tiene:", end=" ")
for carta in main_crupier:
    print(carta, end=" ")
print("  >> su score es {}".format(score_crupier))

#Muestra el ganador en función de la puntuación
if score_crupier > score_jugador:
    print("Has perdido, buena suerte la próxima vez!")
if score_crupier < score_jugador:
    print("Has ganado!")   
