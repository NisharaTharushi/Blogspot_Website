import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.UdemyPage import Udemy   # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://www.pavanonlinetrainings.com/p/udemy-courses.html")

home = Udemy(driver)


home.title2()
home.text()
home.header_links()
home.image()
home.name()
home.ViewCourse_button()

