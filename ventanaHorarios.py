import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiHorarios import uiVent
import ventanaCRutinario
import ventanaListaReserva
import ventanaQuirofano
import ventanaCitaEsp

class ventanaHorarios(QMainWindow):
    def __init__(self, cont, cliente):
        super().__init__()
        self.cont = cont #Contador para reconocer que tipo de reserva es (quirofano, especialista, rutinario)
        self.cliente = cliente
        self.ventanaUi = uiVent()
        self.guardarCont = 0
        self.ventanaUi.setupUi(self)
        if self.cont == 0:
            self.ventanaUi.label_9.setText("Horarios: Ct Rutinario.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaCRutinario.ventanaCRutinario(self.cliente, self.bloque)))
        elif self.cont == 1:
            self.ventanaUi.label_9.setText("Horarios: Quirofano.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaQuirofano.ventanaQuirofano(self.cliente, self.bloque)))
        elif self.cont == 2:
            self.ventanaUi.label_9.setText("Horarios: Esp. Neurologo.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaCitaEsp.ventanaCitaEsp(self.cliente, self.bloque)))
            self.especSelecc = 0
        elif self.cont == 3:
            self.ventanaUi.label_9.setText("Horarios: Esp. Reproduccion.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaCitaEsp.ventanaCitaEsp(self.cliente, self.bloque)))
            self.especSelecc = 0
        elif self.cont == 4:
            self.ventanaUi.label_9.setText("Horarios: Esp. Odontologia.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaCitaEsp.ventanaCitaEsp(self.cliente, self.bloque)))
            self.especSelecc = 0
        elif self.cont == 5:
            self.ventanaUi.label_9.setText("Horarios: Esp. Oncologo.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaCitaEsp.ventanaCitaEsp(self.cliente, self.bloque)))
            self.especSelecc = 0
        elif self.cont == 6:
            self.ventanaUi.label_9.setText("Horarios: Esp. Cardiologia.")
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaCitaEsp.ventanaCitaEsp(self.cliente, self.bloque)))
            self.especSelecc = 0
        self.actualizarFecha()
        self.actualizarHorario()
        self.ventanaUi.FechaHoy.dateChanged.connect(self.actualizarHorario)
        self.ventanaUi.btnElegir.setEnabled(False)
        self.ventanaUi.listaHorario.itemSelectionChanged.connect(self.seleccFila)
        self.ventanaUi.btnElegir.clicked.connect(self.elegirHora)
        self.bloque = []
        
    def volver(self, ventana):
        ventana.show()
        self.close()
        
        
    def actualizarLabel(self):
        if self.guardarCont == 7:
            self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver(ventanaListaReserva.ventanaListaReserva(self.cliente, False)))
            self.actualizarHorario()
            self.ventanaUi.label_9.setText("Horarios: Modificacion.")
            self.posBloque = 0
    
    
    def seleccFila(self):
        self.fila = self.ventanaUi.listaHorario.selectedIndexes()
        if self.fila:
            self.ventanaUi.btnElegir.setEnabled(True)
            self.horaSelecc = self.ventanaUi.listaHorario.currentRow()
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
            fechaHoy = datetime.datetime.now().date()
            horaAhora = datetime.datetime.now().time()
            if self.cont == 0 or self.cont == 7:
                for l in read:
                    horaInicio, horaFin = l[3].split(" - ")
                    horaInicio = datetime.datetime.strptime(horaInicio, "%H:%M").time()
                    if fecha == fechaHoy:
                        if l[4] == fechaH and horaAhora <= horaInicio:
                            self.horarios.append(l)
                    else:
                        if l[4] == fechaH:
                            self.horarios.append(l)
            elif self.cont != 0:
                for l in read:
                    horaInicio, horaFin = l[3].split(" - ")
                    horaInicio = datetime.datetime.strptime(horaInicio, "%H:%M").time()
                    for k in self.veterinarios:
                        if fecha == fechaHoy:
                            if l[0] == k[0] and l[4] == fechaH and horaAhora <= horaInicio:
                                self.horarios.append(l)
                        else:
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
    
    def elegirHora(self):
        if self.guardarCont == 7:
            self.cont = 7
        k = 0
        for l in self.horaEnLista:
            if k == self.horaSelecc and l[5] == "False":
                eleccion = l
                flag = False
                break
            k += 1
            flag = True
        if(flag == False):
            self.bloque = [eleccion[4], eleccion[3], eleccion[2]]
            if self.cont == 0:
                ventana = ventanaCRutinario.ventanaCRutinario(self.cliente, self.bloque)
                ventana.show()
                self.close()
            if self.cont == 1:
                ventana = ventanaQuirofano.ventanaQuirofano(self.cliente, self.bloque)
                ventana.show()
                self.close()
            if self.cont >= 2 and self.cont <= 6:
                with open("veterinarios.csv") as r:
                    read = csv.reader(r)
                    next(read)
                    for l in read:
                        if l[0] == eleccion[0]:
                            nombreVet = l[1]
                ventanaE = ventanaCitaEsp.ventanaCitaEsp(self.cliente, self.bloque)
                ventanaE.show()
                ventanaE.actualizarComboBoxEspLabel(self.especSelecc, str(nombreVet))
                self.close()
            if self.cont == 7:
                ventanaM = ventanaListaReserva.ventanaListaReserva(self.cliente, True)
                ventanaM.getBloque(self.bloque, self.posBloque)
                ventanaM.show()
                self.close()
        else:
            qtw.QMessageBox.warning(self, "ERROR, Horario ya en uso", "Por favor elija un horario que no este en uso.\nTip: Para saber si estan en uso o no, revise el color del horario en la lista.")
            
        
        
#if __name__=="__main__":
#    app = QApplication(sys.argv)
#    ventanaP = ventanaHorarios(1)
#    ventanaP.show()
#    app.exec_()