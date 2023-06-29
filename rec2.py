import serial
from time import sleep
# Configuración del puerto serial
port = '/dev/ttymxc1'  # Reemplaza con el puerto serial correspondiente en tu sistema
baudrate = 115200

try:
    # Abre la conexión serial
    ser = serial.Serial(port, baudrate)
    print(f"Conexión establecida en {port} a {baudrate} bps")

    try:
        while True:
            sleep(1)
            # Intenta leer los datos del puerto serial
            try:
                data = ser.readline().decode().strip()
                print("yes")
                # Verifica si se recibieron datos
                if data:
                    print(data)
                    
            except UnicodeDecodeError:
                print("Error de decodificación: No se pudo decodificar los datos recibidos")

    except KeyboardInterrupt:
        pass

except serial.SerialException as e:
    print(f"Error al abrir el puerto serial: {e}")

finally:
    # Cierra la conexión serial
    if ser.is_open:
        ser.close()
        print("Conexión cerrada")
