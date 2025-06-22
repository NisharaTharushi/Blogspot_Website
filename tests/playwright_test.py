import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.playwright_page import Playwright  # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
home = Playwright(driver)


home.title()
home.subtitle()
home.header()
home.playwright_text()
home.getbyrole()
home.primary_button()
home.toggle_button()
home.formusername(
    username_input="Pavan"
)
home.navigation_text()
home.nav_all_links()
home.accept_terms_label()
home.getbytext()
home.links()
home.submit_button()
home.getByLabel(
    email_input_text="tharushi@gmail.com",
    password_input_text="Pavan",
    age_input_text="25"
)
home.shipping()
home.getbyplaceholder(
    name_input_text="Pavan", 
    phonenumber_input_text="0877878787",
    message_input_text="Pavan",
    search_input_text="Pavan"
)
home.getByAltText()
home.getbytitle()
home.savebutton()
home.getbyTestId()
home.editprofile()
home.productBoxes()
home.links2()









