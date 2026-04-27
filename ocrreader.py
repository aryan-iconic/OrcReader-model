from chandra.model import InferenceManager
from chandra.model.schema import BatchInputItem
from PIL import Image
from PyPDF2 import PdfReader

manager = InferenceManager(method="vllm")
from pdf2image import convert_from_path

def is_valid_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except:
        return False

def is_valid_pdf(file_path):
    try:
        PdfReader(file_path)
        return True
    except:
        return False

def convert_pdf_to_images(file_path):
    try:
        images = convert_from_path(file_path)
        return images
    except:
        return None

def get_file_type(file_path):
    ext = file_path.lower().split('.')[-1]
    try:
        if ext in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
            return "image"
        if ext == 'pdf':
            return "pdf"
    except:
        return None

def ocr_runner(file_path):
    file_type = get_file_type(file_path)
    if file_type is None:
        print("Unsupported file type")
        return 
    try:
        if file_type == "image":
            with Image.open(file_path) as img:
                batch = [
                    BatchInputItem(
                        image=img,
                        prompt_type="ocr_layout"
                    )
                ]
                result = manager.generate(batch)[0] 
                print(result.markdown)
            return result.markdown    
        if file_type == "pdf":
            images = convert_pdf_to_images(file_path)
            if not images:
                return None
            results = []
            for img in images:
                batch = [
                    BatchInputItem(
                        image=img,
                        prompt_type="ocr_layout"
                    )
                ]
                result = manager.generate(batch)[0] 
                results.append(result.markdown)
            return results
    except Exception as e:
        print(f"Error processing file: {e}")
        return None
