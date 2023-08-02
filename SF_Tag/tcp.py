import socket
import sys
import time
from Check_bt import mac_lamp,mac_vehc
def connect():
    # ip=socket.gethostbyname(socket.gethostname())
    # while '127.0.0.1' in ip:
    #     ip=socket.gethostbyname(socket.gethostname())
    time.sleep(30)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('10.90.120.10', 8010)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        while True:
            # Send data
            message = b'\nThis is the message.  It will be repeated.\r\n'
            buffer='\n'+str(mac_lamp)+'\r\n'
            print('sending {!r}'.format( str(buffer).encode('utf-8')))
            sock.sendall(str(buffer).encode('utf-8'))

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(50)
                amount_received += len(data)
                # print('received {!r}'.format(data))
    except ConnectionRefusedError:
        sock.connect(server_address)
    finally:
        print('closing socket')
        sock.close()
        

# ip=socket.gethostbyname(socket.gethostname())
# print(ip)        
