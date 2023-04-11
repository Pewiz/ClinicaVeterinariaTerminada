from ClaseCliente import Cliente
from Urgencia import Urgencia
from Usuario import Usuario
from Consultas import Consulta
from ManejoArchivo import GestionArchivo
from SalasHorario import SalasHorario
from Mascota import Mascota
from urgencias import Urgencias
from operaciones import Operaciones

import os

while True:
    os.system("cls")
    tipo_atencion = input("""Que tipo de consulta viene el paciente:
1. Consultas
2. Urgencias
3. Operaciones
4. Gestion Archivos 
>>> """)

    if tipo_atencion == "1":
        contador_mascota = 0
        os.system("cls")
        print("1. Cliente Nuevo")
        print("2. Cliente Registrado")
        opcionCl = int(input(">>> "))
        if opcionCl == 1:
            cliente_seleccionado = Cliente.ingresoCliente()
            GestionArchivo.insertar("clientes.csv",cliente_seleccionado)
            rutCliente = cliente_seleccionado
                
        elif opcionCl == 2:
            buscar_rut = input("Ingrese rut(21454138-6): ")
            rutCliente = Cliente(rut=buscar_rut)
            listas = GestionArchivo.seleccionar("clientes.csv",rutCliente)
            for lista in listas:
                cliente_seleccionado = Cliente(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8])                    
                
        listasMascotas = GestionArchivo.seleccionar("mascotas.csv",rutCliente)
        os.system("cls")
        while True:
            contador_mascota+=1
            print("Mascotas Encontradas".center(50,"-"))
            i=0
            mascotas = []
            for listaM in listasMascotas:
                mascotaM = Mascota(listaM[0],listaM[1],listaM[2],listaM[3],listaM[4],listaM[5],listaM[6],listaM[7],listaM[8])
                if opcionCl == 2:
                    cliente_seleccionado.añadirMascota(mascotaM)
                print(f"Mascota numero[{i+1}]") 
                print(mascotaM)
                i+=1
                mascotas.append(mascotaM)

            opcionMascota = int(input("Que mascota desea ingresar?: "))
            boolean = Consulta.realizarConsulta(cliente_seleccionado,mascotas[opcionMascota-1],contador_mascota)
            if boolean:
                break
            

    elif tipo_atencion == "2":
        funcionesUrgencia = Urgencias()
        funcionesUrgencia.menu()
    elif tipo_atencion == "3":
        funcionesOperaciones = Operaciones()
        funcionesOperaciones.mostrarMenuOP()
    elif tipo_atencion == "4":
        os.system("cls")
        print("1. Agregar Mascota a cliente")
        print("2. Agregar Veterinario")
        print("3. Crear Sala y Horario")
        print("4. Modificar Hora agendada")
        print("5. Cancelar Hora Agendada")
        opcion = int(input(">>> "))
        if opcion ==1:
            os.system("cls")
            rut = input("Ingrese rut del cliente(21454138-6): ")
            print("Ingresando Mascota".center(50,"-"))
            mascota = Mascota.ingresarMascota(rut)
            os.system("cls")
            print("Mascota Ingresada".center(50,"-"))
            print(mascota)
            os.system("pause")
        elif opcion ==2:
            os.system("cls")
            print("Ingresando Veterinario".center(50,"-"))
            rut = input("Rut: ")
            nombres = input("Nombres: ")
            apellido_pate = input("Apellido Paterno: ")
            apellido_mate = input("Apellido Materno: ")
            genero = input("Genero: ")
            fecha_nacimiento = input("Fecha de nacimiento: ")
            cargo = input("Cargo: ")
            experiencia = input("Experiencia: ")
            veterinario = Usuario(rut,nombres,apellido_pate,apellido_mate,genero,fecha_nacimiento,cargo,experiencia,horario=None)
            GestionArchivo.insertar("veterinarios.csv",veterinario)
            
            os.system("cls")
            print("Veterinario Ingresado".center(50,"-"))
            print(veterinario)
            os.system("pause")
        elif opcion ==3:
            sala = int(input("Sala: "))
            horario = input("Ingresa el Horario (00:00-00:00): ")

            listas = GestionArchivo.seleccionarTodo("veterinarios.csv")
            i=0
            veterinarios = []
            for lista in listas:
                veterinario = Usuario(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],horario=None)
                print(f"Veterinario [{i+1}]\n{veterinario}")
                veterinarios.append(veterinario)
                i+=1

            opcionVet = int(input("A que veterinario le quieres asignar la sala: "))
            salaAsignada = SalasHorario(veterinarios[opcionVet-1].rut,sala,horario)
            GestionArchivo.insertar("salas.csv",salaAsignada)
        elif opcion == 4:
            os.system("cls")
            rutElegido = input("Ingrese rut del cliente: ")
            ides = GestionArchivo.identificarLinea("salasAgendadas.csv",rutElegido)
            salas = GestionArchivo.seleccionarTodo("salasAgendadas.csv")
            salasEncontradas = []
            j=0
            os.system("cls")
            for sala in salas:
                salaEncontrada = SalasHorario(sala[0],sala[1],sala[2],sala[3],sala[4])
                if salaEncontrada.rut == rutElegido:
                    print(f"Codigo Hora Agendada [{j+1}]\n{salaEncontrada}")
                    salasEncontradas.append(salaEncontrada)
                    j+=1
            
            opcionBorr = int(input("Indique el codigo de la hora que desea modificar: "))
            GestionArchivo.eliminar("salasAgendadas.csv",ides[opcionBorr-1])
            os.system("cls")
            rutCliente = Cliente(rut=rutElegido)
            listas = GestionArchivo.seleccionar("clientes.csv",rutCliente)
            for lista in listas:
                cliente_seleccionado = Cliente(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7],lista[8])                    
                
            listasMascotas = GestionArchivo.seleccionar("mascotas.csv",rutCliente)
            os.system("cls")
            print("Mascotas Encontradas".center(50,"-"))
            i=0
            mascotas = []
            for listaM in listasMascotas:
                mascotaM = Mascota(listaM[0],listaM[1],listaM[2],listaM[3],listaM[4],listaM[5],listaM[6],listaM[7],listaM[8])
                print(f"Mascota numero[{i+1}]") 
                print(mascotaM)
                i+=1
                mascotas.append(mascotaM)
                        
            opcionMascota = int(input("Que mascota desea ingresar?: "))
            Consulta.realizarConsulta(cliente_seleccionado,mascotas[opcionMascota-1])
        elif opcion == 5:
            os.system("cls")
            rutElegido = input("Ingrese rut del cliente: ")
            ides = GestionArchivo.identificarLinea("salasAgendadas.csv",rutElegido)
            salas = GestionArchivo.seleccionarTodo("salasAgendadas.csv")
            salasEncontradas = []
            j=0
            os.system("cls")
            for sala in salas:
                salaEncontrada = SalasHorario(sala[0],sala[1],sala[2],sala[3],sala[4])
                if salaEncontrada.rut == rutElegido:
                    print(f"Codigo Hora Agendada [{j+1}]\n{salaEncontrada}")
                    salasEncontradas.append(salaEncontrada)
                    j+=1
            
            opcionBorr = int(input("Indique el codigo de la hora que desea borrar: "))
            GestionArchivo.eliminar("salasAgendadas.csv",ides[opcionBorr-1])
            os.system("cls")
            print("Hora Cancelada correctamente".center(50,"-"))
            print(f"\nHora Cancelada: {salasEncontradas[opcionBorr-1]}")
            os.system("pause")

