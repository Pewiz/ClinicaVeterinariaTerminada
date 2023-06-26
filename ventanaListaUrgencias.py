from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import sys
import csv
import PyQt5.QtWidgets as qtw
from uiListaUrgencias import Ui_mainWindow
import ventanaUrgencia

class ventanaListaUrgencias(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ventana = ventanaUrgencia.ventanaUrgencia()
        self.ui.btnAtras.clicked.connect(self.atras)
        self.actualizarFecha()
        self.actualizar()
        self.ui.fechaFiltro.dateChanged.connect(self.actualizar)
        self.ui.buscarNombre.textChanged.connect(self.buscador)
        self.ui.listaUrgencias.itemDoubleClicked.connect(self.prueba)
        
    def prueba(self):
        cont = self.ui.listaUrgencias.currentRow()
        i = 0
        for l in self.urgencias:
            if i == cont:
                dato = l
                break
            i += 1
        msg = qtw.QMessageBox()
        msg.setWindowTitle("Datos de urgencia")
        if dato[6] == "Si":
            msg.setText("A nombre del cliente " + dato[1] + ".\nSe ha registrado e ingresado la mascota de nombre " + dato[0] + " a urgencias de la Clinica CVI."
                    + "\n\nDatos del Cliente:\n  - Telefono Celular: " + dato[2] + "\n  - Domicilio: " + dato[3] + "\n\nGravedad de urgencia de la mascota (1: Leve - 5: Muy Grave): " + dato[4]
                    + "\nLa mascota requirió de una ambulancia para llegar a la Clinica.\n\nFecha del llamado de urgencia: " + dato[5] + "\nA la hora: " + dato[7])
        else:
            msg.setText("A nombre del cliente " + dato[1] + ".\nSe ha registrado e ingresado la mascota de nombre " + dato[0] + " a urgencias de la Clinica CVI."
                    + "\n\nDatos del Cliente:\n  - Telefono Celular: " + dato[2] + "\n  - Domicilio: " + dato[3] + "\n\nGravedad de urgencia de la mascota (1: Leve - 5: Muy Grave): " + dato[4]
                    + "\nLa mascota NO requirió de una ambulancia para llegar a la Clinica, fue llevado gracias al cliente.\n\nFecha del llamado de urgencia: " + dato[5] + "\nA la hora: " + dato[7])
        msg.exec_()            
        
    def actualizarFecha(self):
        fechaHoy = QtCore.QDate.currentDate()
        self.ui.fechaFiltro.setDate(fechaHoy)
    
    def actualizar(self):
        fecha = self.ui.fechaFiltro.date()
        fechaH = fecha.toString("dd/MM/yyyy")
        self.ui.buscarNombre.clear()
        with open("Urgencias.csv") as r:
            read = csv.reader(r)
            next(read)
            self.urgencias = []
            for l in read:
                if l[5] == fechaH:
                    self.urgencias.append(l)
        contFilas = len(self.urgencias)
        self.ui.listaUrgencias.setRowCount(contFilas)
        
        for i, urgencia in enumerate(self.urgencias):
            mascota = qtw.QTableWidgetItem(urgencia[0])
            self.ui.listaUrgencias.setItem(i, 0, mascota)
            
            dueño = qtw.QTableWidgetItem(urgencia[1])
            self.ui.listaUrgencias.setItem(i, 1, dueño)
            
            gravedad = qtw.QTableWidgetItem(urgencia[4])
            self.ui.listaUrgencias.setItem(i, 2, gravedad)
            
            fecha = qtw.QTableWidgetItem(urgencia[5])
            self.ui.listaUrgencias.setItem(i, 3, fecha)
            
            ambulancia = qtw.QTableWidgetItem(urgencia[6])
            self.ui.listaUrgencias.setItem(i, 4, ambulancia)
    
    def buscador(self, texto):
        for row in range(self.ui.listaUrgencias.rowCount()):
            nombre = self.ui.listaUrgencias.item(row, 0).text()
            if texto in nombre:
                self.ui.listaUrgencias.setRowHidden(row, False)
            else:
                self.ui.listaUrgencias.setRowHidden(row, True)
    
    def atras(self):
        self.ventana.show()
        self.close()