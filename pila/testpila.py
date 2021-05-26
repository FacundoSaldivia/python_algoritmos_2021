from pila import Pila
from random import randint

#PAGINA 83, ej 14 16 22 y 24

#14 Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra no se pueden utilizar métodos de ordenamiento–.

# pila = Pila()
# pila_aux = Pila()
# elemntos_a_ingresar = [2,3,1,6,21,3,0]

# for number in elemntos_a_ingresar:
#     if pila.pila_vacia() == True:
#         pila.apilar(number)
#     else:
#         x = pila.elemento_cima() > number
#         while x:
#             pila_aux.apilar(pila.desapilar())
#             if (pila.pila_vacia()):
#                 x = False
#             elif (pila.elemento_cima() < number):
#                 x = False
#         pila.apilar(number)
#         x = True
#         while not pila_aux.pila_vacia():
#             pila.apilar(pila_aux.desapilar())
# x = pila.tamanio()
# for i in range(x):
#     print(pila.desapilar())

#16 Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

# pila_pj_sw_V = Pila()
# pila_pj_sw_VII = Pila()
# pila_aux_II = Pila()

# lista_de_personajes_VII = ['Kylo Ren','Rey','Finn','Han Solo','Chewbacca','Poe Dameron','Leia Organa','	Maz Kanata','General Armitage Hux','C3PO','Snoke','Luke Skywalker']

# lista_de_personajes_V = ['Luke Skywalker','Han Solo','Darth Vader','Leia Organa','Obi-Wan','C3PO','Yoda','Boba Fett']

# for personaje in lista_de_personajes_V:
#     pila_pj_sw_V.apilar(personaje)

# for personaje in lista_de_personajes_VII:
#     pila_pj_sw_VII.apilar(personaje)

# while(not pila_pj_sw_VII.pila_vacia()):
#     personaje_1 = pila_pj_sw_VII.desapilar()
#     while(not pila_pj_sw_V.pila_vacia()):
#         personaje_2 = pila_pj_sw_V.desapilar()
#         if (personaje_1 == personaje_2):
#             print(personaje_1, 'Aparece en ambas peliculas')
#         else:
#             pila_aux_II.apilar(personaje_2)
    
#     while(not pila_aux_II.pila_vacia()):
#         pila_pj_sw_V.apilar(pila_aux_II.desapilar())


#22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó, costo de la recompensa. Resolver las siguientes actividades: 
# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;

# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;

# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;

# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

# pila_r_boba = Pila()
# pila_r_din = Pila()
# pila_aux = Pila()
# boba = [{"planeta":"Eadu","rehen":"Juan Solo","recompensa":69,},{"planeta":"Endor","rehen":"Gaston","recompensa":299,},{"planeta":"Exegol","rehen":"Joaquin","recompensa":420,},{"planeta":"Eadu","rehen":"Han Solo","recompensa":63,},{"planeta":"Exegol","rehen":"Fionna","recompensa":99,}]

# din = [{"planeta":"Tierra","rehen":"Macri","recompensa":100},{"planeta":"Endor","rehen":"Alibaba","recompensa":22},{"planeta":"Marte","rehen":"Elon Musk","recompensa":200},{"planeta":"Krypton","rehen":"Jor-El","recompensa":1}]

# def cargar_pila(pila,lista):
#     for dic in lista:
#         pila.apilar(dic)
# cargar_pila(pila_r_boba,boba)
# cargar_pila(pila_r_din,din)


# def a_planetas_visitados(pila,pilaAux):
#     print("PLANETAS VISITADOS SEGUN ORDEN")
#     while(not pila.pila_vacia()):
#         pilaAux.apilar(pila.desapilar())
#     while(not pilaAux.pila_vacia()):
#         pj = pilaAux.desapilar()
#         print(pj["planeta"])
#         pila.apilar(pj)
        
# a_planetas_visitados(pila_r_boba,pila_aux)
# a_planetas_visitados(pila_r_din,pila_aux)

