from pathlib import Path
from zipfile import ZipFile

# ++++++ to creat a zip folder  ++++++
with ZipFile("name_of_zip_file.zip", "w") as zip:
    for path in Path("name_of_folder").rglob("*.*"):
        zip.write(path)

# +++++  how to read the zip content  ++++++
# with ZipFile("name_of_folder.zip") as zip:
#     print(zip.namelist())

# +++++ #to extract the zip file we use +++++
# print(zip.extractall("extractFile"))
