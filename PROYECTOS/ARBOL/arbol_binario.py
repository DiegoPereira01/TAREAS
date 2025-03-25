class nodoarbol(object):
    dato = None
    izquierda= None
    derecha= None
class arbolbinario(object):
    def __init__(self):
        self.raiz = None
    def arbolvoid(self):
        return self.raiz == None
    def reiniciar(self):
        self.raiz = None
    def printer(self, option):
        cadena=""
        if option==0:
            cadena = self.__prefijo(self.raiz)
        elif option == 1:
            cadena = self.__postfijo(self.raiz)
        elif option == 2:
            cadena = self.__entrefijo(self.raiz)
        return cadena
    def __prefijo(self, subarbol):
        cadena= ""
        if subarbol != None:
            cadena += subarbol.dato + "\n" + self.__prefijo(subarbol.izquierda) + self.__prefijo(subarbol.derecha)
        return cadena
    def __postfijo(self, subarbol):
        cadena= ""
        if subarbol != None:
            cadena += self.__postfijo(subarbol.izquierda) + self.__postfijo(subarbol.derecha) + subarbol.dato + "\n"
        return cadena
    def __entrefijo(self, subarbol):
        cadena= ""
        if subarbol != None:
            cadena += self.__entrefijo(subarbol.izquierda) + subarbol.dato + "\n" + self.__entrefijo(subarbol.derecha)
        return cadena
    def insertar(self, dato):
        self.raiz = self.__insertar_nod(self.raiz, dato)
    def __insertar_nod(self, subarbol,dato):
        if subarbol == None:
            nod= nodoarbol()
            nod.dato= dato
            subarbol= nod
        else:
            if dato < subarbol.dato:
                subarbol.izquierda = self.__insertar_nod(subarbol.izquierda, dato)
            elif dato > subarbol.dato:
                subarbol.derecha = self.__insertar_nod(subarbol.derecha, dato)
        return subarbol


