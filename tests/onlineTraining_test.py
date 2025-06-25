import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.onlineTrainingPage import OnlineTraining  # importing from pages/home_page.py

driver = webdriver.Firefox()  # Make sure chromedriver is in your PATH
driver.get("https://www.pavanonlinetrainings.com/")

home = OnlineTraining(driver)

home.title()
home.description()
home.image()
home.heading()
home.parahraph()
home.links()
home.socialmedia()
home.profile()
home.loadmore()
home.embed()
home.footer()

