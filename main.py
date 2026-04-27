from config import config
from ocrreader import ocr_runner

if __name__ == "__main__":
    file_path = input("Enter the path to the image or PDF file: ")
    result = ocr_runner(file_path)
    if result:
        print("OCR Result:")
        print(result)
    else:
        print("Failed to process the file.")
