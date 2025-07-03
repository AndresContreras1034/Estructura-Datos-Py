class NodoBST:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if not nodo:
            return NodoBST(clave, valor)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar(nodo.izquierda, clave, valor)
        elif clave > nodo.clave:
            nodo.derecha = self._insertar(nodo.derecha, clave, valor)
        else:
            nodo.valor = valor  # actualizar
        return nodo

    def buscar(self, clave):
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        if not nodo:
            return None
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar(nodo.izquierda, clave)
        else:
            return self._buscar(nodo.derecha, clave)

    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if not nodo:
            return None
        if clave < nodo.clave:
            nodo.izquierda = self._eliminar(nodo.izquierda, clave)
        elif clave > nodo.clave:
            nodo.derecha = self._eliminar(nodo.derecha, clave)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            sucesor = self._minimo(nodo.derecha)
            nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.clave)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def mostrar(self):
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierda)
            print(f"{nodo.clave}: {nodo.valor}", end=" | ")
            self._inorden(nodo.derecha)

class TablaConArbol:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [ArbolBinario() for _ in range(capacidad)]

    def _hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        idx = self._hash(clave)
        self.tabla[idx].insertar(clave, valor)

    def buscar(self, clave):
        idx = self._hash(clave)
        return self.tabla[idx].buscar(clave)

    def eliminar(self, clave):
        idx = self._hash(clave)
        self.tabla[idx].eliminar(clave)

    def mostrar(self):
        for i, arbol in enumerate(self.tabla):
            print(f"[{i}]: ", end="")
            arbol.mostrar()
