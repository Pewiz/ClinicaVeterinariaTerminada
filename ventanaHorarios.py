from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiHorarios import uiVent
import ventanaCRutinario
import ventanaQuirofano

class ventanaHorarios(QMainWindow):
    def __init__(self, cont, cliente):
        super().__init__()
        self.cont = cont #Contador para reconocer que tipo de reserva es (quirofano, especialista, rutinario)
        self.cliente = cliente
        self.ventanaUi = uiVent()
        self.ventanaUi.setupUi(self)
        if self.cont == 0:
            self.ventanaUi.label_9.setText("Horarios: Ct Rutinario.")
        elif self.cont == 1:
            self.ventanaUi.label_9.setText("Horarios: Quirofano.")
        elif self.cont == 2:
            self.ventanaUi.label_9.setText("Horarios: Esp. Neurologo.")
        elif self.cont == 3:
            self.ventanaUi.label_9.setText("Horarios: Esp. Reproduccion.")
        elif self.cont == 4:
            self.ventanaUi.label_9.setText("Horarios: Esp. Odontologia.")
        elif self.cont == 5:
            self.ventanaUi.label_9.setText("Horarios: Esp. Oncologo.")
        elif self.cont == 6:
            self.ventanaUi.label_9.setText("Horarios: Esp. Cardiologia.")
        self.actualizarFecha()
        self.actualizarHorario()
        self.ventanaUi.FechaHoy.dateChanged.connect(self.actualizarHorario)
        self.ventanaUi.btnElegir.setEnabled(False)
        self.ventanaUi.listaHorario.itemSelectionChanged.connect(self.seleccFila)
        self.ventanaUi.btnElegir.clicked.connect(self.elegirHora)
        self.bloque = []
        
    
    def seleccFila(self):
        self.fila = self.ventanaUi.listaHorario.selectedIndexes()
        if self.fila:
            self.ventanaUi.btnElegir.setEnabled(True)
            self.horaSelecc = self.ventanaUi.listaHorario.currentRow()
            print(self.horaSelecc)
        else:
            self.ventanaUi.btnElegir.setEnabled(False)
        
        
    def actualizarFecha(self):
        fechaHoy = QtCore.QDate.currentDate()
        self.ventanaUi.FechaHoy.setMinimumDate(fechaHoy)
        self.ventanaUi.FechaHoy.setDate(fechaHoy)

    def actualizarHorario(self):
        self.horaEnLista = []
        if self.cont != 0:
            with open("veterinarios.csv") as r:
                read = csv.reader(r)
                next(read)
                self.veterinarios = []
                if self.cont == 1:
                    for l in read:
                        if l[6] == "Cirujano":
                            self.veterinarios.append(l)
                elif self.cont == 2:
                    for l in read:
                        if l[6] == "Neurologia":
                            self.veterinarios.append(l)
                elif self.cont == 3:
                    for l in read:
                        if l[6] == "Reproduccion":
                            self.veterinarios.append(l)
                elif self.cont == 4:
                    for l in read:
                        if l[6] == "Odontologia":
                            self.veterinarios.append(l)
                elif self.cont == 5:
                    for l in read:
                        if l[6] == "Oncologia":
                            self.veterinarios.append(l)
                elif self.cont == 6:
                    for l in read:
                        if l[6] == "Cardiologia":
                            self.veterinarios.append(l)
        with open('salas.csv') as r:
            read = csv.reader(r)
            next(read)
            self.horarios = []
            fecha = self.ventanaUi.FechaHoy.date()
            fechaH = fecha.toString("dd/MM/yyyy")
            if self.cont == 0:
                for l in read:
                    if l[4] == fechaH:
                        self.horarios.append(l)
            elif self.cont != 0:
                for l in read:
                    for k in self.veterinarios:
                        if l[0] == k[0] and l[4] == fechaH:
                            self.horarios.append(l)
        
        self.horarios = sorted(self.horarios, key=lambda x: (int(x[3].split(':')[0]),int(x[2])))
        
        
        contFilas = len(self.horarios)
        self.ventanaUi.listaHorario.setRowCount(contFilas)
        
        for i, horario in enumerate(self.horarios):
            self.horaEnLista.append(horario)
            hora = qtw.QTableWidgetItem(horario[3])
            self.ventanaUi.listaHorario.setItem(i, 0, hora)
            
            fechaL = qtw.QTableWidgetItem(horario[4])
            self.ventanaUi.listaHorario.setItem(i, 1, fechaL)
            
            sala = qtw.QTableWidgetItem(horario[2])
            self.ventanaUi.listaHorario.setItem(i, 2, sala)
            
            with open('veterinarios.csv') as r:
                read = csv.reader(r)
                next(read)
                for l in read:
                    if l[0] == horario[0]:
                        personaAux = (l[1] + " " + l[2])
                        break
                    
            persona = qtw.QTableWidgetItem(personaAux)
            self.ventanaUi.listaHorario.setItem(i, 3, persona)
            
            etiqueta = qtw.QTableWidgetItem()
            if str(horario[5]) == "False":
                etiqueta.setBackground(qtg.QColor('green'))
            else:
                etiqueta.setBackground(qtg.QColor('red'))
            etiqueta.setTextAlignment(qc.Qt.AlignCenter)
            etiqueta.setFlags(qc.Qt.ItemIsEnabled)
            self.ventanaUi.listaHorario.setItem(i, 4, etiqueta)
        print(str(self.horaEnLista))
    
    def elegirHora(self):
        k = 0
        for l in self.horaEnLista:
            if k == self.horaSelecc:
                eleccion = l
                break
            k += 1
        self.bloque = [eleccion[4], eleccion[3], eleccion[2]]
        if self.cont == 0:
            ventana = ventanaCRutinario.ventanaCRutinario(self.cliente, self.bloque)
            ventana.show()
            self.hide()
        if self.cont == 1:
            ventanaQ = ventanaQuirofano.ventanaQuirofano(self.cliente, self.bloque)
            ventanaQ.show()
            self.hide()
            
        
        
if __name__=="__main__":
   app = QApplication(sys.argv)
   ventanaP = ventanaHorarios(1)
   ventanaP.show()
   app.exec_()