clientes = {}
def menu():
    print("Bienvenido al cliente del usuario")
    print("1.Ingreso de cliente")
    print("2.Mostrar")
    print("3.Salir")
    op = int(input("Ingrese su opción"))

    if op == "1":
        cantidad = int(input("Ingrese la cantidad de clientes: "))
        for i in range(cantidad):
            print(f"Cliente:{i+1}")
            while True:
                print("ingrese codigo del cliente: ")
                codigo = input()
                if codigo in clientes:
                    print(f"El cliente ya existe")
                else:
                    clientes[codigo] = {}
                clientes[codigo]["nombre"] = input("Ingrese el nombre del cliente: ")
                clientes[codigo]["viajes"] = {}
                cantiviaje = int(input("Ingrese la cantidad de viajes: "))
                for i in range(cantiviaje):
                    print(f"Destino:{i+1}")
                    nombredestino = input("Ingrese el nombre del destino: ")
                    clientes[codigo]["viajes"][nombredestino] = {}