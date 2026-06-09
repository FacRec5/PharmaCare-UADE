import random

def imprimirMatriz(matriz): #Por si alguno quiere imprimir la matriz para ver como esta quedando o para el informe llame esta funcion, dando como parametro la matriz
    filas=len(matriz)
    col=len(matriz[0])
    for f in range(filas):
        for c in range(col):
            print("%40s" %matriz[f][c], end="")
        print()

def opciones_menu():
    print("1: Alta de Producto")
    print("2: Modificar stock")
    print("3: Eliminar stock")
    print("4: Informes")
    print("5: Salida")


def ingresar_opcionMenu(desde, hasta):
    '''valida ingresar un valor en el rango desde-hasta
    retorna el valor ingresado del teclado'''
    op = int(input("Selecicone una opcion:"))
    while op<desde or op>hasta:
        print("La opcion seleccionada no es valida")
        op = int(input("Selecicone una opcion:"))
    return op

def ingresarPositivo(msg, entero):
    '''Ingresar del teclado un numero y validar que sea positivo. Recibe como parametros un mensaje a mostrar y un bool para verificar si es entero o no)'''
    if entero:
        num=int(input(msg))
    else:
        num=float(input(msg))

    while num<=0:
        print("Error debe ser positivo")
        if entero:
            num=int(input(msg))
        else:
            num=float(input(msg))
    return num

#Esta función es la misma que la del programa de las bicicletas pero adaptada a matrices y a la consigna
#Habría que adaptar todo el resto
def altaProductos(infoproducto):

    codigo = input('Ingrese un codigo unico para el producto (Ingrese "EXIT" para finalizar) ')

    while not codigo.isalnum() or (len(codigo) < 4 or len(codigo) > 10): #Chequeo que este en el limite y sea alfanumerico

        print("Error, codigo invalido")
        print("El código debe contener solo caracteres alfanuméricos y debe tener entre 4 y 10 caractéres")
        codigo=input('Ingrese un codigo unico para el producto (Ingrese "EXIT" para finalizar) ')

    while codigo != "EXIT":

        contador = 0
        if len(infoproducto[1]) > 0: #Este if es para solucionar un index out of range
            while contador < len(infoproducto[1]) and infoproducto[1][contador] != codigo: #Busco si ya existe el codigo
                contador += 1

        if contador < len(infoproducto[1]):
            print("Error, ese codigo ya está en uso")
        else:
            
            #Pido todos los valores
            nombre= input("Nombre del producto:")
            laboratorio = input("Nombre del laboratorio fabricante del producto: ")
            precio = ingresarPositivo("Ingrese el precio unitario del producto ", False)
            cantidad = ingresarPositivo("Ingrese cantidad de stock disponible: ", True)
            cobertura = input("¿El producto posee cobertura medica? (Si/No) ")
            while (cobertura.upper() != "SI") and (cobertura.upper() != "NO"):
                cobertura = input("¿El producto posee cobertura medica? (Si/No) ")
            vencimiento = 30 * random.randint(1,24) 
            print("Fecha aproximada de vencimiento:", vencimiento)

            #Meto todo en su respectiva fila de la matriz
            infoproducto[0].append(nombre)
            infoproducto[1].append(codigo)
            infoproducto[2].append(laboratorio)
            infoproducto[3].append(precio)
            infoproducto[4].append(cantidad)
            infoproducto[5].append(cobertura)
            infoproducto[6].append(vencimiento)

        codigo = input('Ingrese un codigo unico para el producto (Ingrese "EXIT" para finalizar)')
        while not codigo.isalnum() or (len(codigo) < 4 or len(codigo) > 10):
            print("Error, codigo invalido")
            print("El código debe contener solo caracteres alfanuméricos y debe tener entre 4 y 10 caractéres")
            codigo=input('Ingrese un codigo unico para el producto (Ingrese "EXIT" para finalizar) ')
    

