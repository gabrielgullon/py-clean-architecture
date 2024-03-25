# %%
import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import firestore

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_env = load_dotenv(dotenv_path)

cred_obj = firebase_admin.credentials.Certificate(
    "D:\\ggull\\Documentos\\fundamentus\\backend\\fundamentus-firebase.json"
)

firebase_app = ""

try:
    firebase_app = firebase_admin.initialize_app()
except:
    firebase_admin.get_app()

firestore = firestore.client()

# %%
