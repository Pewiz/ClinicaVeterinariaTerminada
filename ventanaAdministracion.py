#ESTE ARCHIVO ES EL MAIN DEL CODIGO, EJECUTAR DESDE AQUI
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from uiAdministracion import uiAdmin
import ventanaCliente
import ventanaLista


class ventanaAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaUi = uiAdmin()
        self.ventanaUi.setupUi(self)
        
        self.ventanaCl = ventanaCliente.ventanaCliente()
        self.ventanaLis = ventanaLista.ventanaLista()
        self.ventanaUi.AGREGARPACIENTE.clicked.connect(lambda: self.cambioV(self.ventanaCl))
        self.ventanaUi.BUSCARPACIENTE.clicked.connect(lambda: self.cambioV(self.ventanaLis))
        
    def cambioV(self, ventana):
        ventana.show()
        self.hide()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaAdmin()
    ventanaP.show()
    app.exec_()
