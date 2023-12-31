import serial

# Configuración del puerto serial
port = '/dev/ttymxc1'  # Reemplaza con el puerto serial correspondiente en tu sistema
baudrate = 115200
#port = 'COM15'  # Reemplaza con el puerto serial correspondiente en tu sistema
#baudrate = 115200
# Abre la conexión serial
ser = serial.Serial(port, baudrate)
start_scan='set scanner on 0\n'
ser.write(start_scan.encode())

# Función para leer la entrada del usuario y enviarla al puerto serial
def send_input():
    try:
        while True:
            # Lee la entrada del usuario
            user_input = input('> ')
            user_input=user_input+'\n'

            # Verifica si el usuario desea salir del terminal
            if user_input.lower() == 'exit\n':
                break

            # Envía los datos al puerto serial
            ser.write(user_input.encode())

    except KeyboardInterrupt:
        
        pass
        

    # Cierra la conexión serial
    ser.close()

# Función para recibir datos del puerto serial y mostrarlos en el terminal
def receive_data():
    try:
        while True:
            # Lee los datos del puerto serial
            data = ser.readline().decode('latin-1').strip()

            # Muestra los datos en el terminal
            if data:
                print(data)

    except KeyboardInterrupt:
        pass

# Ejecuta las funciones en hilos separados para permitir interacción simultánea
try:
    import threading

    send_thread = threading.Thread(target=send_input)
    receive_thread = threading.Thread(target=receive_data)

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

except ImportError:
    # Si threading no está disponible, se ejecutan las funciones en secuencia
    send_input()
    receive_data()
