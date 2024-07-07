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

    def insert_row(self, values, index=1):
        self.working_sheet.insert_row(values, index)

    def update_cell(self, row, col, value):
        self.working_sheet.update_cell(row, col, value)

    def add_worksheet(self, title, rows=2100, cols=26):
        new_worksheet = self.excel.add_worksheet(title=title, rows=rows, cols=cols)

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

    excel.insert_row(["Ana Andrei",
                       "andrei.ana@gmail.com",
                       "HR", "Diana Radulescu",
                       "radulescu.diana95@gmail.com",
                       "08/07/2025"],index=4)

    excel.update_cell(2, 3, "marketing")
    excel.add_worksheet("New Data")
