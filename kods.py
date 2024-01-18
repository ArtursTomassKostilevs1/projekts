import PyPDF2
print("Ievadiet ceļu pie pdf faila,kur jāmekle vārdu:")
file=input()
if file!="":        
    row1=[]
    pages=[]
    text=[]
    pdf_file=PyPDF2.PdfReader(open(file,"rb"))
    number_of_pages=len(pdf_file.pages)
    for i in range(number_of_pages):
        pages.append(pdf_file.pages[i])
    for i in range(number_of_pages):
        text.append(pages[i].extract_text())
    print("Ievadiet vārdu, kuru jāmekle:")
    find_word=input()
    page_number=[]
    approximate_location=[]
    for i in range(len(text)):
        page=text[i]
        pos1=page.find(str(find_word))
        if(pos1!=""):
             check=page[pos1:pos1+100]
             if(check!=""):
                 page_number.append(i+1)
                 approximate_location.append(page[pos1:pos1+100])
else:
    print("Kļūda ar faila atrašanu.")
if(len(page_number)>0):
    print("Lapas, kur bija vārds ir:", page_number)
    print("Apmēram tie atrodas:")
    for i in range(len(approximate_location)):
        print(approximate_location[i])
else:
    print("Vārds nav atrasts.")