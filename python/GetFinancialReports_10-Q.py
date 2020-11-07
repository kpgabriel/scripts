import requests
from bs4 import BeautifulSoup
import re
from datetime import date

# Get Ciks from file of today
cik_dict = {}

today = date.today()    
fname = 'C:\Projects\Reports\\10Q CIK Filings\{}_{}_5_10QFilings'.format(today.year,today.month,today.day)
file_cik = open(fname,'r')
for line in file_cik:
    line_search = line.split()
    name = ' '.join(line_search[3:])
    
    company_name = re.sub('[^a-zA-Z0-9 \n\.]', '', name)
    cik_dict[line_search[2]] = company_name
    # print(company_name)

for cik_value, company  in cik_dict.items(): 
    # Make a request
    if cik_value == 'Form':
        pass
    else:
        url = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK={}'.format(cik_value)
        source = requests.get(url, allow_redirects=True).text
        soup = BeautifulSoup(source,'lxml')

        # Searching the html tags
        text_to_search = soup.find(id='seriesDiv')
        table_body = text_to_search.find('table')
        table_row_data = table_body.find_all('td')

        # regex for finding the account number associated with the 10-Q report
        quarterly_report = re.compile('(?<=Quarterly report).+?(?=(34 Act))')
        acc_id = re.compile('(?<=Acc-no:).[0-9]+-[0-9]+-[0-9]+')
       
        match = re.search(quarterly_report,str(table_row_data))
      
        if match:
            
            acc_no = re.search(acc_id,match.group(0))
            if acc_no:
                # Clean up the account number
                number = acc_no.group(0).split()
                truncated_acc_number = number[0].replace('-','')
                # Get the report
                financial_report_url = 'https://www.sec.gov/Archives/edgar/data/{0}/{1}/Financial_Report.xlsx'.format(cik_value,truncated_acc_number)
                source = requests.get(financial_report_url, allow_redirects=True)
                if today.month <= 3 and today.day <= 31:
                    open('C:\Projects\Reports\{}\Q1\Financial_Report_{}.xlsx'.format(today.year,company),'wb').write(source.content)    
                elif today.month <= 6 and today.day <= 30:
                    open('C:\Projects\Reports\{}\Q2\Financial_Report_{}.xlsx'.format(today.year,company),'wb').write(source.content)    
                elif today.month <= 9 and today.day <= 30:
                    open('C:\Projects\Reports\{}\Q3\Financial_Report_{}.xlsx'.format(today.year,company),'wb').write(source.content)    
                else:
                    open('C:\Projects\Reports\{}\Q4\Financial_Report_{}.xlsx'.format(today.year,company),'wb').write(source.content)    
                