from services.decode.do201 import DO201
#from database.DAO.sensor_DAO import upload_status_sensor

'''
Aqui é possivel tesstar o decode que importa o utility e model
tambem o database e sensor_dao
'''

#uploader = upload_status_sensor()

# response = DO201.parse_data_DO201('8000310327010218053C003C143132302E39322E38392E3132323B23823B186973806917580581')

response = DO201.parse_data_do201(
    '8000310226270f00000169fdbdfd92fb96172d000000006705f4a8000a186973806917602781')


# if response:
#     data_type, interpretedData, equipmentIMEI = response
#     print(interpretedData)
#     resultado = uploader.upload_0x01_0x02(interpretedData)
#     print(resultado)

print(response)
