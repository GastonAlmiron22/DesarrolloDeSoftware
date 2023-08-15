def calculateDeduction(price):
    if(price >= 3500):
        return (price -(price * 0.10))
    else:
        return price

print("Ingrese el total a pagar")
price = float(input())
price = calculateDeduction(price)
print("El total a pagar es: $%.2f"%(price))