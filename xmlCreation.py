#! /usr/bin/python3
import re
from datetime import datetime
import lxml.etree as ET

input = input()
gtin = re.search(r"F7[A-Za-z0-9]{15}", input)
gtin = gtin.group(0)
gtin = gtin[3:]
print("GTIN: " + gtin)

date = str(datetime.now())
date = date[:-3]
date = date.replace(' ', 'T')
print("DATE: " + date)


# We can change the xml file however in order to do that we need to create a new file.
# Given the time we have left we cannot make this change