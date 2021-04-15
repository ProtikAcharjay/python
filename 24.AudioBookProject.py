import PyPDF2

a=PyPDF2.PdfFileReader('read.pdf')
# print(a.documentInfo)
pages = a.numPages
print("No of pages: ",pages)

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("sapi.spvoice")
    speak.speak(str)

for num in range(pages):
    page = a.getPage(num)
    text = page.extractText()
    # print(text)
    speak(text)
