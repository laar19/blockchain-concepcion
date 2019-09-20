from lib.blockchain import*

# Crea un nuevo bloque
def generateBlock(bloque_anterior, walletSender=None, walletReceiver=None, amountSent=None):
    bloque = Block(bloque_anterior.index + 1)
    bloque.previousHash = bloque_anterior.currentHash

    return bloque

# Crea el bloque génesis
def createGenesisBlock():
    bloque_genesis = Block(0)
    bloque_genesis.data = "BLOQUE GÉNESIS"

    return bloque_genesis

# Funciones de validación
# Compara dos bloques
def isSameBlock(bloque1, bloque2):
    if bloque1.index != bloque2.index:
        return True
    elif bloque1.previousHash != bloque2.previousHash:
        return True
    elif bloque1.timestamp != bloque2.timestamp:
        return True
    elif bloque1.data != bloque2.data:
        return True
    elif bloque1.currentHash != bloque2.currentHash:
        return True

    return False

# Verifica la validez del nuevo bloque
def isValidNewBlock(previousBlock, newBlock):
    if previousBlock.index + 1 != newBlock.index:
        print('LOS ÍNDICES NO COINCIDEN')
        return False
    elif previousBlock.currentHash != newBlock.previousHash:
        print("EL HASH PREVIO NO CONCUERDA")
        return False

    return True

# Transacción
# Función que simula el envío de monedas de una cuenta a otra
# Reibe como parámetros la dirección de la billetera que envía,
# la dirección de la billetera que recibe y el monto a enviar
def transactionSent(walletSender, walletReceiver, amountSent):
    amountWalletSender     = walletSender.amount
    amountWalletReceiver   = walletReceiver.amount
    previousAmountSender   = walletSender.previousAmount
    previousAmountReceiver = walletReceiver.previousAmount

    previousAmountSender   = amountWalletSender
    previousAmountReceiver = amountWalletReceiver

    if(amountSent > amountWalletSender):
        amountWalletSender   -= amountSent
        amountWalletReceiver += amountSent
        print("\nTRANSACCIÓN FALLIDA")
        print("EL MONTO ENVIADO NO PUEDE SUPERAR EL MONTO POSEÍDO")

        return walletSender, walletReceiver, amountSent
    else:
        amountWalletSender           -= amountSent
        amountWalletReceiver         += amountSent
        walletSender.amount           = amountWalletSender
        walletReceiver.amount         = amountWalletReceiver
        walletSender.previousAmount   = previousAmountSender
        walletReceiver.previousAmount = previousAmountReceiver
        print("\nTRANSACCIÓN EXITOSA")

        return walletSender, walletReceiver, amountSent