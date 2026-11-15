# AMKO Receipt OCR

A Flask scaffold for a planned receipt system for AMKO. The imports and the Arabic landing page suggest the intended workflow: a user uploads an image of a card, text is extracted with OCR (EasyOCR, Arabic and English), and a receipt is generated as a PDF (ReportLab).

## Project status

**Early scaffold, not functional.** `app.py` contains the placeholder comment `# ... (Omitted for brevity; actual function implementations go here)`. No OCR, image processing, database or PDF logic is implemented.

## Current contents

| File | Description |
|---|---|
| `app.py` | Flask app with a single route (`/`) that renders `templates/index.html`. It configures an `uploads/` folder and a 16 MB upload limit, and initialises an EasyOCR reader for `ar` and `en`. Most imports (OpenCV, NumPy, Pillow, ReportLab, SQLite and others) are unused. |
| `templates/index.html` | Minimal right-to-left Arabic page with a heading and a line that asks the user to upload a card image. It has no form or upload control. |
| `requirements.txt` | Pinned dependencies: Flask, Werkzeug, opencv-python, easyocr, Pillow, reportlab, numpy |
| `static/logo.png` | Empty placeholder file (0 bytes) |

## Running the scaffold

```bash
git clone https://github.com/Rewanooo22/amko-receipt-ocr.git
cd amko-receipt-ocr
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

The app runs in debug mode on `0.0.0.0:5000`, so the page is at http://localhost:5000. At startup it creates the `uploads/`, `static/` and `templates/` folders if they are missing. EasyOCR downloads its Arabic and English model files the first time it starts.

## Notes

- `app.secret_key` is hard-coded in `app.py`. Move it to an environment variable before any real use.
- Debug mode combined with binding to `0.0.0.0` makes the debugger reachable from the network. Use these settings only for local development.

## Planned work

- Add an upload form and an upload route that use `secure_filename`.
- Preprocess images with OpenCV and extract Arabic and English text with EasyOCR.
- Parse the extracted fields and store receipts (SQLite is imported).
- Generate PDF receipts with ReportLab and return them with `send_file`.
