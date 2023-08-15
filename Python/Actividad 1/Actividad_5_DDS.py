def defineCategory(age):
    if age >= 13 and age < 15:
        return "Infantites"
    elif age >=15 and  age <17:
        return "Cadetes"
    elif age >=17 and  age <19:
        return "Juveniles"
    elif age > 19:
        return "Mayores"
    else:
        return None

name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
categoria = defineCategory(age)

print("Hola %s"%(name))
print("Su edad es %i"%(age))
if categoria:
    print("Su categoria es %s"%(categoria))
else:
    print("No existe categoria para su edad")
    