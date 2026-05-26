from playwright.sync_api import Page, expect

class HomePage:
    
    def __init__(self, page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.directory_link = page.get_by_role("link", name="Directory")
        
    def is_upgrade_button_visible(self):
        expect(self.upgrade_button).to_be_visible()
    
    def click_performance(self):
        self.performance_link.click()
        
    def click_directory(self):
        self.directory_link.click()
             
        