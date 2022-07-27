#google sheets API
#%%
from doctest import testfile
from heapq import nlargest
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Glide administratie").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(2)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1,2).value  # Get the value of a specific cell

testList = [1,3,4,5,6,7,8,9,3,10]

# return begin_row with last filled row number
begin_row = 1
for i in range(1,50):
    
    if (sheet.cell(i,1).value == None):
        begin_row = i
        break    
    
# Updating cells by the given list
testList = [[20221901,43.75,43.75],[ 2019210,12.75,80.75]]
for j in range(len(testList)):
    for i in range(1,len(testList[0])+1):
        sheet.update_cell(begin_row + j, i, testList[j][i-1])
#%%