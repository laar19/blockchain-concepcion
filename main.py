import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, previousHash, timestamp, data, currentHash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash

#lista donde se almacenará la cadena de bloques
VergBlockChain = [] #hay que trabajar los nombres desde el punto de vista del marketing xD

#hash del bloque creado
def blockHash(index, previousHash, timestamp, data):
    value = str(index) + str(previousHash) + str(timestamp) + str(data)
    sha = hashlib.sha256(value.encode("utf-8"))

    return sha.hexdigest()

#boque génesis
def createGenesisBlock():
    currentHash = blockHash(0, 0, datetime.now(), "BLOQUE GÉNESIS")

    return Block(0, 0, datetime.now(), "BLOQUE GÉNESIS", currentHash)

#inserción de un bloque en la blockchain
def insertNextBlock(blockChain):
    VergBlockChain.append(generateNextBlock(blockChain[-1]))

VergBlockChain.append(createGenesisBlock())

#información del último bloque insertado en la blockchain
def getLatestBlock():
    return VergBlockChain[len(VergBlockChain)-1]

#creación de un bloque nuevo
def generateNextBlock(last_block):
    this_index = last_block.index + 1
    previousHash = last_block.currentHash
    this_timestamp = datetime.now()
    this_data = "BLOQUE {}".format(this_index)
    this_hash = blockHash(this_index, previousHash, this_timestamp, this_data)

    f = open(this_hash, "w")
    f.write("this_hash = {}\nthis_index = {}\nthis_timestamp = {}\nthis_data = {}\npreviousHash = {}".format(this_hash, this_index, this_timestamp, this_data, previousHash))
    f.close()

    return Block(this_index, previousHash, this_timestamp, this_data, this_hash) 

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

#insertNextBlock(VergBlockChain)

for i in range(0, 10):
    insertNextBlock(VergBlockChain)
    print(isSameBlock(VergBlockChain[i], VergBlockChain[i+1]))
    print(isValidNewBlock(VergBlockChain[i], VergBlockChain[i+1]))

for item in VergBlockChain:
	print("\ndata: {}".format(item.data))
	print("currentHash: {}".format(item.currentHash))
	print("index: {}".format(item.index))
	print("time: {}".format(item.timestamp))
	print("previousHash: {}".format(item.previousHash))
