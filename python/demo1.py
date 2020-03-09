import os
import re
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage

# return list of current path(root path not included)
def getFileNames(path):
    files=os.listdir(path)
    for file in files:
        if not isPdfFile(file):
            files.remove(file)
    return files

# return list of all pdf files(root not included)
def recGetFileNames(path):
    l=[]
    for root, dirs, files in os.walk(path):
        if len(files)!=0:
            for file in files:
                l.append(file)
    return l

def isPdfFile(fileName):
    return re.match('(.*)\.pdf',fileName)!=None

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


root_path='E:\makangyao\SAP\project\VTProject\source data\Customer Experience\Customer Data Cloud\Support '\
    'Engine\Case Management'
print(root_path)
files=getFileNames(root_path)
#files=recGetFileNames(root_path)
print(files)
for file in files:
    text=convert_pdf_to_txt(os.path.expanduser(root_path+'\\'+file))
    with open(root_path+'\\pdf2txt.txt', 'a', encoding='utf-8') as f:
        f.write(file+'\n')
        f.write(text)

#text=convert_pdf_to_txt(os.path.expanduser(root_path+'\\'+files[0]))
#with open(root_path+'pdf2txt.txt', 'a', encoding='utf-8') as pdf2txt:
    #pdf2txt.write(text)