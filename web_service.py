import datetime
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, request

from gsheets import GoogleSheets

def read_config(path: str="config.json") -> dict:
    with open(path, "r") as f:
        config = json.loads(f.read())
        return config

app = Flask(__name__)


@app.route("/")
def password_form():
    return render_template("password_form.html")

@app.route("/password_reset", methods=["POST"])
def reset_password(data):
    username = request.form["username"]
    new_password = request.form["new-password"]
    confirm_password = request.form["confirm-password"]

    if new_password == confirm_password:
        excel = GoogleSheets(scopes=gsheets_config["scopes"],
                             credentials_path="credentials.json",
                             excel_key=gsheets_config["excel_id"])

        cell = excel.working_sheet.find(username)
        print(f"{username} was found at row {cell.row}.")
        today = datetime.now() + datetime.delta
        today = datetime.strftime("%d%m%Y")
        excel.working_sheet.update_cell(cell.row, "F", today)

if __name__ == '__main__':
    gsheets_config = read_config()
    app.run()