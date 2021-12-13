

# 1 - Préstamo de/ Película : puede tener un sub-Menú que tenga las opciones:
   #     A - Consultar todos las/películas disponibles (verificando el campo estado)
    #    B - Registrar préstamo (deberá buscar película y cambiar el campo de estado a 
    # "P" de prestado y en el cliente con "O" de ocupado)
     #   C - Registrar Devolución (pedir datos necesarios para buscar el cliente y  pelicula y cambiar 
     # el campo de estado dejándolo con "D" de disponible)
import os
#funciones
#1 - Consultar disponibilidad película
def peliculasDisponibles():
    with open("peliculas.txt","r+" ) as pArchivo:
        print("***************** LISTA COMPLETA ***************\n")
        print("{0:^16} {1:^16} {2:^16} {3:^16} {4:^16}".format("Codigo_de_Barra","Titulo", "Genero", "Estado", "DNI_Cliente" , "|"))
        #print("{0:<10} {1:>8} {2:>8} {3:<6} {4:>8}".format("Codigo_de_Barra","Titulo", "Genero", "Estado", "DNI_Cliente" , "|"))
        for linea in pArchivo:
            datos = linea.split(',')
            if 'D' in datos[3]:
                datos[3] = "Disponible"
                print("{0:^16} {1:^16} {2:^16} {3:^16} {4:^16}".format(datos[0], datos[1], datos[2], datos[3], datos[4]))
                   #código de barra, titulo, genero, estado, DNI del cliente
            
                #código de barra, titulo, genero, estado, DNI del cliente
    #fin funcion peliculasDisponibles

#prestamo de pelicula
'''
def prestamoPelicula(codigo,codigoCliente):
    with open("peliculas.txt","r+") as pArchivo:
        with open("clientes.txt","r+") as cArchivo:
            
            for linea in pArchivo:
                datos = linea.split(',')
                if codigo in datos:
                    if 'D' in datos[3]:
                        print("Pelicula disponible")
                        
                        for linea in cArchivo:
                            datos = linea.split(',')
                            if codigoCliente in datos:
                                if 'O' in datos[3]:
                                    print("Cliente ocupado")
                                    break
                                else:
                                    datos[3] = "O"
                                    datos[4] = codigo
                                    print("Prestamo realizado")
                                    break
                            else:
                                print("Cliente no registrado")
                                break
                    else:
                        print("Pelicula no disponible")
                        break
                else:
                    print("Pelicula no registrada")
                    break
       
'''

#PELICULAS
def altaPelicula(codigoBarras,tituloPeli, generoPeli, estadoPeli, dniAlquiler):
    with open("peliculas.txt", "a") as jArchi:
        jArchi.write(codigoBarras + "," + tituloPeli + "," + generoPeli + "," + estadoPeli + "," + dniAlquiler +"\n")
        jArchi.close()
        
def consultarPelicula(codigoBarras):
    pelicula= []
    with open("peliculas.txt","r+") as cArchivo:
        for linea in cArchivo:
            datos = linea.split(',')
            if codigoBarras in datos:
                pelicula.append(datos)
                print(pelicula)

def modificarPelicula(codigoBarras, tituloPeli):
    with open("peliculas.txt", "r") as pelisOriginal:
	    with open("peliculascopy.txt", "w") as pelisCopia:
		    filaPeli = pelisOriginal.readline()
		    while filaPeli != "":
			    renglon = filaPeli.split(',')
			    if codigoBarras == renglon[0]:
				    pelisCopia.writelines(renglon[0] + "," + tituloPeli + "," + renglon[2] + "," + renglon[3] + "\n")
			    else:
				    pelisCopia.write(filaPeli)
			    filaPeli = pelisOriginal.readline()
		    pelisCopia.close()
	    pelisOriginal.close()
		
    with open("peliculascopy.txt", "r") as pelisCopia:
	    with open("peliculas.txt", "w") as pelisOriginal:
		    for registro in pelisCopia:
			    pelisOriginal.write(registro)
		    pelisCopia.close()
	    pelisOriginal.close()

def eliminarPelicula(codigoPeliEliminar):
    with open("peliculas.txt", "r") as rArchi:
	    with open("peliculascopy.txt", "w") as wArchi:
		    linea = rArchi.readline()
		    while linea != "":
			    renglon = linea.split(',')
			    if codigoPeliEliminar != renglon[0]:
				    wArchi.write(linea)
			    linea = rArchi.readline()
		    wArchi.close()
	    rArchi.close()
		
    with open("peliculascopy.txt", "r") as fcopia:
	    with open("peliculas.txt", "w") as foriginal:
		    for registro in fcopia:
			    foriginal.write(registro)
		    fcopia.close()
	    foriginal.close()  

