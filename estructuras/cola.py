class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def insertar(self, valor):  # enqueue
        nuevo = Nodo(valor)
        if not self.final:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def buscar(self, valor):
        actual = self.frente
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, _=None):  # dequeue
        if not self.frente:
            return False
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        return True

    def mostrar(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        print(" -> ".join(elementos) if elementos else "[vacía]")
