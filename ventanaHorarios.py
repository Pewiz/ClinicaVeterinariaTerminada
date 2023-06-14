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
        
        acTimer = QtCore.QTimer()
        acTimer.timeout.connect(self.actualizarFecha)
        acTimer.start(5000)
        self.actualizarHorario()
        self.ventanaUi.FechaHoy.dateChanged.connect(self.actualizarHorario)
    
    def actualizarFecha(self):
        fechaHoy = QtCore.QDate.currentDate()
        self.ventanaUi.FechaHoy.setMinimumDate(fechaHoy)
        self.ventanaUi.FechaHoy.setDate(fechaHoy)

    def actualizarHorario(self):
        with open('salas.csv') as r:
            read = csv.reader(r)
            next(read)
            self.horarios = []
            fecha = self.ventanaUi.FechaHoy.date()
            fechaH = fecha.toString("dd/MM/yyyy")
            for l in read:
                if l[4] == fechaH:
                    self.horarios.append(l)
                
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
    ventanaP = ventanaHorarios()
    ventanaP.show()
    app.exec_()