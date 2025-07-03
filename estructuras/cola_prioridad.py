class Nodo:
    def __init__(self, valor, prioridad):
        self.valor = valor
        self.prioridad = prioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.frente = None

    def insertar(self, valor, prioridad):
        nuevo = Nodo(valor, prioridad)

        if not self.frente or prioridad < self.frente.prioridad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def buscar(self, valor):
        actual = self.frente
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, _=None):
        if not self.frente:
            return False
        self.frente = self.frente.siguiente
        return True

    def mostrar(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(f"{actual.valor}({actual.prioridad})")
            actual = actual.siguiente
        print(" -> ".join(elementos) if elementos else "[vacía]")
