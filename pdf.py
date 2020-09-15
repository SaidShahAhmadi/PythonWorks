import PyPDF2

# with open("Doc1.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)

#     with open("rotated.pdf", "wb") as output:
#         writer.write(output)


# +----------++++++++++++++++++++++++ ------------
# joned two pages togeter
mergee = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]

for file_name in file_namsses:
    mergee.append(file_name)
mergee.write("combined.pdf ")