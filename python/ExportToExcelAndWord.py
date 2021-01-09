import pandas as pd
import re
from xlsxwriter.utility import xl_rowcol_to_cell



try:
    xls = pd.ExcelFile('C:\Projects\Reports\\2021\Q1\\10-K\Financial_Report_Guskin Gold Corp..xlsx')
    form_pattern = re.compile('(Consolidated|Statements)')
    sheets = xls.sheet_names
    newlist = list(filter(form_pattern.match, sheets))
    newlist.insert(0,sheets[0])
    dict_sheets = pd.read_excel('C:\Projects\Reports\\2021\Q1\\10-K\Financial_Report_Guskin Gold Corp..xlsx',sheet_name=newlist)
    print(newlist)

    income_sheets = {}
    for x in range(len(newlist)):
        # Create the dictionary of data fram objects with sheet names
        income_sheets['{0}'.format(newlist[x])] =  pd.DataFrame(dict_sheets[newlist[x]])

    # Make a writer using xlsxwriter library
    writer_orig = pd.ExcelWriter('C:/Projects/Reports/simple.xlsx', engine='xlsxwriter')

    # Simple excel document
    for sheet_name in income_sheets.keys():
        income_sheets[sheet_name].to_excel(writer_orig, sheet_name=sheet_name, index=False)
    
    writer_orig.save()



    # Now we format and write a more complicated output




    writer = pd.ExcelWriter('C:/Projects/Reports/fancy.xlsx', engine='xlsxwriter')
    # Get the workbook
    workbook = writer.book

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    # Add a custom format for cells with money.
    money = workbook.add_format({'num_format': '_("$ "#,##0_);_("$ "(#,##0)'})

    num_sheet = 0
    for sheet_name in income_sheets.keys():
        income_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

        # Get the worksheet
        worksheet = writer.sheets[sheet_name]
        # Change the cell columns in all sheets
        
        worksheet.set_column('A:A', 40)
        worksheet.set_column('B:B', 25)
        worksheet.set_column('C:C', 25)
        
    writer.save()

except Exception as e:
    print(e)
