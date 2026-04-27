# OCR Project

A simple OCR (Optical Character Recognition) tool that processes images and PDF files using the Chandra OCR engine.

## Features

- **Image OCR**: Supports JPG, JPEG, PNG, BMP, GIF formats
- **PDF OCR**: Converts PDF pages to images and extracts text
- **Layout-aware OCR**: Uses `ocr_layout` prompt type for better results

## Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for dependencies

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the program:
```bash
python main.py
```

2. Enter the path to your image or PDF file when prompted.

Example:
```
Enter the path to the image or PDF file: D:\images\document.pdf
```

## Project Structure

```
OCR_Project/
├── main.py          # Entry point
├── config.py        # Configuration settings
├── ocrreader.py    # OCR processing logic
├── input/          # Input files folder
└── model/          # Model files folder (if needed)
```

## Output

The OCR results are printed as markdown-formatted text.