############################################################# DE ACA PARA ABAJO FALTA ADAPTAR TODO ##########################################################################################################################
def modificarStock(infoproducto):
    codigo=int(input("Ingrese un codigo -1 para finalizar"))
    while codigo <=0 and codigo != -1:
        codigo=int(input("Ingrese un codigo -1 para finalizar"))
    
    while codigo != -1:
        contador = 0
        while lst_codigos[contador] != codigo and contador < len(lst_codigos) - 1:
            contador += 1

        if lst_codigos[contador] == codigo:
            print(f"Qué desea hacer con {lst_nombres[contador]}")
            print("1- Agregar stock")
            print("2- Quitar stock")
            operacion = ingresarPositivo("")
            while operacion < 1 and operacion > 2:
                print("Opción invalida")
                print("1- Agregar stock")
                print("2- Quitar stock")
                operacion = ingresarPositivo("")

            if operacion == 1:
                cambio = int(input(f"Cuántas unidades de {lst_nombres[contador]} desea agregar al stock? ({lst_stock[contador]} unidades restantes) "))
                while cambio < 0:
                    print("ERROR, la cantidad de stock de un producto no puede quedar negativa")
                    cambio = int(input(f"Cuántas unidades de {lst_nombres[contador]} desea agregar al stock? ({lst_stock[contador]} unidades restantes) "))
                lst_stock[contador] += cambio
            else:
                cambio = int(input(f"Cuántas unidades de {lst_nombres[contador]} desea quitar al stock? ({lst_stock[contador]} unidades restantes) "))
                while lst_stock[contador] - cambio < 0 or cambio < 0:
                    print("ERROR, la cantidad de stock de un producto no puede quedar negativa")
                    cambio = int(input(f"Cuántas unidades de {lst_nombres[contador]} desea quitar al stock? ({lst_stock[contador]} unidades restantes) "))
                lst_stock[contador] -= cambio

            
            print(f"Stock de {lst_nombres[contador]} modificado correctamente!")
            
        else:
            print("No existe un producto con ese código")
        codigo=int(input("Ingrese un codigo -1 para finalizar"))
        while codigo <=0 and codigo != -1:
            codigo=int(input("Ingrese un codigo -1 para finalizar"))

def eliminar(infoproducto):

    codigo=int(input("Ingrese un codigo -1 para finalizar"))
    while codigo <=0 and codigo != -1:
        codigo=int(input("Ingrese un codigo -1 para finalizar"))
    
    while codigo != -1:
        contador = 0
        while lst_codigos[contador] != codigo and contador < len(lst_codigos) - 1:
            contador += 1

        if lst_codigos[contador] == codigo:
            print(f"Seguro que desea eliminar {lst_nombres[contador]}?")
            print("1- Si")
            print("2- Cancelar")
            operacion = ingresarPositivo("")
            while operacion < 1 and operacion > 2:
                print("Opción invalida")
                print("1- Si")
                print("2- Cancelar")
                operacion = ingresarPositivo("")

            if operacion == 1:
                print(f"Se eliminó {lst_nombres[contador]}")
                lst_codigos.pop(contador)
                lst_nombres.pop(contador)
                lst_stock.pop(contador)
               
            else:
                print(f"Eliminación de {lst_nombres[contador]} cancelada")
            
        else:
            print("No existe un producto con ese código")
        if len(lst_codigos) > 0:    
            codigo=int(input("Ingrese un codigo -1 para finalizar"))
            while codigo <=0 and codigo != -1:
                codigo=int(input("Ingrese un codigo -1 para finalizar"))
        else:
            print("No existen más elementos que eliminar")
            codigo = -1
     

def mostrarProductos(infoproducto):
    '''Muestra por pantalla los productos'''
    menorstock = []
    print("-" * 20)
    print("Código", "" * 5, "Nombre", "" * 5, "Stock")
    print("-" * 20)
    for i in range(len(lst_codigos)):
        print(lst_codigos[i], lst_nombres[i], lst_stock[i])
        if lst_stock[i] < 5:
            menorstock.append(i)
    print("-" * 20)
    print("-" * 15, "PRODUCTOS POR DEBAJO DEL STOCK MINIMO", "-" * 15)
    print("-" * 20)
    print("Código", "" * 5, "Nombre", "" * 5, "Stock")
    print("-" * 20)
    for i in range(len(menorstock)):
        print(lst_codigos[menorstock[i]], lst_nombres[menorstock[i]], lst_stock[menorstock[i]])
    print("-" * 20)