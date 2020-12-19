import pandas as pd
import re
from xlsxwriter.utility import xl_rowcol_to_cell



try:
    xls = pd.ExcelFile('C:\Projects\Reports\\2020\Q4\\10-K\Financial_Report_Quanex Building Products CORP.xlsx')
    form_pattern = re.compile('(Consolidated|Statements)')
    sheets = xls.sheet_names
    newlist = list(filter(form_pattern.match, sheets))
    newlist.insert(0,sheets[0])
    df = pd.read_excel('C:\Projects\Reports\\2020\Q4\\10-K\Financial_Report_Quanex Building Products CORP.xlsx',sheet_name=newlist)
    # print(newlist)
    coverpage          = df[newlist[0]]
    balancesheet1      = df[newlist[1]]
    balancesheet2      = df[newlist[2]]
    statementofincome  = df[newlist[3]]
    statementofcomp    = df[newlist[4]]
    statementofstock1  = df[newlist[5]]
    statementofstock2  = df[newlist[6]]
    statementofcash    = df[newlist[7]]

    coverpage_df          = pd.DataFrame(coverpage)
    balancesheet1_df      = pd.DataFrame(balancesheet1)
    balancesheet2_df      = pd.DataFrame(balancesheet2)
    statementofincome_df  = pd.DataFrame(statementofincome)
    statementofcomp_df    = pd.DataFrame(statementofcomp)
    statementofstock1_df  = pd.DataFrame(statementofstock1)
    statementofstock2_df  = pd.DataFrame(statementofstock2)
    statementofcash_df    = pd.DataFrame(statementofcash)


    # print(type(newdf))
    # df.to_excel('C:\Projects\Reports\\2020\Q4\\10-K\temp\Financial_Report_Quanex Building Products CORP.xlsx')   
    income_sheets = {'coverpage': coverpage_df, 'balancesheet1': balancesheet1_df, 'balancesheet2': balancesheet2_df, 
                    'statementofincome': statementofincome_df,'statementofcomp': statementofcomp_df,'statementofstock1': statementofstock1_df,
                    'statementofstock2': statementofstock2_df,'statementofcash':statementofcash_df}

    writer = pd.ExcelWriter('C:/Projects/Reports/2020/Q4/10-K/temp/Financial_Report_Quanex Building Products CORP.xlsx', engine='xlsxwriter')
    
    for sheet_name in income_sheets.keys():
        income_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    
except Exception as e:
    print(e)
