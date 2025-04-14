class conjunto:
    def __init__(self, elemento=None):
        if elemento is None:
            self.elemento = []
        else:
            self.elemento = list(elemento)

    def agregar(self, dato):
        if dato not in self.elemento:
            self.elemento.append(dato)

    def quitar(self, dato):
        if dato in self.elemento:
            self.elemento.remove(dato)

    def union(self, otro_conjunto):
        nuevo_conjunto = conjunto(self.elemento.copy())
        for elemento in otro_conjunto.elemento:
            nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto
    
    def interseccion(self, otro_conjunto):
        nuevo_conjunto = conjunto()
        for elemento in self.elemento:
            if elemento in otro_conjunto.elemento:
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto
    
    def diferencia(self, otro_conjunto):
        nuevo_conjunto = conjunto()
        for elemento in self.elemento:
            if elemento not in otro_conjunto.elemento:
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto
    
    def __str__(self):
        return "{" + ", ".join(map(str, self.elemento)) + "}"

if __name__ == "__main__":
    def menu():
        print("\n1. Agregar elemento conjunto 1")
        print("2. Agregar elemento conjunto 2")
        print("3. Quitar elemento conjunto 1")
        print("4. Quitar elemento conjunto 2")
        print("5. Unión")
        print("6. Intersección")
        print("7. Diferencia")
        print("8. Mostrar conjunto")
        print("9. Salir")
        return int(input("Seleccione una opción: "))

    conjunto1 = conjunto()
    conjunto2 = conjunto()

    while True:
        opcion = menu()
        if opcion == 1:
            dato = int(input("Ingrese el elemento a agregar al conjunto 1: "))
            conjunto1.agregar(dato)
            print(f"Conjunto 1: {conjunto1}")
        elif opcion == 2:
            dato = int(input("Ingrese el elemento a agregar al conjunto 2: "))
            conjunto2.agregar(dato)
            print(f"Conjunto 2: {conjunto2}")
        elif opcion == 3:
            dato = int(input("Ingrese el elemento a quitar del conjunto 1: "))
            conjunto1.quitar(dato)
            print(f"Conjunto 1: {conjunto1}")
        elif opcion == 4:
            dato = int(input("Ingrese el elemento a quitar del conjunto 2: "))
            conjunto2.quitar(dato)
            print(f"Conjunto 2: {conjunto2}")
        elif opcion == 5:
            conjunto_union = conjunto1.union(conjunto2)
            print(f"Unión de Conjunto 1 y Conjunto 2: {conjunto_union}")
        elif opcion == 6:
            conjunto_interseccion = conjunto1.interseccion(conjunto2)
            print(f"Intersección de Conjunto 1 y Conjunto 2: {conjunto_interseccion}")
        elif opcion == 7:
            conjunto_diferencia = conjunto1.diferencia(conjunto2)
            print(f"Diferencia de Conjunto 1 y Conjunto 2: {conjunto_diferencia}")
        elif opcion == 8:
            print(f"Conjunto 1: {conjunto1}")
            print(f"Conjunto 2: {conjunto2}")
        elif opcion == 9:
            print("Saliendo del programa...")
            break
        else:
            print("ERROR, opción no válida")