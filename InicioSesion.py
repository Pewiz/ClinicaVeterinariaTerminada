import sys
from menu import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ManejoArchivo import GestionArchivo
from menu import uiMenu


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        Form.setStyleSheet("background-color:rgb(79, 163, 166)")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(55, 140, 291, 311))
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 125, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #ccc;\n"
"color:  rgb(20, 189, 189);\n"
"border: 2px solid  rgb(0, 189, 189);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(79, 163, 166);\n"
"background-color: #ccc;\n"
"border-radius: 15;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.iniciarSesion)
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 0, 171, 101))
        self.label_3.setStyleSheet("background-image: url(imagenes/usuario.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 170, 221, 31))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: #ccc;\n"
"color:  rgb(20, 189, 189);\n"
"border: 2px solid  rgb(0, 189, 189);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 470, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Chewy")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 40, 1000, 61))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")

        self.setTabOrder(self.lineEdit, self.lineEdit_3)
        
        self.setWindowIcon(QtGui.QIcon('Imagenes/logo.png'))
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Clinica CVI"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Email"))
        self.pushButton.setText(_translate("Form", "Ingresar"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Contraseña"))
        self.label_2.setText(_translate("Form", "@ICINF TPA 2023"))
        self.label.setText(_translate("Form", "Clinica CVI"))
        self.setWindowTitle("Clinica CVI")

    def iniciarSesion(self):
        email = self.lineEdit.text()
        password = self.lineEdit_3.text()
        

        fileHandle = GestionArchivo()
        vets = fileHandle.seleccionarTodo('ArchivosCSV/usuarios.csv')
        
        for vet in vets:
            if vet[6] == email and password == vet[-1]:
                self.ventana = QtWidgets.QMainWindow()
                self.ui = uiMenu()
                self.ui.setupUi(self.ventana)
                self.ventana.show()
                self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

        