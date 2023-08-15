import random

def generateAthletesList():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	athletesList = []
	names = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	lastNames = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"name": random.choice(names)+" "+random.choice(lastNames),
			"number": i,
			"timeOfArrival": random.random()*120
		}
		athletesList.append(atleta)
	return athletesList

def showAthletesList(athletesList):
    print("Lista de atletas con tiempos de llegada en segundos:\n")
    for athlet in athletesList:
        print(f"{athlet['number']} {athlet['name']} {athlet['timeOfArrival']:.2f} segundos")
    print("\n")

def selectWiner(athletesList):
    winer = athletesList[0]
    for athlet in athletesList:
        if athlet['timeOfArrival'] < winer['timeOfArrival']:
            winer = athlet
    return winer

def searchAthlet(AthletNumber):
    for athlet in athletesList:
        if athlet['number'] == AthletNumber:
            return athlet
    return None

def ShowNumberWiners(oldAthletesList):
    athletesList = sorted(oldAthletesList,key=lambda athlet: athlet['timeOfArrival'])
    winers = []
    for i in range(3):
        winers.append(athletesList[i])
    return winers

athletesList = generateAthletesList()
showAthletesList(athletesList)

winer = selectWiner(athletesList)
print(f"El ganador es: {winer['name']} con un tiempo de {winer['timeOfArrival']:.2f} segundos \n")

athletNumber = int(input("Ingrese el número de atleta: "))
athlet = searchAthlet(athletNumber)
if athlet:
    print(f"A seleccionado a {athlet['name']} con un tiempo de {athlet['timeOfArrival']:.2f} segundos\n")
else:
    print("No existe un atleta con ese número")

winers = ShowNumberWiners(athletesList)
print("Los tres primeros atletas son:")
for i in range(3):
    print(f"{i+1} {winers[i]['name']} con un tiempo de {winers[i]['timeOfArrival']:.2f} segundos")