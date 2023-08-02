mac_info = {
    'MAC':{
        'RSSI':'-91',
        'Flag':'1'}
    }


# # syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct['key5'] = 'value5'

# # mac_info['mac2']={'RSSI':'-91','Flaf':'1'}
# print(mac_info)

# mac_info={}

def db_mac(data:str):

    if  data.rfind('BD Address:') and len(data)!=0:
        _filter1=data.rfind('BD Address:')
        _filter2=data.find(',')
        
        _redata=data[_filter1:_filter2]
        _redata=_redata.strip('BD Address:')
        _redata=_redata.replace(' ',':')


        if _redata not in mac_info:
            # db_list.append(str(_redata))
            mac_info[str(_redata)]={'Flag':'1'}
            # print('existe')

    return mac_info

key=mac_info.keys()

for kei in key:
    print(kei)
# print(mac_info.update(['']))
