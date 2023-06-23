import sys
import random
from PyQt5.QtCore import * #QTimer
from PyQt5.QtGui import * #QFont
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prevencion de Colicion")
        self.setFixedSize(700, 500)

        self.fondo = QLabel(self)
        self.fondo.setStyleSheet("background:#081F36")
        self.fondo.setGeometry(0, 0, 700, 500)

        self.label1 = QLabel(self)
        self.label1.setGeometry(255, 200, 75, 100)
        self.label1.setStyleSheet("color:#4EB8CE")
        self.label1.setFont(QFont('Arial', 90))

        self.label2 = QLabel(self)
        self.label2.setGeometry(380, 200, 75, 100)
        self.label2.setStyleSheet("color:#4EB8CE")
        self.label2.setFont(QFont('Arial', 90))

        self.fon2 = QLabel (self)
        self.fon2.setStyleSheet("background:#15407F")
        self.fon2.setGeometry(0, 0, 700, 60)

        self.labela = QLabel("ABORDAMIENTO", self)
        self.labela.setGeometry(10, 10, 150, 40)
        self.labela.setStyleSheet("color:#000000")
        self.labela.setFont(QFont('Arial Font', 14))
        self.labela.mousePressEvent = self.modo_abordamiento


        self.imagen_persona = QLabel(self)
        self.imagen_persona.setGeometry(130, 100,  300, 300)
        self.imagen_persona.setPixmap(QPixmap("Persona_1.png").scaled(130, 130))

        self.imagen_camion = QLabel(self)
        self.imagen_camion.setGeometry(430, 200, 200, 100)
        self.imagen_camion.setPixmap(QPixmap("Camion1.png").scaled(200, 200))

        self.imagen_volumen = QLabel(self)
        self.imagen_volumen.setGeometry(600,10, 100, 50)
        self.imagen_volumen.setPixmap(QPixmap("B_A.png").scaled(80, 50))
        self.imagen_volumen.mousePressEvent = self.alternar_imagenes

        self.numeros = [0, 0]
        self.indice_imagen = 0
        self.imagenes = [
            "B_A.png",
            "son_des.png"
        ]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_numeros)
        self.timer.start(1000)  # Actualizar cada segundo

    def actualizar_numeros(self):
        numero1 = random.randint(0, 9)
        numero2 = random.randint(0, 9)

        self.label1.setText(str(numero1))
        self.label2.setText(str(numero2))

    def modo_abordamiento(self, event):
        print("Lampara Abordada")

       # abordar = QLabel("Que onda mundo", self)
        # label.setGeometry(20, 40, width, height) # la posicion de izquierda a derecha, de arriba a abajo, el largo y el alto
       # argo de el elemento es: ", label.frameGeometry().width(), "\nY el alto es: ",
       # abordar.frameGeometry().height())
       # label.setStyleSheet(
        #    "border: 19px solid; border-color:#000000; background:#050050; color:#fcfcfc")  # Estilos que pueden ser aplicados al label
        #label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # Posicion del texto respecto al label
        #self.setCentralWidget(label)  # Expandir el label al tamaño de la ventana principal

    def alternar_imagenes(self, event):
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes)
        imagen_actual = self.imagenes[self.indice_imagen]

        pixmap = QPixmap(imagen_actual).scaled(80, 50)
        self.imagen_volumen.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())