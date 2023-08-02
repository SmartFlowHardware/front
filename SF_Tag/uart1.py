import serial
import Check_bt

# port = '/dev/ttymxc1'  # Reemplaza con el puerto serial correspondiente en tu sistema
# baudrate = 230400
port = 'COM25'  # Reemplaza con el puerto serial correspondiente en tu sistema
baudrate = 115200
# Abre la conexión serial
ser = serial.Serial(port, baudrate)
start_scan='set scanner on 0\n'
ser.write(start_scan.encode())


def receive_data():
    try:
        while True:
            # Lee los datos del puerto serial
            data = ser.readline().decode('latin-1').strip()

            # Muestra los datos en el terminal
            if len(data)!=0:
                # print(data)
                Check_bt.db_mac(data)

    except KeyboardInterrupt:
        pass
