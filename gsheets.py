import json

import gspread
from google.oauth2.service_account import Credentials



class GoogleSheets:

    def __init__(self, scopes, credentials_path, excel_key):
        self.scopes = scopes
        self.creds = Credentials.from_service_account_file(credentials_path, scopes=self.scopes)
        self.client = gspread.authorize(self.creds)
        self.excel = self.client.open_by_key(excel_key)
        self.working_sheet = self.excel.sheet1


    def insert_row(self):
        pass

    def modify_cell(self):
        pass

    def get_values(self):
        return self.working_sheet.get_all_records()




# scopes = [
#     "https://www.googleapis.com/auth/spreadsheets"
# ]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
#
# client = gspread.authorize(creds)
#
# full_excel = client.open_by_key("1jdbZ30JGxarzDVxOXrpeev6QtP5MecrMaifDIKXVy_A")
# working_sheet = full_excel.sheet1
# values = working_sheet.get_all_records()
# print(values)

if __name__ == '__main__':

    with open("config.json", "r") as f:
        gsheets_config = json.loads(f.read())

    excel = GoogleSheets(scopes=gsheets_config["scopes"],
                         credentials_path="credentials.json",
                         excel_key=gsheets_config["excel_id"])

    employees = excel.get_values()
    print(employees)





