import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.PlaywrightPage import Playwright  # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
home = Playwright(driver)


home.title()
home.title2()
home.header()
home.playwright_text()
home.getbyrole()
home.primary_button()
home.toggle_button()
home.formusername_label()
home.username_input()
home.navigation_text()
home.nav_all_links()
home.accept_terms_label()
home.getbytext()
home.links()
home.submit_button()
home.getByLabel()
home.email()
home.password()
home.age()
home.shipping()
home.getbyplaceholder()
home.name()
home.phonenumber()
home.message()
home.search()
home.searchbutton()
home.getbytitle()
home.savebutton()
home.getbyTestId()
home.editprofile()
home.productBoxes()
home.links2()









