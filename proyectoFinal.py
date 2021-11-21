# TP GRUPAL - Proyecto Final
#
#Gestion de VideoClub / Biblioteca:
#- Tendrán los siguientes archivos:
 #   1) clientes.txt : con los siguientes campos en cada registro (línea, renglon): DNI, Nombre Completo, Telefono, direccion, estado, codigo de barra o ISBN si es libro
  #  2) peliculas.txt (para el videoclub): campos: código de barra, titulo, genero, estado, DNI del cliente (solo cuando la pelicula esté en préstamo)
   # 2) libros.txt (para la biblioteca) : campos: ISBN, Titulo, Autor, estado, DNI del cliente (solo cuando el libro esté en préstamo)


 
  
    #2 - Gestión del cliente: tendrá un sub-menú:
     #   A - Alta de cliente
      #  C - Consulta estado del cliente
       # M - Modificar teléfono o direccion del cliente
       # E - Eliminar cliente (deberán eliminar el registro y verificar que el archivo no quede con un registro en blanco)
    #3 - Gestión de Libro / Película: tendrá un sub-menu:
    #    A - Alta de Libro / película
     #   C - Consultar un libro/película (mostrando todos sus datos)
      #  M - Modificar Libro
       # E - Eliminar Libro

#Grupos que deberán hacer Gestión de VideoClub: 2, 4, 6, 8.
##############FUNCIONES####################
#
#  0 - Consulta de disponibilidad (deberá mostrar las películas que """"""NO ESTEN PRESTADAS""""""")
def peliculasDisponibles():
    print("\nPeliculas disponibles:")
    with open("peliculas.txt", "r") as pArchivo:
        print("***************** LISTA COMPLETA ***************")
        print("{4}{0:^8}{4} {4}{1:^16}{4} {4}{2:^15}{4} {4}{3:^11}{4}".format("DNI","Nombre", "Apellido", "Telefono", "|"))
        linea = pArchivo.readline()
        while linea != "":
            renglon = linea.split(',')
            print("{4}{0:>8}{4} {4}{1:16s}{4} {4}{2:15s}{4} {4}{3:>11}{4}".format(renglon[0], renglon[1], renglon[2], renglon[3][:-1], "|"))
            linea = pArchivo.readline()
            print("------------------------------------------------------------")
            pArchivo.close()
# 1 - Préstamo de/ Película : puede tener un sub-Menú que tenga las opciones:
   #     A - Consultar todos las/películas disponible (verificando el campo estado)
    #    B - Registrar préstamo (deberá buscar película y cambiar el campo de estado a 
    # "P" de prestado y en el cliente con "O" de ocupado)
     #   C - Registrar Devolución (pedir datos necesarios para buscar el cliente y  pelicula y cambiar 
     # el campo de estado dejándolo con "D" de disponible)
def prestamoPelicula():
    print("\nPrestamo de pelicula:")

###funcionescliente####

###funcionespelicula####
def altaPelicula():
	nombrePeli = input("Ingrese el nombre: ")
	anioPeli = input("Ingrese el año: ")
	generoPeli = input("Ingrese el genero: ")
	directorPeli = input("Ingrese el director: ")
	print("Se agregó una nueva pelicula ", agregoEntradaPeli(nombrePeli, anioPeli, generoPeli, directorPeli))

def agregoEntradaPeli(nombrePeli, anioPeli, generoPeli, directorPeli):
    with open("peliculas.txt", "a") as jArchi:
	    jArchi.write(nombrePeli + "," + anioPeli + "," + generoPeli + "," + directorPeli + "\n")
	    jArchi.close()

##############FIN FUNCIONES####################

#######MENUS########
#Deberán mostrar un menú con las siguientes opciones:
def menuPrincipal() : 
    print(""" Bienvenido al sistema de gestión de VideoClub BLOK-BUSTER

    ############## Sistema de Gestion ABM ###############

     1 - Consulta de disponibilidad
     
     2 - Préstamo de  Película
        
     3 - Gestión del Cliente

     4 - Gestión de  Película

     5 - Salir

    ############## Sistema de Gestion ABM ##############\n """)

def menuCliente(): 
    print(""" ############## Gestión de  Cliente ###############

     1 - Alta de cliente
     
     2 - Consulta estado del cliente
        
     3 - Modificar teléfono o direccion del cliente

     4 - Eliminar cliente (deberán eliminar el registro y verificar que el archivo no quede con un registro en blanco)

     5 - Volver al menu principal

    ############## Gestión de  Película ##############\n """)

def menuPelicula(): 
    print(""" ############## Gestión de  Película ###############

    1 - Alta Película
     
    2 - Modificar Pelicula
        
    3 - Eliminar Pelicula

    4 - Volver al menu principal

    ############## Gestión de  Película ##############\n """)
#######FIN MENUS########

#######MENU PRINCIPAL#########
aux = 0
while aux != 5:
    menuPrincipal()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("Las peliculas Disponibles son las siguientes: ")
        peliculasDisponibles()
        # 1 - Préstamo de/ Película : puede tener un sub-Menú que tenga las opciones:
   #     A - Consultar todos las/películas disponibles (verificando el campo estado)
    #    B - Registrar préstamo (deberá buscar película y cambiar el campo de estado a 
    # "P" de prestado y en el cliente con "O" de ocupado)
     #   C - Registrar Devolución (pedir datos necesarios para buscar el cliente y  pelicula y cambiar 
     # el campo de estado dejándolo con "D" de disponible)
    elif opcion == 2:
         opcion1= int(print("""-Bienvenido al Sistema de Consultas-"
         "1 - Consultar todos las películas disponibles
         "2 - Registrar préstamo
         "3 - Registrar Devolución"""))
         if opcion1 == 1:
            peliculasDisponibles()
         elif opcion1 == 2:
            print("Registrar préstamo")
         elif opcion1 == 3:
            print("Registrar Devolución")
         else:
            print("Opcion no valida")
    # 2 - Gestión del cliente: tendrá un sub-menú:
     #   A - Alta de cliente
      #  C - Consulta estado del cliente
       # M - Modificar teléfono o direccion del cliente
       # E - Eliminar cliente (deberán eliminar el registro y verificar que el archivo no quede con un registro en blanco)
    
    elif opcion == 3:
        menuCliente()
        opcionMenuCliente = int(input("Ingrese una opcion: "))    
    
    elif opcion == 4:
        menuPelicula()
        opcionMenuPelicula = int(input("Ingrese una opcion: "))
        if opcionMenuPelicula == 1:
            altaPelicula()
        elif opcionMenuPelicula == 2:
            modificarPelicula()
        elif opcionMenuPelicula == 3:
            modificarPelicula()
        else:
            print("Opcion no valida")
        




#crear archivo clientes.txt y consultar los datos de los clientes
