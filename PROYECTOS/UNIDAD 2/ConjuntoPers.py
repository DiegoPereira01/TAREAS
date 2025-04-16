import pickle
import os

class ConjuntoPers:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                self.elementos = pickle.load(f)
        else:
            self.elementos = set()

    def guardar(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.elementos, f)
            
    def agregar(self, dato):
        self.elementos.add(dato)
        self.guardar()

    def eliminar(self, dato):
        if dato in self.elementos:
            self.elementos.remove(dato)
            self.guardar()

    def contiene(self, dato):
        return dato in self.elementos

    def union(self, otro_conjunto):
        nuevo_conjunto = ConjuntoPers(self.filename + '_union')
        nuevo_conjunto.elementos = self.elementos.union(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    def interseccion(self, otro_conjunto):
        nuevo_conjunto = ConjuntoPers(self.filename + '_interseccion')
        nuevo_conjunto.elementos = self.elementos.intersection(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto


    def diferencia(self, otro_conjunto):
        nuevo_conjunto = ConjuntoPers(self.filename + '_diferencia')
        nuevo_conjunto.elementos = self.elementos.difference(otro_conjunto.elementos)
        nuevo_conjunto.guardar()
        return nuevo_conjunto

    

    def mostrar(self):
        print(self.elementos)

if __name__ == "__main__":
    def menu():
        print("\n1. Agregar datos al conjunto 1")
        print("2. Agregar datos al conjunto 2")
        print("3. Quitar datos al conjunto 1")
        print("4. Quitar datos al conjunto 2")
        print("5. Unión")
        print("6. Intersección")
        print("7. Diferencia")
        print("8. Mostrar conjuntos")
        print("9. Eliminar conjunto 1")
        print("10. Eliminar conjunto 2")
        print("11. Salir") 
        return int(input("Seleccione una opción: "))

    conjunto1 = ConjuntoPers('conjunto1.dat')
    conjunto2 = ConjuntoPers('conjunto2.dat')

    while True:
        opcion = menu()
        if opcion == 1:
            dato = int(input("Ingresar el dato a agregar al conjunto 1: "))
            conjunto1.agregar(dato)
            print("Conjunto 1:")
            conjunto1.mostrar()
        elif opcion == 2:
            dato = int(input("Ingresar el dato a agregar al conjunto 2: "))
            conjunto2.agregar(dato)
            print("Conjunto 2:")
            conjunto2.mostrar()
        elif opcion == 3:
            dato = int(input("Ingresar el dato a quitar del conjunto 1: "))
            conjunto1.eliminar(dato)
            print("Conjunto 1:")
            conjunto1.mostrar()
        elif opcion == 4:
            dato = int(input("Ingresar el dato a quitar del conjunto 2: "))
            conjunto2.eliminar(dato)
            print("Conjunto 2:")
            conjunto2.mostrar()
        elif opcion == 5:
            conjunto_union = conjunto1.union(conjunto2)
            print("Unión de conjuntos:")
            conjunto_union.mostrar()
        elif opcion == 6:
            conjunto_interseccion = conjunto1.interseccion(conjunto2)
            print("Intersección de conjuntos:")
            conjunto_interseccion.mostrar()
        elif opcion == 7:
            conjunto_diferencia = conjunto1.diferencia(conjunto2)
            print("Diferencia de conjuntos (Conjunto 1 - Conjunto 2):")
            conjunto_diferencia.mostrar()
        elif opcion == 8:
            print("Conjunto 1:")
            conjunto1.mostrar()
            print("Conjunto 2:")
            conjunto2.mostrar()
        elif opcion == 9:
            conjunto1 = ConjuntoPers('conjunto1.dat') 
            conjunto1.elementos.clear()
            conjunto1.guardar()
            print("Conjunto 1 eliminado...")
        elif opcion == 10:
            conjunto2 = ConjuntoPers('conjunto2.dat')  
            conjunto2.elementos.clear()
            conjunto2.guardar()
            print("Conjunto 2 eliminado...")
        elif opcion == 11:
            print("saliendo...")
            break
        else:
            print("Error, intente denuevo...")