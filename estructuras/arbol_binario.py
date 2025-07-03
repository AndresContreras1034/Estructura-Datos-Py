class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if not nodo:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if not nodo:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if not nodo:
            return None
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            # Nodo encontrado
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            # Nodo con dos hijos: buscar sucesor
            sucesor = self._minimo(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def mostrar(self):
        print("Inorden:", end=" ")
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquie_
