import json
from pathlib import Path
import os

# converting this file data to json file
# movies = [
#     {"id": 1, "title": "Terminator", "year": 2019},
#     {"id": 2, "title": "Kindergarten Cop", "year": 2015},
#     {"id": 3, "title": "Hacked", "year": 2019},
#     {"id": 4, "title": "MyName is Khan", "year": 2018},
# ]

# data = json.dumps(movies)
# # print(data)
# Path("movies.json").write_text(data)

# ++++++++++++++++++++++++++++++_---------------------+++++++
# reading data for json file
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
