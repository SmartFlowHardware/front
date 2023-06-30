import sys
import random
from PyQt5.QtCore import * #QTimer
from PyQt5.QtGui import * #QFont
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setWindowTitle("Prevencion de Colicion")
        self.setFixedSize(700, 500)

        self.fondo = QLabel(self)
        self.fondo.setStyleSheet("background:#081F36")
        self.fondo.setGeometry(0, 0, 700, 500)

        self.fon2 = QLabel (self)
        self.fon2.setStyleSheet("background:#15407F")
        self.fon2.setGeometry(0, 0, 700, 60)

        self.imagen_persona = QLabel(self)
        self.imagen_persona.setGeometry(130, 100,  300, 300)
        self.imagen_persona.setPixmap(QPixmap("Persona_1.png").scaled(130, 130))

        self.imagen_camion = QLabel(self)
        self.imagen_camion.setGeometry(430, 200, 200, 100)
        self.imagen_camion.setPixmap(QPixmap("Camion1.png").scaled(200, 200))

        self.label1 = QLabel(self)
        self.label1.setGeometry(255, 200, 75, 100)
        self.label1.setStyleSheet("color:#4EB8CE")
        self.label1.setFont(QFont('Arial', 90))

        self.label2 = QLabel(self)
        self.label2.setGeometry(380, 200, 75, 100)
        self.label2.setStyleSheet("color:#4EB8CE")
        self.label2.setFont(QFont('Arial', 90))

        self.labela = QLabel("ABORDAMIENTO", self)
        self.labela.setGeometry(10, 10, 150, 40)
        self.labela.setStyleSheet("color:#000000")
        self.labela.setFont(QFont('Arial Font', 14))
        self.labela.mousePressEvent = self.funcion_1

        self.imagen_volumen = QLabel(self)
        self.imagen_volumen.setGeometry(600, 10, 100, 50)
        self.imagen_volumen.setPixmap(QPixmap("B_A.png").scaled(80, 50))
        self.imagen_volumen.mousePressEvent = self.funcion_2

        self.indice_imagen = 0
        self.imagenes = [
            "B_A.png",
            "son_des.png"
        ]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_numeros)
        self.timer.start(1000)  # Actualizar cada segundo

        self.dialog_shown = False  # Variable para controlar si el diálogo ya ha sido mostrado
    def evento_presionar(self, event):
        if not self.dialog_shown:
            dialog = QMessageBox()
            dialog.setWindowTitle("Diálogo")
            dialog.setText("Sonido desactivado")
            dialog.setStyleSheet("background:#15407F")
            dialog.setFont(QFont('Arial Font', 14))
            dialog.exec_()
            self.dialog_shown = True
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Diálogo")
            dialog.setText("Sonido Activado")
            dialog.setStyleSheet("background:#15407F")
            dialog.setFont(QFont('Arial Font', 14))
            dialog.exec_()
            self.dialog_shown = False

    def actualizar_numeros(self):
        numero1 = random.randint(0, 9)
        numero2 = random.randint(0, 9)

        self.label1.setText(str(numero1))
        self.label2.setText(str(numero2))

    def modo_abordamiento(self, event):
        print("Lampara Abordada")

    def show_window1(self, event):
        self.window1 = Window1()
        self.window1.show()

    def show_window2(self, event):
        self.window2 = Window2()
        self.window2.show()

    def funcion_1(self, event):
        self.show_window1(self)
        self.modo_abordamiento(self)

    def funcion_2 (self, event):
        self.alternar_imagenes(self)
        self.evento_presionar(self)

    def alternar_imagenes(self, event):
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes)
        imagen_actual = self.imagenes[self.indice_imagen]

        pixmap = QPixmap(imagen_actual).scaled(80, 50)
        self.imagen_volumen.setPixmap(pixmap)



class Window1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ventana 1")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(300, 200)
        self.setStyleSheet("background:#15407F")

        layout = QVBoxLayout()
        label = QLabel("MODO ABORDAMIENTO")
        label.setStyleSheet("color:#FF50FF")
        label.setFont(QFont("Arial", 15))
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignCenter)
        button = QPushButton("Cerrar")
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)  # Configurar para que se dispare solo una vez
        self.timer.timeout.connect(self.close)
        self.timer.start(10000)  # 10000 milisegundos = 10 segundos

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())