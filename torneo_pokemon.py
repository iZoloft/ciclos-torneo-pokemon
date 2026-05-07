# Torneo Pokémon
# Objetivo
# Desarrollar un programa en Python que administre un pequeño torneo Pokémon utilizando:
# •	while 
# •	for in range 
# •	contadores 
# •	acumuladores 
# •	banderas 
# •	estructuras condicionales 
# •	validaciones 
# •	números aleatorios 
# ________________________________________
# Enunciado
# La Liga Pokémon organizará un torneo de combates entre entrenadores.
# Debes crear un programa que permita registrar varios combates y mostrar estadísticas finales del torneo.
# ________________________________________
# 🔹 Reglas del torneo
# El programa debe:
# 1.	Solicitar la cantidad de combates a realizar. 
# o	Debe ser mayor que 0. 
# 2.	Por cada combate (for in range):
# Solicitar:
# o	Nombre del entrenador 
# o	Tipo de Pokémon: 
# 	"F" → Fuego 
# 	"A" → Agua 
# 	"P" → Planta  
# 3.	Generar aleatoriamente un poder entre 1 y 20: 
# import random
# poder = random.randint(1,20)
# ________________________________________
# 🔹 Bonificaciones por tipo
# Según el tipo elegido:
# •	Fuego → +3 poder 
# •	Agua → +2 poder 
# •	Planta → +1 poder 
# ________________________________________
# 🔹 Resultado del combate
# Después de calcular el poder final:
# •	Poder ≥ 18 →  Victoria 
# •	Poder entre 10 y 17 →  Batalla difícil 
# •	Poder < 10 →  Derrota 
# ________________________________________
# 🔹 El programa debe utilizar
# Contadores
# Contar:
# •	Cantidad de victorias 
# •	Cantidad de derrotas 
# •	Cantidad de Pokémon de cada tipo 
# ________________________________________
# Acumuladores
# Acumular:
# •	Suma total de poderes finales 
# ________________________________________

# Bandera
# Usar una bandera para detectar:
# •	Si algún jugador obtuvo poder mayor o igual a 25 
# Al finalizar:
# •	Mostrar mensaje especial si ocurrió. 
# Ejemplo:
# "¡Hubo un Pokémon legendario en el torneo!"
# ________________________________________
# Al finalizar el torneo mostrar
# •	Total de combates 
# •	Cantidad de victorias 
# •	Cantidad de derrotas 
# •	Cantidad de Pokémon Fuego 
# •	Cantidad de Pokémon Agua 
# •	Cantidad de Pokémon Planta 
# •	Promedio de poder final 
# •	Mensaje especial si hubo Pokémon legendario 

import os, random

cantidad_combates = 0

try:
    while cantidad_combates <= 0: # En el while siempre ponemos lo que no queremos que pase, y esto se haga bucle
        cantidad_combates = int(input("Ingrese cantidad de combates \n"))
        if cantidad_combates <= 0:
            print("Debes ingresar un valor positivo") # Creamos este if para dar a saber el valor que va
    # Fuera del while, porque ya asumimos que el valor que viene esta correcto
    for x in range (cantidad_combates):
        nombre_entrendor = ""
        tipo_pokemon = ""
        while len(nombre_entrendor) < 3: #aqui entramos al while gracias a las variables vacias, que tienen valor 0
            nombre_entrendor = input("Ingrese nombre \n")
            if len(nombre_entrendor) < 3:
                print("El largo mínimo es de 3 caracteres")
        while len (tipo_pokemon) < 0 or (tipo_pokemon != 'a' and tipo_pokemon != 'f' and tipo_pokemon != 'p'):
            tipo_pokemon = input("Ingrese tipo pokemon \n").lower()
            if len(tipo_pokemon) < 0:
                print("Debes colocar un caracter")
            if len(tipo_pokemon) != 'a' and 
except:
    print("Debe ser un valor numérico")