########

def modificarPeliculas(codigo):
    with open("peliculas.txt","r+") as pArchivo:
        with open("peliculascpy.txt","w") as pArchivocpy:
            estado = "D"
            estado2= "p"
            linea = pArchivo.readline()
            while linea != "":
                renglon = linea.split(',')
                if estado == renglon[3] and codigo == renglon[0]:
                    pArchivocpy.writelines(str(codigo)+','+renglon[1]+','+renglon[2]+','+str(estado)+','+renglon[4]+'\n')
                elif estado2 == renglon[3] and codigo == renglon[0]:
                    pArchivocpy.writelines(str(codigo)+','+renglon[1]+','+renglon[2]+','+str(estado2)+','+renglon[4]+'\n')
                else:
                    pArchivocpy.write(linea)
                linea = pArchivo.readline()
            pArchivocpy.close()
        pArchivo.close()

def modificarCliente(codigoCliente):
    with open("clientes.txt","r+") as cArchivo:
        with open("clientescpy.txt","w") as cArchivocpy:
            estado = "L"
            estado2= "O"
            linea = cArchivo.readline()
            while linea != "":
                renglon = linea.split(',')
                if codigoCliente == renglon[0] and estado == renglon[4]:
                    cArchivocpy.write(str(codigoCliente)+','+renglon[1]+','+renglon[2]+','+renglon[3]+','+str(estado)+'\n')
                elif codigoCliente == renglon[0] and estado2 == renglon[4]:
                    cArchivocpy.write(str(codigoCliente)+','+renglon[1]+','+renglon[2]+','+renglon[3]+','+str(estado2)+'\n')
                else:
                    cArchivocpy.write(linea)
                linea = cArchivo.readline()
            cArchivocpy.close()
        cArchivo.close()

def prestamoPelicula(codigo,codigoCliente):
    modificarPeliculas(codigo)
    modificarCliente(codigoCliente)
    #fin funcion prestamoPelicula

# c devoluion de pelicula
def devolucionPelicula(codigo,codigoCliente):
    modificarPeliculas(codigo)
    modificarCliente(codigoCliente)
    #fin funcion devolucionPelicula

# Menu clientes 
#ALTA CLIENTE
def altaCliente(dni,nombreYapellido,telF,direccion,estado,codigo):
    with open("clientes.txt","a") as cArchivo:
        cArchivo.write(str(dni)+','+nombreYapellido+','+str(telF)+','+str(direccion)+','+estado+','+str(codigo)+'\n')
    cArchivo.close()

# Consultar estado del cliente
def consultarCliente(dni):
    clientes= []
    with open("clientes.txt","r+") as cArchivo:
        for linea in cArchivo:
            datos = linea.split(',')
            if dni in datos:
                clientes.append(datos)
                print(clientes)
    #fin funcion estado cliente

def modificarTelefonoYdireccionCliente(dni,telefono,direccion):
    with open("clientes.txt","r+") as cArchivo:
        with open("clientescpy.txt","w") as cArchivocpy:
            linea = cArchivo.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni == renglon[0]:
                    cArchivocpy.write(str(dni)+','+renglon[1]+','+str(telefono)+','+str(direccion)+','+renglon[4]+renglon[5]+'\n')
                else:
                    cArchivocpy.write(linea)
                linea = cArchivo.readline()
            cArchivocpy.close()
        cArchivo.close()

    with open("clientes.txt","w") as cArchivo:
        with open("clientescpy.txt","r+") as cArchivocpy:
            for datos in cArchivocpy:
                cArchivo.write(datos)
                cArchivo.close()
            cArchivocpy.close()

def eliminarCliente(dni):
    with open("clientes.txt","r+") as cArchivo:
        with open("clientescpy.txt","w") as cArchivocpy:
            linea = cArchivo.readline()
            while linea != "":
                renglon = linea.split(',')
                if dni != renglon[0]:
                    cArchivocpy.write(linea)
                linea = cArchivo.readline()
            cArchivocpy.close()
        cArchivo.close()

    with open("clientes.txt","w") as cArchivo:
        with open("clientescpy.txt","r+") as cArchivocpy:
            for datos in cArchivocpy:
                cArchivo.write(datos)
                cArchivo.close()
            cArchivocpy.close()



