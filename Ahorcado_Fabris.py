# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:40:41 2021

@author: Usuario
"""
# Proyecto El Ahorcado
# Germán Fabris

import math
import random
import re

# ================================================================

dibujos = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''','''
      +---+
      |   |
     >O   |
     /|\  |
     / \  |
          |
    =========''','''
      +---+
      |   |
    >>O   |
     /|\ |
     / \  |
          |
    =========''','''
      +---+
      |   |
   >>>O   |
     /|\ |
     / \  |
          |
    =========''','''
      +---+
      |   |
  >>>>O   |
     /|\ |
     / \  |
          |
    =========''','''
      +---+
      |   |
 >>>>>O   |
     /|\ |
     / \  |
          |
    =========''']
    
#========= Palabras    
leer_archiv = open ('palabras.txt', 'r')
with leer_archiv:
    contenido = leer_archiv.readlines()
    contenido = "".join(contenido)
    for linea in contenido:
        contenido = contenido.lower()
    contenido = contenido.split()
    for i in contenido:
        if i != "abcdefghijklmnopqrstuvwxyz":
            contenido.remove(i)
palabras = contenido

#======== Palabra aleatoria
def buscarPalabraAleat(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

#======= Juego    

def base(dibujos, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(dibujos[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): 
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
 

def elijeLetra(algunaLetra):
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra, prueba otra')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
 
def empezar():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')
 
    
print (' EL JUEGO DEL AHORCADO')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = buscarPalabraAleat(palabras)
finJuego = False
while True:
    base(dibujos, letraIncorrecta, letraCorrecta, palabraSecreta)
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        if len(letraIncorrecta) == len(dibujos) - 1:
            base(dibujos, letraIncorrecta, letraCorrecta, palabraSecreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erroneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
            finJuego = True
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = buscarPalabraAleat(palabras)
        else:
            print('''El juego ha finalizado
Muchas gracias por haber participado''')
            break