import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI="mongodb+srv://azharyazied2:14juni2002@cluster0.4uh4rdq.mongodb.net/?retryWrites=true&w=majority"
DB_NAME="dbyzd"


client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)