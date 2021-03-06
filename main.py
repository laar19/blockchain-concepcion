from lib.funciones import*
from lib.wallet import*

# Inicialización
blockChain = list()                   		 # Lista donde se almacenará la cadena de bloques
bloque_genesis = createGenesisBlock()
bloque_genesis.blockchain_append(blockChain) # Crea el bloque génesis y lo inserta en la blockchain
bloque_genesis.crea_archivo_texto()

#totalLochas = 100					   # Total de monedas creadas. Se agregará esta función a futuro
luis = Wallet("Luis", 1111, 100, 0, 0) # Billetera de Luis
ana  = Wallet("Ana", 2222, 0, 0, 0)    # Billetera de Ana
wallets = [luis, ana]

# Creación de unos bloques de ejemplo
# Ciclo que crea 10 bloques en la blockchain
for i in range(0, 10):
    bloque = generateBlock(blockChain[-1])
    
    # Inserta el bloque en la blockchain
    bloque.blockchain_append(blockChain)
    bloque.crea_archivo_texto()

    print(isSameBlock(blockChain[i], blockChain[i+1]))
    print(isValidNewBlock(blockChain[i], blockChain[i+1]))

# Muestra la información de los bloques de la blockchain
for item in blockChain:
	print("\ndata:               {}".format(item.data))
	print("currentHash:          {}".format(item.currentHash))
	print("index:                {}".format(item.index))
	print("time:                 {}".format(item.timestamp))
	print("previousHash:         {}".format(item.previousHash))
	print("monto enviado:        {}".format(item.amountSent))
	print("dirección que envía:  {}".format(item.addressSender))
	print("dirección que recibe: {}".format(item.addressReceiver))

# Transacción de ejemplo
# Envío de monedas de una billetera a otra
wallet1, wallet2, amount = transactionSent(wallets[0], wallets[1], 50)  # Transacción correcta
bloque = generateBlock(blockChain[-1], wallet1, wallet2, amount)    	# Crea el bloque con la transacción anterior
bloque.amountSent = amount
bloque.addressSender = wallet1.address
bloque.addressReceiver = wallet2.address
bloque.blockchain_append(blockChain)
bloque.crea_archivo_texto()

wallet1, wallet2, amount = transactionSent(wallets[0], wallets[1], 101) # Transacción fallida
bloque = generateBlock(blockChain[-1], wallet1, wallet2, amount)    	# Crea el bloque con la transacción anterior
bloque.amountSent = amount
bloque.addressSender = wallet1.address
bloque.addressReceiver = wallet2.address
bloque.blockchain_append(blockChain)
bloque.crea_archivo_texto()

# Información de las carteras
for item in wallets:
	print("\nnombre:	   {}".format(item.nombre))
	print("address: 	   {}".format(item.address))
	print("amount:		   {}".format(item.amount))
	print("time: 		   {}".format(item.timestamp))
	print("previousAmount: {}".format(item.previousAmount))