#MENU PRINCIPAL
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
        
        opcion2 = str(input("""\n\nQue desea hacer?: 
        A-Consultar Peliculas Disponibles
        B-Registrar Préstamo
        C-Registrar Devolución \n
        Elija una opcion:
         """))
        if opcion2 == "A" or opcion2 == "a":
            peliculasDisponibles()
        elif opcion2 == "B" or opcion2 == "b":
            print("\nRegistrar Préstamo\n")
            codigo = input("Ingrese el codigo de barra de la pelicula a prestar\n")
            codigoCliente = input("Ingrese el DNI del cliente\n")
            print("Se realizo el prestamo " ,prestamoPelicula(codigo,codigoCliente))
           # registrarPrestamo(#codigo_barra, dni_cliente)#


        elif opcion2 == "C" or opcion2 == "c":
            print("Registrar Devolución\n")
            codigo = input("Ingrese el codigo de barra de la pelicula a devolver\n")
            codigoCliente = input("Ingrese el DNI del cliente\n")
            print("Se realizo la devolucion " ,devolucionPelicula(codigo,codigoCliente))
        
        else:
            print("Opcion no valida")

    elif opcion == 3:
        opcion3 = str(input("""\n\nQue desea hacer?: 
        A- Alta Cliente
        B- Consultar estado del Cliente
        C- Modificar Telefono o direccion del Cliente 
        D- Eliminar Cliente\n
        Elija una opcion:
         """))
        if opcion3 == "A" or opcion3 == "a":
            print("\nAlta Cliente\n")
            dni = input("Ingrese el DNI del cliente\n")
            nombreYapellido = input("Ingrese el nombre y apellido del cliente\n")
            telF = input("Ingrese el telefono fijo del cliente\n")
            direccion = input("Ingrese la direccion del cliente\n")
            estado = "L"
            codigo = input("Sin reservas por 48hs hasta completar alta definitiva\n")
            altaCliente(dni,nombreYapellido,telF,direccion,estado,codigo)
            print("Se registro el cliente")
        elif opcion3 == "B" or opcion3 == "b":
            print("\nConsultar estado del Cliente\n")
            dni = input("Ingrese el DNI del cliente\n")
            consultarCliente(dni)
        elif opcion3 == "C" or opcion3 == "c":
            print("\nModificar Telefono o direccion del Cliente\n")
            dni = input("Ingrese el DNI del cliente\n")
            telF = input("Ingrese el nuevo telefono  del cliente\n")
            direccion = input("Ingrese la nueva direccion del cliente\n")
            modificarTelefonoYdireccionCliente(dni,telF,direccion)
        elif opcion3 == "D" or opcion3 == "d":
            print("\nEliminar Cliente\n")
            dni = input("Ingrese el DNI del cliente\n")
            eliminarCliente(dni)
    elif opcion == 4:
        opcion4 = str(input("""\n\nQue desea hacer?: 
        A- Alta Pelicula
        B- Consultar datos Pelicula
        C- Modificar Pelicula
        D- Eliminar Pelicula\n
        Elija una opcion:
         """))
        if opcion4 == "A" or opcion4 == "a":
            print("\nAlta Pelicula\n")
            codigoBarras = input("Ingrese el codigo de barras: ")
            tituloPeli = input("Ingrese el titulo: ")
            generoPeli = input("Ingrese el genero: ")
            estadoPeli = input("Ingrese el estado de la peli: ")
            ###TO-DO agregar if esta alquilada agregar el dni del cl else 0000####
            dniAlquiler = "None"
            altaPelicula(codigoBarras,tituloPeli, generoPeli, estadoPeli, dniAlquiler)
        elif opcion4 == "B" or opcion4 == "b":
            print("\nConsulta el estdo de la pelicula\n")
            codigoBarras = input("Ingrese el codigo de barras: ")
            consultarPelicula(codigoBarras)
        elif opcion4 == "C" or opcion4 == "c":
            print("\nModificar titulo de la pelicula\n")
            codigoBarras = input("Ingrese el codigo de barras de la pelicula que quiere modificar")
            ###TO-DO preguntar cuales campos quiere cambiar while - if####
            tituloPeli = input("Ingrese el nuevo titulo: ")
            modificarPelicula(codigoBarras, tituloPeli)
            print("Se cambio el titulo de la pelicula " + codigoBarras + " a " + tituloPeli)
        elif opcion4 == "D" or opcion4 == "d":
            print("\nEliminar pelicula\n")
            codigoPeliEliminar = input("Ingrese el codigo de la pelicula\n")
            eliminarPelicula(codigoPeliEliminar)
    elif opcion == 5:
        print("Saliendo")
    else:
        print("Opcion no valida")
#fin llamadas a funciones
