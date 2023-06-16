from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiHorarios import uiVent

class ventanaHorarios(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont #Contador para reconocer que tipo de reserva es (quirofano, especialista, rutinario)
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
    
    def actualizarFecha(self):
        fechaHoy = QtCore.QDate.currentDate()
        self.ventanaUi.FechaHoy.setMinimumDate(fechaHoy)
        self.ventanaUi.FechaHoy.setDate(fechaHoy)

    def actualizarHorario(self):
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
                etiqueta.setBackground(qtg.QColor('green'))
            etiqueta.setTextAlignment(qc.Qt.AlignCenter)
            etiqueta.setFlags(qc.Qt.ItemIsEnabled)
            self.ventanaUi.listaHorario.setItem(i, 4, etiqueta)
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaHorarios(0)
    ventanaP.show()
    app.exec_()