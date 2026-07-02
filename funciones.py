

def imprimirMatriz(matriz):
    '''Imprime una matriz de manera ordenada en forma de cuadro'''
    filas=len(matriz)
    col=len(matriz[0])
    etiquetas = ["Nombre:", "Código:", "Laboratorio:", "Precio:", "Stock:", "Cobertura:", "Vencimiento:"]
    #Imprimimos los encabezados primero (todos en la misma línea)
    for e in etiquetas:
        print("%-15s" % e, end="")
    print()
    print("-" * 105) # Una línea separadora

    #Imprimimos la matriz de forma normal alineando las columnas
    for c in range(col):
        for f in range(filas):
            print("%-15s" % str(matriz[f][c]), end="")
        print()
        

def opciones_menu():
    '''Imprime todas las opciones del menu principal del programa'''
    print("="*40)
    print("SISTEMA DE GESTIÓN: PHARMACARE CENTRAL")
    print("="*40)
    print("1: Registrar nuevo medicamento")
    print("2- Eliminar medicamento")
    print("3: Modificar stock o precio")
    print("4: Informe general / visualización de los datos")
    print("5: Salir")
    print("="*40)

def ordenarLista(matriz):
    '''Ordena la lista por fecha de vencimiento o nombre, si las fechas coinciden'''
    cantidad_productos = len(matriz[0])
    
    for i in range(1, cantidad_productos):
        nombre_insertar      = matriz[0][i]
        codigo_insertar      = matriz[1][i]
        laboratorio_insertar = matriz[2][i]
        precio_insertar      = matriz[3][i]
        stock_insertar       = matriz[4][i]
        cobertura_insertar   = matriz[5][i]
        vencimiento_insertar = matriz[6][i]

        j = i
        
        
        while j > 0 and matriz[6][j-1] >= vencimiento_insertar:
            vencimiento_izq = matriz[6][j-1]
            nombre_izq      = matriz[0][j-1]
            
            # CASO 1: Si el de la izquierda es mayor, hay que desplazar
            if vencimiento_izq > vencimiento_insertar:
                # Desplazamos las 7 categorías de j-1 hacia j
                matriz[0][j] = matriz[0][j-1]
                matriz[1][j] = matriz[1][j-1]
                matriz[2][j] = matriz[2][j-1]
                matriz[3][j] = matriz[3][j-1]
                matriz[4][j] = matriz[4][j-1]
                matriz[5][j] = matriz[5][j-1]
                matriz[6][j] = matriz[6][j-1]
                j = j - 1
                
            # CASO 2: Si los vencimientos son iguales, desempatamos por nombre
            elif vencimiento_izq == vencimiento_insertar:
                if nombre_izq > nombre_insertar:
                    # Desplazamos las 7 categorías de j-1 hacia j
                    matriz[0][j] = matriz[0][j-1]
                    matriz[1][j] = matriz[1][j-1]
                    matriz[2][j] = matriz[2][j-1]
                    matriz[3][j] = matriz[3][j-1]
                    matriz[4][j] = matriz[4][j-1]
                    matriz[5][j] = matriz[5][j-1]
                    matriz[6][j] = matriz[6][j-1]
                    j = j - 1
                
        # Al salir del while, insertamos en el hueco final 'j'
        matriz[0][j] = nombre_insertar
        matriz[1][j] = codigo_insertar
        matriz[2][j] = laboratorio_insertar
        matriz[3][j] = precio_insertar
        matriz[4][j] = stock_insertar
        matriz[5][j] = cobertura_insertar
        matriz[6][j] = vencimiento_insertar
    return matriz

