from cola import Cola
from random import randint

from heap import HeapMax

#PAGINA 95 EJ: 11,12 y 16

#11 Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

# cola_pj_sw = Cola()

# lista_pj = [{"name":"Han Solo","planet":"Alderaan"},{"name":"Bail Organa","planet":"Endor"},{"name":"Aika Lars","planet":"Alderaan"},{"name":"Cliegg Lars","planet":"Alderaan"},{"name":"Sola Naberrie","planet":"Endor"},{"name":"Luke Skywalker","planet":"Endor"},{"name":"Maestro Yoda","planet":"Tattoine"},{"name":"Ezra Bridger","planet":"Alderaan"},{"name":"Jar Jar Binks","planet":"Endor"},{"name":"Rey","planet":"Tatooine"},{"name":"Macri","planet":"Tierra"},{"name":"Trump","planet":"Tierra"},{"name":"Elon Musk","planet":"Marte"}]

# for pj in lista_pj:
#     cola_pj_sw.arribo(pj) 
# elementos = 0




# # Mostrando todos los personajes que pertenecen a los planetas Alderaan, Endor y Tatooine
# print('PUNTO B, Mostrando todos los personajes que pertenecen a los planetas Alderaan, Endor y Tatooine')
# while(elementos < cola_pj_sw.tamanio()):
#     if cola_pj_sw.en_frente()["planet"] == "Alderaan" or cola_pj_sw.en_frente()["planet"] == "Endor" or cola_pj_sw.en_frente()["planet"] == "Tatooine":
#         print(cola_pj_sw.en_frente()["name"]," Pertenece a: ",cola_pj_sw.en_frente()["planet"])
#     cola_pj_sw.mover_final()
#     elementos += 1

# print(' ')
# print('PUNTO B, indicar el plantea natal de Luke Skywalker y Han Solo')
# elementos = 0
# while(elementos < cola_pj_sw.tamanio()):
#     if cola_pj_sw.en_frente()["name"] == "Luke Skywalker" or cola_pj_sw.en_frente()["name"] == "Han Solo":
#         print(cola_pj_sw.en_frente()["name"]," Pertenece a: ",cola_pj_sw.en_frente()["planet"])
#     cola_pj_sw.mover_final()
#     elementos += 1

# print(' ')
# print('PUNTO C y D, Insertar un nuevo pj desp de Yoda y eliminar el personaje que le sigue a Jar Jar Binks')
# elementos = 0
# while ( elementos < cola_pj_sw.tamanio()):
#     if cola_pj_sw.en_frente()["name"] == "Jar Jar Binks":
#         cola_pj_sw.mover_final()
#         pj_borrado = cola_pj_sw.atencion()
#         print('Se elimino ',pj_borrado['name'],' ya que le seguia a Jar Jar Binks')
#     elif cola_pj_sw.en_frente()["name"] == "Maestro Yoda":
#         cola_pj_sw.mover_final()
#         cola_pj_sw.arribo({"name":"Facundo Saldivia","planet":"Tierra"})
#         print('Se agrego un nuevo personaje (Facundo Saldvia del planeta Tierra) ya que le seguia al Maestro Yoda')
#     else:
#         cola_pj_sw.mover_final()
#     elementos += 1 
#     print(cola_pj_sw.en_frente()['name'])
# elementos = 0

#12 Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, ni métodos de ordenamiento.

# cola_1 = Cola()
# cola_2 = Cola()
# cola_combinada = Cola()

# cola1 = [1,4,7,8,13,17,19,26,29,35,100]
# cola2 = [0,1,5,6,10,12,18,31,38,49,101]

# for num in cola1:
#     cola_1.arribo(num)

# for num in cola2:
#     cola_2.arribo(num)


# def combinacion_colas(cola_1,cola_2,cola_combinada):
#     size = cola_1.tamanio() + cola_2.tamanio()
#     for i in range(size):
#         if cola_1.cola_vacia() :
#             cola_combinada.arribo(cola_2.atencion())

#         elif cola_2.cola_vacia():
#             cola_combinada.arribo(cola_1.atencion())

#         elif cola_1.en_frente() > cola_2.en_frente():
#             cola_combinada.arribo(cola_2.atencion())

#         else:
#             cola_combinada.arribo(cola_1.atencion())

