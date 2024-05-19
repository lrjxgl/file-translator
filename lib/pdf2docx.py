from pdf2docx import Converter
def pdf_docx(pdf_file,doc_file):
    cv = Converter(pdf_file)
    cv.convert(doc_file)
    cv.close()