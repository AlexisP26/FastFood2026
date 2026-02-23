from metodos import *
from ObjFastFood import Pedido
from Catalogo import menu_productos

def main():

    # CATÁLOGO INTERNO (MATRIZ DE PRODUCTOS)
    menu_productos = [
        ["Perro", 1, 8000],
        ["Perro", 2, 10000],
        ["Perro", 3, 12000],
        ["Hamburguesa", 1, 12000],
        ["Hamburguesa", 2, 15000],
        ["Hamburguesa", 3, 18000],
        ["Salchipapa", 1, 9000],
        ["Salchipapa", 2, 11000],
        ["Salchipapa", 3, 13000]
    ]

    filas = validar_entero("Filas de la matriz: ")
    columnas = validar_entero("Columnas de la matriz: ")

    matriz = crear_matriz_vacia(filas, columnas)

    numero = 1

    while True:

        print("\n===== SISTEMA FASTFOOD =====")
        print("1) Crear pedido")
        print("2) Mostrar todos")
        print("3) Buscar pedido")
        print("4) Cambiar estado")
        print("5) Eliminar pedido")
        print("6) Salir")

        opcion = validar_entero("Seleccione opción: ")

        if opcion == 1:

            for i in range(len(matriz)):
                for j in range(len(matriz[i])):

                    if matriz[i][j] is None:
                        pedido = crear_pedido(menu_productos, numero)

                        if pedido is not None:
                            matriz[i][j] = pedido
                            numero += 1
                            print("Pedido creado")
                            break
                else:
                    continue
                break

        elif opcion == 2:
            mostrar_todos(matriz)

        elif opcion == 3:
            num = validar_entero("Número de pedido: ")
            pedido = buscar_pedido(matriz, num)
            mostrar_pedido(pedido)

        elif opcion == 4:
            num = validar_entero("Número de pedido: ")
            cambiar_estado(matriz, num)

        elif opcion == 5:
            num = validar_entero("Número de pedido: ")
            eliminar_pedido(matriz, num)

        elif opcion == 6:
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()