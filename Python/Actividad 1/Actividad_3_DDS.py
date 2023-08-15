def convertToBitcoin(bitcoins):
    bitcoinValue = 8258507.04
    monto = bitcoins*bitcoinValue
    return monto

print("Convertir a Bitcoin")
print("Ingrese la cantidad de bitcoins")
bitcoins = float(input())
monto = convertToBitcoin(bitcoins)

print("El monto en pesos es: $%.2f"%(monto))