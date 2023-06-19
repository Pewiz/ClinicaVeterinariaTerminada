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

class ventanaListaReserva(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.resEnLista = []
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.actualizar()
        self.ui.buscarNombre.textChanged.connect(self.buscador)
        self.ui.listaReservas.itemSelectionChanged.connect(self.seleccFila)
        self.ui.btnEliminar.clicked.connect(self.eliminarHora)
        
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
            elif fechaHoy == fechaRes and horaInicio <= horaAhora:
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

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaListaReserva(1)
    ventanaP.show()
    app.exec_()