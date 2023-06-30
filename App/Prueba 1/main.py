import sys
import random
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import * #QFont
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("Prevencion de Colicion")
        self.setFixedSize(700, 500)
        self.setWindowFlag (Qt.FramelessWindowHint)

        self.fon1 = QLabel(self)
        self.fon1.setStyleSheet("background:#081F36")
        self.fon1.setGeometry(0, 0, 700, 500)

        self.fon2 = QLabel(self)
        self.fon2.setStyleSheet("background:#15407F")
        self.fon2.setGeometry(0, 0, 700, 60)

        self.label3 = QLabel(self)
        self.label3.setGeometry(170, 200, 130, 100)
        self.label3.setStyleSheet("color:#4EB8CE")
        self.label3.setFont(QFont('Arial', 90))
        self.label3.setAlignment(Qt.AlignCenter)

        self.imagen_persona = QLabel(self)
        self.imagen_persona.setGeometry(55, 100, 300, 300)
        self.imagen_persona.setPixmap(QPixmap("Persona_1.png").scaled(130, 130))

        self.label4 = QLabel(self)
        self.label4.setGeometry(340, 200, 130, 100)
        self.label4.setStyleSheet("color:#4EB8CE")
        self.label4.setFont(QFont('Arial', 90))
        self.label4.setAlignment(Qt.AlignCenter)

        self.imagen_camion = QLabel(self)
        self.imagen_camion.setGeometry(460, 200, 200, 100)
        self.imagen_camion.setPixmap(QPixmap("Camion1.png").scaled(200, 200))

        self.labelA = QLabel(self)
        self.labelA.setGeometry(25, 10, 150, 40)
        self.labelA.setText("ABORDAMIENTO")
        self.labelA.setStyleSheet("color:#000000")
        self.labelA.setFont(QFont("Times", 14))

        self.labelA.mousePressEvent = self.toggle_blink

        self.labelp = QLabel("ABORDAMIENTO",self)
        self.labelp.setGeometry(0, 0, 700, 500)
        self.labelp.setStyleSheet("border: 20px solid; border-color:#0018FF ;color:#0018FF")
        self.labelp.setVisible(False)
        self.labelp.setFont(QFont('Arial Font', 50))
        self.labelp.setAlignment(Qt.AlignCenter)

        self.label_zr = QLabel(self)
        self.label_zr.setGeometry(290, 300, 150, 100)
        self.label_zr.setPixmap(QPixmap("Advertencia.png").scaled(120, 100))
        #self.label_zr.setScaledContents(True)
        self.label_zr.setVisible(False)

        self.label_bzr_yellow = QLabel(self)
        self.label_bzr_yellow.setGeometry(0, 0, 700, 500)
        self.label_bzr_yellow.setStyleSheet("border: 20px solid; border-color:#FFB200")
        self.label_bzr_yellow.setVisible(False)
        self.label_bzr_yellow.setAlignment(Qt.AlignCenter)

        self.label_bzr_red = QLabel(self)
        self.label_bzr_red.setGeometry(0, 0, 700, 500)
        self.label_bzr_red.setStyleSheet("border: 20px double; border-color:#FF0000; color:#FF0000")
        self.label_bzr_red.setVisible(False)
        self.label_bzr_red.setAlignment(Qt.AlignCenter)

        self.label_Alertamiento = QLabel(self)
        self.label_Alertamiento.setGeometry(0, 0, 700, 500)
        self.label_Alertamiento.setStyleSheet("border: 20px solid; border-color:#FF0000; color:#FF0000")
        self.label_Alertamiento.setVisible(False)
        self.label_Alertamiento.setAlignment(Qt.AlignCenter)
        self.label_Alertamiento.setText("ADVERTENCIA DE PROXIMIDAD")
        self.label_Alertamiento.setFont(QFont('Arial Font', 30))

        self.imagen_volumen = QLabel(self)
        self.imagen_volumen.setGeometry(600, 10, 100, 50)
        self.imagen_volumen.setPixmap(QPixmap("B_A.png").scaled(80, 50))
        self.imagen_volumen.mousePressEvent = self.alternar_imagenes

        self.labelW = QLabel(self)
        self.labelW.setGeometry(280, 80, 150, 100)
        self.labelW.setPixmap(QPixmap("wifi.png").scaled(100, 80))
        self.labelW.setScaledContents(True)
        self.labelW.setVisible(False)

        self.indice_imagen = 0
        self.imagenes = [
            "B_A.png",
            "son_des.png"
        ]

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.update_label3_and_label4)
        self.timer1.start(1000)  # Actualizar label3 y label4 cada segundo

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.toggle_label2_visibility)
        self.counter = 0
        self.is_blinking = False

    def alternar_imagenes(self, event):
        self.indice_imagen = (self.indice_imagen + 1) % len(self.imagenes)
        imagen_actual = self.imagenes[self.indice_imagen]

        pixmap = QPixmap(imagen_actual).scaled(80, 50)
        self.imagen_volumen.setPixmap(pixmap)

    def toggle_blink(self, event):
        self.is_blinking = not self.is_blinking

        if self.is_blinking:
            self.timer.start(500)  # Parpadeo cada 500 ms (medio segundo)
        else:
            self.timer.stop()
            self.labelp.setVisible(False)

    def toggle_label2_visibility(self):
        self.labelp.setVisible(not self.labelp.isVisible())

        self.counter += 1
        if self.counter == 20:  # Detener parpadeo después de 10 segundos (20 ciclos de 500 ms)
            self.timer.stop()
            self.labelp.setVisible(False)
            self.counter = 0

    def update_label3_and_label4(self):
        random_number1 = random.randint(0, 20)
        random_number2 = random.randint(0, 20)
        self.label3.setText(str(random_number1))
        self.label4.setText(str(random_number2))

        if random_number1 == 15:
            self.labelW.setVisible(True)
        else:
            self.labelW.setVisible(False)

        if random_number2 == 15:
            self.label_zr.setVisible(True)
            self.label_bzr_yellow.setVisible(True)
            self.label_bzr_red.setVisible(True)
        else:
            self.label_zr.setVisible(False)
            self.label_bzr_yellow.setVisible(False)
            self.label_bzr_red.setVisible(False)

        if random_number2 == 20 or random_number1 == 10:
            self.label_Alertamiento.setVisible(True)
        else:
            self.label_Alertamiento.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())