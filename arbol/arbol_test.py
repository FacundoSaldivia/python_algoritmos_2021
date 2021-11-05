# Entrega de los ejercicios 5, 16, 23 solo entregar el link del repositorio donde están los archivos resueltos. PAG 158

from sys  import getsizeof
from random import randint
from collections import Counter
from cola import Cola
'''
# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
  # I. determinar cuántos nodos tiene cada árbol;
  # II. realizar un barrido ordenado alfabéticamente de cada árbol.
from arbol import Arbol
arbol = Arbol()


superheroe = {'name': 'Doctor Strnge', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Capitan America', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Capitana Marvel', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Docasdasdas', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Iron Man', 'villano': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Thanos', 'villano': True, 'aparicion': 1946}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Galactus', 'villano': True, 'aparicion': 1944}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Loki', 'villano': True, 'aparicion': 1941}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)


# b. listar los villanos ordenados alfabéticamente;
def ver_villanos(arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            ver_villanos(arbol.izq)
        if(arbol.datos['villano']):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            ver_villanos(arbol.der)
ver_villanos(arbol)

# c. mostrar todos los superhéroes que empiezan con C;
def ver_super_heroes_segun_primera_letra(arbol,letra):
  if(arbol.info is not None):
    if(arbol.izq is not None):
      ver_super_heroes_segun_primera_letra(arbol.izq,letra)
    if(arbol.datos['name'][0] == letra and not arbol.datos['villano']):
      print(arbol.info,arbol.datos)
    if(arbol.der is not None):
      ver_super_heroes_segun_primera_letra(arbol.der,letra)
ver_super_heroes_segun_primera_letra(arbol,'C')

# d. determinar cuántos superhéroes hay el árbol;
def cuantos_supers_hay_en_el_arbol(arbol):
  c = 0
  if(arbol.info is not None):
    if(arbol.izq is not None):
      c += cuantos_supers_hay_en_el_arbol(arbol.izq)
    if not(arbol.datos['villano']):
      c += 1
    if(arbol.der is not None):
      c += cuantos_supers_hay_en_el_arbol(arbol.der)
  return c
print(cuantos_supers_hay_en_el_arbol(arbol))

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
def corregir_nombre(arbol,nombre_a_corregir,nombre_corregido):
  pos = arbol.busqueda(nombre_a_corregir)
  if (pos):
    pos.datos['name'] = nombre_corregido
    print(pos.datos,'Corregido')
  else:
    print(nombre_a_corregir,'No encontrado')
corregir_nombre(arbol,'Doctor Strnge','Doctor Strange')

# f. listar los superhéroes ordenados de manera descendente;
def ver_heroes_de_manera_descendente(arbol):
  if(arbol.info is not None):
    if(arbol.der is not None):
      ver_heroes_de_manera_descendente(arbol.der)
      print(arbol.info)
    if(arbol.izq is not None):
      ver_heroes_de_manera_descendente(arbol.izq)
ver_heroes_de_manera_descendente(arbol)

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
  # I. determinar cuántos nodos tiene cada árbol;
  # II. realizar un barrido ordenado alfabéticamente de cada árbol.
arbol_heroe = Arbol()
arbol_villano = Arbol()
def dividir_heroes_y_villanos(arbol,arbol_heroe,arbol_villano):
  if(arbol.info is not None):
    if(arbol.datos['villano']):
      arbol_villano = arbol_villano.insertar_nodo(arbol.info ,arbol.datos)
      print('orden supuesto a medida que avanza VILLANO')
      arbol_villano.inorden()
    else:
      arbol_heroe = arbol_heroe.insertar_nodo(arbol.info ,arbol.datos)
      print('orden supuesto a medida que avanza HERO')
      arbol_heroe.inorden()
    if(arbol.izq is not None):
      dividir_heroes_y_villanos(arbol.izq,arbol_heroe,arbol_villano)
    if(arbol.der is not None):
      dividir_heroes_y_villanos(arbol.der,arbol_heroe,arbol_villano)
  
dividir_heroes_y_villanos(arbol,arbol_heroe,arbol_villano)
print('villanos')
arbol_villano.inorden()
print('heroes')
arbol_heroe.inorden()
#No comprendo por que no funciona, chequear antes de enviar 



# Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al agro, tiene problemas para la transmisión de los datos recolectados, dado que la ventana de tiempo que dispone para enviar los datos antes de una nueva medición es muy corta, por lo que nos solicita desarrollar un algoritmo que permita comprimir la información para poder enviarla más rápido, para lo cual se debe tener en cuenta los siguientes requerimientos:

# a. la información transmitida por el nano satélite son estado del tiempo, humedad del suelo, y tres dígitos que identifican el lote al cual pertenecen los datos;

# b. desarrollar un árbol de Huffman que permita comprimir la información para transmitirla, la frecuencia de la información transmitida se observa en la siguiente tabla:


# Variable                            Símbolo               Frecuencia
# Estado del clima                    Despejado               0.22
#                                     Nublado                 0.15
#                                     Lluvia                  0.03

# Humedad del suelo                   Baja                    0.26
#                                     Alta                    0.14
# Código de identificación 1           1                      0.05
#                                      2                      0.01
# Código de identificación 2           3                      0.035
#                                      5                      0.06
# Código de identificación 2           7                      0.02
#                                      8                      0.025

# c. comprimir un mensaje y descomprimirlo, para ver si no se pierde información durante el proceso de codificación, la trama enviada por el nano satélite tiene el siguiente formato (estado del clima-humedad del suelo-cod1-cod2-cod3), por ejemplo la siguiente trama es válida “Nublado-Baja-1-5-7”, –los guiones son a fines de comprender como está formada la trama pero no forman parte de la misma–;

# d. determinar la diferencia en tamaño de memoria utilizada por la trama original y la tramacomprimida –puede utilizar la función getsizeof() de la librería sys–.
from arbol_frecuencia import Arbol # Solucion rustica
arbol_climatico = Arbol()
bosque = []
diccionario = {}

def medida_de_comparacion(arbol):
  return arbol.frecuencia

bosque.sort(key=medida_de_comparacion)

def generar_tabla(arbol,cadena='',dic=None):
  if(arbol is not None):
    if(arbol.izq is None):
      dic[arbol.info] = cadena
      # print(arbol.info,cadena,dic)
    else:
      cadena += '0'
      generar_tabla(arbol.izq, cadena, dic)
      cadena = cadena[0:-1]
      cadena += '1'
      generar_tabla(arbol.der, cadena, dic)

def codificar(cadena,dic):
  cadena_cod = ''
  for char in cadena:
    cadena_cod += dic[char]
  return cadena_cod

def decodificar(cadena_cod,arbol_huff):
  cadena_deco = ''
  arbol_aux = arbol_huff
  pos = 0
  while (pos < len(cadena_cod)):
    if(cadena_cod[pos] == '0'):
      arbol_aux = arbol_aux.izq
    else:
      arbol_aux = arbol_aux.der
    pos += 1
    if(arbol_aux.izq is None):
      cadena_deco +=arbol_aux.info
      arbol_aux = arbol_huff
  return cadena_deco
  


tabla = [
  ['Despejado',0.22],
  ['Nublado',0.15],
  ['Lluvia',0.03],
  ['Baja',0.26],
  ['Alta',0.14],
  ['1',0.05],
  ['2',0.01],
  ['3',0.035],
  ['5',0.06],
  ['7',0.02],
  ['8',0.025]
]

for elemnto in tabla:
  nodo = Arbol(elemnto[0],elemnto[1])
  bosque.append(nodo)

while(len(bosque)>1):
  arbol1 = bosque.pop(0)
  arbol2 = bosque.pop(0)
  nuevo_arbol= Arbol(frecuencia = arbol1.frecuencia + arbol2.frecuencia)
  nuevo_arbol.izq = arbol1
  nuevo_arbol.der = arbol2
  bosque.append(nuevo_arbol)
  bosque.sort(key=medida_de_comparacion)

arbol_climatico = bosque[0]

# arbol_climatico.barrido_por_nivel_huff()

# c. comprimir un mensaje y descomprimirlo, para ver si no se pierde información durante el proceso de codificación, la trama enviada por el nano satélite tiene el siguiente formato (estado del clima-humedad del suelo-cod1-cod2-cod3), por ejemplo la siguiente trama es válida “Nublado-Baja-1-5-7”, –los guiones son a fines de comprender como está formada la trama pero no forman parte de la misma–;

trama = ['Nublado','Baja','1','5','7']
print('Tramana enviada',trama)
generar_tabla(arbol_climatico,dic = diccionario)
# print(diccionario)
cadena_cod = codificar(trama,diccionario)
# print(cadena_cod)
# print(getsizeof(cadena_cod),getsizeof(b'1111001000110011101'))
print('Trama codificada:',cadena_cod)
print('Trama recibida luego de la codificacion y decodificacion',decodificar(cadena_cod,arbol_climatico))

# d. determinar la diferencia en tamaño de memoria utilizada por la trama original y la trama comprimida –puede utilizar la función getsizeof() de la librería sys–

print('Tamaño de la trama original',getsizeof(trama))
print('Tamaño de la trama comprimida',getsizeof(cadena_cod))


# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

dic_criaturas = [{'Criatura': 'Ceto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Tifon', 'Derrotado': 'Zeus', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Equidna', 'Derrotado': 'Argos panoptnes', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Dino', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Pefredo', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Enio', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Escila', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 2, 'Capturada' : '-'},
                {'Criatura': 'Caribdis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 5, 'Capturada' : '-'},
                {'Criatura': 'Euriale', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Esteno', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Medusa', 'Derrotado': 'Perseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Ladon', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Aguila del Caucaso', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 4, 'Capturada' : '-'},
                {'Criatura': 'Quimera', 'Derrotado': 'Belerofonte', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Leon de Nemea', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Esfinge', 'Derrotado': 'Edipo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Dragon de la Colquida', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Cerbero', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Cerda de Cromion', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Ortro', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : 'Heracles'},
                {'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Jabali De Calidon', 'Derrotado': 'Atalanta', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Carcinos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Gerion', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Cloto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Laquesis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : 'Heracles'},
                {'Criatura': 'Atropos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Harpias', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Argos Panoptnes', 'Derrotado': 'Hermes', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Aves del Estinfalo', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 5, 'Capturada' : '-'},
                {'Criatura': 'Talos', 'Derrotado': 'Medea', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Sirenas', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Piton', 'Derrotado': 'Apolo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                {'Criatura': 'Cierva de Cerinea', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Basilisco', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                {'Criatura': 'Jabali de Erimanto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                ]

from arbol import Arbol
arbol = Arbol()

for criatura in dic_criaturas:
  arbol = arbol.insertar_nodo(criatura['Criatura'],criatura)

# a. listado inorden de las criaturas y quienes la derrotaron;
#arbol.inorden_criatura_derrotado()

# b. se debe permitir cargar una breve descripción sobre cada criatura;
def cargar_descripciones(arbol):
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()
    print('Criatura :',nodo.info)
#     nodo.datos['Descripcion'] =input('Agregue una breve descripcion de la criatura')
    nodo.datos['Descripcion'] = randint(0,100) #Lo dejo por default ya que es mejor para probarlo
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der)    

#cargar_descripciones(arbol)

# c. mostrar toda la información de la criatura Talos;
criatura_a_mostrar = arbol.busqueda('Talos')
#print(criatura_a_mostrar.datos)

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def tres_heroes_con_mayor_cantidad_de_victorias(arbol):
  lista_heroes = []
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()
    # print(nodo.datos['Derrotado'],nodo.datos)
    if (nodo.datos['Derrotado'] != '-'):
      lista_heroes.append(nodo.datos['Derrotado']) # cargo en una lista todo los heroes
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der) 
  c = Counter(lista_heroes).most_common(3) # Counter me permite ordenarlos y ver su cantidad de ocurrencias, most_common es para ver los primeros 3 (en este caso)
  return c
print(tres_heroes_con_mayor_cantidad_de_victorias(arbol))

# e. listar las criaturas derrotadas por Heracles;

def criaturas_derrotadas_por(arbol,heroe):
  lista_criaturas = []
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()
    if (nodo.datos['Derrotado'] == heroe):
      lista_criaturas.append(nodo.info)
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der) 
  return lista_criaturas
print('Heracles derroto a:',criaturas_derrotadas_por(arbol,'Heracles'))

# f. listar las criaturas que no han sido derrotadas;
def criaturas_no_derrotadas(arbol):
  lista_criaturas = []
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()
    if (nodo.datos['Derrotado'] == '-'):
      lista_criaturas.append(nodo.info)
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der) 
  return lista_criaturas

print('criaturas no derrotadas:',criaturas_no_derrotadas(arbol))

# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
def agregar_campo(arbol,campo):
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()
    nodo.datos[campo] = '-'
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der) 

agregar_campo(arbol,'Capturada')
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
def corregir_campo(arbol,criatura,campo,correccion):
  pos = arbol.busqueda(criatura)
  if (pos):
    pos.datos[campo] = correccion
    print(pos.datos,'Corregido')
  else:
    print(criatura,'No encontrada')

lista_aux = ['Cerbero','Toro de Creta', 'Cierva de Cerinea', 'Jabali De Calidon']
for i in lista_aux:
  corregir_campo(arbol,i,'Capturada','Heracles')

# j. eliminar al Basilisco y a las Sirenas;
def eliminar_criatura(arbol,criatura):
  print(arbol.eliminar_nodo(criatura),'Eliminado')
#eliminar_criatura(arbol,'Basilisco')

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
corregir_campo(arbol,'Aves del Estinfalo','Caputarada','Heracles derroto a varias')

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
corregir_campo(arbol,'Ladon','Criatura','Dragon Ladon')

# m. realizar un listado por nivel del árbol;
def barrido_por_nvl_criaturas(arbol):
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()
    print(nodo.datos,nodo.info)
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der) 
print('barrido')
barrido_por_nvl_criaturas(arbol)

# n. muestre las criaturas capturadas por Heracles.
def criaturas_capturadas_por(arbol,heroe):
  lista_criaturas = []
  pendientes = Cola()
  pendientes.arribo(arbol)
  while(not pendientes.cola_vacia()):
    nodo = pendientes.atencion()

    if (nodo.datos['Capturada'] == heroe):
       lista_criaturas.append(nodo.info)
    if(nodo.izq is not None):
        pendientes.arribo(nodo.izq)
    if(nodo.der is not None):
        pendientes.arribo(nodo.der) 
  return lista_criaturas

print(criaturas_capturadas_por(arbol,'Heracles'))
'''