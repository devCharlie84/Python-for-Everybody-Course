############
# Assigment 1
############
import urllib.error
import urllib.parse
import urllib.request
import json
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
import socket
import re
fname = ("regex_sum_930681.txt")
fh = open(fname)
lst = list()
sumatoria = 0
count = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        for num in numbers:
            lst.append(num)
            count = count+1
for item in lst:
    sumatoria = int(item) + sumatoria
print("There are", count, "values with a sum=", sumatoria)