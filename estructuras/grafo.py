class Grafo:
    def __init__(self, dirigido=False):
        self.vertices = {}
        self.dirigido = dirigido

    def insertar(self, origen, destino):
        if origen not in self.vertices:
            self.vertices[origen] = set()
        if destino not in self.vertices:
            self.vertices[destino] = set()

        self.vertices[origen].add(destino)
        if not self.dirigido:
            self.vertices[destino].add(origen)

    def buscar(self, origen, destino):
        if origen in self.vertices and destino in self.vertices[origen]:
            return True
        return False

    def eliminar(self, origen, destino):
        if origen in self.vertices and destino in self.vertices[origen]:
            self.vertices[origen].remove(destino)
        if not self.dirigido and destino in self.vertices and origen in self.vertices[destino]:
            self.vertices[destino].remove(origen)

    def eliminar_vertice(self, nodo):
        if nodo in self.vertices:
            del self.vertices[nodo]
        for v in self.vertices:
            self.vertices[v].discard(nodo)

    def mostrar(self):
        for vertice, adyacentes in self.vertices.items():
            print(f"{vertice}: {', '.join(str(v) for v in adyacentes)}")
