import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.Blog_page import Blog   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://www.pavantestingtools.com/")

home = Blog(driver)


home.print_title()
home.print_header_links()
home.click_header_links()
home.print_h3_Paragraph()
home.search()
home.click_all_buttons()
home.print_footer_links()
