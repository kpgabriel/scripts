import requests
from bs4 import BeautifulSoup
import re

# Make a request
url = 'https://entergy.sharepoint.com/sites/fleetmanagement/SitePages/Home.aspx'
source = requests.get(url, allow_redirects=True).text
# cik = re.search('(?<=data/).+?(?=/)',url)
# cik_number = cik.group(0)
# open('C:\Projects\Reports\Financial_Report_{0}.xlsx'.format(cik_number),'wb').write(source.content)
soup = BeautifulSoup(source,'html.parser')
print(soup)