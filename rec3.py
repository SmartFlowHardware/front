import serial

# Configura el puerto serie
puerto = '/dev/ttymxc1'  # Cambia esto por tu puerto UART
velocidad = 115200  # Cambia esto por la velocidad de baudios adecuada
ser = serial.Serial(puerto, velocidad)

# Espera y lee los datos recibidos
while True:
    if ser.in_waiting > 0:
        datos_recibidos = ser.readline().decode().strip()
        print('Datos recibidos:', datos_recibidos)