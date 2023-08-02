import pyaudio
import socket

# Configuración del cliente
host = '192.168.1.74'  # Cambia esto a la dirección IP del servidor si estás ejecutando el cliente en una máquina diferente
port = 12345

# Configuración de PyAudio
chunk_size = 1024
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100

# Inicializar PyAudio
audio = pyaudio.PyAudio()

# Configurar el socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print('Conectado al servidor {}:{}'.format(host, port))

# Abrir el flujo de audio
stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, output=True, frames_per_buffer=chunk_size)

try:
    while True:
        # Recibir datos de audio del servidor
        audio_data = client_socket.recv(chunk_size)

        # Reproducir el audio recibido
        stream.write(audio_data)
finally:
    # Detener la reproducción y cerrar el socket
    stream.stop_stream()
    stream.close()
    audio.terminate()
    client_socket.close()
