from pdf2image import convert_from_bytes

def pdf_to_images(pdf_file) -> list:
    return convert_from_bytes(pdf_file.read())
