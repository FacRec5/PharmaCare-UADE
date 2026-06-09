from funciones import *

def main():
    infoproducto = [[],[],[],[],[],[],[]] #Orden de listas: 0: Nombre, 1: código, 2: Laboratorio, 3: Precio, 4: Stock, 5: Cobertura (si o no), 6: vencimiento
    
    opciones_menu()
    opcion = ingresar_opcionMenu(1,5)
    while opcion != 5:
        
        #analizamos opcion de menu
        if opcion ==1:
            print("Alta de producto")
            altaProductos(infoproducto) #Mando la matriz en vez de mandar un montonazo de listas
        elif opcion==2:
            print("Modificar stock")
            if len(lst_codigos) > 0:
                modificarStock(lst_codigos, lst_nombres, lst_stock)
            else:
                print("No existe stock que modificar")
        elif opcion ==3:
            print("Eliminar")
            if len(lst_codigos) > 0:
                eliminar(lst_codigos, lst_nombres, lst_stock)
            else:
                print("No existen elementos para eliminar")
        elif opcion == 4:
            print("Informes")
            if len(lst_codigos) > 0:
                mostrarProductos(lst_codigos, lst_nombres, lst_stock)
            else:
                print("No existen elementos")
        
        opciones_menu()
        opcion = ingresar_opcionMenu(1,5)       
    

main()
