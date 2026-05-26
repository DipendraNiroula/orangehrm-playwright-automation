from playwright.sync_api import Page, expect
import pytest
import csv
import json

def get_csv_data():
    rows = []
    with open("./test_data/data.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)   # debug
            rows.append(
                (row.get("username"), row.get("password"))
            )
    return rows
def get_json_data():
   with open("./test_data/data.json") as f:
       raw = json.load(f)
       return [(item["username"], item["password"]) 
               for item in raw]
@pytest.mark.parametrize("username,password", get_json_data())
def test_example(page: Page, username, password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()