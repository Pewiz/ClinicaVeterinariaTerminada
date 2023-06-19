import typing
import datetime
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiListaReserva import Ui_mainWindow
from ManejoArchivo import GestionArchivo
import ventanaHorarios
import ventanaMenuReserva

class ventanaListaReserva(QMainWindow):
    def __init__(self, cont, mod):
        super().__init__()
        self.cont = cont
        self.mod = mod
        self.modBloque = []
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.actualizar()
        self.ui.buscarNombre.textChanged.connect(self.buscador)
        self.ui.listaReservas.itemSelectionChanged.connect(self.seleccFila)
        self.ui.btnEliminar.clicked.connect(self.eliminarHora)
        self.ui.btnVer.clicked.connect(self.verHora)
        self.ventanaH = ventanaHorarios.ventanaHorarios(7, self.cont)
        self.ui.btnModificar.clicked.connect(lambda: self.modificarHora(self.ventanaH))
        self.ui.btnAtras.clicked.connect(lambda: self.volver(ventanaMenuReserva.ventanaMenuReserva(self.cont)))
        
    def volver(self, ventana):
        ventana.show()
        self.hide()    
        
    def getBloque(self, bloque, posi):
        self.mod = True
        self.modBloque = bloque
        self.filaSelecc = posi
        self.modificarHora(self.ventanaH)
        

        
    def modificarHora(self, ventana):
        t = 0
        for r in self.resEnLista:
            if t == self.filaSelecc:
                res = r
                break
            t += 1
        if self.mod == True:
            with open('salas.csv') as file:
                reader = csv.reader(file)
                next(reader)
                i = 0
                for l in reader:
                    if l[4] == res[2] and l[3] == res[4] and l[2] == res[3]:
                        posFila = i
                        break
                    i += 1
            GestionArchivo.modificarLinea("salas.csv", posFila, 1, "None")
            GestionArchivo.modificarLinea("salas.csv", posFila, 5, "False")
            if res[1] == "Control Rutinario":
                with open("Control.csv") as r:
                    read = csv.reader(r)
                    next(read)
                    i = 0
                    for l in read:
                        if l[0] == res[2] and l[1] == res[0] and l[2] == res[4] and l[3] == res[3]:
                            pos = i
                            break
                        i += 1
                GestionArchivo.modificarLinea("Control.csv", pos, 0, self.modBloque[0])
                GestionArchivo.modificarLinea("Control.csv", pos, 2, self.modBloque[1])
                GestionArchivo.modificarLinea("Control.csv", pos, 3, self.modBloque[2])
            elif res[1] == "Quirofano":
                with open("Quirofano.csv") as r:
                    read = csv.reader(r)
                    next(read)
                    i = 0
                    for l in read:
                        if l[0] == res[2] and l[1] == res[0] and l[2] == res[4] and l[3] == res[3]:
                            posi = i
                            break
                        i += 1
                GestionArchivo.modificarLinea("Quirofano.csv", posi, 0, self.modBloque[0])
                GestionArchivo.modificarLinea("Quirofano.csv", posi, 2, self.modBloque[1])
                GestionArchivo.modificarLinea("Quirofano.csv", posi, 3, self.modBloque[2])
            else:
                with open("Citas.csv") as r:
                    read = csv.reader(r)
                    next(read)
                    i = 0
                    for l in read:
                        if l[0] == res[2] and l[1] == res[0] and l[5] == res[3] and l[4] == res[4]:
                            posi = i
                            break
                        i += 1
                with open("salas.csv") as r:
                    read = csv.reader(r)
                    next(read)
                    for l in read:
                        if l[4] == self.modBloque[0] and l[3] == self.modBloque[1] and l[2] == self.modBloque[2]:
                            rutEsp = l[0]
                with open("veterinarios.csv") as r:
                    read = csv.reader(r)
                    next(read)
                    for l in read:
                        if l[0] == rutEsp:
                            nombre = l[1]
                GestionArchivo.modificarLinea("Citas.csv", posi, 0, self.modBloque[0])
                GestionArchivo.modificarLinea("Citas.csv", posi, 2, nombre)
                GestionArchivo.modificarLinea("Citas.csv", posi, 4, self.modBloque[1])
                GestionArchivo.modificarLinea("Citas.csv", posi, 5, self.modBloque[2])
            with open('salas.csv') as file:
                reader = csv.reader(file)
                next(reader)
                i = 0
                for l in reader:
                    if l[4] == self.modBloque[0] and l[3] == self.modBloque[1] and l[2] == self.modBloque[2]:
                        posFila = i
                        break
                    i += 1
            GestionArchivo.modificarLinea("salas.csv", posFila, 1, self.persona[0])
            GestionArchivo.modificarLinea("salas.csv", posFila, 5, "True")
            self.actualizar()
        else:
            if res[1] == "Control Rutinario":
                ventana.cont = 0
            elif res[1] == "Quirofano":
                ventana.cont = 1
            else:
                for l in self.especialista:
                    if l[0] == res[0] and l[1] == res[1] and l[2] == res[2] and l[3] == res[3] and l[4] == res[4]:
                        esp = l[5]
                if esp == "Neurologia":
                    ventana.cont = 2
                elif esp == "Reproduccion":
                    ventana.cont = 3
                elif esp == "Odontologia":
                    ventana.cont = 4
                elif esp == "Oncologia":
                    ventana.cont = 5
                else:
                    ventana.cont = 6
            ventana.guardarCont = 7
            ventana.actualizarLabel()
            ventana.posBloque = self.filaSelecc
            ventana.show()
            self.hide()
        self.mod = False
        
    def verHora(self):
        t = 0
        for r in self.resEnLista:
            if t == self.filaSelecc:
                res = r
                break
            t += 1

        msg = qtw.QMessageBox()
        msg.setWindowTitle("Datos de Reserva")
        fechaHoy = datetime.datetime.now().date()
        fechaH = fechaHoy.strftime("%d/%m/%Y")
        if res[5] == "Por Cumplir":
            msg.setText("Reserva a Nombre del Cliente: " + self.persona[1] + "\nMascota en la Reserva: " + res[0]
                    + "\nTipo de Reserva: " + res[1] + "\n\nBloque de Horario de la Reserva:\n  - Fecha: " + res[2]
                    + "\n  - Horario: " + res[4] + "\n  - En la Sala " + res[3] + "\n\nReserva habilitada para modificacion o cancelacion: Si")
        else:
            msg.setText("Reserva a Nombre del Cliente: " + self.persona[1] + "\nMascota en la Reserva: " + res[0]
                    + "\nTipo de Reserva: " + res[1] + "\n\nBloque de Horario de la Reserva:\n  - Fecha: " + res[2]
                    + "\n  - Horario: " + res[4] + "\n  - En la Sala " + res[3] + "\n\nReserva habilitada para modificacion o cancelacion: No"
                    + "\nRazon: La reserva sobrepasa la fecha en la que fue reservada, para modificar y/o eliminar, esta debe ser antes de la fecha y horas acordadas."
                    + "\nFecha de la Reserva: " + res[2] + " --> Fecha de hoy: " + fechaH)
        msg.exec()
        
    def seleccFila(self):
        self.fila = self.ui.listaReservas.selectedIndexes()
        if self.fila:
            self.ui.btnVer.setEnabled(True)
            self.filaSelecc = self.ui.listaReservas.currentRow()
            i = 0
            for l in self.resEnLista:
                if i == self.filaSelecc:
                    if l[5] == "Por Cumplir":
                        self.ui.btnEliminar.setEnabled(True)
                        self.ui.btnModificar.setEnabled(True)
                    else:
                        self.ui.btnEliminar.setEnabled(False)
                        self.ui.btnModificar.setEnabled(False)
                i += 1
        else:
            self.ui.btnVer.setEnabled(False)
            self.ui.btnAtras.setEnabled(False)
            self.ui.btnEliminar.setEnabled(False)
        
    def eliminarHora(self):
        t = 0
        for r in self.resEnLista:
            if t == self.filaSelecc:
                res = r
                break
            t += 1
        with open('salas.csv') as file:
                reader = csv.reader(file)
                next(reader)
                i = 0
                for l in reader:
                    if l[4] == res[2] and l[3] == res[4] and l[2] == res[3]:
                        posFila = i
                        break
                    i += 1
        GestionArchivo.modificarLinea("salas.csv", posFila, 1, "None")
        GestionArchivo.modificarLinea("salas.csv", posFila, 5, "False")

        if res[1] == "Control Rutinario":
            with open("Control.csv") as r:
                read = csv.reader(r)
                next(read)
                i = 1
                for l in read:
                    if l[0] == res[2] and l[1] == res[0] and l[2] == res[4] and l[3] == res[3]:
                        pos = i
                        break
                    i += 1
            GestionArchivo.eliminar("Control.csv", pos)    
        elif res[1] == "Quirofano":
            with open("Quirofano.csv") as r:
                read = csv.reader(r)
                next(read)
                i = 1
                for l in read:
                    if l[0] == res[2] and l[1] == res[0] and l[2] == res[4] and l[3] == res[3]:
                        posi = i
                        break
                    i += 1
            GestionArchivo.eliminar("Quirofano.csv", posi)
        else:
            with open("Citas.csv") as r:
                read = csv.reader(r)
                next(read)
                i = 1
                for l in read:
                    if l[0] == res[2] and l[1] == res[0] and l[5] == res[3] and l[4] == res[4]:
                        posi = i
                        break
                    i += 1
            GestionArchivo.eliminar("Citas.csv", posi)            
        self.actualizar()
        
                    
        
    
    def actualizar(self):
        self.resEnLista = []
        self.especialista = []
        with open('clientes.csv') as r:
            read = csv.reader(r)
            next(read)
            i = 1
            for l in read:
                if i == self.cont:
                    self.persona = l
                    break    
                i += 1
        self.ui.labelNombre.setText(str(self.persona[1]))
        
        with open("salas.csv") as r:
            read = csv.reader(r)
            next(read)
            self.reservas = []
            for l in read:
                if l[1] == self.persona[0]:
                    self.reservas.append(l)
        
        contFilas = len(self.reservas)
        self.ui.listaReservas.setRowCount(contFilas)
        
        for i, reserva in enumerate(self.reservas):
            with open("Control.csv") as r:
                read = csv.reader(r)
                next(read)
                for l in read:
                    if l[0] == reserva[4] and l[2] == reserva[3] and l[3] == reserva[2]:
                        nombre = l[1]
                        tipo = "Control Rutinario"
                        
            with open("Quirofano.csv") as r:
                read = csv.reader(r)
                next(read)
                for l in read:
                    if l[0] == reserva[4] and l[2] == reserva[3] and l[3] == reserva[2]:
                        nombre = l[1]
                        tipo = "Quirofano"
                        
            with open("Citas.csv") as r:
                read = csv.reader(r)
                next(read)
                for l in read:
                    if l[0] == reserva[4] and l[4] == reserva[3] and l[5] == reserva[2]:
                        nombre = l[1]
                        tipo = ("Cita con especialista: " + str(l[3]))
                        especialista = l[3]
                        especial = [nombre, tipo, reserva[4], reserva[2], reserva[3], especialista]
                        self.especialista.append(especial)
            
            mascota = qtw.QTableWidgetItem(nombre)
            self.ui.listaReservas.setItem(i, 0, mascota)
            
            tipoRes = qtw.QTableWidgetItem(tipo)
            self.ui.listaReservas.setItem(i, 1, tipoRes)
            
            fecha = qtw.QTableWidgetItem(reserva[4])
            self.ui.listaReservas.setItem(i, 2, fecha)
            
            sala = qtw.QTableWidgetItem(reserva[2])
            self.ui.listaReservas.setItem(i, 3, sala)
            
            horario = qtw.QTableWidgetItem(reserva[3])
            self.ui.listaReservas.setItem(i, 4, horario)
            
            fechaHoy = datetime.datetime.now().date()
            horaAhora = datetime.datetime.now().time()
            fechaRes = datetime.datetime.strptime(reserva[4], "%d/%m/%Y").date()
            horaInicio, horaFin = reserva[3].split(" - ")
            horaInicio = datetime.datetime.strptime(horaInicio, "%H:%M").time()
            
            if fechaHoy < fechaRes:
                est = "Por Cumplir"
            elif fechaHoy == fechaRes and horaAhora <= horaInicio:
                est = "Por Cumplir"
            else:
                est = "Cumplido"
            
            estado = qtw.QTableWidgetItem(est)
            self.ui.listaReservas.setItem(i, 5, estado)
            res = [nombre, tipo, reserva[4], reserva[2], reserva[3], est]
            self.resEnLista.append(res)

            
    def buscador(self, texto):
        for row in range(self.ui.listaReservas.rowCount()):
            nombre = self.ui.listaReservas.item(row, 0).text()
            if texto in nombre:
                self.ui.listaReservas.setRowHidden(row, False)
            else:
                self.ui.listaReservas.setRowHidden(row, True)