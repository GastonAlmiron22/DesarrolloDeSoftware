from random import randint

print("Bienvenido/a a la APP de numeros aleatorios")

def generateRandomNumberList():
    numList = []
    for i in range(10):
        numList.append(randint(1, 20))
    return numList

def countAmount(num):
    amount = 0
    for i in range(10):
        if numList[i] > num:
            amount += 1
    return amount

def calculateAvarege(numList):
    sum = 0
    for i in range(10):
        sum += numList[i]
    return sum / 10

def defineMaxAndMin(numList):
    max = numList[0]
    min = numList[0]
    for i in range(10):
        if numList[i] > max:
            max = numList[i]
        if numList[i] < min:
            min = numList[i]
    return (max, min)
numList = generateRandomNumberList()
print("La lista de numeros aleatorios es: ", numList)

num = int(input("Ingrese un numero: "))
amount = countAmount(num)
print("La cantidad de numeros mayores a ", num, " es: ", amount)

avarege = calculateAvarege(numList)
print("El promedio de la lista es: ", avarege)

max,min= defineMaxAndMin(numList)
print("El numero mayor de la lista es: ", max , " y el menor es: ", min)