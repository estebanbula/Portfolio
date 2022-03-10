import os
from flask import Flask, request, jsonify
from firebase_admin import credendials, firestore, initialize_app

app = Flask(__name__)

cred = credendials.Certificate('C:\Users\carlos.bula\Documents\Python\Portfolio\portfolio_key.json')
default_app = initialize_app(cred)
todo_ref = db.co