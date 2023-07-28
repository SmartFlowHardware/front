db_list=list()
mac_lamp={}
mac_vehc={}

d_mac='Address: '
d_mac_f='  ,'
d_rssi='RSSI:'
d_name='Name:'
lamp='L4SEC'
vhec='LAIRD'

def db_mac(data:str):

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
        
        name_bt=data[data.find(d_name):]
        name_bt=name_bt.replace(' ','')    
        name_bt=name_bt.strip(d_name)

        # print(lamp.encode('utf-8').hex())
        # print(name_bt)

        if lamp in name_bt:
            if _redata not in mac_lamp:
                # db_list.append(str(_redata))
                mac_lamp[str(_redata)]={'Flag':'1','RSSI':''}
                # print('existe')
            else:
                mac_lamp[str(_redata)]['RSSI']=_re_rssi
        else:
            if _redata not in mac_vehc:
                # db_list.append(str(_redata))
                mac_vehc[str(_redata)]={'Flag':'1','RSSI':''}
                # print('existe')
            else:
                mac_vehc[str(_redata)]['RSSI']=_re_rssi
                    
    return 'Success'






