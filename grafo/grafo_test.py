# Entrega de los ejercicios 6 y 16 solo entregar el link del repositorio donde están los archivos resueltos. PAGINA 228

from grafo import Grafo
from pila import Pila

# Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio 20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:

# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que representa, no más de 20 palabras;
# b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano, pareja, la etiquetas de dichas aristas son estos nombre de relación.
# c. dado el nombre de un dios mostrar los hijos de este;
# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación entre ambos;
# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como camino más corto el que tenga menor número de aristas;
# g. realizar un barrido en profundidad y amplitud de dicho grafo;
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
# i. mostrar todos los ancestros de un determinado dios;
# j. mostrar todos los nietos de Cronos;
# k. mostrar todos los hijos de Tea;
# l. persista los datos del grafo en archivos, uno para los vértices y otro para las aristas.

grafo_dioses = Grafo(False)
grafo_dioses.cargar_dioses()
# print(grafo_dioses.tamanio())
# print(grafo_dioses.inicio.obtener_elemento()))

# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que representa, no más de 20 palabras;                                                                               


def cargar_descripcion_corta(grafo):
    cant_palabras = 20
    for i in range(grafo.inicio.tamanio()):
        descripcion = 'a ' * 21
        while(len(descripcion.split()) > cant_palabras):
            descripcion = input('Dar descripcion de:'+ grafo.inicio.obtener_elemento(i)['info']+ ':  ')
            if (len(descripcion.split()) <= cant_palabras):
                grafo.inicio.obtener_elemento(i)['data'] = descripcion
            else:
                print('Descripcion mayor a 20 palabras, vuelva a introducir una descripcion mas corta') 

# cargar_descripcion_corta(grafo_dioses)

# k. mostrar todos los hijos de Tea;
# c. dado el nombre de un dios mostrar los hijos de este;
def mostrar_hijos(grafo,dios):
    ubicacion_dios = grafo.inicio.busqueda(dios,'info')
    print(ubicacion_dios)
    for i in range (grafo.inicio.obtener_elemento(ubicacion_dios)['aristas'].tamanio()):
        if grafo_dioses.inicio.obtener_elemento(ubicacion_dios)['aristas'].obtener_elemento(i)['data']['relacion'][0] == 'padre' or grafo_dioses.inicio.obtener_elemento(ubicacion_dios)['aristas'].obtener_elemento(i)['data']['relacion'][0] == 'madre':
            print(grafo_dioses.inicio.obtener_elemento(ubicacion_dios)['aristas'].obtener_elemento(i)['destino'] + ' es hijo de ' + dios)

# mostrar_hijos(grafo_dioses,'Tea')
# print(grafo_dioses.inicio.obtener_elemento(45)['aristas'].tamanio())
# for i in range (grafo_dioses.inicio.obtener_elemento(45)['aristas'].tamanio()):
#     print(grafo_dioses.inicio.obtener_elemento(45)['aristas'].obtener_elemento(i)['data']['relacion'][0])

# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
def mostrar_familia(grafo,dios):
    ubicacion_dios = grafo.inicio.busqueda(dios,'info')
    print(ubicacion_dios)
    arista = grafo_dioses.inicio.obtener_elemento(ubicacion_dios)['aristas']
    for i in range (arista.tamanio()):
        if arista.obtener_elemento(i)['data']['relacion'][0] != 'pareja':
            print(dios,arista.obtener_elemento(i)['data']['relacion'][0],'de',arista.obtener_elemento(i)['destino'])
# mostrar_familia(grafo_dioses,'Zeus')

# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación entre ambos;
def buscar_relacion(grafo,d1,d2):
    ubicacion_dios = grafo.buscar_arista(d1,d2)
    if (ubicacion_dios > 0):
        arista = grafo.inicio.obtener_elemento(ubicacion_dios)['aristas']
        for i in range (arista.tamanio()):
            if d2 == arista.obtener_elemento(i)['destino']:
                print('Relacion entre',d1,d2,':',arista.obtener_elemento(i)['data']['relacion'])
# buscar_relacion(grafo_dioses,'Zeus','Hera')

# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como camino más corto el que tenga menor número de aristas;

def camino_mas_corto(grafo,d1,d2):
    encontrado = False
    d_aux = d2
    arr_dioses = []
    d1_ubicacion = grafo.inicio.busqueda(d1, 'info') # para comprobar que ambox dioses existan
    d2_ubicacion = grafo.inicio.busqueda(d2, 'info')# para comprobar que ambox dioses existan
    if (d1_ubicacion > 0 and d2_ubicacion > 0):# para comprobar que ambox dioses existan
        pila = grafo.dijkstra(d1_ubicacion) # almaceno la pila
        while not encontrado: # mientras que no se haya encontrado el dios 1 (d1)
            while not pila.pila_vacia(): # desapilo hasta encontrar el d2
                conexion = pila.desapilar()
                pila_aux = Pila()
                if conexion[1][0] == d_aux: # desapilo hasta encontrar el d2
                    arr_dioses.append(d_aux) # guardo el dios
                    d_aux = conexion[1][1] # guardo la conexion del d2 y repetir hasta encontrar d1
                    if conexion[1][0] == d1:# encuentra d1 sale del while
                        encontrado = True
                pila_aux.apilar(conexion)   
            while not pila_aux.pila_vacia():
                pila.apilar(pila_aux.desapilar())
        for dioses in arr_dioses: # muestro los dioses 
            print(dioses)
            print('|')
            print('V')
