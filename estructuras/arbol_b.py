class NodoB:
    def __init__(self, t, hoja=True):
        self.t = t  # mínimo grado
        self.hoja = hoja
        self.llaves = []
        self.hijos = []

class ArbolB:
    def __init__(self, t=3):
        self.raiz = NodoB(t)

    def insertar(self, valor):
        raiz = self.raiz
        if len(raiz.llaves) == 2 * raiz.t - 1:
            nueva = NodoB(raiz.t, hoja=False)
            nueva.hijos.insert(0, raiz)
            self._dividir_hijo(nueva, 0)
            self._insertar_no_lleno(nueva, valor)
            self.raiz = nueva
        else:
            self._insertar_no_lleno(raiz, valor)

    def _insertar_no_lleno(self, nodo, valor):
        i = len(nodo.llaves) - 1
        if nodo.hoja:
            nodo.llaves.append(None)
            while i >= 0 and valor < nodo.llaves[i]:
                nodo.llaves[i + 1] = nodo.llaves[i]
                i -= 1
            nodo.llaves[i + 1] = valor
        else:
            while i >= 0 and valor < nodo.llaves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].llaves) == 2 * nodo.t - 1:
                self._dividir_hijo(nodo, i)
                if valor > nodo.llaves[i]:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], valor)

    def _dividir_hijo(self, padre, i):
        t = padre.t
        y = padre.hijos[i]
        z = NodoB(t, y.hoja)
        padre.hijos.insert(i + 1, z)
        padre.llaves.insert(i, y.llaves[t - 1])
        z.llaves = y.llaves[t:]
        y.llaves = y.llaves[:t - 1]
        if not y.hoja:
            z.hijos = y.hijos[t:]
            y.hijos = y.hijos[:t]

    def buscar(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz
        i = 0
        while i < len(nodo.llaves) and valor > nodo.llaves[i]:
            i += 1
        if i < len(nodo.llaves) and valor == nodo.llaves[i]:
            return True
        if nodo.hoja:
            return False
        return self.buscar(valor, nodo.hijos[i])

    def mostrar(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + str(nodo.llaves))
        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)

    def eliminar(self, valor):
        print("Eliminar no implementado aún para B-Tree.")
