import firebase_admin
from firebase_admin import credentials, firestore

address = r"D:\OneDrive\Projeto - Sensor indutivo\NB-IoT_Gateway\NB-IoT_Gateway\services\firebase\service_account_key.json"

cred = credentials.Certificate(address)
firebase_admin.initialize_app(cred)

db = firestore.client()


def update_park(alarm_park):
    # Reference -> Collection | Document ID
    doc_ref = db.collection("status_park").document("Inatel")

    doc_ref.update({
        "001": alarm_park
    })


# To test the code
if __name__ == "__main__":
    alarm_park = False
    update_park(alarm_park)
