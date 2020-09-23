from pandas.tseries.offsets import Second
from prettytable import PrettyTable
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
from prettytable import from_csv
from fpdf import FPDF
import pyinputplus as pyip
import pandas as pd
import sys
import csv
import fpdf
from fpdf import FPDF
from os import listdir


print("")
sheet_name = pyip.inputStr(
    "Pleas type your Excel (CSV) Format file name to open table: ")
print("")
string = ":+++------------------ STUDENT LIST ----------------+++:"
print(string.center(77))


# selecting data from sheet

with open(sheet_name, "r") as csv_file:
    csv_reader = from_csv(csv_file)
    print(csv_reader)


def change_data_to_pdf(data):
    pdf = FPDF(orientation='L', unit='mm')
    # pdf = fpdf.FPDF('L', 'mm', format=(30, 10))
    pdf = fpdf.FPDF(format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=12,)
    pdf.cell(150, 10,  txt="Results Sheet", ln=1, align="C")

    # border styling
    pdf.set_line_width(1)
    pdf.set_fill_color(0, 255, 0)
    pdf.rect(2, 2, 205, 160)

    # excel cell data
    text = f"""
        Name: {data[1]}
        Father Name: {data[2]}

        subject
        Math: {data[3]}
        Chemistry: {data[4]}
        Biology: {data[5]}
        Geology: {data[6]}
        English: {data[7]}

        Average score:

        Final Result:
    """
    # show excel data
    pdf.set_right_margin(444)
    pdf.multi_cell(150, 9, text, align='R')

    # adding Image
    pdf.image('images/1_jobs.jpeg', x=50, y=50, w=50)
    # pdf.cell(400, 40, txt="{}".format('images/Ahmad.jpeg'), ln=1)

    pdf.ln()
    pdf.output("File.pdf")


class Searching():
    # @staticmethods
    # def images():

    #     path = "/home/ubuntu/Desktop/Netlink/python/resheetr/images/"  # get the path of images

    #     imagelist = listdir(path)  # get list of all images

    #     pdf = FPDF('P', 'mm', 'A4')  # create an A4-size pdf document

    #     x, y, w, h = 0, 0, 200, 250

    #     for image in imagelist:
    #         pdf.add_page()
    #         pdf.image(path+image, x, y, w, h)
    #         print(image)

    # @staticmethods
    def search_data(stype):
        search_key = input(f"type your {stype}: ")
        with open(sheet_name, "r") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            all_data = []
            for row in csvReader:
                if stype == "id":
                    if search_key == row[0]:
                        rowdata = row
                        print(rowdata)
                        for data in rowdata:
                            all_data.append(data)
                            # sum1 = data.sum()
                            # print('total is:'+sum1)
                        change_data_to_pdf(all_data)
                        break
                elif stype == "name":
                    if search_key.lower() == row[1].lower():
                        rowdata = row
                        for data in rowdata:
                            all_data.append(data)
                        change_data_to_pdf(all_data)
                        break
                else:
                    print(csv_reader)
                    change_data_to_pdf(csv_reader)
                    break


stype = pyip.inputMenu(["Id", "Name", "all"], numbered=True)
if stype.lower() == "name":
    Searching.search_data("name")
elif stype.lower() == "id":
    Searching.search_data("id")
elif stype.lower() == "all":
    Searching.search_data('all')
