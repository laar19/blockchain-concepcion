import hashlib
from datetime import datetime

# Bloque que contiene la transacción
class Block:
    def __init__(self, numero_bloque):
        self.index           = numero_bloque                  # Número cronológico del bloque
        self.previousHash    = None                           # Hash del bloque anterior
        self.timestamp       = datetime.now()                 # Fecha de creación del bloque
        self.data            = "BLOQUE {}".format(self.index) # Informaxión extra del bloque
        self.currentHash     = self.generateHash()            # Hash del bloque actual creado
        self.amountSent      = None                           # Monto enviado
        self.addressSender   = None                           # Wallet que envía
        self.addressReceiver = None                           # Wallet que recibe

    # Genera el hash del bloque recién creado
    def generateHash(self):
        value = str(self.index) + str(self.previousHash) + str(self.timestamp) + str(self.data)
        sha = hashlib.sha256(value.encode("utf-8"))

        return sha.hexdigest()

    # Crea un archivo de texto con la información del bloque recién creado
    def crea_archivo_texto(self):
        nombre_archivo = "BLOQUE " + str(self.index)
        archivo_de_texto = open(nombre_archivo, "w")
        archivo_de_texto.write("this_hash = {}\nthis_index = {}\nthis_timestamp = {}\nthis_data = {}\npreviousHash = {}".format(self.currentHash, self.index, self.timestamp, self.data, self.previousHash))
        archivo_de_texto.close()

    # Inserta el bloque en la blockchain
    def blockchain_append(self, blockchain):
        blockchain.append(self)