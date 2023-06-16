from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiReserva import Ui_MainWindow
#import ventanaEjemplo

class ventanaReserva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.actualizarComboBox()
        self.ventanaUi.ButtonIngresar.clicked.connect(self.elegirPersona)
        
    def actualizarComboBox(self):
        with open('clientes.csv') as r:
            read = csv.reader(r)
            next(read)
            nombres = [row for row in read]
        #SOLO CUANDO SE RESERVE, BORRAR DESPUES DE OCUPAR    
            #cliente = []
            #i = 1
            #for l in read:
                #if i == cont:
                    #cliente.append(l)
                    #break
        #masc = []
        #with open('mascotas.csv') as r:
            #lector = csv.reader(r)
            #next(lector)
            #for l in lector:
                #if l[0] == cliente[0]:
                    #masc.append(l)
        
        for nombre in nombres:
            self.ventanaUi.ComboBoxCliente.addItem(str(nombre[1] + " " + str(nombre[2] + " " + str(nombre[3]))))
    
    def elegirPersona(self):
        if self.ventanaUi.ComboBoxCliente.currentIndex() == 0:
            qtw.QMessageBox.warning(self, "ERROR", "Por favor elija un cliente antes de avanzar.\n>:c")
        else:
            persona = self.ventanaUi.ComboBoxCliente.currentIndex()
            #ventana = ventanaEjemplo.ventanaUi(persona) #TAREA CHIQUILLOS, a poco si tilin
            #En la siguiente ventana llaman a la persona y guardan el numero (IMPORTANTE PARA LAS DEMAS VENTANAS)
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaReserva()
    ventanaP.show()
    app.exec_()