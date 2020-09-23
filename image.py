import os
import img2pdf

from fpdf import FPDF
from os import listdir
from numpy.core.records import record
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
import pyinputplus as pyip
from prettytable import PrettyTable
from prettytable import from_csv


path = '/home/ubuntu/Desktop/Netlink/python/resheetr/images/'
os.chdir(path)
images = [i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]

with open("output.pdf", "wb") as csv_file:
    csv_file.write(img2pdf.convert(images))
    csv_reader = csv_file
    records = csv_reader

    images = []

    for image in images:
        print(images[0])

        for record in records:
            print(record)
            images.append(record)
