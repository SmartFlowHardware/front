import serial

# Configuración del puerto serial
port = '/dev/ttymxc1'  # Reemplaza con el puerto serial correspondiente en tu sistema
baudrate = 115200

# Abre la conexión serial
ser = serial.Serial(port, baudrate)

try:
    while True:
        # Lee los datos del puerto serial
        data = ser.readline().decode().strip()

        # Muestra los datos en el terminal
        if data:
            print(data)

except KeyboardInterrupt:
    pass

# Cierra la conexión serial
ser.close()
