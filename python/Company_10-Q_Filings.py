import requests
import bs4
from bs4 import BeautifulSoup
from datetime import date
import re
import io

# Make a request
cik_url='https://www.sec.gov/cgi-bin/current?q1=0&q2=1&q3='
# url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK={0}&owner=exclude'.format(cik)
source = requests.get(cik_url, allow_redirects=True).text
# cik = re.search('(?<=data/).+?(?=/)',url)
# cik_number = cik.group(0)
# open('C:\Projects\Reports\Financial_Report_{0}.xlsx'.format(cik_number),'wb').write(source.content)
soup = BeautifulSoup(source,'lxml')
pre = soup.find('pre')
pattern = re.compile('(?<=Company Name).?')
formated_text = re.sub(pattern, "\n1", pre.text)
today = date.today()
#print pre
fname = 'C:\Projects\Reports\\10Q CIK Filings\{}_{}_{}_10QFilings'.format(today.year,today.month,today.day)
with open(fname,'w', encoding="utf-8") as f:
    f.write(formated_text)