def buscarElemento(infoproducto, nombre):
    '''Pide un producto y lo busca en la lista, fijandose si existe o no y en qué posición se encuentra'''
    
    if nombre == False:
        codigo = input('Ingrese el codigo unico del producto (Ingrese "EXIT" para finalizar) ')
        while not codigo.isalnum() or (len(codigo) < 4 or len(codigo) > 10): #Chequeo que este en el limite y sea alfanumerico

            print("Error, codigo invalido")
            print("El código debe contener solo caracteres alfanuméricos y debe tener entre 4 y 10 caractéres")
            codigo=input('Ingrese un codigo unico para el producto (Ingrese "EXIT" para finalizar) ')

        contador = 0
        if len(infoproducto[1]) > 0: #Este if es para solucionar un index out of range
            while contador < len(infoproducto[1]) and infoproducto[1][contador] != codigo: #Busco si ya existe el codigo
                contador += 1
    else:
        codigo = input('Ingrese el codigo unico o el nombre del producto (Ingrese "EXIT" para finalizar) ')
        contador = 0
        if len(infoproducto[1]) > 0: #Este if es para solucionar un index out of range
            while contador < len(infoproducto[1]) and (infoproducto[1][contador] != codigo and infoproducto[0][contador] != codigo): #Busco si ya existe el codigo
                contador += 1

    return codigo, contador

    


def ingresar_opcionMenu(desde, hasta):
    '''valida ingresar un valor en el rango desde-hasta
    retorna el valor ingresado del teclado'''
    op = input("Seleccione una opción: ")
    while op.isdigit() == False or (int(op)<desde or int(op)>hasta):
        print("La opción seleccionada no es válida")
        op = input("Seleccione una opción: ")
    return int(op)

def ingresarPositivo(msg, esEntero):
    '''Ingresar del teclado un numero y validar que sea positivo.'''
    
    num=input(msg)
    if esEntero:
        while num.isdigit() == False or int(num) <= 0 or len(str(num)) > 14:
            print("Error debe ser un número entero positivo de no mas de 14 caracteres")
            num=input(msg)
    else:
        while esDecimal(num) == False or float(num) <= 0 or len(str(num)) > 14:
            print("Error debe ser un número positivo de no mas de 14 caracteres")
            num=input(msg)
    return num

def esDecimal(num):
    if "." in num:
        num = num.replace(".", "", 1)

    if num.isdigit() == True:
        return True
    else:
        return False

#Esta función es la misma que la del programa de las bicicletas pero adaptada a matrices y a la consigna
#Habría que adaptar todo el resto
def altaProductos(infoproducto):
    '''Pide una matriz y agrega elementos a la misma'''
    codigo, contador = buscarElemento(infoproducto, False)

    while codigo.upper() != "EXIT":

        if contador < len(infoproducto[1]):
            print("Error, ese codigo ya está en uso")
        else:
            
            #Pido todos los valores
            nombre= input("Nombre del producto:")
            while len(nombre) == 0 or nombre.isspace() or len(nombre) > 14:
                print("Error: El campo no puede estar vacío ni contener solo espacios. No puede superar los 14 caracteres")
                nombre= input("Nombre del producto:")
            
            laboratorio = input("Nombre del laboratorio fabricante del producto: ")
            while len(laboratorio) == 0 or laboratorio.isspace() or len(laboratorio) > 14:
                print("Error: El campo no puede estar vacío ni contener solo espacios. No puede superar los 14 caracteres")
                laboratorio = input("Nombre del laboratorio fabricante del producto: ")
            
            precio = ingresarPositivo("Ingrese el precio unitario del producto ", False)

            cantidad = ingresarPositivo("Ingrese cantidad de stock disponible: ", True)

            cobertura = input("¿El producto posee cobertura medica? (Si/No) ")
            while (cobertura.upper() != "SI") and (cobertura.upper() != "NO"):
                cobertura = input("¿El producto posee cobertura medica? (Si/No) ")
            cobertura = cobertura.upper().strip()

            vencimiento = ingresarPositivo("Ingresar dias restantes aproximados para el vencimiento del producto ", True)
           

            #Verifico si el producto ya existe
            contador = 0
            if len(infoproducto[1]) > 0: #Antes de revisar la matríz se verifica que hayan elementos
                while contador < len(infoproducto[1]) and (infoproducto[0][contador].lower().strip() != nombre.lower().strip() or infoproducto[2][contador].lower().strip() != laboratorio.lower().strip() or infoproducto[5][contador] != cobertura.upper().strip() or infoproducto[6][contador] != vencimiento): #Busco si ya existe el producto
                    contador += 1
                    
            if contador < len(infoproducto[1]):
                print(f"El producto ya está añadido en la lista de productos bajo el codigo {infoproducto[1][contador]}, desea sumar el stock del producto agregado al existente?")
                print("1- Si")
                print("2- Cancelar operación")
                eleccion = ingresar_opcionMenu(1,2)
                if eleccion == 1:
                    infoproducto[4][contador] = str(int(infoproducto[4][contador]) + int(cantidad))
                    print("Stock sumado con éxito")
                else:
                    print("Se canceló la operación")
            else:
                infoproducto[0].append(nombre)
                infoproducto[1].append(codigo)
                infoproducto[2].append(laboratorio)
                infoproducto[3].append(precio)
                infoproducto[4].append(cantidad)
                infoproducto[5].append(cobertura)
                infoproducto[6].append(vencimiento)

        codigo, contador = buscarElemento(infoproducto, False)
    

