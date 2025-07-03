class TablaHashLinear:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.claves = [None] * capacidad

    def _hash(self, clave):
        return hash(clave) % self.capacidad

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        for i in range(self.capacidad):
            idx = (indice + i) % self.capacidad
            if self.claves[idx] is None or self.claves[idx] == clave:
                self.claves[idx] = clave
                self.tabla[idx] = valor
                return
        print("Tabla llena, no se pudo insertar.")

    def buscar(self, clave):
        indice = self._hash(clave)
        for i in range(self.capacidad):
            idx = (indice + i) % self.capacidad
            if self.claves[idx] is None:
                return None
            if self.claves[idx] == clave:
                return self.tabla[idx]
        return None

    def eliminar(self, clave):
        indice = self._hash(clave)
        for i in range(self.capacidad):
            idx = (indice + i) % self.capacidad
            if self.claves[idx] is None:
                return False
            if self.claves[idx] == clave:
                self.claves[idx] = None
                self.tabla[idx] = None
                return True
        return False

    def mostrar(self):
        for i in range(self.capacidad):
            if self.claves[i] is not None:
                print(f"[{i}]: ({self.claves[i]}: {self.tabla[i]})")
            else:
                print(f"[{i}]: vacío")
