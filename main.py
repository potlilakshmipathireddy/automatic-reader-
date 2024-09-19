import pyttsx3
import PyPDF2

book = open('python.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(book)
num_pages = len(pdf_reader.pages)
play = pyttsx3.init()

print("Playing the audio book")

for num in range(num_pages):
    page = pdf_reader.pages[num]
    data = page.extract_text()
    play.say(data)
    play.runAndWait()

book.close()