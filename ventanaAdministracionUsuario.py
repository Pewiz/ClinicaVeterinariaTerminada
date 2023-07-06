from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from uiAdministracionUsuario import uiAdmin
import ventanaUsuario
import ventanaListaUsuario


class ventanaAdminUsuario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaUi = uiAdmin()
        self.ventanaUi.setupUi(self)
        
        self.ventanaCl = ventanaUsuario.ventanaUsuario()
        self.ventanaLis = ventanaListaUsuario.ventanaLista()
        self.ventanaUi.AGREGARUSUARIO.clicked.connect(lambda: self.cambioV(self.ventanaCl))
        self.ventanaUi.BUSCARUSUARIO.clicked.connect(lambda: self.cambioV(self.ventanaLis))
        self.ventanaUi.btnRegresar.clicked.connect(self.close)
        
    def cambioV(self, ventana):
        ventana.show()
        self.hide()
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaAdminUsuario()
    ventanaP.show()
    app.exec_()
