# Image Text Extractor with Tesseract OCR

This Python project extracts text from images using **Tesseract OCR** and automatically saves the text into separate files.

---

🛠️ Installation

1️⃣ **Install Python & Virtual Environment (Optional)**
Make sure Python 3 is installed:

sudo apt update
sudo apt install python3 python3-venv python3-pip
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate

2️⃣ **Install Dependencies**

pip install pytesseract pillow

3️⃣ **Install Tesseract OCR**

sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-ita  # Install Italian language support

🚀 **Usage**
Place your images inside the images/ folder.
Run the script:

python main.py

Extracted text will be saved in output/ as separate .txt files.

⚙️ **How It Works**
✔ Reads all images inside images/.
✔ Uses Italian OCR (-l ita) for text extraction.
✔ If an image filename contains "column", it applies --psm 3 for better column detection.
✔ Saves extracted text into separate .txt files inside Text-extracted/.

📝 **Example**
Input (images/)

images/
│── invoice.jpg

│── document.png

│── column-report.jpeg

│── notes-column.png

Text-extracted (Text-extracted/)

Text-extracted/
│── invoice.txt

│── document.txt

│── column-report.txt  # Processed with --psm 3

│── notes-column.txt   # Processed with --psm 3

🛠️ **Troubleshooting**
❌ Error: "Tesseract couldn't load any languages!"
✅ Fix: Install the Italian OCR package → sudo apt install tesseract-ocr-ita

❌ Error: "Image not found!"
✅ Fix: Ensure images are inside the images/ folder and the filenames are correct.

📜 **License**
This project is open-source and free to use.
