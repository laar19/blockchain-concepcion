import hashlib
from datetime import datetime

totalLochas = 100

class Wallet:
    def __init__(self, address, amount, timestamp, previousAmount):
        self.address = address
        self.amount = amount
        self.timestamp = timestamp
        self.previousAmount = previousAmount

luis = Wallet(0000, 100, 0, 0,)
ana = Wallet(1111, 0, 0, 0)

wallets = [luis, ana]

class Block:
    def __init__(self, index, previousHash, timestamp, data, currentHash, amountSent, addressSender, addressReceiver):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash
        self.amountSent = amountSent
        self.addressSender = addressSender
        self.addressReceiver = addressReceiver

def transactionSent(walletSender, walletReceiver, amountSent):
    amountWalletSender = walletSender.amount
    amountWalletReceiver = walletReceiver.amount
    previousAmountSender = walletSender.previousAmount
    previousAmountReceiver = walletReceiver.previousAmount

    previousAmountSender = amountWalletSender
    previousAmountReceiver = amountWalletReceiver

    if(amountSent > amountWalletSender):
        print("\n¡¡EL MONTO ENVIADO\nNO PUEDE SUPERAR EL MONTO POSEÍDO!!")
        amountWalletSender -= amountSent
        amountWalletReceiver += amountSent
        return walletSender, walletReceiver, amountSent
    else:
        amountWalletSender -= amountSent
        amountWalletReceiver += amountSent
        walletSender.amount = amountWalletSender
        walletReceiver.amount = amountWalletReceiver
        walletSender.previousAmount = previousAmountSender
        walletReceiver.previousAmount = previousAmountReceiver
        return walletSender, walletReceiver, amountSent

#lista donde se almacenará la cadena de bloques
VergBlockChain = [] #hay que trabajar los nombres desde el punto de vista del marketing xD

#hash del bloque creado
def blockHash(index, previousHash, timestamp, data):
    value = str(index) + str(previousHash) + str(timestamp) + str(data)
    sha = hashlib.sha256(value.encode("utf-8"))

    return sha.hexdigest()

#CREAR BLOQUE FÍSICO
#boque génesis
def createGenesisBlock():
    currentHash = blockHash(0, 0, datetime.now(), "BLOQUE GÉNESIS")

    return Block(0, 0, datetime.now(), "BLOQUE GÉNESIS", currentHash, 0, 0, 0)

#inserción de un bloque en la blockchain
def insertNextBlock(blockChain, walletSender, walletReceiver, amountSent):
    VergBlockChain.append(generateNextBlock(blockChain[-1], walletSender, walletReceiver, amountSent))

VergBlockChain.append(createGenesisBlock())

#información del último bloque insertado en la blockchain
def getLatestBlock():
    return VergBlockChain[len(VergBlockChain)-1]

#creación de un bloque nuevo
def generateNextBlock(last_block, walletSender, walletReceiver, amountSent):
    this_index = last_block.index + 1
    previousHash = last_block.currentHash
    this_timestamp = datetime.now()
    this_data = "BLOQUE {}".format(this_index)
    this_hash = blockHash(this_index, previousHash, this_timestamp, this_data)
    this_amountSent = amountSent
    this_addressSender = walletSender.address
    this_addressReceiver = walletReceiver.address

    f = open(this_hash, "w")
    f.write("this_hash = {}\nthis_index = {}\nthis_timestamp = {}\nthis_data = {}\npreviousHash = {}\nmonto enviado = {}\ndirección que envía = {}\ndirección que recibe = {}".format(this_hash, this_index, this_timestamp, this_data, previousHash, this_amountSent, this_addressSender, this_addressReceiver))
    f.close()

    return Block(this_index, previousHash, this_timestamp, this_data, this_hash, this_amountSent, this_addressSender, this_addressReceiver)

#VALIDACIONES
def isSameBlock(block1, block2):
    if block1.index != block2.index:
        return True
    elif block1.previousHash != block2.previousHash:
        return True
    elif block1.timestamp != block2.timestamp:
        return True
    elif block1.data != block2.data:
        return True
    elif block1.currentHash != block2.currentHash:
        return True
    return False

def isValidNewBlock(previousBlock, newBlock):
    if previousBlock.index + 1 != newBlock.index:
        print('LOS ÍNDICES NO COINCIDEN')
        return False
    elif previousBlock.currentHash != newBlock.previousHash:
        print("EL HASH PREVIO NO CONCUERDA")
        return False
    return True

"""
transactionSent(wallets[0], wallets[1], 101)

insertNextBlock(VergBlockChain, wallets[0], wallets[1], 101)
"""

wallet1, wallet2, amount = transactionSent(wallets[0], wallets[1], 101)

insertNextBlock(VergBlockChain, wallet1, wallet2, amount)

"""
for i in range(0, 10):
    insertNextBlock(VergBlockChain)
    print(isSameBlock(VergBlockChain[i], VergBlockChain[i+1]))
    print(isValidNewBlock(VergBlockChain[i], VergBlockChain[i+1]))
"""

for item in wallets:
	print("\naddress: {}".format(item.address))
	print("amount: {}".format(item.amount))
	print("time: {}".format(item.timestamp))
	print("previousAmount: {}".format(item.previousAmount))

for item in VergBlockChain:
	print("\ndata: {}".format(item.data))
	print("currentHash: {}".format(item.currentHash))
	print("index: {}".format(item.index))
	print("time: {}".format(item.timestamp))
	print("previousHash: {}".format(item.previousHash))
	print("monto enviado: {}".format(item.amountSent))
	print("dirección que envía: {}".format(item.addressSender))
	print("dirección que recibe: {}".format(item.addressReceiver))
