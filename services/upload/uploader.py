from database.DAO import updatedDAO
from log import log

def upload(data, data_type):
    response = None
    if data_type == 1:
        response = updatedDAO.upload_0x01_0x02(data)
        
    elif data_type == 3:
        response = updatedDAO.upload_0x03(data)
    
    if response:
        print(f'Documento inserido com ID: {response}')

    else:
        print(f"Data not sent to the database. 'response' not defined!")
        log.logger.error(f"Data not sent to the database. 'response' not defined!")
    
    return None