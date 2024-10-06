from decode.do201 import DO201
from database.DAO.sensor_DAO import upload_status_sensor

'''
Aqui é possivel tesstar o decode que importa o utility e model
tambem o database e sensor_dao
'''

uploader = upload_status_sensor()

response = DO201.parse_data_DO201('80003102260b6a00000168fd71fd85fb341a290000000066d62c2d0001186973806917602781') 

if response:
    data_type, interpretedData, equipmentIMEI = response
    print(interpretedData)
    resultado = uploader.upload_0x01_0x02(interpretedData)
    print(resultado)

print('resultado')
