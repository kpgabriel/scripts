import requests
import bs4
from bs4 import BeautifulSoup
from datetime import date
import re
import io

try:
    # Make a request
    cik_url='https://www.sec.gov/cgi-bin/current?q1=0&q2=1&q3='
    source = requests.get(cik_url, allow_redirects=True).text

    soup = BeautifulSoup(source,'lxml')
    pre = soup.find('pre')
    pattern = re.compile('(?<=Company Name).?')
    formated_text = re.sub(pattern, "\n1", pre.text)
    today = date.today()
    
    fname = 'C:\Projects\Reports\\10Q CIK Filings\{}_{}_{}_10QFilings'.format(today.year,today.month,today.day)
    with open(fname,'w', encoding="utf-8") as f:
        f.write(formated_text)
except Exception as e:
    print(e)
