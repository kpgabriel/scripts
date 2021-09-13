import requests
from bs4 import BeautifulSoup
import re

# Make a request
cik = ''
acc_no = ''
url = 'https://www.sec.gov/Archives/edgar/data/{}/{}/Financial_Report.xlsx'.format(cik,acc_no)
source = requests.get(url, allow_redirects=True)
cik = re.search('(?<=data/).+?(?=/)',url)
cik_number = cik.group(0)
open('C:\Projects\Reports\Financial_Report_{0}.xlsx'.format(cik_number),'wb').write(source.content)
# soup = BeautifulSoup(source,'lxml')