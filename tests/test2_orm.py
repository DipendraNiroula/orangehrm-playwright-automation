import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Recruitment").click()
    page.get_by_role("link", name="Vacancies").click()
    expect(page.get_by_label("Topbar Menu").get_by_role("list")).to_contain_text("Vacancies")
    page.get_by_role("link", name="Leave").click()
    page.get_by_role("link", name="My Info").click()
    page.get_by_role("link", name="Job").click()
    page.get_by_role("link", name="Salary").click()
    page.get_by_role("link", name="Dashboard").click()
    page.get_by_role("link", name="Maintenance").click()
    page.locator("input[name=\"password\"]").click()
