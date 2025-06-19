import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver

from pages.Home_page import PageName   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

# create object of PageName
home = PageName(driver)


home.title()
home.header_links()
home.go_back()
home.Name()
home.email()
home.phone()
home.address()
home.Gender()
home.day()
home.Country()
home.colour()
home.animal()
home.date_picker()
home.links()
home.upload_file()
home.Upload_files_2()
home.static_web_table()
home.dynamic_web_table()
home.pagination_web_table()
home.checkbox()
home.form()
# home.section1()
# home.section2()
# home.section3()
home.footer_links()
home.tabs()
home.search_input()
home.submit_search()
home.Dynamic_Button()
home.Alert_button()
home.Confirm_button()
home.Prompt_button()
home.NewTab()
home.Popup()

home.MouseOver()
home.DoubleClick()
home.DragAndDrop()
home.Slider()
home.Labels()
home.laptops()
home.broken_links()
home.shadow_dom()
# home.mobile_labels()
home.click_blog_link()
home.upload_file2()
home.click_youtube_link()



