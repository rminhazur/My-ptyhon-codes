import PyPDF2
import pyttsx3

book=open("writting.pdf", "rb")
pdfReader= PyPDF2.PdfFileReader(book)
pages =pdfReader.numPages
print(pages)
speaker= pyttsx3.init()
page =pdfReader.getPage(0)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()