

# 1 - Préstamo de/ Película : puede tener un sub-Menú que tenga las opciones:
   #     A - Consultar todos las/películas disponibles (verificando el campo estado)
    #    B - Registrar préstamo (deberá buscar película y cambiar el campo de estado a 
    # "P" de prestado y en el cliente con "O" de ocupado)
     #   C - Registrar Devolución (pedir datos necesarios para buscar el cliente y  pelicula y cambiar 
     # el campo de estado dejándolo con "D" de disponible)
import os
#funciones
#1 - Consultar disponibilidad película
fichero = open("peliculas.txt", "r")
def peliculasDisponibles():
    with fichero as pArchivo:
        print("***************** LISTA COMPLETA ***************\n")
        print("{0:^8} {1:^16} {2:^15} {3:^11} {4:^11}".format("Codigo_de_Barra","Titulo", "Genero", "Estado", "DNI_Cliente" , "|"))
        #print("{0:<10} {1:>8} {2:>8} {3:<6} {4:>8}".format("Codigo_de_Barra","Titulo", "Genero", "Estado", "DNI_Cliente" , "|"))
        for linea in pArchivo:
            datos = linea.split(',')
            if datos[3] == 'D':
                print("{0:^8} {1:^16} {2:^15} {3:^11} {4:^11}".format(datos[0], datos[1], datos[2], datos[3], datos[4]))
                   #código de barra, titulo, genero, estado, DNI del cliente
            else:
                print("No hay Peliculas Disponibles")



#Menu
opcion = 0
def menuPrincipal():
    print("""
    ############## Gestión de  Películas LOCAL BLOCK BUSTER ##############\n """)
    opc=int(input("""
    1 - Consultar disponibilidad película
    2 - Prestamo de Pelicula
    3 - Gestionar Clientes
    4 - Gestionar Peliculas
    5 - Salir\n
    Elija una opcion\n"""))
    return opc
    #fin Menu Principal
#llamadas a funciones
while opcion != 5:
    opcion = menuPrincipal()
    if opcion == 1:
        print("\nLas peliculas Disponibles son las siguientes: \n")
        peliculasDisponibles()
        

    elif opcion == 2:
        print("Prestamo de pelicula")
    elif opcion == 3:
        print("Gestionar Clientes")
    elif opcion == 4:
        print("Gestionar Peliculas")
    elif opcion == 5:
        print("Saliendo")
    else:
        print("Opcion no valida")
#fin llamadas a funciones

