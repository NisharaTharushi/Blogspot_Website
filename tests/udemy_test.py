import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.udemy_page import Udemy   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://www.pavanonlinetrainings.com/p/udemy-courses.html")

home = Udemy(driver)


home.title2()
home.images()
home.header_links()
home.ViewCourse_buttons()
home.loadmore_buttons()
home.embed_links()
home.footer_links()


