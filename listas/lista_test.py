from lista import Lista
from random import randint

#EJERCICIOS 6,7,15 y 22 pag 112
#EJERCICIO 2 Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
# lista_char = Lista()
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# vocales= ['a','e','i','o','u']
# for i in range(30):
#     a = randint(0,25)
#     lista_char.insertar(abc[a])

# lista_char.barrido()
# print(lista_char.tamanio())

# lista_char.barrido_eliminando(vocales)
          
# lista_char.barrido()
# print(lista_char.tamanio())

#EJERCICIO 3 Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos, una que contenga los números pares y otra para los números impares.

# lista_par = Lista()
# lista_inpar= Lista()
# lista_conjunta = Lista()

# for i in range(100):
#     lista_conjunta.insertar(randint(0,100))

# for i in range(lista_conjunta.tamanio()):
#     if lista_conjunta.obtener_elemento(i) % 2 == 0:
#         lista_par.insertar(lista_conjunta.obtener_elemento(i))
#     else:
#         lista_inpar.insertar(lista_conjunta.obtener_elemento(i))

# print('PAR')
# for i in range(lista_par.tamanio()):
#     print(lista_par.obtener_elemento(i))
# print('INPAR')
# for i in range(lista_inpar.tamanio()):
#     print(lista_inpar.obtener_elemento(i))

#EJERCICIO 4 Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

# lista = Lista()
# for i in range(100):
#     lista.insertar({'nro':i,'dato':''},'nro')
# dato = input('Escriba el dato que desea poner')
# pos = int(input('Coloque la posicion'))
# lista.modificar_elemento(pos,{'nro':pos,'dato':dato},'nro')
# print(lista.obtener_elemento(pos)) 

# EJERCICIO 6: Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

# lista_super_heroes = [{'name':'Iron Man','year':'1969','publisher':'Marvel','bio':'Tiene un re armadura'},
#                       {'name':'Wolverine','year':'1899','publisher':'Marvel','bio':'Tiene garras de fierro'},
#                       {'name':'Batamn','year':'1889','publisher':'DC','bio':'Usa traje, se le murieron los papas'},
#                       {'name':'Linterna verde','year':'1899','publisher':'DC','bio':'Le gusta volar, tiene el traje en un anillo'},
#                       {'name':'Flash','year':'1910','publisher':'DC','bio':'Le gusta correr,tambien tiene el traje en un anillo'},
#                       {'name':'Star-Lord','year':'1950','publisher':'Marvel','bio':'Tiene una rata como amigo'},
#                       {'name':'Mujer Maravilla','year':'1969','publisher':'DC','bio':'Vive en una isla'},
#                       {'name':'Capitana Marvel','year':'1980','publisher':'Marvel','bio':'Le robo el nombre a shazam'},
#                       {'name':'Shazam','year':'1901','publisher':'DC','bio':'Capitana marvel le robo el nombre'},
#                       {'name':'Dr Strange','year':'1912','publisher':'DC','bio':'Puede hacer portales, su capa tiene vida propia'},
#                       {'name':'Superman','year':'1839','publisher':'DC','bio':'Tambien se le murieron los papas... y su planeta'},]
# lista_pj = Lista()
# for pj in lista_super_heroes:
#     lista_pj.insertar(pj,'name')

# # a. eliminar el nodo que contiene la información de Linterna Verde;
# def eliminar_pj(lista,nombre_pj):
#     lista.eliminar(nombre_pj,'name')
#     print(nombre_pj,'eliminado')
# eliminar_pj(lista_pj,'Linterna verde')

# # b. mostrar el año de aparición de Wolverine;
# def mostrar_año(lista,nombre_pj):
#     pos = lista.busqueda(nombre_pj,'name')
#     print(lista.obtener_elemento(pos)['year'],'año de aparicion de',lista.obtener_elemento(pos)['name'])
# mostrar_año(lista_pj,'Wolverine')