# camino_mas_corto(grafo_dioses,'Zeus','Selene')

def camino_mas_corto_visto_clases(grafo, origen, destino):
    vertice_origen = grafo.buscar_vertice(origen)
    vertice_destino = grafo.buscar_vertice(destino)
    costo = None

    if vertice_origen != -1 and vertice_destino != -1:
        camino = grafo.dijkstra(vertice_origen)
        while(not camino.pila_vacia()):
            dato = camino.desapilar()
            if(dato[1][0] == destino):
                if(costo is None):
                    costo = dato[0]
                print('paso por', dato[1][0])
                destino = dato[1][1]
        print('Costo total:', costo)
# camino_mas_corto_visto_clases(grafo_dioses,'Zeus','Selene')
# g. realizar un barrido en profundidad y amplitud de dicho grafo;
# grafo_dioses.barrido_profundidad(0)
# grafo_dioses.barrido_amplitud(0)
        
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
def barrido_madre(grafo):
    for i in range(grafo.inicio.tamanio()):
        dios = grafo.inicio.obtener_elemento(i)['info']
        arista = grafo_dioses.inicio.obtener_elemento(i)['aristas']
        for j in range(arista.tamanio()):
            if arista.obtener_elemento(j)['data']['relacion'][0] == 'madre':
                print(arista.obtener_elemento(j)['destino'],'madre:',dios)

# barrido_madre(grafo_dioses)

# i. mostrar todos los ancestros de un determinado dios;

def ver_ancestros(grafo,dios,c = 0):
    ubicacion_dios = grafo.inicio.busqueda(dios,'info')
    arista = grafo_dioses.inicio.obtener_elemento(ubicacion_dios)['aristas']
    if c == 0:
        print('ANCESTROS DE',dios)
    for i in range(arista.tamanio()):
        # print(arista.obtener_elemento(i))
        if arista.obtener_elemento(i)['data']['relacion'][0] == 'hijo':
            # print(arista.obtener_elemento(i),c)
            ver_ancestros(grafo,arista.obtener_elemento(i)['destino'],c+1)
        if arista.obtener_elemento(i)['data']['relacion'][0] == 'hermano' and c != 0:
            print(arista.obtener_elemento(i)['destino'])


# ver_ancestros(grafo_dioses,'Zeus')

# j. mostrar todos los nietos de Cronos;
def ver_nietos(grafo,dios,stop=False):    
    ubicacion_dios = grafo.inicio.busqueda(dios,'info')
    arista = grafo_dioses.inicio.obtener_elemento(ubicacion_dios)['aristas']
    for i in range(arista.tamanio()):
        if arista.obtener_elemento(i)['data']['relacion'][0] == 'padre' and not stop:
            ver_nietos(grafo,arista.obtener_elemento(i)['destino'],True)
        else:
            if arista.obtener_elemento(i)['data']['relacion'][0] == 'padre':
                print(arista.obtener_elemento(i)['destino'])

# ver_nietos(grafo_dioses,'Urano')

# 16. Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determinado país teniendo en cuenta los siguientes requerimientos:
# a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;
# b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Atenas (Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), Artemisa (Éfeso) y Teatro de Dionisio (Acrópolis)
# c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
# d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta el templo de Apolo, en Delfos.

grafo_templos = Grafo(False)

def cargar_grafo(grafo):
    grafo.insertar_vertice('Partenon',data={'latitud':28,'longitud':4})
    grafo.insertar_vertice('Olimpia',data={'latitud':5,'longitud':21})
    grafo.insertar_vertice('Delfos',data={'latitud':14,'longitud':2})
    grafo.insertar_vertice('Sunion',data={'latitud':12,'longitud':16})
    grafo.insertar_vertice('Efeso',data={'latitud':2,'longitud':19})
    grafo.insertar_vertice('Acropolis',data={'latitud':12,'longitud':2})

cargar_grafo(grafo_templos)
for i in range(grafo_templos.inicio.tamanio()):
    origen = grafo_templos.inicio.obtener_elemento(i)
    ubicacion_origen =  origen['data']['latitud'] + origen['data']['longitud']

    for j in range((i+1),grafo_templos.inicio.tamanio()):
        destino = grafo_templos.inicio.obtener_elemento(j)
        if (destino != origen):
            ubicacion_destino =  destino['data']['latitud'] + destino['data']['longitud']
            distancia_ambos = ubicacion_destino - ubicacion_origen

            grafo_templos.insertar_arista(abs(distancia_ambos),origen['info'],destino['info'])

# ubicacion = grafo_templos.inicio.busqueda('Partenon','info')
# print(ubicacion)
# arista = grafo_templos.inicio.obtener_elemento(ubicacion)['aristas']
# for i in range (arista.tamanio()):
#         print(arista.obtener_elemento(i),'de',arista.obtener_elemento(i)['destino'])

# c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
def exp_minimo(grafo,templo):
    pos = grafo.inicio.busqueda(templo,'info')
    print(grafo.prim(pos))
exp_minimo(grafo_templos,'Partenon')
# d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta el templo de Apolo, en Delfos.
camino_mas_corto_visto_clases(grafo_templos,'Partenon','Delfos')