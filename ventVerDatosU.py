import csv
from PyQt5.QtWidgets import QMainWindow
from uiVentVerDatosU import uiVerD
import ventanaListaUsuario
import ventanaAdministracionUsuario


class ventanaVerDatos(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = uiVerD()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver())
        self.ventanaUi.btnMenuPrincipal.clicked.connect(lambda: self.menuP())

    def actualizar(self):
        with open('usuarios.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                i = (i+1)
                if i == (self.cont+1):
                    usuario = l

        self.ventanaUi.labelNombreC.setText(
            str(usuario[1]) + " " + str(usuario[2]) + " " + str(usuario[3]))
        self.ventanaUi.labelRut.setText(str(usuario[0]))
        self.ventanaUi.labelGenero.setText(str(usuario[4]))
        self.ventanaUi.labelFecha.setText(str(usuario[5]))
        self.ventanaUi.labelCorreo.setText(str(usuario[6]))
        self.ventanaUi.labelTelefono.setText(str(usuario[7]))
        self.ventanaUi.labelDireccion.setText(str(usuario[8]))
        self.ventanaUi.labelCargo.setText(str(usuario[9]))
        self.ventanaUi.labelExperiencia.setText(str(usuario[10]))

    def volver(self):
        ventanaListaUsuario.ventanaLista().show()
        self.close()

    def menuP(self):
        ventanaAdministracionUsuario.ventanaAdminUsuario().show()
        self.close()