# def b_creditos(pila,pilaAux):
#     contador = 0
#     while(not pila.pila_vacia()):
#         pilaAux.apilar(pila.desapilar())
#     while(not pilaAux.pila_vacia()):
#         pj = pilaAux.desapilar()
#         contador += pj["recompensa"]
#         pila.apilar(pj)
#     return "Recompensa total:", contador

# print(b_creditos(pila_r_din,pila_aux))
# print(b_creditos(pila_r_boba,pila_aux))

# def c_d(pila,pilaAux):
#     contador = 0
#     while(not pila.pila_vacia()):
#         pilaAux.apilar(pila.desapilar())
#     while(not pilaAux.pila_vacia()):
#         contador += 1
#         pj = pilaAux.desapilar()
#         if pj["rehen"] == "Han Solo":
#             print(pj["rehen"],' fue capturado en la mision nro:',contador)
#         pila.apilar(pj)
#     return 'cant de misiones',contador

# print(c_d(pila_r_boba,pila_aux))
# print(c_d(pila_r_din,pila_aux))
#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

# pj_marvel = [{'name':'Iron Man','nro_de_pelis':10},{'name':'Capitan America','nro_de_pelis':10},{'name':'Thor','nro_de_pelis':8},{'name':'Spiderman','nro_de_pelis':5},{'name':'Nick Fury','nro_de_pelis':11},{'name':'Scarlet Witch','nro_de_pelis':4},{'name':'Rocket Raccoon','nro_de_pelis':4},{'name':'Loki','nro_de_pelis':5},{'name':'Groot','nro_de_pelis':4},{'name':'Hulk','nro_de_pelis':7},{'name':'Black Widow','nro_de_pelis':8}]

# pila_pj_marvel = Pila()
# pila_Aux = Pila()
# #Funciones
# def llenar_pila(lista,pila):
#     for personaje in lista:
#         pila.apilar(personaje)
# def pos_RR_G(pila,pilaAux):
#     contador = 0
#     while(not pila.pila_vacia()):
#         pj = pila.desapilar()
#         if pj['name'] == 'Groot':
#             pos_G = contador
#         elif pj['name'] == 'Rocket Raccoon':
#             pos_RR = contador
#         contador += 1 
#         pilaAux.apilar(pj)
#     while(not pilaAux.pila_vacia()):
#         pila.apilar(pilaAux.desapilar())
#     return ('groot y rocket raccon :',pos_G,pos_RR)

# def pj_con_5_o_mas_participaciones(pila,pilaAux):
#     lista_pj = []
#     while(not pila.pila_vacia()):
#         pj = pila.desapilar()
#         if pj['nro_de_pelis'] > 4:
#             lista_pj.append(pj)
#         pilaAux.apilar(pj)
#     while(not pilaAux.pila_vacia()):
#         pila.apilar(pilaAux.desapilar())
#     return(lista_pj)

# def black_widow(pila,pilaAux):
#     while(not pila.pila_vacia()):
#         pj = pila.desapilar()
#         if pj['name'] == 'Black Widow':
#             natasha = pj
#         pilaAux.apilar(pj)
#     while(not pilaAux.pila_vacia()):
#         pila.apilar(pilaAux.desapilar())
#     return natasha['name'],'Particio en',natasha['nro_de_pelis'],' peliculas'
# def C_D_G(pila,pilaAux):
#     while (not pila.pila_vacia()):
#         pj = pila.desapilar()
#         if pj['name'][0] == 'C' or pj['name'][0] == 'D' or pj['name'][0] == 'G':
#             print(pj['name'])
#         pilaAux.apilar(pj)
#     while(not pilaAux.pila_vacia()):
#         pila.apilar(pilaAux.desapilar())
    
# llenar_pila(pj_marvel,pila_pj_marvel)
# print(pos_RR_G(pila_pj_marvel,pila_Aux))
# pjs = pj_con_5_o_mas_participaciones( pila_pj_marvel,pila_Aux)
# for pj in pjs:
#     print(pj['name'],'nro de peliculas:',pj['nro_de_pelis'])
# print(black_widow(pila_pj_marvel, pila_Aux))
# C_D_G(pila_pj_marvel, pila_Aux)
