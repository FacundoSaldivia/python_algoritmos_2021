from lista import Lista
from cola import Cola
from heap import HeapMin
from pila import Pila
from math import inf
from copy import deepcopy


class Grafo(object):

    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.inicio = Lista()

    def insertar_vertice(self, dato, criterio='info', data=None):  # ! agregar otro
        self.inicio.insertar({'info': dato, 'visitado': False, 'aristas': Lista(), 'data': data}, criterio)


    def insertar_arista(self, peso, origen, destino, criterio='destino', data=None):  # ! agregar otro
        ver_origen = self.inicio.busqueda(origen, 'info')
        ver_destino = self.inicio.busqueda(destino, 'info')
        if(ver_origen != -1 and ver_destino != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].insertar({'peso': peso, 'destino': destino, 'data': data}, criterio)
            if(not self.dirigido and origen != destino):
                data_aux = deepcopy(data)
                if(data):
                    data_aux['relacion'].reverse()
                self.inicio.obtener_elemento(ver_destino)['aristas'].insertar({'peso': peso, 'destino': origen, 'data': data_aux}, criterio)
        else:
            print('los vertices origen o destino no estan en el grafo....', origen, destino)

    def grafo_vacio(self):
        return self.inicio.lista_vacia()

    def tamanio(self):
        return self.inicio.tamanio()
    
    def buscar_vertice(self, clave, criterio='info'):
        return self.inicio.busqueda(clave, criterio=criterio)

    def buscar_arista(self, origen, destino, criterio='destino'):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            return self.inicio.obtener_elemento(ver_origen)['aristas'].busqueda(destino, criterio)
        else:
            return ver_origen

    def barrido_vertices(self):
        self.inicio.barrido()

    def es_adyacente(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            destino = self.buscar_arista(origen, destino)
            if(destino != -1):
                return True
            else:
                return False
        else:
            return False

    def adyacentes(self, origen):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].barrido()

    def eliminar_vertice(self, clave):
        aux = self.inicio.eliminar(clave, criterio='info')
        for posicion in range(self.tamanio()):
            origen = self.inicio.obtener_elemento(posicion)['info']
            self.eliminar_arista(origen, clave)
        return aux


    def eliminar_arista(self, origen, destino):
        ver_origen = self.inicio.busqueda(origen, 'info')
        if(ver_origen != -1):
            self.inicio.obtener_elemento(ver_origen)['aristas'].eliminar(destino, 'destino')
            if(not self.dirigido):
                ver_destino = self.inicio.busqueda(destino, 'info')
                if(ver_destino != -1):
                    self.inicio.obtener_elemento(ver_destino)['aristas'].eliminar(origen, 'destino')

    def barrido_profundidad(self, ver_origen):
        """Barrido en profundidad del grafo."""
        while(ver_origen < self.inicio.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                print(vertice['info'])
                aristas = 0
                while(aristas < vertice['aristas'].tamanio()):
                    arista = vertice['aristas'].obtener_elemento(aristas)
                    pos_vertice = self.buscar_vertice(arista['destino'])
                    nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                    if(not nuevo_vertice['visitado']):
                        self.barrido_profundidad(pos_vertice)
                    aristas += 1
            ver_origen += 1

    def barrido_amplitud(self, ver_origen):
        """Barrido en amplitud del grafo."""
        cola = Cola()
        while(ver_origen < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            if(not vertice['visitado']):
                vertice['visitado'] = True
                cola.arribo(vertice)
                while(not cola.cola_vacia()):
                    nodo = cola.atencion()
                    print(nodo['info'], nodo['data'])
                    aristas = 0
                    while(aristas < nodo['aristas'].tamanio()):
                        adyacente = nodo['aristas'].obtener_elemento(aristas)
                        pos_vertice = self.buscar_vertice(adyacente['destino'])
                        nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                        if(not nuevo_vertice['visitado']):
                            nuevo_vertice['visitado'] = True
                            cola.arribo(nuevo_vertice)
                        aristas += 1
            ver_origen += 1

    def marcar_no_visitado(self):
        """Marca todos los vertices del grafo como no visitados."""
        for i in range(self.tamanio()):
            self.inicio.obtener_elemento(i)['visitado'] = False

    def existe_paso(self, ver_origen, ver_destino):
        """Barrido en profundidad del grafo."""
        resultado = False
        vertice = self.inicio.obtener_elemento(ver_origen)
        if(not vertice['visitado']):
            vertice['visitado'] = True
            aristas = 0
            while(aristas < vertice['aristas'].tamanio() and not resultado):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = self.buscar_vertice(arista['destino'])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                destino = self.inicio.obtener_elemento(ver_destino)
                if(nuevo_vertice['info'] == destino['info']):
                    return True
                else:
                    resultado = self.existe_paso(pos_vertice, ver_destino)
                aristas += 1
        return resultado

    def dijkstra(self, ver_origen):
        """Algoritmo de Dijkstra para hallar el camino mas corto."""
        no_visitados = HeapMin()
        camino = Pila()
        aux = 0
        while(aux < self.tamanio()):
            vertice = self.inicio.obtener_elemento(ver_origen)
            vertice_aux = self.inicio.obtener_elemento(aux)
            vertice_aux['anterior'] = None
            if(vertice_aux['info'] == vertice['info']):
                no_visitados.arribo([vertice_aux['info'], None], 0)
            else:
                no_visitados.arribo([vertice_aux['info'], None], inf)
            aux += 1
        while(not no_visitados.vacio()):
            dato = no_visitados.atencion()
            camino.apilar(dato)
            pos_aux = self.buscar_vertice(dato[1][0])
            vertice_aux = self.inicio.obtener_elemento(pos_aux)
            aristas = 0
            while(aristas < vertice_aux['aristas'].tamanio()):
                arista = vertice_aux['aristas'].obtener_elemento(aristas)
                pos_heap = no_visitados.busqueda(arista['destino'])
                if(pos_heap is not None and no_visitados.elementos[pos_heap][0] > dato[0] + arista['peso']):
                    no_visitados.elementos[pos_heap][1][1] = dato[1][0]
                    nuevo_peso = dato[0] + arista['peso']
                    no_visitados.cambiar_prioridad(pos_heap, nuevo_peso)
                aristas += 1
        # print(no_visitados.elementos)
        return camino

    def busqueda_prim(self, bosque, buscado):
        for elemento in bosque:
            if(buscado in elemento[1]):
                return elemento


    def prim(self, inicio = 0):
        """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
        bosque = []
        aristas = HeapMin()
        origen = self.inicio.obtener_elemento(inicio)
        adyac = 0
        while(adyac < origen['aristas'].tamanio()):
            arista = origen['aristas'].obtener_elemento(adyac)
            aristas.arribo([origen['info'], arista['destino']], arista['peso'])
            adyac += 1
        # print(bosque)
        # print(aristas.elementos)
        # print()
        while(len(bosque) // 2 < self.tamanio() and not aristas.vacio()):
            dato = aristas.atencion()
            if(len(bosque) == 0) or ((self.busqueda_prim(bosque, dato[1][0]) is not None) ^ (self.busqueda_prim(bosque, dato[1][1]) is not None)):
                bosque.append(dato)
                pos_vertice = self.buscar_vertice(dato[1][1])
                nuevo_vertice = self.inicio.obtener_elemento(pos_vertice)
                adyac = 0
                while(adyac < nuevo_vertice['aristas'].tamanio()):
                    arista = nuevo_vertice['aristas'].obtener_elemento(adyac)
                    # print(arista)
                    aristas.arribo([nuevo_vertice['info'], arista['destino']], arista['peso'])
                    adyac += 1
            # print(bosque)
            # print(aristas.elementos)
            # a = input()
        return bosque

# grafo = Grafo()
# grafo.insertar_vertice('A')
# grafo.insertar_vertice('C')
# grafo.insertar_vertice('B')
# grafo.insertar_vertice('F')
# grafo.insertar_vertice('Z')
# grafo.insertar_vertice('X')

# grafo.insertar_arista(5, 'A', 'B')
# grafo.insertar_arista(2, 'C', 'B')
# grafo.insertar_arista(3, 'B', 'C')
# grafo.insertar_arista(9, 'A', 'F')
# grafo.insertar_arista(5, 'B', 'F')
# grafo.insertar_arista(13, 'F', 'X')
# grafo.insertar_arista(7, 'X', 'Z')
# grafo.insertar_arista(5, 'C', 'X')
# vertice_destino = grafo.buscar_vertice('Z')
# vertice_origen = grafo.buscar_vertice('A')

# bosque = grafo.prim()
# print('arbol de expansion')
# peso = 0
# for elemento in bosque:
#     print(elemento[1][0], '-', elemento[1][1])
#     peso += elemento[0]
# print('costo total', peso)
# pila_camino = grafo.dijkstra(vertice_origen, vertice_destino)

# destino = 'Z'
# costo = None
# while(not pila_camino.pila_vacia()):
#     dato = pila_camino.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]
# print('el costo total del camino es:', costo)
# print(grafo.existe_paso(vertice_origen, vertice_destino))
# grafo.barrido_profundidad(vertice_origen)
# grafo.marcar_no_visitado()
# print()
# vertice_origen = grafo.buscar_vertice('F')
# grafo.barrido_amplitud(vertice_origen)

# grafo.insertar_arista(100, 'B', 'B')

# grafo.inicio.obtener_elemento(0)['aristas'].barrido()
# print()
# grafo.inicio.obtener_elemento(1)['aristas'].barrido()

# grafo.barrido_vertices()

# print(grafo.es_adyacente('A', 'F'))
# print(grafo.es_adyacente('A', 'C'))
# # print(grafo.eliminar_vertice('B'))
# print()
# grafo.barrido_vertices()
# print()
# grafo.eliminar_arista('A', 'B')
# grafo.adyacentes('A')
# print()
# grafo.adyacentes('F')
# print()
# grafo.adyacentes('B')

# print(grafo.buscar_vertice('F'))
# print(grafo.buscar_vertice('B'))

# print(grafo.buscar_arista('B','A'))
# print(grafo.buscar_arista('A','A'))

    def cargar_dioses(self):
        self.insertar_vertice('Gaia')
        self.insertar_vertice('Urano')
        
        self.insertar_vertice('Themis')
        self.insertar_vertice('Minemosyne')
        self.insertar_vertice('Hyperion')
        self.insertar_vertice('Theia')
        self.insertar_vertice('Crios')
        self.insertar_vertice('Cronos')
        self.insertar_vertice('Rhea')
        self.insertar_vertice('Kdios')
        self.insertar_vertice('Phoibe')
        self.insertar_vertice('Iapetos')
        self.insertar_vertice('Okeanos')
        self.insertar_vertice('Tedds')
        
        self.insertar_vertice('Helios')
        self.insertar_vertice('Eos')
        self.insertar_vertice('Selene')
        self.insertar_vertice('Prometheus')
        self.insertar_vertice('Epimetheus')
        self.insertar_vertice('Atlas')
        self.insertar_vertice('Pleione')
        
        self.insertar_vertice('Hades')
        self.insertar_vertice('Demeter')
        self.insertar_vertice('Poseidon')
        self.insertar_vertice('Hestia')
        self.insertar_vertice('Hera')
        self.insertar_vertice('Zeus')
        self.insertar_vertice('Leto')
        self.insertar_vertice('Semelle')
        self.insertar_vertice('Maia')
        
        self.insertar_vertice('Persephone')
        self.insertar_vertice('Aphrodite')
        self.insertar_vertice('Ares')
        self.insertar_vertice('Hephaistos')
        self.insertar_vertice('Athena')
        self.insertar_vertice('Apollo')
        self.insertar_vertice('Artemis')
        self.insertar_vertice('Dionysos')
        self.insertar_vertice('Hermes')
        self.insertar_vertice('Penelopeia')
        
        self.insertar_vertice('Phobos')
        self.insertar_vertice('Deimos')
        self.insertar_vertice('Eros')
        self.insertar_vertice('Himeros')
        
        self.insertar_vertice('Hermaphrodite')
        self.insertar_vertice('Pan')
        
        self.insertar_arista(1, 'Urano', 'Gaia', data={'relacion': ['hijo', 'madre', 'pareja']})
        
        self.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Hyperion', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Crios', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Rhea', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Urano', 'Tedds', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Gaia', 'Themis', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Hyperion', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Theia', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Crios', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Cronos', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Rhea', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Iapetos', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Okeanos', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Gaia', 'Tedds', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Hyperion', 'Theia', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Hyperion', 'Helios', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Hyperion', 'Eos', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Hyperion', 'Selene', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})
        
        self.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})
        
        
        self.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Okeanos', 'Pleione', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Tedds', 'Pleione', data={'relacion': ['madre', 'hijo']})
        

        self.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Cronos', 'Poseidon', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Cronos', 'Hestia', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Cronos', 'Hera', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Rhea', 'Hades', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Rhea', 'Demeter', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Rhea', 'Poseidon', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Rhea', 'Hestia', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Rhea', 'Hera', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Rhea', 'Zeus', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Kdios', 'Leto', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Phoibe', 'Leto', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Atlas', 'Pleione', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Atlas', 'Maia', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Pleione', 'Maia', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Demeter', 'Zeus', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Demeter', 'Persephone', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Zeus', 'Persephone', data={'relacion': ['padre', 'hijo']})
        
        
        self.insertar_arista(1, 'Hera', 'Zeus', data={'relacion': ['pareja', 'hermano']})
        
        self.insertar_arista(1, 'Hera', 'Ares', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Hera', 'Hephaistos', data={'relacion': ['madre', 'hijo']})
        
        self.insertar_arista(1, 'Zeus', 'Ares', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})
        
        
        self.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['pareja']})
        
        
        self.insertar_arista(1, 'Zeus', 'Leto', data={'relacion': ['pareja']})
        
        self.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Zeus', 'Artemis', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Leto', 'Apollo', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Leto', 'Artemis', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Zeus', 'Semelle', data={'relacion': ['pareja']})
        
        self.insertar_arista(1, 'Zeus', 'Dionysos', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Semelle', 'Dionysos', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Zeus', 'Maia', data={'relacion': ['pareja']})
        
        self.insertar_arista(1, 'Zeus', 'Hermes', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Maia', 'Hermes', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Hades', 'Persephone', data={'relacion': ['pareja']})
        
        
        self.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['pareja']})
        
        self.insertar_arista(1, 'Aphrodite', 'Phobos', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Aphrodite', 'Deimos', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Aphrodite', 'Eros', data={'relacion': ['padre', 'hijo']})
        self.insertar_arista(1, 'Aphrodite', 'Himeros', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Ares', 'Phobos', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Ares', 'Deimos', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Ares', 'Eros', data={'relacion': ['madre', 'hijo']})
        self.insertar_arista(1, 'Ares', 'Himeros', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Aphrodite', 'Hephaistos', data={'relacion': ['pareja']})
        
        
        self.insertar_arista(1, 'Aphrodite', 'Hermes', data={'relacion': ['pareja']})
        
        self.insertar_arista(1, 'Aphrodite', 'Hermaphrodite', data={'relacion': ['madre', 'hijo']})
        
        self.insertar_arista(1, 'Hermes', 'Hermaphrodite', data={'relacion': ['padre', 'hijo']})
        
        
        self.insertar_arista(1, 'Hermes', 'Penelopeia', data={'relacion': ['pareja']})
        
        self.insertar_arista(1, 'Hermes', 'Pan', data={'relacion': ['padre', 'hijo']})
        
        self.insertar_arista(1, 'Penelopeia', 'Pan', data={'relacion': ['madre', 'hijo']})
        
        
        self.insertar_arista(1, 'Themis', 'Minemosyne', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Hyperion', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Theia', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Crios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Cronos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Rhea', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Kdios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Phoibe', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Themis', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Minemosyne', 'Hyperion', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Theia', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Crios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Cronos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Rhea', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Kdios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Phoibe', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Minemosyne', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Hyperion', 'Crios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Cronos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Rhea', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Kdios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Phoibe', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hyperion', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Theia', 'Cronos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Theia', 'Rhea', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Theia', 'Kdios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Theia', 'Phoibe', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Theia', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Theia', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Theia', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Cronos', 'Kdios', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Cronos', 'Phoibe', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Cronos', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Cronos', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Cronos', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Kdios', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Kdios', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Kdios', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Phoibe', 'Iapetos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Phoibe', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Phoibe', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Iapetos', 'Okeanos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Iapetos', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Helios', 'Eos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Helios', 'Selene', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Eos', 'Selene', data={'relacion': ['hermano']})
        
        
        self.insertar_arista(1, 'Prometheus', 'Epimetheus', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Prometheus', 'Atlas', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Epimetheus', 'Atlas', data={'relacion': ['hermano']})

        
        self.insertar_arista(1, 'Hades', 'Demeter', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hades', 'Poseidon', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hades', 'Hestia', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hades', 'Hera', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hades', 'Zeus', data={'relacion': ['hermano']})
        

        self.insertar_arista(1, 'Demeter', 'Poseidon', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Demeter', 'Hestia', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Demeter', 'Hera', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Poseidon', 'Hestia', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Poseidon', 'Hera', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Poseidon', 'Zeus', data={'relacion': ['hermano']})

        self.insertar_arista(1, 'Hestia', 'Hera', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Hestia', 'Zeus', data={'relacion': ['hermano']})

        
        self.insertar_arista(1, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})
        
        
        self.insertar_arista(1, 'Apollo', 'Artemis', data={'relacion': ['hermano']})
        
        
        self.insertar_arista(1, 'Phobos', 'Deimos', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Phobos', 'Eros', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Phobos', 'Himeros', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Deimos', 'Eros', data={'relacion': ['hermano']})
        self.insertar_arista(1, 'Deimos', 'Himeros', data={'relacion': ['hermano']})
        
        self.insertar_arista(1, 'Eros', 'Himeros', data={'relacion': ['hermano']})