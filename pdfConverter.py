from pdf2docx import Converter
pdf_file = 'nghir.pdf'
docx_file= 'nghirou.docx'

fichier = Converter(pdf_file)
fichier.convert(docx_file)
fichier.close()