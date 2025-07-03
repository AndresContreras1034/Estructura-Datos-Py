class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def insertar(self, valor):  # push
        nuevo = Nodo(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def buscar(self, valor):
        actual = self.tope
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, _=None):  # pop
        if not self.tope:
            return False
        self.tope = self.tope.siguiente
        return True

    def mostrar(self):
        actual = self.tope
        elementos = []
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        print(" <- ".join(elementos) if elementos else "[vacía]")
