from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ventanaReserva import ventanaReserva
from VentAdminPrincipal import Ui_VentAdminisracionPrincipal


class uiMenu(QMainWindow):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(989, 595)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 270, 301, 81))
        self.pushButton.clicked.connect(lambda: self.abrirVentanaReserva())
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(imagenes/clinica.png);\n"
"background-repeat: no-repeat;\n"
"background-color: rgb(79, 163, 166);\n"
"border-radius: 30%;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 270, 301, 81))
        self.pushButton_2.clicked.connect(lambda: self.abrirVentanaAdministracion())
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-image: url(imagenes/admin.png);\n"
"background-repeat: no-repeat;\n"
"background-color: rgb(79, 163, 166);\n"
"border-radius: 30%;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 131))
        self.frame.setStyleSheet("background-color: rgb(79, 163, 166);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 30, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
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
        self.ButtonAtras.clicked.connect(Menu.close)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 150, 371, 361))
        self.label_2.setStyleSheet("image: url(imagenes/Logo-removebg-preview.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.frame.raise_()
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 21))
        self.menubar.setObjectName("menubar")
        Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def cambioV(self, ventana):
        ventana.show()
        self.hide()
    
    def abrirVentanaReserva(self):
        self.ventanaReserva = ventanaReserva()
        self.ventanaReserva.show()

    def abrirVentanaAdministracion(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentAdminisracionPrincipal()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.pushButton.setText(_translate("Menu", "Clinica"))
        self.pushButton_2.setText(_translate("Menu", " Administracion"))
        self.label.setText(_translate("Menu", "CLINICA CVI"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
