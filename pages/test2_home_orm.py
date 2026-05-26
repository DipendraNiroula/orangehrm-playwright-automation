from playwright.sync_api import Page

class HomePage:
    
    def __init__(self, page:Page):
        self.page = page
        self.recruitment_link = page.get_by_role("link", name="Recruitment")
        self.vacancies_link = page.get_by_role("link", name="Vacancies")
        self.leave_link = page.get_by_role("link", name="Leave")
        self.job_link = page.get_by_role("link", name="Job")
        self.myinfo_link = page.get_by_role("link", name="My Info")
        self.job_link = page.get_by_role("link", name="Job")
        self.salary_link = page.get_by_role("link", name="Salary")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        self.maintenance_link = page.get_by_role("link", name="Maintenance")
        
        
    
    def click_myinfo(self):
        self.myinfo_link.click()
        
    def click_recruitment(self):
        self.recruitment_link.click()
        
    def click_vacancies(self):
        self.vacancies_link.click()
  
    def click_leave(self):
        self.leave_link.click()
  
    def click_job(self):
        self.job_link.click()
  
    def click_salary(self):
        self.salary_link.click()
  
    def click_dashboard(self):
        self.dashboard_link.click()
  
    def click_maintenance(self):
        self.maintenance_link.click()
             
        