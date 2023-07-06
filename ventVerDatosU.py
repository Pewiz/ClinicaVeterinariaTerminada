import csv
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from uiVentVerDatosU import uiVerD
import ventanaListaUsuario
import ventanaAdministracionUsuario
from VentAsignarHoraVet import Ui_VentAsignarHorario



class ventanaVerDatos(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = uiVerD()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.btnAtras.clicked.connect(lambda: self.volver())
        self.ventanaUi.btnMenuPrincipal.clicked.connect(lambda: self.menuP())
        self.ventanaUi.btnAsignarHorario.clicked.connect(lambda: self.cambiarVent(Ui_VentAsignarHorario, self._usuario))


    def actualizar(self):
        with open('ArchivosCSV/usuarios.csv', 'r', encoding="ISO 8859-1") as r:
            lector = csv.DictReader(r, delimiter=",")
            usuarios = list(lector)

        if self.cont < len(usuarios):
            self._usuario = usuarios[self.cont]
            self.ventanaUi.labelNombreC.setText(
                str(self._usuario['nombres']) + " " + str(self._usuario['apellido_paterno']) + " " + str(self._usuario['apellido_materno']))
            self.ventanaUi.labelRut.setText(str(self._usuario['rut']))
            self.ventanaUi.labelGenero.setText(str(self._usuario['genero']))
            self.ventanaUi.labelFecha.setText(str(self._usuario['fecha_nacimiento']))
            self.ventanaUi.labelCorreo.setText(str(self._usuario['email']))
            self.ventanaUi.labelTelefono.setText(str(self._usuario['telefono']))
            self.ventanaUi.labelDireccion.setText(str(self._usuario['domicilio']))
            self.ventanaUi.labelCargo.setText(str(self._usuario['cargo']))
            self.ventanaUi.labelExperiencia.setText(str(self._usuario['experiencia']))

    def volver(self):
        ventanaListaUsuario.ventanaLista().show()
        self.close()

    def menuP(self):
        self.close()

    def cambiarVent(self,nombre_Vent,usuario):
        self.nombre_Vent = QtWidgets.QMainWindow()
        self.ui = nombre_Vent(usuario)
        self.ui.setupUi(self.nombre_Vent)
        self.nombre_Vent.show()