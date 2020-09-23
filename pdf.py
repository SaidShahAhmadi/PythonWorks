from fpdf import FPDF
from prettytable import PrettyTable
from prettytable import from_csv
import pyinputplus as pyip
import sys
import csv
import fpdf
from fpdf import FPDF


# class CustomPDF(FPDF):

#     def header(self):
#         # Set up a logo
#         self.image('images/Ahmad.jpeg', 10, 8, 33)
#         self.set_font('Arial', 'B', 15)

#         # Add an address
#         self.cell(100)
#         self.cell(0, 5, 'Mike Driscoll', ln=1)
#         self.cell(100)
#         self.cell(0, 5, '123 American Way', ln=1)
#         self.cell(100)
#         self.cell(0, 5, 'Any Town, USA', ln=1)

#         # Line break
#         self.ln(20)

#     def footer(self):
#         self.set_y(-10)

#         self.set_font('Arial', 'I', 8)

#         # Add a page number
#         page = 'Page ' + str(self.page_no()) + '/{nb}'
#         self.cell(0, 10, page, 0, 0, 'C')


sheet_name = pyip.inputStr(
    "Pleas type your Excel (CSV) Format file name to open table: ")

with open(sheet_name, "r") as csv_file:
    csv_reader = from_csv(csv_file)
    print(csv_reader)


# def add_image(image_path):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.image(image_path, x=10, y=8, w=100)
#     pdf.set_font("Arial", size=12)
#     pdf.ln(85)  # move 85 down
#     pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
#     pdf.output("add1_image.pdf")

#     pdf = FPDF(orientation='L', unit='mm', format='A4')

#     # page styling
#     pdf = fpdf.FPDF(format='letter')
#     pdf.add_page()
#     pdf.set_font("Arial", size=15)

#     # border styling
#     pdf.set_line_width(1)
#     pdf.set_fill_color(0, 255, 0)
#     pdf.rect(2, 2, 212, 150)

#     pdf.cell(200, 10,  txt="Results Sheet", ln=1, align="C")

#     # for i in csv_reader:
#     #     print(i[0])
#     #     pdf.write(5,  str(i))
#     #     pdf.ln()
#     pdf.write(9,  str(csv_reader))
#     pdf.ln()
#     pdf.output("testings3343.pdf")


# add_image('images/Ahmad.jpeg')


# # data = [1, 2, 3, 4, 5, 6]
pdf = FPDF(orientation='L', unit='mm', format='A4')

# page styling
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=15)


# border styling
pdf.set_line_width(1)
pdf.set_fill_color(0, 255, 0)
pdf.rect(2, 2, 212, 150)


pdf.cell(200, 10,  txt="Results Sheet", ln=1, align="C")

# for i in csv_reader:
#     print(i[0])
#     pdf.write(5,  str(i))
#     pdf.ln()
pdf.write(9,  str(csv_reader))
pdf.ln()
pdf.output("testings3343.pdf")
