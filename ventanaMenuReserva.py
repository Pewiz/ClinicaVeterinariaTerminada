from PyQt5.QtWidgets import QMainWindow
import csv
from uiMenuClinica import Ui_MainWindow
import ventanaReserva
import ventanaCRutinario
import ventanaQuirofano
import ventanaCitaEsp
import ventanaListaReserva

class ventanaMenuReserva(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.hora = []
        self.actualizarNombre()
        self.v = ventanaReserva.ventanaReserva()
        self.ventanaUi.botonAtras.clicked.connect(lambda: self.cambio(self.v))
        self.venCt = ventanaCRutinario.ventanaCRutinario(self.cont, self.hora)
        self.venQ = ventanaQuirofano.ventanaQuirofano(self.cont, self.hora)
        self.venCE = ventanaCitaEsp.ventanaCitaEsp(self.cont, self.hora)
        self.venL = ventanaListaReserva.ventanaListaReserva(self.cont, False)
        self.ventanaUi.control_rutinario.clicked.connect(lambda: self.cambio(self.venCt))
        self.ventanaUi.quirofano.clicked.connect(lambda: self.cambio(self.venQ))
        self.ventanaUi.especialista.clicked.connect(lambda: self.cambio(self.venCE))
        self.ventanaUi.Lista_reservas.clicked.connect(lambda: self.cambio(self.venL))

    def cambio(self, ventana):
        ventana.show()
        self.close()

    def actualizarNombre(self):
        with open("clientes.csv") as r:
            reader = csv.reader(r)
            next(reader)
            i = 1
            for l in reader:
                if i == self.cont:
                    self.persona = l
                    break
                i += 1
        self.ventanaUi.label_2.setText("Bienvenido: " + self.persona[1])