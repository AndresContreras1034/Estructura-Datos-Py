class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad

    def _hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        nodo = self.tabla[indice]
        if not nodo:
            self.tabla[indice] = Nodo(clave, valor)
            return
        while True:
            if nodo.clave == clave:
                nodo.valor = valor  # actualizar
                return
            if not nodo.siguiente:
                break
            nodo = nodo.siguiente
        nodo.siguiente = Nodo(clave, valor)

    def buscar(self, clave):
        indice = self._hash(clave)
        nodo = self.tabla[indice]
        while nodo:
            if nodo.clave == clave:
                return nodo.valor
            nodo = nodo.siguiente
        return None

    def eliminar(self, clave):
        indice = self._hash(clave)
        nodo = self.tabla[indice]
        anterior = None
        while nodo:
            if nodo.clave == clave:
                if anterior:
                    anterior.siguiente = nodo.siguiente
                else:
                    self.tabla[indice] = nodo.siguiente
                return True
            anterior = nodo
            nodo = nodo.siguiente
        return False

    def mostrar(self):
        for i, nodo in enumerate(self.tabla):
            print(f"[{i}]:", end=" ")
            actual = nodo
            while actual:
                print(f"({actual.clave}: {actual.valor})", end=" -> ")
                actual = actual.siguiente
            print("None")
