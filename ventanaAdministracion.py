from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtCore, QtGui
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
        self.ventanaUi.AGREGARCLIENTE.clicked.connect(lambda: self.cambioV(self.ventanaCl))
        self.ventanaUi.BUSCARCLIENTE.clicked.connect(lambda: self.cambioV(self.ventanaLis))
        self.ventanaUi.btnRegresar.clicked.connect(self.close)

        self.ButtonAtras = QPushButton(self.ventanaUi.centralwidget)
        self.ButtonAtras.setGeometry(QtCore.QRect(20, 25, 34, 34))
        self.ButtonAtras.setIcon(QtGui.QIcon('imagenes\Atras.png'))
        self.ButtonAtras.setText("")
        self.ButtonAtras.setIconSize(QtCore.QSize(150, 150))
        self.ButtonAtras.setStyleSheet("background-color: transparent;\n""border: none;\n""")
        self.ButtonAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonAtras.clicked.connect(self.close)

    def cambioV(self, ventana):
        ventana.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaAdmin()
    ventanaP.show()
    sys.exit(app.exec_())