# # c. cambiar la casa de Dr. Strange a Marvel;
# def cambiar_casa(lista,nombre_pj,casa):
#     pos = lista.busqueda(nombre_pj,'name')
#     pj = lista.obtener_elemento(pos)
#     casa_og = pj['publisher']
#     pj['publisher'] = casa
#     lista.modificar_elemento(pos,pj,'name')
#     print(lista.obtener_elemento(pos)['name'],'cambio de', casa_og, 'a',lista.obtener_elemento(pos)['publisher'])
# cambiar_casa(lista_pj,'Dr Strange','Marvel')

# # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# def mostrar_nombre_segun_fecha(lista,fecha_pj):
#     for i in range(lista.tamanio() - 1):
#         if int(lista.obtener_elemento(i)['year']) <= int(fecha_pj):
#             print(lista.obtener_elemento(i)['name'],lista.obtener_elemento(i)['publisher'])
# mostrar_nombre_segun_fecha(lista_pj,1963)

# # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# def mostrar_casa(lista,pj):
#     se_encuentra_algo = False
#     for i in range(lista.tamanio() - 1):
#         if (lista.obtener_elemento(i)['name'] == pj):
#             print(lista.obtener_elemento(i)['publisher'])
#             se_encuentra_algo = True
#     if not se_encuentra_algo:
#         print('No se a encontrado',pj)
# mostrar_casa(lista_pj,'Mujer Maravilla')
# mostrar_casa(lista_pj,'Capitana Marvel')

# # g. mostrar toda la información de Flash y Star-Lord;
# def mostrar_info(lista,pj):
#     se_encuentra_algo = False
#     for i in range( lista.tamanio() -1 ):
#        if (lista.obtener_elemento(i)['name'] == pj):
#            print(lista.obtener_elemento(i))
#            se_encuentra_algo = True
#     if not se_encuentra_algo:
#         print('No se a encontrado',pj)
# mostrar_info(lista_pj,"Flash")
# mostrar_info(lista_pj,"Star-Lord")

# # h. listar los superhéroes que comienzan con la letra B, M y S;
# def mostrar_por_primera_letra(lista,primera_letra):
#     for i in range(lista.tamanio() -1):
#         if lista.obtener_elemento(i)['name'][0] == primera_letra:
#             print(lista.obtener_elemento(i)['name'])
# mostrar_por_primera_letra(lista_pj,'B')
# mostrar_por_primera_letra(lista_pj,'M')
# mostrar_por_primera_letra(lista_pj,'S')

# # i. determinar cuántos superhéroes hay de cada casa de comic.
# def mostrar_por_casa(lista,casa):
#     for i in range(lista.tamanio() -1):
#         if lista.obtener_elemento(i)['publisher'] == casa:
#             print(lista.obtener_elemento(i)['name'])
# mostrar_por_casa(lista_pj,'DC')

# 7 Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

lista_1 = Lista()
lista_2 = Lista()
lista_aux = Lista()

def cargar_lista_ran(lista):
    for i in range(10):
        lista.insertar(randint(0,100))    
def print_lista(lista):
    for i in range(lista.tamanio()-1):
        print(lista.obtener_elemento(i))

cargar_lista_ran(lista_1)
cargar_lista_ran(lista_2)
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
def concatenar_lista(lista1,lista2,lista_aux):
    repetidos = 0
    for i in range(lista1.tamanio()-1):
        if lista2.busqueda(lista1.obtener_elemento(i)) != -1:
            repetidos += 1
        if lista_aux.busqueda(lista1.obtener_elemento(i)) == -1:
            lista_aux.insertar(lista1.obtener_elemento(i))
    for i in range(lista2.tamanio()-1):
        if lista2.busqueda(lista2.obtener_elemento(i)) == -1:
            lista_aux.insertar(lista2.obtener_elemento(i))
    print('Cantidad de repetidos', repetidos)

concatenar_lista(lista_1,lista_2,lista_aux)
print('Primera lista')
print_lista(lista_1)
print('Segunda lista')
print_lista(lista_2)
print('Tercera lista')
print_lista(lista_aux)

# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
def eliminar_lista(lista):
    for i in range(lista.tamanio()-1):
        print(lista.obtener_elemento(i))
        lista.eliminar(i)
print('Eliminar lista')
eliminar_lista(lista_aux)

# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;