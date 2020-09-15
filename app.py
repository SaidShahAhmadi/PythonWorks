# from sales import cal_x, cal_y
# import sales
#  sales.cal_y

# accesing file form sub-directory

# from ecommerce_module.sales import cal_x, cal_y

# cal_x()

import pathlib
import os
import glob

# path = input("Enter Your Directory path: ")
# listdir = os.listdir(path)

# massage = f"In This Directory You have {len(listdir)} Files: "
# print(massage)
# print(listdir)


# this is second way
extension_path = glob.glob('*.py')
massage = f"In This dirctory You have {len(extension_path)} files: "
print(massage)
print(extension_path)

# this is second way
# extension_path = input("enter your ext: ")
# extension = glob.glob(extension_path)
# massage = f"In This dirctory You have {len(extension)} files: "
# print(massage)
# print(extension)

# to show full path
# for file in g:
#     print(os.path.join(path, file))
