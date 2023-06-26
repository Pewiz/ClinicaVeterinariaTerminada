from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import PyQt5.QtWidgets as qtw
from uiReserva import Ui_MainWindow
import ventanaMenuReserva
import ventanaUrgencia

class ventanaReserva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.ButtonIngresar.clicked.connect(self.elegirPersona)
        self.ventanaUi.ButtonUrgencia.clicked.connect(self.urgencia)
        self.cargarClientes()

    def cargarClientes(self):
        with open('clientes.csv') as file:
            reader = csv.reader(file)
            next(reader)

            self.clientes = [row for row in reader]
            
            for cliente in self.clientes:
                nombre_completo = f"{cliente[1]} {cliente[2]} {cliente[3]}"
                self.ventanaUi.ComboBoxCliente.addItem(nombre_completo)

    def elegirPersona(self):
        if self.ventanaUi.ComboBoxCliente.currentIndex() == 0:
            qtw.QMessageBox.warning(self, "ERROR", "Por favor elija un cliente antes de avanzar.\n>:c")
        else:
            contador = self.ventanaUi.ComboBoxCliente.currentIndex()
            self.ventana = ventanaMenuReserva.ventanaMenuReserva(contador)
            self.ventana.show()
            self.close()
    
    def urgencia(self):
        self.ventanaUrgencia = ventanaUrgencia.ventanaUrgencia()
        self.ventanaUrgencia.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaP = ventanaReserva()
    ventanaP.show()
    app.exec_()