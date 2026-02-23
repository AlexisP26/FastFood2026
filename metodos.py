from ObjFastFood import Pedido


# VALIDACIONES
def validar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido")


def validar_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un número válido")


# MOSTRAR MENU DE PRODUCTOS
def mostrar_menu_productos(menu):
    print("\n===== MENU DE PRODUCTOS =====")
    for i in range(len(menu)):
        print(i + 1, ")",
              menu[i][0],
              "- Tamaño:", menu[i][1],
              "- Precio:", menu[i][2])


# CREAR MATRIZ VACÍA
def crear_matriz_vacia(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(None)
        matriz.append(fila)
    return matriz


# CREAR PEDIDO DESDE MENU
def crear_pedido(menu, numero):
    mostrar_menu_productos(menu)

    opcion = validar_entero("Seleccione producto: ")

    if opcion < 1 or opcion > len(menu):
        print("Opción inválida")
        return None

    producto = menu[opcion - 1]

    tipo = producto[0]
    tamano = producto[1]
    precio = producto[2]

    cantidad = validar_entero("Cantidad: ")

    pedido = Pedido(numero, tipo, tamano, cantidad, precio)

    return pedido


# BUSCAR PEDIDO
def buscar_pedido(matriz, numero):
    for fila in matriz:
        for pedido in fila:
            if pedido is not None:
                if pedido.numero == numero:
                    return pedido
    return None


# MOSTRAR UN PEDIDO
def mostrar_pedido(pedido):
    if pedido is None:
        print("Pedido no encontrado")
        return

    print("Número:", pedido.numero)
    print("Tipo:", pedido.tipo)
    print("Tamaño:", pedido.tamano)
    print("Cantidad:", pedido.cantidad)
    print("Precio unitario:", pedido.precio_unitario)
    print("Total:", pedido.calcular_total())

    if pedido.estado == Pedido.Estado_Pendiente:
        print("Estado: Pendiente")
    else:
        print("Estado: Atendido")


# MOSTRAR TODOS
def mostrar_todos(matriz):
    for fila in matriz:
        for pedido in fila:
            if pedido is not None:
                mostrar_pedido(pedido)
                print("--------------------")


# CAMBIAR ESTADO
def cambiar_estado(matriz, numero):
    pedido = buscar_pedido(matriz, numero)

    if pedido is not None:
        pedido.cambiar_estado()
        print("Estado actualizado")
    else:
        print("Pedido no encontrado")


# ELIMINAR PEDIDO
def eliminar_pedido(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] is not None:
                if matriz[i][j].numero == numero:
                    matriz[i][j] = None
                    print("Pedido eliminado")
                    return

    print("Pedido no encontrado")