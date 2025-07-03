from estructuras.pila import Pila
from estructuras.cola import Cola
from estructuras.cola_prioridad import ColaPrioridad
from estructuras.arbol_binario import ArbolBinario
from estructuras.arbol_avl import ArbolAVL
from estructuras.arbol_rojo_negro import ArbolRojoNegro
from estructuras.arbol_b import ArbolB
from estructuras.tabla_hash import TablaHash
from estructuras.tabla_hash_linear import TablaHashLinear
from estructuras.tabla_arbol import TablaConArbol
from estructuras.grafo import Grafo

def menu_estructura():
    print("\n--- Menú Principal ---")
    print("1. Pila")
    print("2. Cola")
    print("3. Cola de Prioridad")
    print("4. Árbol Binario (BST)")
    print("5. Árbol AVL")
    print("6. Árbol Rojo-Negro")
    print("7. Árbol B")
    print("8. Tabla Hash (Encadenamiento)")
    print("9. Tabla Hash (Linear Probing)")
    print("10. Tabla con Árbol Binario")
    print("11. Grafo")
    print("0. Salir")
    return input("Seleccione una estructura: ")

def menu_operaciones():
    print("\nOperaciones:")
    print("1. Insertar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("0. Volver")
    return input("Seleccione una operación: ")

def ejecutar_operaciones(estructura):
    while True:
        op = menu_operaciones()
        match op:
            case "1":
                if isinstance(estructura, ColaPrioridad):
                    val = input("Valor: ")
                    prioridad = int(input("Prioridad: "))
                    estructura.insertar(val, prioridad)
                elif isinstance(estructura, Grafo):
                    origen = input("Origen: ")
                    destino = input("Destino: ")
                    estructura.insertar(origen, destino)
                elif isinstance(estructura, TablaHash | TablaHashLinear | TablaConArbol):
                    clave = input("Clave: ")
                    valor = input("Valor: ")
                    estructura.insertar(clave, valor)
                elif isinstance(estructura, ArbolB):
                    val = int(input("Valor: "))
                    estructura.insertar(val)
                else:
                    val = input("Valor: ")
                    estructura.insertar(val)
            case "2":
                if isinstance(estructura, Grafo):
                    origen = input("Origen: ")
                    destino = input("Destino: ")
                    encontrado = estructura.buscar(origen, destino)
                elif isinstance(estructura, TablaHash | TablaHashLinear | TablaConArbol):
                    clave = input("Clave: ")
                    encontrado = estructura.buscar(clave)
                else:
                    val = input("Valor: ")
                    encontrado = estructura.buscar(val)
                print("Encontrado" if encontrado else "No encontrado")
            case "3":
                if isinstance(estructura, Grafo):
                    tipo = input("¿Eliminar vértice (v) o arista (a)? ")
                    if tipo == "v":
                        nodo = input("Nodo: ")
                        estructura.eliminar_vertice(nodo)
                    else:
                        origen = input("Origen: ")
                        destino = input("Destino: ")
                        estructura.eliminar(origen, destino)
                elif isinstance(estructura, TablaHash | TablaHashLinear | TablaConArbol):
                    clave = input("Clave: ")
                    eliminado = estructura.eliminar(clave)
                    print("Eliminado" if eliminado else "No encontrado")
                else:
                    val = input("Valor: ")
                    estructura.eliminar(val)
            case "4":
                estructura.mostrar()
            case "0":
                break
            case _:
                print("Opción inválida")

def main():
    while True:
        opcion = menu_estructura()
        match opcion:
            case "1": ejecutar_operaciones(Pila())
            case "2": ejecutar_operaciones(Cola())
            case "3": ejecutar_operaciones(ColaPrioridad())
            case "4": ejecutar_operaciones(ArbolBinario())
            case "5": ejecutar_operaciones(ArbolAVL())
            case "6": ejecutar_operaciones(ArbolRojoNegro())
            case "7": ejecutar_operaciones(ArbolB())
            case "8": ejecutar_operaciones(TablaHash())
            case "9": ejecutar_operaciones(TablaHashLinear())
            case "10": ejecutar_operaciones(TablaConArbol())
            case "11": ejecutar_operaciones(Grafo())
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()
