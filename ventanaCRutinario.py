from PyQt5.QtWidgets import QMainWindow
import csv
from uiReservaCtRutinario import Ui_MainWindow
import ventanaReserva
import ventanaHorarios

class ventanaCRutinario(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.horario = ventanaHorarios.ventanaHorarios(0)
        self.ventanaUi.ButtonHorarios.clicked.connect(lambda : self.cambio(self.horario))
        #self.ventanaReserva = ventanaReserva.ventanaReserva()
        #self.ventanaUi.ButtonAtras.clicked.connect(self.retroceder)

    def actualizarComboBoxMascota(self, rut_cliente):
        self.ventanaUi.MascotaComboBox.clear()
        self.ventanaUi.MascotaComboBox.addItem("Elegir Mascota")

        with open('mascotas.csv') as file:
            reader = csv.reader(file)
            next(reader)

            mascotas_cliente = [mascota for mascota in reader if mascota[0] == rut_cliente]

        for mascota in mascotas_cliente:
            self.ventanaUi.MascotaComboBox.addItem(mascota[1])
    
    # def retroceder(self):
    #     self.ventanaReserva.show()
    #     self.close()
    
    def cambio(self, ventana):
        ventana.actualizarHorario()
        ventana.show()
        self.hide()



if __name__ == "__main__":
    ventanaC = ventanaCRutinario(0)
    ventanaC.show()