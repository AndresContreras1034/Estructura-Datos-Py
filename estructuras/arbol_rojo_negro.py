ROJO = True
NEGRO = False

class NodoRBN:
    def __init__(self, valor, color=ROJO):
        self.valor = valor
        self.color = color
        self.izquierda = None
        self.derecha = None

class ArbolRojoNegro:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)
        self.raiz.color = NEGRO

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoRBN(valor)
        
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        if self._es_rojo(nodo.derecha) and not self._es_rojo(nodo.izquierda):
            nodo = self._rotar_izquierda(nodo)
        if self._es_rojo(nodo.izquierda) and self._es_rojo(nodo.izquierda.izquierda):
            nodo = self._rotar_derecha(nodo)
        if self._es_rojo(nodo.izquierda) and self._es_rojo(nodo.derecha):
            self._cambiar_colores(nodo)

        return nodo

    def _es_rojo(self, nodo):
        return nodo is not None and nodo.color == ROJO

    def _rotar_izquierda(self, h):
        x = h.derecha
        h.derecha = x.izquierda
        x.izquierda = h
        x.color = h.color
        h.color = ROJO
        return x

    def _rotar_derecha(self, h):
        x = h.izquierda
        h.izquierda = x.derecha
        x.derecha = h
        x.color = h.color
        h.color = ROJO
        return x

    def _cambiar_colores(self, nodo):
        nodo.color = ROJO
        nodo.izquierda.color = NEGRO
        nodo.derecha.color = NEGRO

    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return False

    def mostrar(self):
        print("Inorden:", end=" ")
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierda)
            print(f"{nodo.valor}({'R' if nodo.color else 'N'})", end=" ")
            self._inorden(nodo.derecha)
