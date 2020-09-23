# # import cv2
# # import os


# # def load_images_from_folder(folder):
# #     images = []
# #     for filename in os.listdir(folder):
# #         img = cv2.imread(os.path.join(folder, filename))
# #         if img is not None:
# #             images.append(img)
# #     return images


# # folder = ""

# import numpy as np
# import cv2
# # Load an color image in grayscale
# img = cv2.imread('images/1_jobs.jpeg', 0)
# # Display the image
# cv2.imshow('image', img)
# # key binding function
# cv2.waitKey(0)
# # Destroyed all window we created earlier.
# cv2.destroyAllWindows()

# print(img)

from fpdf import FPDF
from os import listdir
from numpy.core.records import record
from openpyxl.workbook import Workbook
from openpyxl.styles import Font
import pyinputplus as pyip
from prettytable import PrettyTable
from prettytable import from_csv


# sheet_name = pyip.inputStr(
#     "Pleas type your Excel (CSV) Format file name to open table: ")
# with open(sheet_name, "r") as csv_file:
#     csv_reader = from_csv(csv_file)
#     print(csv_reader)


path = "/home/ubuntu/Desktop/Netlink/python/resheetr/images/"  # get the path of images

imagelist = listdir(path)  # get list of all images

pdf = FPDF('P', 'mm', 'A4')  # create an A4-size pdf document

x, y, w, h = 0, 0, 200, 250

sheet_name = pyip.inputStr(
    "Pleas type your Excel (CSV) Format file name to open table: ")

with open(sheet_name, "r") as csv_file:
    csv_reader = csv_file
    records = csv_reader
    images = []
    for record in records:
        print(record)
        images.append(record)

        for image in imagelist:
            pdf.add_page()
            pdf.image(path+image, x, y, w, h)
            print(image)
pdf.output("images.pdf", "F")
