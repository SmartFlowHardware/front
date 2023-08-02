db_list=list()
mac_lamp={}
mac_vehc={}

#  Name: L4SEC BSL1	Address: [9c 50 d1 1b 04 b8 ]  , RSSI: -67 


d_mac='Address: '
d_mac_f='  ,'
d_rssi='RSSI:'
d_name='Name:'
lamp='L4SEC'
vehc='LAIRD'

def db_mac(data:str):
    try:
        if  data.rfind(d_mac) and len(data)!=0:

            _filter_1=data.rfind(d_mac)
            _filter_2=data.find(d_mac_f)
            
            _redata=data[_filter_1:_filter_2]
            _redata=_redata.strip(d_mac)
            _redata=_redata.replace(' ','')
            _redata=_redata.replace('[','')
            _redata=_redata.replace(']','')

            _filter_3=data.find(d_rssi)
            _re_rssi=data[_filter_3:]
            _re_rssi=_re_rssi.strip(d_rssi)
            _re_rssi=_re_rssi.replace(' ','')
            
            name_bt=data[data.find(d_name):]
            name_bt=name_bt.replace(' ','')    
            name_bt=name_bt.strip(d_name)

            # print(lamp.encode('utf-8').hex())
            # print(name_bt)

            if lamp in name_bt:
                if _redata not in mac_lamp:
                    # db_list.append(str(_redata))
                    mac_lamp[str(_redata)]={'Flag':'1','RSSI':'-100'}
                    # print('existe')
                else:
                    mac_lamp[str(_redata)]['RSSI']=_re_rssi
                    mac_lamp[str(_redata)]['Flag']='1'

            elif vehc in name_bt :
                if _redata not in mac_vehc:
                    # db_list.append(str(_redata))
                    mac_vehc[str(_redata)]={'Flag':'1','RSSI':'-100'}
                    # print('existe')
                else:
                    mac_vehc[str(_redata)]['RSSI']=_re_rssi
                    mac_vehc[str(_redata)]['Flag']='1'
    except:
        print('Something ')



    return 'Success'


def db_view(data:dict):
    for key in data:
        # print(data[key])
        # print(key)
        data[key]['Flag']='0'
        
    return data


def check_delete(data:dict):
     for key in data:
        # print(key)
        if data[key]['Flag'] == '0':
            # print('borrar')
            data.pop(str(key))
            break
