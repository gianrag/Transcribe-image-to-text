import pytesseract
import os
from PIL import Image

# Ensure the images folder path is correct
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
images_folder = os.path.join(script_dir, "images")  # Folder containing images
text_folder = os.path.join(images_folder, "Text-extracted")  # Output folder for text files

# Create 'Text' folder if it doesn't exist
os.makedirs(text_folder, exist_ok=True)

# Check if Tesseract OCR is installed
tesseract_cmd = "/usr/bin/tesseract"  # Default path on Ubuntu
if not os.path.exists(tesseract_cmd):
    raise FileNotFoundError("Tesseract OCR is not installed or not found at /usr/bin/tesseract")


# Process all images in the folder
image_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")  # Supported image formats
image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(image_extensions)]

if not image_files:
    print("No images found in the folder!")
else:
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        
        # Choose OCR settings
        custom_config = "-l ita"  # Default Italian language
        if "column" in image_file.lower():  # If the filename contains "column"
            custom_config += " --psm 3"  # Apply page segmentation mode for columns

        # Load image and extract text
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, config=custom_config)

        # Generate output text file name (same name as image, but with .txt)
        text_file_name = os.path.splitext(image_file)[0] + ".txt"
        text_file_path = os.path.join(text_folder, text_file_name)

        # Save the extracted text
        with open(text_file_path, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Extracted text saved to: {text_file_path}")
