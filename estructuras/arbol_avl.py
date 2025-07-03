class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        else:
            return nodo  # Valor duplicado, no se inserta

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        balance = self._balance(nodo)

        # Rotaciones
        if balance > 1 and valor < nodo.izquierda.valor:
            return self._rotar_derecha(nodo)
        if balance < -1 and valor > nodo.derecha.valor:
            return self._rotar_izquierda(nodo)
        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if not nodo:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if not nodo:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            temp = self._minimo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        balance = self._balance(nodo)

        if balance > 1 and self._balance(nodo.izquierda) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.derecha) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.derecha) > 0:
            nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)

        return nodo

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha) if nodo else 0

    def _rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha = T2
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

    def _rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        return y

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
            self._inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden(nodo.derecha)
