menu = [
    'Ingresar valor 1',
    'Ingresar valor 2',
    'Mostrar suma',
    'Mostrar resta',
    'Mostrar multiplicación',
    'Mostrar división',
    'salir'
];
firstNum = 0;
secondNum = 0;

def calculateOperation(_firstNum,_secondNum,operation):
    global firstNum, secondNum
    if(operation == 1):
        firstNum = int(input("Ingrese el primer valor: "))
        showMenu()
    elif(operation == 2):
        secondNum = int(input("Ingrese el segundo valor: "))
        showMenu()
    elif(operation == 3):
        return (_firstNum + _secondNum)
    elif(operation == 4):
        return (_firstNum - _secondNum)
    elif(operation == 5):
        return (_firstNum * _secondNum)
    elif(operation == 6):
        if (_secondNum != 0):
            return (_firstNum / _secondNum)
        else:
            return None
    elif(operation == 7):
        print("Adios \n")
        return None
    else:
        return None


def showMenu():
    print("\n Menu de opciones:")
    for i in range(0,len(menu)):
        print(f"{i+1}: {menu[i]}")
    numberSelected = int(input())
    result = calculateOperation(firstNum,secondNum,numberSelected)
    if(result == "exit"):
        return
    elif(result):
        print(f"El resultado es {result}")
        showMenu()
    else:
        print("Opcion no valida")
        showMenu()

firstNum = int(input("Ingrese el primer valor: "))
secondNum = int(input("Ingrese el segundo valor: \n"))
showMenu()
