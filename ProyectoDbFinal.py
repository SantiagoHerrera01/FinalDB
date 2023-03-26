import mysql.connector  

def conectar ():
    global mydb
    global cursor
    mydb = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "",
        database = "tienda",
    )
    cursor = mydb.cursor()

def menu2 (isActived,cursor):
    while isActived == True:
        print("Bienvenido... " + name)
        opcMenu2 = input("Seleccione una opción:  \n 1.1. Ver Usuarios \n 1.2. Modificar Usuarios \n 1.3. Eliminar Usuarios \n"
                         + "2.1. Crear Producto \n 2.2. Ver Productos \n 2.3. Buscar Productos \n"
                         + "3.1. Registrar Venta \n 3.2. Imprimir Factura De Ventas\n 3.3. Ver compras por cliente \n"
                         +"4. Salir/Volver al menu \n")
        match opcMenu2:
            case "1.1":
                print("Listado usuarios")
                cursor.excecute("SHOW TABLES")
                for X in cursor:
                    print(X)
                pass
            case "1.2":
                
                print("Modificar Usuario")
                nombre_Usuario = input("Nombre Usuario: ")
                apellido = input("Apellido Usuario: ")
                pass
            case "1.3":
                print("Eliminar Usuario")
                pass
            case "2.1":
                print("Crear Producto")
                pass
            case "2.2":
                print("Ver Productos")
                pass
            case "2.3":
                print("Buscar productos")
                pass
            case "3.1":
                print("Registrar venta")
                pass
            case "3.2":
                print("Imprimir factura de ventas")
                pass
            case "3.3":
                print("Ver compras por cliente ")
                pass
            case "4":
                print("Sair/Volver al menu")
                pass
            case _:
                print("Seleccione una opción valida")

        opcMenu2 = input("Seleccione una opción:  \n 1.1. Ver Usuarios \n 1.2. Modificar Usuarios \n 1.3. Eliminar  Usuarios \n"
                         + "2.1. Crear Producto \n 2.2. Ver Productos \n 2.3. Buscar Productos \n"
                         + "3.1. Registrar Venta \n 3.2. Imprimir Factura De Ventas\n 3.3. Ver compras por cliente \n"
                         +"4. Salir/Volver al menu \n")


print ("Bienvenido...")
opc = int(input("Seleccione una opción: \n 1. Formulario \n 2. Login \n 3. Salir \n"))
isActived= False
while opc != 3:
    try:
        match opc:
            case 1: 
                print('Formulario')
                name=input('Digite su nombre: ')
                conectar()
                pass
            case 2:
                print ('Login')
                menu2(True,cursor)
                pass
            case 3:
                print ('Salir')
            case _: 
                print("Ingrese una opcion valida...")
                pass
        opc = int(input("Seleccione una opción: \n 1. Formulario \n 2. Login \n 3. Salir \n"))
    
    except:
        print('Ingrese solo números...')



