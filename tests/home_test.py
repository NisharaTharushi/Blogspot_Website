import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver

from pages.home_page import PageName   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

# create object of PageName
home = PageName(driver)


home.title()
home.header_links()
home.go_back()
home.form1(
    name_input="Nishara",
    email_input="tharushi@gmail",
    phone_input="0777777777",
    address_input="Colombo",
    country_input="Japan",
    colour_input="Red",
    animal_input="Dog",
    date_input="05/15/2025",
)
home.links()
home.upload_file(r"C:\Users\User\Downloads\is it worth it_.jpg")
home.Upload_files_multiple(
    r"C:\Users\User\Downloads\is it worth it_.jpg", 
    r"C:\Users\User\Downloads\is it worth it_.jpg")
home.static_web_table()
home.dynamic_web_table()
home.pagination_web_table()
home.checkbox()
home.form_3("Hello world",
            "Hello world", 
            "Nishara")
home.footer_links()
home.tabs()
home.search_input("Selenium")
home.submit_search()
home.Dynamic_Button()
home.Alert_button()
home.Confirm_button()
home.Prompt_button()
home.NewTab()
home.Popup()
home.MouseOver()
home.DoubleClick("hello")
home.DragAndDrop()
home.Slider()
home.Labels()
home.laptops()
home.broken_links()
home.shadow_dom()
home.click_blog_link()
home.upload_file2(r"C:\Users\User\Downloads\is it worth it_.jpg")
home.click_youtube_link()



