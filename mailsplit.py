from pypdf import PdfReader, PdfWriter

subject = "pdf 2_untiltwo 5_untilfive 9_untilnine 15_untilfifteen"

# make a list of given split points / names
splitlist=[]
for x in subject.split()[1:]:
    try:
        number = int(x[:x.find("_")])
    except:
        print("Number not found")
    try:
        name = x[x.find("_")+1:] + str(".pdf")
    except:
        print("Name not found")

    try:
        splitlist.append([number, name])
    except:
        print("Creation of list not possible")

# adding the starting page for each splitpoint
temp_number=0
for x in splitlist:
    if temp_number == 0:
        x.insert(0, 1)
        temp_number = x[1]
    else:
        x.insert(0, temp_number)
        temp_number = x[1]

# write pdf files
with open("combinedminutes.pdf",'rb') as pdf_file:
    reader = PdfReader(pdf_file)
    writer = PdfWriter()

    for x in splitlist:
        for page in reader.pages[x[0]:x[1]+1]:
            writer.add_page(page)

            with open(x[2], 'wb') as output_pdf:
                writer.write(output_pdf)
                
        # reset PdfWriter
        writer = PdfWriter()
