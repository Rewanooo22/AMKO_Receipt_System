# AMKO Receipt System

A Flask web app for AMKO that reads an uploaded card image with OCR (Arabic and English) and generates a receipt. The interface is in Arabic (right-to-left).

> **Status: early scaffold.** The app starts, loads the EasyOCR reader for Arabic and English, and serves the landing page. The upload, OCR extraction, storage and PDF receipt steps are not implemented yet. `app.py` marks where they go.

## Planned flow

1. Upload a card image in the browser.
2. Pre-process it (OpenCV, Pillow) and extract text with EasyOCR (`ar`, `en`).
3. Parse the fields and save the record (SQLite).
4. Generate a PDF receipt (ReportLab) for download.

## Tech stack

Flask · EasyOCR · OpenCV · Pillow · NumPy · SQLite · ReportLab

## Run locally

Requires Python 3.9–3.11. The pinned versions (for example `numpy==1.24.3`) don't install on newer Pythons.

```bash
git clone https://github.com/Rewanooo22/amko-receipt-ocr.git
cd amko-receipt-ocr
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. On first start, EasyOCR downloads its Arabic and English models, which takes a minute.

## Project structure

```text
amko-receipt-ocr/
├── app.py              # Flask app and OCR reader setup
├── requirements.txt
├── templates/
│   └── index.html      # Arabic landing page
└── static/
    └── logo.png
```

## Before deploying

- `app.secret_key` is hard-coded in `app.py`. Read it from an environment variable instead.
- The app runs with `debug=True` on `0.0.0.0`. Turn debug off and bind to `127.0.0.1` outside local development.
