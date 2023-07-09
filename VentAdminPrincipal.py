from PyQt5 import QtCore, QtGui, QtWidgets
import ventanaCliente
import ventanaLista
import ventanaUsuario
import ventanaListaUsuario

class Ui_VentAdminisracionPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, VentAdminisracionPrincipal):
        VentAdminisracionPrincipal.setWindowIcon(QtGui.QIcon('Imagenes/logo.png'))
        VentAdminisracionPrincipal.setObjectName("VentAdminisracionPrincipal")
        VentAdminisracionPrincipal.resize(989, 620)
        VentAdminisracionPrincipal.setMinimumSize(QtCore.QSize(989, 620))
        VentAdminisracionPrincipal.setMaximumSize(QtCore.QSize(989, 620))
        VentAdminisracionPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregarCliente = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnAgregarCliente.setGeometry(QtCore.QRect(120, 230, 301, 81))
        self.btnAgregarCliente.setFont(font)
        self.btnAgregarCliente.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAgregarCliente.setStyleSheet("background-image: url(imagenes/cliente_logo.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnAgregarCliente.clicked.connect(lambda: self.cambioV(ventanaCliente.ventanaCliente()))
        self.btnBuscarCliente = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnBuscarCliente.setGeometry(QtCore.QRect(600, 230, 301, 81))
        self.btnBuscarCliente.setFont(font)
        self.btnBuscarCliente.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnBuscarCliente.setStyleSheet("background-image: url(imagenes/cliente_buscar_logo.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnBuscarCliente.clicked.connect(lambda: self.cambioV(ventanaLista.ventanaLista()))
        
        self.btnAgregarUsuario = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnAgregarUsuario.setGeometry(QtCore.QRect(120, 420, 301, 81))
        self.btnAgregarUsuario.setFont(font)
        self.btnAgregarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAgregarUsuario.setStyleSheet("background-image: url(imagenes/usuario_logo.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnAgregarUsuario.clicked.connect(lambda: self.cambioV(ventanaUsuario.ventanaUsuario()))
        self.btnBuscarUsuario = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnBuscarUsuario.setGeometry(QtCore.QRect(600, 420, 301, 81))
        self.btnBuscarUsuario.setFont(font)
        self.btnBuscarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnBuscarUsuario.setStyleSheet("background-image: url(imagenes/usuario_buscar_logo.png);\n"
                                      "background-repeat: no-repeat;\n"
                                      "background-color: rgb(79, 163, 166);\n"
                                      "border-radius: 30%;")
        self.btnBuscarUsuario.clicked.connect(lambda: self.cambioV(ventanaListaUsuario.ventanaLista()))
        
        
        self.frame = QtWidgets.QFrame(VentAdminisracionPrincipal)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 131))
        self.frame.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ButtonAtras = QtWidgets.QPushButton(self.frame)
        self.ButtonAtras.setGeometry(QtCore.QRect(30, 30, 50, 50))
        self.ButtonAtras.setStyleSheet("\n"
"\n"
"\n"
"QPushButton {\n"
"  \n"
"    \n"
"    border-radius: 20px;\n"
"\n"
"  \n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: #74b6b6;\n"
"}\n"
"")
        self.ButtonAtras.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/boton_regresar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonAtras.setIcon(icon)
        self.ButtonAtras.setIconSize(QtCore.QSize(50, 50))
        self.ButtonAtras.setObjectName("ButtonAtras")
        self.ButtonAtras.clicked.connect(VentAdminisracionPrincipal.close)
        self.label_2 = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label_2.setGeometry(QtCore.QRect(320, 150, 371, 361))
        self.label_2.setStyleSheet("image: url(imagenes/Logo-removebg-preview.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label_titulo = QtWidgets.QLabel(self.frame)
        self.label_titulo.setGeometry(QtCore.QRect(240, 30, 540, 75))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(60)
        self.label_titulo.setFont(font)
        self.label_titulo.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_titulo.setObjectName("label_titulo")
        self.btnBuscarCliente.raise_()
        self.btnAgregarCliente.raise_()
        self.btnAgregarUsuario.raise_()
        self.btnBuscarUsuario.raise_()

        self.retranslateUi(VentAdminisracionPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentAdminisracionPrincipal)

    def cambioV(self, ventana):
        self.hide()
        ventana.show()
        
    
    def retranslateUi(self, VentAdminisracionPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentAdminisracionPrincipal.setWindowTitle(_translate("VentAdminisracionPrincipal", "Clinica CVI"))
        self.btnAgregarCliente.setText(_translate("VentAdminisracionPrincipal", "      Agregar Cliente"))
        self.btnBuscarCliente.setText(_translate("VentAdminisracionPrincipal", "     Buscar Cliente"))
        self.btnAgregarUsuario.setText(_translate("VentAdminisracionPrincipal", "      Agregar Usuario"))
        self.btnBuscarUsuario.setText(_translate("VentAdminisracionPrincipal", "     Buscar Usuario"))
        self.label_titulo.setText("Administración")