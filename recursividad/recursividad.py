# EJERCICIOS = 5, 8, 22 ,23

#5 Desarrollar una función que permita convertir un número romano en un número decimal.

def convertir_num_romano(roman_num):
    if (len(roman_num) == 0):
        return 0
    else:
        if  roman_num[-1] == 'I':
            aux = 1
        elif roman_num[-1] == 'V':
            aux = 5
        elif roman_num[-1] == 'X':
            aux = 10
        elif roman_num[-1] == 'L':
            aux = 50
        elif roman_num[-1] == 'C':
            aux = 100
        elif roman_num[-1] == 'D':
            aux = 500
        elif roman_num[-1] == 'M':
            aux = 1000
        if len(roman_num) > 1:
            if (roman_num[-2] == 'I' and roman_num[-1] != 'I'):
                return (aux - 2 ) + convertir_num_romano(roman_num[:-1]) # el -2 es por que luego va a usar el 1(I) anterior
        else:
            return aux + convertir_num_romano(roman_num[:-1])


#8 Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.


def binario(num):
    num = str(num)
    if len(num) == 1:
        return int(num)
    else:
        potencia = len(num) - 1
        base = int(num[0]) * 2
        return base ** potencia + binario(num[1:len(num)])


#22 El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# A. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
# B. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo 
# C. Utilizar un vector para representar la mochila.

mochila = ['botella', 'celular','sable de luz','billetera']

def usar_la_fuerza(lista, cantObj):
    if lista[0] == 'sable de luz':
        return lista[0], 'posicion:', cantObj - len(lista) + 1
    else:
        lista.pop(0)
        if (len(mochila) < 1):
            return 'No hay ningun sable en la mochila'
        else:
            return usar_la_fuerza(lista, cantObj)
        

print(usar_la_fuerza(mochila,len(mochila)))
#23 Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

laberinto = [[' ','0','0','0','0','0','0','0','0','0','0','0'],
             [' ',' ','|','|',' ','|','|','|','|','|','|','0'],
             ['0',' ','|','|',' ','|','|','|','|','|','|','0'],
             ['0',' ',' ',' ',' ','|','|','|','|','|','|','0'],
             ['0','|','|','|',' ','|','|','|','|','|',' ','0'],
             ['0','|','|','|',' ','|','|','|','|','|',' ','0'],
             ['0','|','|','|',' ','|',' ',' ',' ',' ',' ','0'],
             ['0','|','|','|',' ','|',' ','|','|',' ','|','0'],
             ['0','|','|','|',' ',' ',' ','|','|',' ','|','0'],
             ['0','|','|','|',' ','|','|','|','|',' ','|','0'],
             ['0','|','|','|',' ','|','|','|','|',' ','S','0'],
             ['0','0','0','0','0','0','0','0','0','0','0','0']]


def res_laberinto(p1,p2,laberinto):
    if laberinto[p1+1][p2] == 'S'or laberinto[p1][p2+1] == 'S':
        return print('RESUELTO!')
    else:
        if laberinto[p1][p2] == ' ':
            laberinto[p1][p2] = '.' # Si es la primera vez que pasa por un lugar deja '.'
        else:
            laberinto[p1][p2] = '•' # en cambio si es la 2da vez que pasa ya que se encontro con un lugar sin salida deja una . mas marcada '•'
        for lista in laberinto: # Voy mostrando el laberinto a medida que avanza
            print(lista)
        input('Enter para continuar') # Hay que presionar enter para que avance le bolita por el laberinto
        if laberinto[p1+1][p2] == ' ': #Comprueba que a su al rededor haya un espacio vacio
            p1 = p1 + 1
        elif laberinto[p1][p2+1] == ' ':
            p2 = p2 + 1
        elif laberinto[p1-1][p2] == ' ':
            p1 = p1 - 1 
        elif laberinto[p1][p2-1] == ' ':
            p2 = p2 -1
        elif laberinto[p1+1][p2] == '.': # de no haber un espacio vacio empieza a buscar uno donde este la '.' para poder volver
            laberinto[p1][p2] = '•'
            p1 = p1 + 1
        elif laberinto[p1][p2+1] == '.':
            laberinto[p1][p2] = '•'
            p2 = p2 + 1
        elif laberinto[p1-1][p2] == '.':
            laberinto[p1][p2] = '•'
            p1 = p1 - 1 
        elif laberinto[p1][p2-1] == '.':
            laberinto[p1][p2] = '•'
            p2 = p2 -1
        return res_laberinto(p1,p2,laberinto)

res_laberinto(0,0,laberinto)