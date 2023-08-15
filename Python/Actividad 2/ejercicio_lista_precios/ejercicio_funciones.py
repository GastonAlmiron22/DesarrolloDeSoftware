# -*- coding: utf-8 -*-
# TODO #1a: importar  el modulo db_productos
import db_productos

products = []
# TODO #1b: cargar la lista de productos con la función
#          cargar_productos() del módulo db_productos.
products = db_productos.cargar_productos()

# TODO #2: definir una función mostrar_productos()
#          que reciba la lista de productos, no retorne nada,
#          y muestre la lista utilizando el siguiente formato para cada producto:
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# ...
def showProducts():
    for product in products:
        print(f"Producto {product['id']}")
        print(f"{product['nombre']} ${product['precio']}")
        print("---")

# TODO #3: definir una función calcular_precio_actualizado()
#          que reciba: el precio anterior y porcentaje de aumento
#          y retorne: el precio con el aumento.
def calculatePrice(price, percent):
    return (price + (percent * price / 100))


# TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y 
#          el porcentaje de aumento. La función debe recorrer cada producto de la
#          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
#          el precio del producto y el porcentaje de aumento) para obtener el precio
#          actualizado y modifique la lista "in-place" actualizando el precio de cada
#          producto. La función no debe retornar nada sino dejar modificada la lista
#          pasada por el usuario.
def updatePrices(products, percent):
    for product in products:
        oldPrice = product['precio']
        product['precio'] = calculatePrice(oldPrice, percent)

if __name__ == '__main__':
    # TODO #5a: mostrar la lista cargada
    showProducts()

    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
    percent = int(input("Ingrese el porcentaje de aumento: "))

    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
    updatePrices(products, percent)
    # TODO #5d: mostrar la lista con los precios actualizados
    print("La lista de precios actualizada es:")
    showProducts()