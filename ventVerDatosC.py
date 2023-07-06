import csv
from PyQt5.QtWidgets import QMainWindow
from uiVentVerDatosC import uiVerD
import ventanaLista
import ventanaAdministracion


class ventanaVerDatos(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = uiVerD()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver())
        self.ventanaUi.btnMenuPrincipal.clicked.connect(lambda: self.menuP())

    def actualizar(self):
        with open('ArchivosCSV/clientes.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                i = (i+1)
                if i == (self.cont+1):
                    cliente = l

        self.ventanaUi.labelNombreC.setText(
            str(cliente[1]) + " " + str(cliente[2]) + " " + str(cliente[3]))
        self.ventanaUi.labelRut.setText(str(cliente[0]))
        self.ventanaUi.labelGenero.setText(str(cliente[4]))
        self.ventanaUi.labelFecha.setText(str(cliente[5]))
        self.ventanaUi.labelCorreo.setText(str(cliente[6]))
        self.ventanaUi.labelTelefono.setText(str(cliente[7]))
        self.ventanaUi.labelDireccion.setText(str(cliente[8]))

    def volver(self):
        ventanaLista.ventanaLista().show()
        self.close()

    def menuP(self):
        self.close()
