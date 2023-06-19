from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiRegistroUrgencia import Ui_MainWindow
import ventanaUrgencia

class ventanaRegistroUrgencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.botonAtras.clicked.connect(self.atras)
        self.cargarCSV("Urgencias.csv")
        
    def cargarCSV(self, filename):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            filas = list(reader)
            
            self.ventanaUi.tableWidget.setRowCount(len(filas))
            self.ventanaUi.tableWidget.setColumnCount(len(filas[0]))
            
            for row in range(len(filas)):
                for column in range(len(filas[row])):
                    item = QTableWidgetItem(filas[row][column])
                    self.ventanaUi.tableWidget.setItem(row, column, item)
                    
    def atras(self):
        self.ventanaUrgencia = ventanaUrgencia.ventanaUrgencia()
        self.ventanaUrgencia.show()
        self.hide()
