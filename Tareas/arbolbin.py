class Nodo_binario:

    def __init__(self, valor=None, nod=None, es_raiz=False, es_izquierda=False, es_derecha=False):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.nod = nod
        self.es_raiz = es_raiz
        self.es_izquierda = es_izquierda
        self.es_derecha = es_derecha


class arbolbin:

    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz == None

    def __lugar(self, valor):
        aux = self.raiz
        while aux != None:
            temp = aux
            if valor <= aux.valor:
                aux = aux.izquierda
            else:
                aux = aux.derecha
        return temp

    def agregar_valor(self, valor):
        if self.vacio():
            self.raiz = Nodo_binario(valor=valor, es_raiz=True)
        else:
            nodo = self.__lugar(valor)
            if valor <= nodo.valor:
                nodo.izquierda = Nodo_binario(
                    valor=valor, nod=nodo, es_izquierda=True)
            else:
                nodo.derecha = Nodo_binario(valor=valor, nod=nodo, es_derecha=True)

    def recorrer_ordenado(self, node):
        if node:
            self.recorrer_ordenado(node.izquierda)
            print(node.valor)
            self.recorrer_ordenado(node.derecha)
            
    def recorrer_arbol(self, node):
        if node:
            print(node.valor)
            self.recorrer_arbol(node.izquierda)
            self.recorrer_arbol(node.derecha)
            

    def buscar(self, nodo, valor):
        if nodo == None:
            return None
        else:
            if nodo.valor == valor:
                return nodo
            elif valor <= nodo.valor:
                return self.buscar(nodo.izquierda, valor)
            else:
                return self.buscar(nodo.derecha, valor)


if __name__ == "__main__":

    def menu():
        opc = 0
        arbol_binario = arbolbin()
        try:
            while opc != 5:
                print("\nDiccionario Artículos\n"
                      + "\n\t1. Agregar"
                      + "\n\t2. Recorrer"
                      + "\n\t3. Recorrer en orden"
                      + "\n\t4. Buscar"
                      + "\n\t5. Salir")

                opc = int(input("Ingrese su opción "))

                if opc == 1:
                    dato = int(input("Ingrese el dato a anexar al arbol "))
                    arbol_binario.agregar_valor(dato)
                elif opc == 2:
                    arbol_binario.recorrer_arbol(arbol_binario.raiz)
                elif opc == 3:
                    arbol_binario.recorrer_ordenado(arbol_binario.raiz)
                elif opc == 4:
                    dato = int(input("Ingrese el dato a buscar en el arbol "))
                    print(arbol_binario.buscar(arbol_binario.raiz, dato))
                elif opc == 5:
                    print("Adios")
                else:
                    print("Ingresaste una opción errónea")
        except Exception as e:
            print("\n Solo se permiten caracteres numéricos")
            print(e)

    menu()