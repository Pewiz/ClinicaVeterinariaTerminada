from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
import csv
from uiReservaCitaEsp import Ui_MainWindow
from ManejoArchivo import GestionArchivo
import ventanaMenuReserva
import ventanaHorarios

class ventanaCitaEsp(QMainWindow):
    def __init__(self, cont, hora):
        super().__init__()
        self.cont = cont
        self.hora = hora
        self.flag = False
        self.nombreV = ""
        self.ventanaUi = Ui_MainWindow()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.seleccionar_bloquebtn.setEnabled(False)
        self.ventanaUi.especialidad_box.currentIndexChanged.connect(self.seleccionCambio)
        self.ventanaUi.seleccionar_bloquebtn.clicked.connect(self.cambio)
        self.ventanaUi.botonAtras.clicked.connect(lambda: self.atras(ventanaMenuReserva.ventanaMenuReserva(self.cont)))
        self.ventanaUi.agregar_hora_3.clicked.connect(self.agendar)
        self.actualizarComboBoxMascota()
    
    def actualizarComboBoxEspLabel(self, combo, nombre):
        self.flag = True
        self.ventanaUi.seleccionar_bloquebtn.setEnabled(True)
        self.ventanaUi.especialidad_box.setCurrentIndex(combo)
        self.ventanaUi.label_9.setText("Horario Escogido:\nFecha: " + self.hora[0] +"\nHorario: " + self.hora[1] + "\nSala N° " + self.hora[2])
        self.nombreV = nombre
        self.ventanaUi.labelEncargado.setText(self.nombreV)
        if self.ventanaUi.especialidad_box.currentIndex() == 1:
            self.seleccion = 2
        if self.ventanaUi.especialidad_box.currentIndex() == 2:
            self.seleccion = 3
        if self.ventanaUi.especialidad_box.currentIndex() == 3:
            self.seleccion = 4
        if self.ventanaUi.especialidad_box.currentIndex() == 4:
            self.seleccion = 5
        if self.ventanaUi.especialidad_box.currentIndex() == 5:
            self.seleccion = 6
        self.horario = ventanaHorarios.ventanaHorarios(self.seleccion, self.cont)
        self.flag = False
    
    def atras(self, ventana):
        ventana.show()
        self.close()
    
    def cambio(self):
        self.horario.show()
        self.horario.especSelecc = self.ventanaUi.especialidad_box.currentIndex()
        self.close()
    
    def actualizarComboBoxMascota(self):
        with open("clientes.csv") as r:
            reader = csv.reader(r)
            next(reader)
            i = 1
            for l in reader:
                if i == self.cont:
                    self.rutCliente = l[0]
                    self.nombreC = l[1]
                    break
                i += 1

        with open('mascotas.csv') as file:
            reader = csv.reader(file)
            next(reader)
            self.mascota = []
            for l in reader:
                if l[0] == self.rutCliente:
                    self.mascota.append(l)

        for mascota in self.mascota:
            self.ventanaUi.mascota_box.addItem(mascota[1])
    
    def seleccionCambio(self):
        if self.flag == False:
            if self.ventanaUi.especialidad_box.currentIndex() == 0:
                self.ventanaUi.seleccionar_bloquebtn.setEnabled(False)
            else:
                self.ventanaUi.seleccionar_bloquebtn.setEnabled(True)
                if self.ventanaUi.especialidad_box.currentIndex() == 1:
                    self.seleccion = 2
                if self.ventanaUi.especialidad_box.currentIndex() == 2:
                    self.seleccion = 3
                if self.ventanaUi.especialidad_box.currentIndex() == 3:
                    self.seleccion = 4
                if self.ventanaUi.especialidad_box.currentIndex() == 4:
                    self.seleccion = 5
                if self.ventanaUi.especialidad_box.currentIndex() == 5:
                    self.seleccion = 6
                self.horario = ventanaHorarios.ventanaHorarios(self.seleccion, self.cont)
            self.ventanaUi.label_9.setText("Tu Horario seleccionado se mostrará aqui")
            self.ventanaUi.labelEncargado.setText("Encargado aparece aqui...")
            self.nombreV = ""
            self.hora = []

    def agendar(self):
        if(self.ventanaUi.mascota_box.currentIndex() == 0 or self.hora == [] or self.nombreV == "" or self.ventanaUi.especialidad_box.currentIndex() == 0):
            qtw.QMessageBox.warning(self, "ERROR, Datos incompletos", "Por favor revise si ha escogido una mascota, si ha escodigo especialidad, o si ha escogido un horario.")
        else:
            i = 1
            for l in self.mascota:
                if i == self.ventanaUi.mascota_box.currentIndex():
                    nombreMascota = l[1]
                    break
                i += 1
            with open('salas.csv') as file:
                reader = csv.reader(file)
                next(reader)
                i = 0
                for l in reader:
                    if l[4] == self.hora[0] and l[3] == self.hora[1] and l[2] == self.hora[2]:
                        posFila = i
                        break
                    i += 1
            fl = False
            with open('Control.csv') as file:
                reader = csv.reader(file)
                next(reader)
                for l in reader:
                    if l[0] == self.hora[0] and l[1] == nombreMascota and l[2] == self.hora[1]:
                        fl = True
                        break
            with open('Quirofano.csv') as file:
                reader = csv.reader(file)
                next(reader)
                for l in reader:
                    if l[0] == self.hora[0] and l[1] == nombreMascota and l[2] == self.hora[1]:
                        fl = True
                        break
            with open('Citas.csv') as file:
                reader = csv.reader(file)
                next(reader)
                for l in reader:
                    if l[0] == self.hora[0] and l[1] == nombreMascota and l[4] == self.hora[1]:
                        fl = True
                        break
            if fl == True:
                qtw.QMessageBox.warning(self, "ERROR, Fecha y hora hacen conflicto", "La hora y fecha de esta reserva hacen conflicto con otra reserva realizada para la misma mascota.\nPara solucionar esto, porfavor seleccione otro bloque horario, cambie de mascota o modifique la reserva realizada anteriormente.")
            else:
                GestionArchivo.modificarLinea("salas.csv",posFila,1,self.rutCliente)
                GestionArchivo.modificarLinea("salas.csv",posFila,5,"True")
                if self.ventanaUi.especialidad_box.currentIndex() == 1:
                    especialidad = "Neurologia"
                    espEmer = "Neurologo/a"
                elif self.ventanaUi.especialidad_box.currentIndex() == 2:
                    especialidad = "Reproduccion"
                    espEmer = "Experto/a en Reproduccion"
                elif self.ventanaUi.especialidad_box.currentIndex() == 3:
                    especialidad = "Odontologia"
                    espEmer = "Odontologo/a"
                elif self.ventanaUi.especialidad_box.currentIndex() == 4:
                    especialidad = "Oncologia"
                    espEmer = "Oncologo/a"
                elif self.ventanaUi.especialidad_box.currentIndex() == 5:
                    especialidad = "Cardiologia"
                    espEmer = "Cardiologo/a"
                reserva = [self.hora[0], nombreMascota, self.nombreV, especialidad, self.hora[1], self.hora[2]]
                with open("Citas.csv","a",newline="") as archivo:
                    escritor = csv.writer(archivo,delimiter=",") 
                    escritor.writerow(reserva)
                msg = qtw.QMessageBox()
                msg.setWindowTitle("Reserva Cita con " + espEmer + " realizada con exito.")
                msg.setText("Felicidades señor " + self.nombreC + " su reserva ha sido realizada con exito.\nSi necesita saber mas detalles, dirigase hacia Lista de Reservas para cancelar, modificar o mostrar su reserva.")
                msg.exec_()
                self.atras(ventanaMenuReserva.ventanaMenuReserva(self.cont))
    
    
