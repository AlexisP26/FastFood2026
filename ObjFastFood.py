class Pedido:

    Estado_Pendiente = 0
    Estado_Atendido = 1

    def __init__(self, numero, tipo, tamano, cantidad, precio_unitario):
        self.numero = numero
        self.tipo = tipo
        self.tamano = tamano
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.estado = Pedido.Estado_Pendiente

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    def cambiar_estado(self):
        self.estado = Pedido.Estado_Atendido