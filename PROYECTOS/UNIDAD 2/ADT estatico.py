class conjunto_estatico:
    def __init__(self, elementos):
        if not isinstance(elementos, list):
            raise TypeError("Elementos debe ser una lista")
        self.elementos = elementos 

    def agregar(self, dato):
        if dato not in self.elementos:
            self.elementos.append(dato)

    def eliminar(self, dato):
        if dato in self.elementos:
            self.elementos.remove(dato)
        else:
            print("ERROR: El elemento no existe en el conjunto")

    def union(self, otro_conjunto):
        elementos_union = list(set(self.elementos) | set(otro_conjunto.elementos))
        return conjunto_estatico(elementos_union)

    def interseccion(self, otro_conjunto):
        elementos_interseccion = list(set(self.elementos) & set(otro_conjunto.elementos))
        return conjunto_estatico(elementos_interseccion)

    def diferencia(self, otro_conjunto):
        elementos_diferencia = list(set(self.elementos) - set(otro_conjunto.elementos))
        return conjunto_estatico(elementos_diferencia)

    def es_subconjunto(self, otro_conjunto):
        return set(self.elementos).issubset(set(otro_conjunto.elementos))

    def contiene(self, dato):
        return dato in self.elementos

    def __str__(self):
        return str(self.elementos)
    

vector1 = conjunto_estatico([5,6,7])
print("Conjunto estático con vector:", vector1)
vector1.agregar(10)
print("Conjunto estático con vector (agregado 10):", vector1)
vector1.eliminar(5)
print("Conjunto estático con vector (eliminado 5):", vector1)


vector2 = conjunto_estatico([7,8,9])

print("Unión:", vector1.union(vector2))
print("Intersección:", vector1.interseccion(vector2))
print("Diferencia:", vector1.diferencia(vector2))
print("¿Es subconjunto?:", vector1.es_subconjunto(vector2))
print("¿Contiene el elemento 7?:", vector1.contiene(7))