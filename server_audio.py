import pyaudio
import socket

# Configuración del servidor
host = '192.168.1.74'  # Cambia esto a la dirección IP del servidor si estás ejecutando el cliente en una máquina diferente
port = 12345

# Configuración de PyAudio
chunk_size = 1024
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100

# Inicializar PyAudio
audio = pyaudio.PyAudio()

# Configurar el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print('Servidor escuchando en {}:{}'.format(host, port))

# Aceptar una conexión del cliente
client_socket, client_address = server_socket.accept()
print('Cliente conectado:', client_address)

# Abrir el flujo de audio
stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

try:
    while True:
        # Leer audio desde el micrófono
        audio_data = stream.read(chunk_size)

        # Enviar los datos al cliente
        client_socket.sendall(audio_data)
finally:
    # Detener la transmisión y cerrar los sockets
    stream.stop_stream()
    stream.close()
    audio.terminate()
    client_socket.close()
    server_socket.close()