def modificarStock(infoproducto):
    '''Modifica el precioo el stock de un producto'''
    codigo, contador = buscarElemento(infoproducto, True)
    
    while codigo.upper() != "EXIT":

        if contador < len(infoproducto[1]):
            print("Qué desea hacer con", infoproducto[0][contador]) 
            print("1- Agregar stock")
            print("2- Quitar stock")
            print("3- Modificar precio")
            
            operacion = ingresar_opcionMenu(1, 3)

            if operacion == 1:
                cambio = input("Cuántas unidades desea agregar al stock?: ")
                while cambio.isdigit() == False or int(cambio) < 0:
                    print("Error, la cantidad a agregar debe ser un número entero positivo")
                    cambio = input("Cuántas unidades desea agregar al stock?: ")
                
                infoproducto[4][contador] = str(int(infoproducto[4][contador]) + int(cambio)) # infoproducto[4] es el stock
            elif operacion == 2:
                cambio = input("Cuántas unidades desea quitar al stock?: ")
                while cambio.isdigit() == False or (int(infoproducto[4][contador]) - int(cambio) < 0 or int(cambio) < 0):
                    print("ERROR, la cantidad de stock de un producto no puede quedar negativa y el número ingresado debe ser un entero positivo")
                    cambio = input("Cuántas unidades desea quitar al stock?: ")
                
                infoproducto[4][contador] = str(int(infoproducto[4][contador]) - int(cambio))
            else:
                infoproducto[3][contador] = ingresarPositivo("Ingrese el nuevo precio unitario del producto ", False)

            print(infoproducto[0][contador], "modificado correctamente!")
            
        else:
            print("No existe un producto con ese código o nombre")
            
        codigo, contador = buscarElemento(infoproducto, True)

def eliminar(infoproducto):
    '''Elimina un producto entero de la matriz solo si su stock es 0'''
    codigo, contador = buscarElemento(infoproducto, False)
    
    while codigo.upper() != "EXIT":
        if contador < len(infoproducto[1]):
            if int(infoproducto[4][contador]) == 0:
                print(f"Seguro que desea eliminar {infoproducto[0][contador]}?")
                print("1- Si")
                print("2- Cancelar")
                operacion = ingresar_opcionMenu(1, 2)

                if operacion == 1:
                    print(f"Se eliminó {infoproducto[0][contador]}")
                    for fila in infoproducto:
                        fila.pop(contador)
                else:
                    print(f"Eliminación de {infoproducto[0][contador]} cancelada")
            else:
                print("No se pueden eliminar productos que no tengan 0 de stock")
        else:
            print("No existe un producto con ese código")

        if len(infoproducto[1]) > 0:    
            codigo, contador = buscarElemento(infoproducto, False) # Cambiado a False para mantener coherencia al salir
        else:
            print("No existen más elementos que eliminar")
            codigo = "EXIT"

     
 
   