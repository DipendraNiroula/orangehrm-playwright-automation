import re
from playwright.sync_api import Page
from pages.test2_login_orm import LoginPage
from pages.test2_home_orm import HomePage

def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    home_page.click_recruitment()
    home_page.click_vacancies()
    home_page.click_leave()
    home_page.click_myinfo()
    home_page.click_job()
    home_page.click_salary()
    home_page.click_dashboard()
    home_page.click_maintenance()