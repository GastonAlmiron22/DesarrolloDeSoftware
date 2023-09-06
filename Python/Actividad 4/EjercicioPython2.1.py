import random

numList=[]
def generateNumberList():
    for i in range(1,10):
        num = random.randint(1, 20) 
        numList.apend(num)

generateNumberList()
print(numList)
