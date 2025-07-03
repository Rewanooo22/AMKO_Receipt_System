# 1. app.py - Main Flask Application
from flask import Flask, render_template, request, jsonify, send_file
import os
import easyocr
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import re
from datetime import datetime
import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import red, black, blue
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'amko-receipt-system-2024'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('static', exist_ok=True)
os.makedirs('templates', exist_ok=True)

reader = easyocr.Reader(['ar', 'en'])

# ... (Omitted for brevity; actual function implementations go here)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
