import requests
import bs4
from bs4 import BeautifulSoup
from datetime import date
import re
import io
import os

def checkPath(path):
    # If it does not exist
    if os.path.exists(path) == False:
        os.makedirs(path)
    # If it exists
    else:
        pass

def CreatTextFile(url):
    today = date.today()
    source = requests.get(url, allow_redirects=True).text

    soup = BeautifulSoup(source,'lxml')
    pre = soup.find('pre')

    form_pattern = re.compile('(10-K|10-Q)')
    form_name = re.search(form_pattern,pre.text)
    
    pattern = re.compile('(?<=Company Name).?')
    formated_text = re.sub(pattern, "\n1", pre.text)
    directory = 'C:\Projects\Reports\\{} Filings\\'.format(form_name.group(0))
    fname = directory + '{}_{}_{}_CompanyFilings'.format(today.year,today.month,today.day)
    checkPath(directory)
    with open(fname,'w', encoding="utf-8") as f:
        f.write(formated_text)

try:
    # Make a request
    urls = ['https://www.sec.gov/cgi-bin/current?q1=0&q2=0&q3=','https://www.sec.gov/cgi-bin/current?q1=0&q2=1&q3=']
    for url in urls:
        CreatTextFile(url)
    
except Exception as e:
    print(e)
