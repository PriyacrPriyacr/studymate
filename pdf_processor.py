import pdfplumber
import os

# Function to extract text from a PDF file using pdfplumber
def extract_text_from_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        raise RuntimeError(f"Error reading PDF: {e}")

# Function to split text into smaller chunks
def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = [
        ' '.join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]
    return chunks

if __name__ == "__main__":
    test_pdf_path = "my_notes.pdf"  # Replace with your actual PDF path

    try:
        text = extract_text_from_pdf(test_pdf_path)
        chunks = chunk_text(text)
        print(f"✅ Total Chunks: {len(chunks)}")
        print("\n📄 First chunk preview:\n")
        print(chunks[0])
    except Exception as err:
        print(f"❌ Error: {err}")
