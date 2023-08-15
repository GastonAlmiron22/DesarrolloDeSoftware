print("A continuacion se le solicitara que ingrese 5 temperaturas");
tempList = []

def averageTemp(tempList):
    num = 0 
    length = len(list)
    for i in range(length+1):
        num +=i
    prom = num/length
    return prom

for i in range(5):
    temp = float(input("Ingrese una temperatura: "))
    tempList.append(temp)

prom = averageTemp(tempList)
print("El promedio de temperaturas es: %.2f" %(prom))
