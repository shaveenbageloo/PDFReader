import PyPDF2
import pandas as pd

# Function to extract text from each page of the PDF
def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to process the extracted text and convert it into a list of rows
def process_text_to_rows(text):
    rows = []
    lines = text.split('\n')
    for line in lines:
        if line.strip():  # Ignore empty lines
            rows.append(line.split())  # Assuming data is space-separated; adjust if necessary
    return rows

# Function to convert the rows into a DataFrame and save as CSV
def save_rows_to_csv(rows, csv_path):
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False, header=False)

# Main function to handle the extraction and saving process
def extract_pdf_to_csv(pdf_path, csv_path):
    text = extract_text_from_pdf(pdf_path)
    rows = process_text_to_rows(text)
    save_rows_to_csv(rows, csv_path)

# Example usage
pdf_path='/Users/shaveenbageloo/Downloads/Certificate of Attendance JaWs.pdf'
csv_path = 'output.csv'
extract_pdf_to_csv(pdf_path, csv_path)





