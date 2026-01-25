from pypdf import PdfReader, PdfWriter

subject = "pdf 2_untiltwo 5_untilfive"

pdflist = subject.split()[1:]
print(pdflist)

pdfdict={}
for x in pdflist:
    try:
        number = int(x[:x.find("_")])
    except:
        print("Number not found")
    try:
        name = x[x.find("_")+1:] + str(".pdf")
    except:
        print("Name not found")
    try:
        pdfdict[name] = number
    except:
        print("Dictionary can not be created!")

print(pdfdict)




reader = PdfReader("combinedminutes.pdf")
output_pdf = PdfWriter()

"""
for k, v in page_dict.items():
    for page in reader.pages[v[0]:v[1]]:
        output_pdf.add_page(page)
    output_pdf.write(k + ".pdf")
    output_pdf = PdfWriter()
"""

