from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaAdministracion import ventanaAdmin
from ventanaAdministracionUsuario import ventanaAdminUsuario
import ventanaReserva

class Ui_VentAdminisracionPrincipal(object):
    def setupUi(self, VentAdminisracionPrincipal):
        VentAdminisracionPrincipal.setObjectName("VentAdminisracionPrincipal")
        VentAdminisracionPrincipal.resize(797, 527)
        VentAdminisracionPrincipal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnAdminCliente = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnAdminCliente.setGeometry(QtCore.QRect(130, 250, 191, 61))
        self.btnAdminCliente.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAdminCliente.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                           "border-style: solid;\n"
                                           "border-width: 1px;\n"
                                           "border-color: rgb(0, 51, 102);\n"
                                           "border-radius: 5px;")
        self.btnAdminCliente.setObjectName("btnAdminCliente")
        self.btnAdminCliente.clicked.connect(lambda: self.cambioV())
        self.btnAdminUsuario = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnAdminUsuario.setGeometry(QtCore.QRect(450, 250, 191, 61))
        self.btnAdminUsuario.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnAdminUsuario.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                           "border-style: solid;\n"
                                           "border-width: 1px;\n"
                                           "border-color: rgb(0, 51, 102);\n"
                                           "border-radius: 5px;")
        self.btnAdminUsuario.setObjectName("btnAdminUsuario")
        self.btnAdminUsuario.clicked.connect(lambda: self.cambioV2())
        self.btnReservas = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnReservas.setGeometry(QtCore.QRect(290, 330, 191, 61))
        self.btnReservas.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btnReservas.setStyleSheet("background-color: rgb(79, 163, 166);\n"
                                       "border-style: solid;\n"
                                       "border-width: 1px;\n"
                                       "border-color: rgb(0, 51, 102);\n"
                                       "border-radius: 5px;")
        self.btnReservas.setObjectName("btnReservas")
        self.btnReservas.clicked.connect(lambda: self.cambioV3())
        self.label = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label.setGeometry(QtCore.QRect(0, 0, 797, 120))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes/banner_admin.png").scaled(797, 120))
        self.label.setObjectName("label")
        self.btnRegresar = QtWidgets.QPushButton(VentAdminisracionPrincipal)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.btnRegresar.setStyleSheet("background-color: transparent;")
        self.btnRegresar.setText("")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnRegresar.clicked.connect(VentAdminisracionPrincipal.close)
        self.label_2 = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label_2.setGeometry(QtCore.QRect(240, 140, 281, 311))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagenes/Logo-removebg-preview.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(70, 250, 111, 381))
        self.label_3.setStyleSheet("background-color: transparent;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imagenes/logoLabel3.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(230, 250, 271, 61))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setMouseTracking(False)
        self.label_4.setStyleSheet("background-color: transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imagenes/logoLabel4.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(VentAdminisracionPrincipal)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(300, 330, 50, 61))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setMouseTracking(False)
        self.label_5.setStyleSheet("background-color: transparent;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imagenes/logo_reserva.png").scaled(50, 50))
        self.label_5.setObjectName("label_4")
        self.label_2.raise_()
        self.btnAdminUsuario.raise_()
        self.label.raise_()
        self.btnRegresar.raise_()
        self.label_4.raise_()
        self.btnAdminCliente.raise_()
        self.label_3.raise_()
        self.btnReservas.raise_()
        self.label_5.raise_()

        self.retranslateUi(VentAdminisracionPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentAdminisracionPrincipal)

    def retranslateUi(self, VentAdminisracionPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentAdminisracionPrincipal.setWindowTitle(_translate("VentAdminisracionPrincipal", "Dialog"))
        self.btnAdminCliente.setText(_translate("VentAdminisracionPrincipal", "      Admin Cliente"))
        self.btnAdminUsuario.setText(_translate("VentAdminisracionPrincipal", "     Admin Usuario"))
        self.btnReservas.setText(_translate("VentAdminisracionPrincipal", "     Reservas"))

    def cambiarVent(self, nombre_Vent):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent()
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()

    def cambioV(self):
        ventanaP = ventanaAdmin()
        ventanaP.show()
        
    def cambioV2(self):
        ventanaP = ventanaAdminUsuario()
        ventanaP.show()
        
    def cambioV3(self):
        self.ventana_reserva = ventanaReserva.ventanaReserva()
        self.ventana_reserva.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_VentAdminisracionPrincipal()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())