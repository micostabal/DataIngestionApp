import requests
import os
import PyPDF2

class ScraperUtils:
    
    @staticmethod
    def download_file(download_url, filename):
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        
        while True:
            try:
                response = requests.get(download_url, headers=headers, timeout = 30)
                break
            except:
                print('Intento Fallido')
                continue
        
        with open(filename, 'wb') as f:
            f.write(response.content)

    @staticmethod
    def get_text_from_pdf(pdf_path):
        pdfFileObject = open(pdf_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        count = pdfReader.numPages
        
        pages = []
        for i in range(count):
            page = pdfReader.getPage(i)
            pages.append(page.extractText())
        return '\n'.join(pages)

    @staticmethod
    def remove_file(filename):
        os.remove(filename)

    @staticmethod
    def preprocess_string(value):
        return r'{}'.format(value
            .replace('\n', '\\n')
            .replace('%', '')
            .replace("'", "\\'")
        )