import uart1
import time
import Check_bt
import tcp
# from uart1 import init_uart

def screen():
    while True:


        # print(Check_bt.mac_vehc)
        # dict={}
        dict=Check_bt.mac_vehc|Check_bt.mac_lamp
        print(Check_bt.mac_lamp)
        print(Check_bt.mac_vehc)


        print('Lamparas: ',len(Check_bt.mac_lamp))
        print('Vehiculo: ',len(Check_bt.mac_vehc))
        Check_bt.check_delete(Check_bt.mac_lamp)
        Check_bt.check_delete(Check_bt.mac_vehc)


        Check_bt.mac_vehc=Check_bt.db_view(Check_bt.mac_vehc)
        Check_bt.mac_lamp=Check_bt.db_view(Check_bt.mac_lamp)
        time.sleep(.6)


try:
    import threading
    
    wifi_thread = threading.Thread(target=tcp.connect)
    screen_thread = threading.Thread(target=screen)
    receive_thread = threading.Thread(target=uart1.receive_data)
    
    screen_thread.start()
    receive_thread.start()
    wifi_thread.start()
    
    screen_thread.join()
    receive_thread.join()
    wifi_thread.join()

except ConnectionRefusedError:
    print('ERROR')
    pass
except ImportError:
    uart1.receive_data()
    screen()
    tcp.connect()
except:
    print('sad')
    pass