# combinacion_colas(cola_1,cola_2,cola_combinada)

# elementos = 0
# while elementos < cola_combinada.tamanio():
#     print(cola_combinada.en_frente())
#     elementos += 1
#     cola_combinada.mover_final()

# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

empleado = 1
ti = 2
gerente = 3

cola_prioridad = HeapMax()

documentos = [['Investigacion',empleado],['Informe',empleado],['Resumen',empleado]]
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre)
cola_prioridad.arribo_muchos(documentos)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# print(cola_prioridad.atencion()[1])

# c. cargue dos documentos del staff de TI.
documentos_2 = [['Revision',ti],['Semi informe',ti]]
cola_prioridad.arribo_muchos(documentos_2)

# d. cargue un documento del gerente.
documentos_3 = [['Revision - gerencial',gerente]]
cola_prioridad.arribo_muchos(documentos_3)

# e. imprima los dos primeros documentos de la cola.
# print(cola_prioridad.atencion())
# print(cola_prioridad.atencion())

# f. cargue dos documentos de empleados y uno de gerente.

documentos_4 = [['Documento empleado',empleado],['Documento empleado2',empleado],['Documento gerente',gerente]]
cola_prioridad.arribo_muchos(documentos_4)

# g. imprima todos los documentos de la cola de impresión.
while not cola_prioridad.vacio():
    print(cola_prioridad.atencion())


#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

# cola_pj_marvel = Cola()

# pj_marvel = [{"name":"Tony Stark", "s-name":"Iron Man","S":"M"}, {"name":"Steve Rogers", "s-name":"Capitán América","S": "M"}, {"name": "Natasha Romanoff","s-name" :"Black Widow","S":"F"},{"name":"Scott Lang","s-name":"Ant-Man","S":"M"},{"name":"Carol Denvers","s-name":"Capitana Marvel","S":"F"},{"name":"Peter Parker","s-name":"Spiderman","S":"M"},{"name":"Stephen Strange","s-name":"Doctor Strange","S":"M"}]

# for pj in pj_marvel:
#     cola_pj_marvel.arribo(pj)
# # a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# def encontrar_por_nombre_de_superheroe(cola,snombre):
#     elementos = 0
#     while elementos < cola.tamanio():
#         if cola.en_frente()["s-name"] == snombre:
#             print("El nombre de ", snombre," es: ",cola.en_frente()["name"])
#         elementos += 1
#         cola.mover_final()   
# encontrar_por_nombre_de_superheroe(cola_pj_marvel,"Capitana Marvel")

# # b. mostrar los nombre de los superhéroes femeninos;
# # c. mostrar los nombres de los personajes masculinos;
# def mostrar_pjs_x_sexo(cola,sexo):
#     elementos = 0
#     while elementos < cola.tamanio():
#         if cola.en_frente()["S"] == sexo:
#             print(cola.en_frente()["name"])
#         elementos += 1
#         cola.mover_final() 
# print("")
# print("Sexo Masculino")
# mostrar_pjs_x_sexo(cola_pj_marvel,"M")
# print("")
# print("Sexo Femenino")
# mostrar_pjs_x_sexo(cola_pj_marvel,"F")

# # d. determinar el nombre del superhéroe del personaje Scott Lang;
# def encontrar_por_nombre(cola,nombre):
#     texto = ('No se encontro ',nombre,' chequea si esta bien escrito y sus mayusculas')
#     elementos = 0
#     while elementos < cola.tamanio():
#         if cola.en_frente()["name"] == nombre:
#             texto = nombre," es: ",cola.en_frente()["s-name"]
#         elementos += 1
#         cola.mover_final()   
#     print(texto)

# encontrar_por_nombre(cola_pj_marvel,"Scott Lang")

# # e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# def encontrar_por_primera_letra_sname(cola,letra):
#     elementos = 0
#     lista_pj = []
#     while elementos < cola.tamanio():
#         if cola_pj_marvel.en_frente()["name"][0] == letra.upper():
#             lista_pj.append(cola_pj_marvel.en_frente())
#         elementos += 1
#         cola.mover_final() 
#     for pj in lista_pj:
#         print(pj)
# encontrar_por_primera_letra_sname(cola_pj_marvel,"s")