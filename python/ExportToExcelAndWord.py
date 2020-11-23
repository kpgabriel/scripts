import pandas


try:
    xls = pandas.ExcelFile('path')
    sheets = xls.sheet_names
    print(sheets)    
except Exception as e:
    print(e)
