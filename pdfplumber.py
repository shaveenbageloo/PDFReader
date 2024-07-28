import pdfplumber
import pandas as pd

# Open the PDF file
with pdfplumber.open('/Users/shaveenbageloo/Downloads/Certificate of Attendance JaWs.pdf') as pdf:
    # Extract the first page
    page = pdf.pages[0]
    # Extract tables from the page
    tables = page.extract_tables()

# Convert the first table to a DataFrame
df = pd.DataFrame(tables[0], columns=["Column1", "Column2", "Column3"])

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)
