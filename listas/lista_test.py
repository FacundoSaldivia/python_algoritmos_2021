from lista import Lista
from random import randint
'''

#EJERCICIOS 6,7,15 y 22 pag 112

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

lista_super_heroes = [{'name':'Iron Man','year':'1969','publisher':'Marvel','bio':'Tiene un re armadura'},
                      {'name':'Wolverine','year':'1899','publisher':'Marvel','bio':'Tiene garras de fierro'},
                      {'name':'Batamn','year':'1889','publisher':'DC','bio':'Usa traje, se le murieron los papas'},
                      {'name':'Linterna verde','year':'1899','publisher':'DC','bio':'Le gusta volar, tiene el traje en un anillo'},
                      {'name':'Flash','year':'1910','publisher':'DC','bio':'Le gusta correr,tambien tiene el traje en un anillo'},
                      {'name':'Star-Lord','year':'1950','publisher':'Marvel','bio':'Tiene una rata como amigo'},
                      {'name':'Mujer Maravilla','year':'1969','publisher':'DC','bio':'Vive en una isla'},
                      {'name':'Capitana Marvel','year':'1980','publisher':'Marvel','bio':'Le robo el nombre a shazam'},
                      {'name':'Shazam','year':'1901','publisher':'DC','bio':'Capitana marvel le robo el nombre'},
                      {'name':'Dr Strange','year':'1912','publisher':'DC','bio':'Puede hacer portales, su capa tiene vida propia'},
                      {'name':'Superman','year':'1839','publisher':'DC','bio':'Tambien se le murieron los papas... y su planeta'},]
lista_pj = Lista()
for pj in lista_super_heroes:
    lista_pj.insertar(pj,'name')

# a. eliminar el nodo que contiene la información de Linterna Verde;
def eliminar_pj(lista,nombre_pj):
    lista.eliminar(nombre_pj,'name')
    print(nombre_pj,'eliminado')
eliminar_pj(lista_pj,'Linterna verde')

# b. mostrar el año de aparición de Wolverine;
def mostrar_año(lista,nombre_pj):
    pos = lista.busqueda(nombre_pj,'name')
    print(lista.obtener_elemento(pos)['year'],'año de aparicion de',lista.obtener_elemento(pos)['name'])
mostrar_año(lista_pj,'Wolverine')

# c. cambiar la casa de Dr. Strange a Marvel;
def cambiar_casa(lista,nombre_pj,casa):
    pos = lista.busqueda(nombre_pj,'name')
    pj = lista.obtener_elemento(pos)
    casa_og = pj['publisher']
    pj['publisher'] = casa
    lista.modificar_elemento(pos,pj,'name')
    print(lista.obtener_elemento(pos)['name'],'cambio de', casa_og, 'a',lista.obtener_elemento(pos)['publisher'])
cambiar_casa(lista_pj,'Dr Strange','Marvel')

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
def mostrar_nombre_segun_fecha(lista,fecha_pj):
    for i in range(lista.tamanio() - 1):
        if int(lista.obtener_elemento(i)['year']) <= int(fecha_pj):
            print(lista.obtener_elemento(i)['name'],lista.obtener_elemento(i)['publisher'])
mostrar_nombre_segun_fecha(lista_pj,1963)

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
def mostrar_casa(lista,pj):
    se_encuentra_algo = False
    for i in range(lista.tamanio() - 1):
        if (lista.obtener_elemento(i)['name'] == pj):
            print(lista.obtener_elemento(i)['publisher'])
            se_encuentra_algo = True
    if not se_encuentra_algo:
        print('No se a encontrado',pj)
mostrar_casa(lista_pj,'Mujer Maravilla')
mostrar_casa(lista_pj,'Capitana Marvel')

# g. mostrar toda la información de Flash y Star-Lord;
def mostrar_info(lista,pj):
    se_encuentra_algo = False
    for i in range( lista.tamanio() -1 ):
       if (lista.obtener_elemento(i)['name'] == pj):
           print(lista.obtener_elemento(i))
           se_encuentra_algo = True
    if not se_encuentra_algo:
        print('No se a encontrado',pj)
mostrar_info(lista_pj,"Flash")
mostrar_info(lista_pj,"Star-Lord")

# h. listar los superhéroes que comienzan con la letra B, M y S;
def mostrar_por_primera_letra(lista,primera_letra):
    for i in range(lista.tamanio() -1):
        if lista.obtener_elemento(i)['name'][0] == primera_letra:
            print(lista.obtener_elemento(i)['name'])
mostrar_por_primera_letra(lista_pj,'B')
mostrar_por_primera_letra(lista_pj,'M')
mostrar_por_primera_letra(lista_pj,'S')

# i. determinar cuántos superhéroes hay de cada casa de comic.
def mostrar_por_casa(lista,casa):
    for i in range(lista.tamanio() -1):
        if lista.obtener_elemento(i)['publisher'] == casa:
            print(lista.obtener_elemento(i)['name'])
mostrar_por_casa(lista_pj,'DC')

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

lista_entrenadores = Lista()


entrenadores = [
     {'name':'juan','torneos_ganados': 12, 'batallas_perdidas' : 5, 'batallas_ganadas': 32, 'pokemons': Lista()},
     {'name':'enzo','torneos_ganados': 2, 'batallas_perdidas' : 8, 'batallas_ganadas': 20, 'pokemons': Lista()},
     {'name':'maria','torneos_ganados': 4, 'batallas_perdidas' : 15, 'batallas_ganadas': 28, 'pokemons': Lista()},
]

pokemons = [{'name':'tyrantrum', 'nivel': 12 ,'tipo':'fuego', 'subtipo':'planta', 'entrenador': 'juan' },
            {'name':'wingull', 'nivel': 180 ,'tipo':'agua','subtipo':'volador', 'entrenador': 'juan'},
            {'name':'wolverine', 'nivel':3  ,'tipo':'fuego'  ,'subtipo':'terreno', 'entrenador': 'enzo' },
            {'name':'tyrantrum'  , 'nivel': 12 ,'tipo':'fuego'  ,'subtipo':'planta', 'entrenador': 'maria' },
            {'name':'wingull' , 'nivel': 18 ,'tipo':'agua'  ,'subtipo':'volador', 'entrenador': 'enzo' },
            {'name':'tyrantrum'  , 'nivel': 12 ,'tipo':'fuego'  ,'subtipo':'planta', 'entrenador': 'maria' },
            {'name':'gigante' , 'nivel': 21 ,'tipo':'agua','subtipo':'volador', 'entrenador': 'juan' },
            {'name':'rayo' , 'nivel':3  ,'tipo':'fuego'  ,'subtipo':'terreno', 'entrenador': 'enzo' }
]


for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador, 'name')

for pokemon in pokemons:
    pos = lista_entrenadores.busqueda(pokemon['entrenador'], 'name')
    if(pos > -1):
        del pokemon['entrenador']
        lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'name')

# print(lista_entrenadores.obtener_elemento(0)['pokemons'].barrido())

# a. obtener la cantidad de Pokémons de un determinado entrenador;
def cantidad_de_pkm(lista,entrenador):
    aux = lista.busqueda(entrenador,'name')
    cantPkm = lista.obtener_elemento(aux)['pokemons'].tamanio()
    print('La cantidad de pokemons que tiene el entrandor',entrenador,'es',cantPkm)
cantidad_de_pkm(lista_entrenadores,'enzo')

# b. listar los entrenadores que hayan ganado más de tres torneos;
def entrenadores_con_mas_de_3_torneos_ganados(lista):
    print('Entrenadores con 3 o mas torneos ganados')
    for i in range(lista.tamanio()):
        if lista.obtener_elemento(i)['torneos_ganados'] >= 3:
            print(lista.obtener_elemento(i)['name'])
entrenadores_con_mas_de_3_torneos_ganados(lista_entrenadores)

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def pkm_mas_nivel_del_mejor_entrenador(lista):
    max = 0
    pos = 0
    for i in range(lista.tamanio()):
        if lista.obtener_elemento(i)['torneos_ganados'] > max:
            pos = i
            max = lista.obtener_elemento(i)['torneos_ganados']
    max_entrenador = lista.obtener_elemento(pos)
    max_level = 0
    for i in range(max_entrenador['pokemons'].tamanio()):
        if max_entrenador['pokemons'].obtener_elemento(i)['nivel'] > max_level:
            max_level = max_entrenador['pokemons'].obtener_elemento(i)['nivel']
            pokemon_max_level = max_entrenador['pokemons'].obtener_elemento(i)
    print('Mejor entrenador',max_entrenador,'y su pokemon de mayor nivel',pokemon_max_level)
pkm_mas_nivel_del_mejor_entrenador(lista_entrenadores)

# d. mostrar todos los datos de un entrenador y sus Pokémos;
def datos_de_entrenador(lista,entrenador):
    pos = lista.busqueda(entrenador,'name')
    print('Nombre:',lista.obtener_elemento(pos)['name'])
    print('Torneos ganados:',lista.obtener_elemento(pos)['torneos_ganados'])
    print('Batallas ganadas:',lista.obtener_elemento(pos)['batallas_ganadas'])
    print('Batallas perdidas:',lista.obtener_elemento(pos)['batallas_perdidas'])
    lista_pkm = lista.obtener_elemento(pos)['pokemons']
    print('Lista de pokemons:')
    for i in range (lista_pkm.tamanio()):
        print(' ',lista_pkm.obtener_elemento(i)['name'])
datos_de_entrenador(lista_entrenadores,'enzo')

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def entrenadores_con_79_o_mas_porcentaje_de_vicotrias(lista):
    for i in range(lista.tamanio()):
        cant_de_batallas = lista.obtener_elemento(i)['batallas_ganadas'] + lista.obtener_elemento(i)['batallas_perdidas']
        porcentaje = (lista.obtener_elemento(i)['batallas_ganadas'] * 100) / cant_de_batallas
        if (porcentaje >= 79):
            print('Nombre',lista.obtener_elemento(i)['name'],'winrate:',str(round(porcentaje)) +'%')
entrenadores_con_79_o_mas_porcentaje_de_vicotrias(lista_entrenadores)

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
def mostrar_entrenador_segun_tipos(lista,tipo1,tipo2):
    aux = []
    for i in range(lista.tamanio()):
        lista_pkm = lista.obtener_elemento(i)['pokemons']
        for i in range (lista_pkm.tamanio()):
            if lista_pkm.obtener_elemento(i)['tipo'] == tipo1 and lista_pkm.obtener_elemento(i)['subtipo'] == tipo2:
                print(lista.obtener_elemento(i)['name'],'posee pokemons con los tipos:',tipo1,tipo2)
mostrar_entrenador_segun_tipos(lista_entrenadores,'fuego','planta')
mostrar_entrenador_segun_tipos(lista_entrenadores,'agua','volador')

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promedio_de_niveles_de_pkm(lista,entrenador):
    aux = 0
    pos = lista.busqueda(entrenador,'name')
    lista_pkm = lista.obtener_elemento(pos)['pokemons']
    for i in range (lista_pkm.tamanio()):
        aux += lista_pkm.obtener_elemento(i)['nivel']
    promedio = aux / lista_pkm.tamanio()
    print(aux)
    print('el promedio de nivel que poseen los pkm de',entrenador,'es',promedio)
promedio_de_niveles_de_pkm(lista_entrenadores,'maria')

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def ejercicio_h(lista,pokemon):
    tiene_el_pkm = False
    aux2 = 0
    for i in range(lista.tamanio()):
        lista_pkm = lista.obtener_elemento(i)['pokemons']
        for i in range (lista_pkm.tamanio()):
            if lista_pkm.obtener_elemento(i)['name'] == pokemon:
               tiene_el_pkm = True
        if tiene_el_pkm:
            aux2 += 1
        tiene_el_pkm = False
    print('Numero de entrenadores que poseen este pkm es:',aux2)
ejercicio_h(lista_entrenadores,'tyrantrum')

# i. mostrar los entrenadores que tienen Pokémons repetidos;
def entrenadores_con_pkms_repetidos(lista):
    pkm_repetido = False
    for i in range(lista.tamanio()):
        lista_pkm = lista.obtener_elemento(i)['pokemons']
        for h in range (lista_pkm.tamanio()):
            for j in range(lista_pkm.tamanio()):
                if lista_pkm.obtener_elemento(h)['name'] == lista_pkm.obtener_elemento(j)['name']:
                    pkm_repetido = True
    if pkm_repetido:
        print('Entrenador/es con pkms repetidos',lista.obtener_elemento(i)['name'])
entrenadores_con_pkms_repetidos(lista_entrenadores)

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
def buscar_entrenador_que_tenga_un_pkm_determinado(lista,pokemon):
    for i in range(lista.tamanio()):
        lista_pkm = lista.obtener_elemento(i)['pokemons']
        pos = lista_pkm.busqueda(pokemon,'name')
        if pos > 0:
            print(lista.obtener_elemento(i)['name'],'posee este pokemon:',pokemon)
buscar_entrenador_que_tenga_un_pkm_determinado(lista_entrenadores,'tyrantrum')
buscar_entrenador_que_tenga_un_pkm_determinado(lista_entrenadores,'terrakion')
buscar_entrenador_que_tenga_un_pkm_determinado(lista_entrenadores,'wingull')

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

def entrenador_pkm(lista,entrenador,pkm):
    for i in range(lista.tamanio()):
        lista_pkm = lista.obtener_elemento(i)['pokemons']
        for j in range(lista_pkm.tamanio()):
            if lista.obtener_elemento(i)['name'] == entrenador and lista_pkm.obtener_elemento(j)['name'] == pkm:
                print(entrenador,'posee el pkm:',pkm)
                print('datos del entrenador:')
                datos_de_entrenador(lista,entrenador)
                print('datos del pkm:')
                print(lista_pkm.obtener_elemento(j)['name'])
                print('Nivel:',lista_pkm.obtener_elemento(j)['nivel'])
                print('Tipo:',lista_pkm.obtener_elemento(j)['tipo'])
                print('Subtipo:',lista_pkm.obtener_elemento(j)['subtipo'])
                break
entrenador_pkm(lista_entrenadores,'enzo','wingull')

# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

datosJedis = [
             {'nombre' : 'Bo Keevil', 'maestros' : Lista(), 'coloresDeSablesUsados' : Lista(), 'especie' : 'Humano'},
             {'nombre' : 'Ahsoka Tano', 'maestros' : Lista(), 'coloresDeSablesUsados' : Lista(), 'especie' : 'Togruta'},
             {'nombre' : 'kit Fisto', 'maestros' : Lista(), 'coloresDeSablesUsados' : Lista(), 'especie' : 'Nautolano'},
             {'nombre' : 'Boba Fett:', 'maestros' : Lista(), 'coloresDeSablesUsados' : Lista(), 'especie' : 'desconocida'},
             {'nombre' : 'Jinx', 'maestros' : Lista(), 'coloresDeSablesUsados' : Lista(), 'especie' : 'Twi´lek'},
             {'nombre' : 'Bossk', 'maestros' : Lista(), 'coloresDeSablesUsados' : Lista(), 'especie' : 'Humano'},
            ]

maestrosJedis = [['Mace Windu', 'Yoda'],
                 ['Luke Skywalker'],
                 ['Lucien Draay'],
                 ['Yoda', 'Qui-Gon jin'],
                 ['Luke Skywalker'],
                 ['Qui-Gon jin'],
                 ]

sablesUsados = [
                ['rojo', 'azul', 'verde'],
                ['violeta'],
                ['gris', 'blanco', 'violeta'],
                ['rosado'], ['amarillo'],
                ['azul'], ['verde'], ['morado'], ['marron'],
                ['blanco']
                ]

listaJedis = Lista()

for datosJedi in datosJedis:
    listaJedis.insertar(datosJedi, 'nombre')


for i in range(0, listaJedis.tamanio()):
    for m in range(len(maestrosJedis[i])):
        listaJedis.obtener_elemento(i)['maestros'].insertar(maestrosJedis[i][m])
    for j in range(len(sablesUsados[i])):
        listaJedis.obtener_elemento(i)['coloresDeSablesUsados'].insertar(sablesUsados[i][j])
    
# a. listado ordenado por nombre y por especie;}
print(listaJedis.barrido_jedi())

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
def mostrar_info_del_jedi(lista,jedi):
    pos = lista.busqueda(jedi , 'nombre')
    jedi_info = lista.obtener_elemento(pos)
    print('Nombre:',jedi_info['nombre'])
    print('Maestros:')
    for i in range(jedi_info['maestros'].tamanio()):
        print(jedi_info['maestros'].obtener_elemento(i))
    print('Color de sables:')
    for i in range(jedi_info['coloresDeSablesUsados'].tamanio()):
        print(jedi_info['coloresDeSablesUsados'].obtener_elemento(i))
    print('Especie:',jedi_info['especie'])
mostrar_info_del_jedi(listaJedis,'Ahsoka Tano')

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
def mostrar_aprendices(lista,maestro):
    for i in range(lista.tamanio()):
        if lista.obtener_elemento(i)['maestros'].busqueda(maestro) > -1:
            print(lista.obtener_elemento(i)['nombre'],'alumno de',maestro)

mostrar_aprendices(listaJedis,'Luke Skywalker')
mostrar_aprendices(listaJedis,'Yoda')
mostrar_aprendices(listaJedis,'Mace Windu')
mostrar_aprendices(listaJedis,'Qui-Gon Jin')

# d. mostrar los Jedi de especie humana y twi'lek;
def mostrar_segun_especie(lista,especie):
    for i in range(lista.tamanio()):
        if lista.obtener_elemento(i)['especie'] == especie:
            print(lista.obtener_elemento(i)['nombre'],'es:',especie)

mostrar_segun_especie(listaJedis,'Humano')

# e. listar todos los Jedi que comienzan con A;
def mostrar_por_primera_letra(lista,letra):
    for i in range(lista.tamanio()):
        if lista.obtener_elemento(i)['nombre'][0] == letra:
            print(lista.obtener_elemento(i)['nombre'])

mostrar_por_primera_letra(listaJedis,'A')

# f. mostrar los Jedi que usaron sable de luz de más de un color;
def jedis_con_mas_de_un_color_de_sable(lista):
    for i in range(lista.tamanio()):
        if lista.obtener_elemento(i)['coloresDeSablesUsados'].tamanio() > 1:
            print(lista.obtener_elemento(i)['nombre'])
            print('Sables:')
            for j in range(lista.obtener_elemento(i)['coloresDeSablesUsados'].tamanio()):
                print(lista.obtener_elemento(i)['coloresDeSablesUsados'].obtener_elemento(j))

jedis_con_mas_de_un_color_de_sable(listaJedis)

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def color_sable(lista,color):
    for i in range(lista.tamanio()):
        for j in range(lista.obtener_elemento(i)['coloresDeSablesUsados'].tamanio()):
            if lista.obtener_elemento(i)['coloresDeSablesUsados'].obtener_elemento(j) == color:
                print(lista.obtener_elemento(i)['nombre'],'color de sable:',lista.obtener_elemento(i)['coloresDeSablesUsados'].obtener_elemento(j))
color_sable(listaJedis,'violeta')
color_sable(listaJedis,'amarillo')
'''