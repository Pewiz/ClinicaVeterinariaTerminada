from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ventanaCliente
import ventanaLista
import ventanaUsuario
import ventanaListaUsuario

class Ui_VentAdminisracionPrincipal(object):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, VentAdminisracionPrincipal):
        VentAdminisracionPrincipal.setObjectName("VentAdminisracionPrincipal")
        VentAdminisracionPrincipal.resize(989, 620)
        VentAdminisracionPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ventanaCl = ventanaCliente.ventanaCliente()
        self.ventanaLis = ventanaLista.ventanaLista()
        self.ventanaClUsuario = ventanaUsuario.ventanaUsuario()
        self.ventanaLisUsuario = ventanaListaUsuario.ventanaLista()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregarCliente = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnAgregarCliente.setGeometry(QtCore.QRect(120, 230, 301, 81))
        self.btnAgregarCliente.setFont(font)
        self.btnAgregarCliente.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAgregarCliente.setStyleSheet("background-image: url(imagenes/logoLabel4.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnAgregarCliente.clicked.connect(lambda: self.cambioV(self.ventanaCl))
        self.btnBuscarCliente = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnBuscarCliente.setGeometry(QtCore.QRect(600, 230, 301, 81))
        self.btnBuscarCliente.setFont(font)
        self.btnBuscarCliente.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnBuscarCliente.setStyleSheet("background-image: url(imagenes/logoLabel3.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnBuscarCliente.clicked.connect(lambda: self.cambioV(self.ventanaLis))
        
        self.btnAgregarUsuario = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnAgregarUsuario.setGeometry(QtCore.QRect(120, 420, 301, 81))
        self.btnAgregarUsuario.setFont(font)
        self.btnAgregarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAgregarUsuario.setStyleSheet("background-image: url(imagenes/logoLabel4.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnAgregarUsuario.clicked.connect(lambda: self.cambioV(self.ventanaClUsuario))
        self.btnBuscarUsuario = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnBuscarUsuario.setGeometry(QtCore.QRect(600, 420, 301, 81))
        self.btnBuscarUsuario.setFont(font)
        self.btnBuscarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnBuscarUsuario.setStyleSheet("background-image: url(imagenes/logoLabel3.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnBuscarUsuario.clicked.connect(lambda: self.cambioV(self.ventanaLisUsuario))
        
        self.label = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label.setGeometry(QtCore.QRect(0, 0, 989, 140))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes/banner_admin.png").scaled(989, 140))
        self.label.setObjectName("label")
        self.btnRegresar = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.btnRegresar.setStyleSheet("background-color: transparent;")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnRegresar.clicked.connect(VentAdminisracionPrincipal.close)
        self.label_2 = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label_2.setGeometry(QtCore.QRect(320, 150, 371, 361))
        self.label_2.setStyleSheet("image: url(imagenes/Logo-removebg-preview.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.btnBuscarCliente.raise_()
        self.label.raise_()
        self.btnRegresar.raise_()
        self.btnAgregarCliente.raise_()
        self.btnAgregarUsuario.raise_()
        self.btnBuscarUsuario.raise_()

        self.retranslateUi(VentAdminisracionPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentAdminisracionPrincipal)

    def retranslateUi(self, VentAdminisracionPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentAdminisracionPrincipal.setWindowTitle(_translate("VentAdminisracionPrincipal", "Dialog"))
        self.btnAgregarCliente.setText(_translate("VentAdminisracionPrincipal", "      Agregar Cliente"))
        self.btnBuscarCliente.setText(_translate("VentAdminisracionPrincipal", "     Buscar Cliente"))
        self.btnAgregarUsuario.setText(_translate("VentAdminisracionPrincipal", "      Agregar Usuario"))
        self.btnBuscarUsuario.setText(_translate("VentAdminisracionPrincipal", "     Buscar Usuario"))

    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()
        
    def cambioV(self, ventana):
        #ventanaPrincipal = self.btnAgregarCliente.window()
        #ventanaPrincipal.hide()
        ventana.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_VentAdminisracionPrincipal()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())