import requests
from bs4 import BeautifulSoup
import re

# Make a request
url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK=40545'
source = requests.get(url, allow_redirects=True).text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())
text_to_search = soup.find(id='seriesDiv')
table_body = text_to_search.find('table')
table_row_data = table_body.find_all('td')
file = open("C:\Projects\scripts\python\\test.txt","w")
for row in table_row_data:
    file.write(str(row))
file.close()

quarterly_report = re.compile('(?<=Quarterly report).+?(?=(34 Act))')
acc_id = re.compile('(?<=Acc-no:).[0-9]+-[0-9]+-[0-9]+')
file = open("C:\Projects\scripts\python\\test.txt","r")
match = re.search(quarterly_report,file.read())
file.close()
if match:
    print(match.group(0))
    acc_no = re.search(acc_id,match.group(0))
    if acc_no:
        number = acc_no.group(0)
        print(number.replace('-',''))
# cik_number = cik.group(0)
# open('C:\Projects\Reports\Financial_Report_{0}.xlsx'.format(cik_number),'wb').write(source.content)