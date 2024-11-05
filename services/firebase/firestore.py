import firebase_admin
import traceback

from services.logger import log
from firebase_admin import credentials, firestore


try:
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
except Exception as e:
    detail_error = traceback.format_exc()
    log.logger.error(
        f"Error in Firebase: {e} \n DETAIL ERROR \n {
            detail_error}"
    )
