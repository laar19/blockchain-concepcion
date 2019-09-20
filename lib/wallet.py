class Wallet:
    def __init__(self, nombre, address, amount, timestamp, previousAmount):
        self.nombre         = nombre         # Nombre del dueño de la billetera
        self.address        = address        # Dirección de la billetera
        self.amount         = amount         # Total de monedas guardadas en la billetera
        self.timestamp      = timestamp      # Fecha en que se realiza la transacción
        self.previousAmount = previousAmount # Monto previo antes de la transacción