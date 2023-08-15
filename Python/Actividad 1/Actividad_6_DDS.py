def calculateAmount(totalDiners):
    return (totalDiners * 0.7 * 2500)
def calculateAmountOfMeat(totalDiners):
    return (totalDiners * 0.7) 

print("Ingrese el total de comensales:")
totalDiners = int(input())
amount = calculateAmount(totalDiners)
amountOfMeat = calculateAmountOfMeat(totalDiners)
print("El monto a pagar es: $%.2f"%(amount))
print("La cantidad de carne a comprar es: %.2f kg"%(amountOfMeat))