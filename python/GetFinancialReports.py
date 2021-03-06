import requests
from bs4 import BeautifulSoup
import re
from datetime import date
import time
import os


def getFile(today):
    ret_list = []
    files = ['Q','K']
    for i in range(len(files)):
        fname = 'C:\Projects\Reports\\10-{} Filings\{}_{}_{}_CompanyFilings'.format(files[i],today.year,today.month,today.day)
        ret_list.insert(i,fname)
    return ret_list

def checkPath(path):
    # If it does not exist
    if os.path.exists(path) == False:
        os.makedirs(path)
    # If it exists
    else:
        pass

try:
    
    if __name__ == "__main__":
        
        # Get Ciks from file of today
        today = date.today()
        files = getFile(today)
        # regex for finding the account number associated with the 10-Q report
        quarterly_report = re.compile('(?<=Quarterly report).+?(?=(34 Act))')
        annual_report = re.compile('(?<=Annual report).+?(?=(34 Act))')
        acc_id = re.compile('(?<=Acc-no:).[0-9]+-[0-9]+-[0-9]+')
        

        for file in files:
            form = re.search('(10-K|10-Q)',file).group(0)
            cik_dict = {}
            file_cik = open(file,'r')

            for i in range(4):
                filePath = 'C:\Projects\Reports\{}\Q{}\\{}'.format(today.year,i+1,form)
                checkPath(filePath)

            for line in file_cik:
                line_search = line.split()
                name = ' '.join(line_search[3:])
                company_name = re.sub('[^a-zA-Z0-9 \n\.]', '', name)
                cik_dict[line_search[2]] = company_name
            
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

                    if form == '10-K':
                        match = re.search(annual_report,str(table_row_data))
                    elif form == '10-Q':
                        match = re.search(quarterly_report,str(table_row_data))
                    else:
                        continue
                
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
                                filePath = 'C:\Projects\Reports\{}\Q1\\{}\Financial_Report_{}.xlsx'.format(today.year,form,company)
                                open(filePath,'wb').write(source.content)    
                            elif today.month <= 6 and today.day <= 30:
                                filePath = 'C:\Projects\Reports\{}\Q2\\{}\Financial_Report_{}.xlsx'.format(today.year,form,company)
                                open(filePath,'wb').write(source.content)    
                            elif today.month <= 9 and today.day <= 30:
                                filePath = 'C:\Projects\Reports\{}\Q3\\{}\Financial_Report_{}.xlsx'.format(today.year,form,company)
                                open(filePath,'wb').write(source.content)    
                            else:
                                filePath = 'C:\Projects\Reports\{}\Q4\\{}\Financial_Report_{}.xlsx'.format(today.year,form,company)
                                open(filePath,'wb').write(source.content) 
                    time.sleep(.1)   
                            
except Exception as e:
    print(e)