from PyPDF2 import PdfReader    
from pdf2image import convert_from_path
import requests

#token
bot_token = '8062639023:AAHHtOneX9PqwXY8ACaHst2lhWyEOC52hsw'
#function which extract first page of the pdf file
def extract_first_page_as_image(pdf_path):
    pdf = PdfReader(open(pdf_path, 'rb'))
    first_page = pdf.pages[0]

    image_path = 'first_page.jpg'
    images = convert_from_path(pdf_path, first_page=1, last_page=1)
    images[0].save(image_path, 'JPEG')
    return image_path
# function to send image and pdf file to my channel
def send_image_and_pdf(chat_id, image_path, pdf_path):
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    image_files = {'photo': open(image_path, 'rb')}
    image_data = {'chat_id': chat_id}

    pdf_url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    pdf_files = {'document': open(pdf_path, 'rb')}
    pdf_data = {'chat_id': chat_id}

    response_image = requests.post(url, files=image_files, data=image_data)
    print(response_image.json())

    response_pdf = requests.post(pdf_url, files=pdf_files, data=pdf_data)
    print(response_pdf.json())


# id of my channel and path where I want send my pdf file
chat_id = '-1002297050802'
pdf_path = './files/r4.pdf' 

# get object image_path 
image_path = extract_first_page_as_image(pdf_path)

# sending image and pdf file
send_image_and_pdf(chat_id, image_path, pdf_path)
