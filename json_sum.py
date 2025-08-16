"""
===============================================================================
 Project Title : JSON Comment Counter
 Author        : Anup Sharma
 Description   :
    This project demonstrates how to fetch, parse, and analyze JSON data
    using Python. It retrieves a JSON file from a web URL, extracts
    all comment counts, and calculates:
      1. The total number of comments
      2. The sum of all comment counts

 Skills Demonstrated :
    - Python scripting
    - JSON parsing using 'json' library
    - Web data handling with 'urllib.request'
    - Data aggregation (counting & summing values)
    - Writing clean, recruiter-friendly code

 Tools & Libraries :
    - Python 3.x
    - urllib (to fetch data from URL)
    - json (to parse JSON format)

===============================================================================
"""

# -------------------- Step 1: Import Required Libraries -------------------- #
import urllib.request
import json

# -------------------- Step 2: Prompt User for URL -------------------------- #
url = input('Enter location: ')  # Example: http://py4e-data.dr-chuck.net/comments_42.json

# -------------------- Step 3: Retrieve Data from the URL ------------------- #
print(f'Retrieving data from {url} ...')
data = urllib.request.urlopen(url).read().decode()

# -------------------- Step 4: Load JSON Data into Python Dictionary -------- #
info = json.loads(data)

# -------------------- Step 5: Extract and Process Comment Counts ----------- #
total = sum(item['count'] for item in info['comments'])
count = len(info['comments'])

# -------------------- Step 6: Display the Results -------------------------- #
print('Count:', count)
print('Sum:', total)
