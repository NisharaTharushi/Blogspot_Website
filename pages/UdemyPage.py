from selenium.webdriver.common.by import By
import time

class Udemy:
    def __init__(self, driver):
        self.driver = driver


    TITLE = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    TEXT = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    HEADER = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    HEADER_LINKS = (By.TAG_NAME, "ul")
    IMAGE = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    NAME = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    VIEW_COURSE = (By.LINK_TEXT, "View Course")
    


# titles   
    def title2 (self):
        print("---- Udemy Page ----")
        print("---- Title ----")
        title2 = self.driver.find_element(*self.TITLE)
        print("title2 is: " ,title2.get_attribute("innerText"))
        print("")

    def text (self):
        text = self.driver.find_element(*self.TEXT)
        print("text is: ",text.text)
        print("")

# header
    def header_links (self):
        print("---- Header links ----")

        header = self.driver.find_element(*self.HEADER)
        header_links = header.find_elements(*self.HEADER_LINKS)
        for link in header_links:
            print(link.text)
        print("")

      
# image      
    def image (self):
        print("---- Image ----")
        image = self.driver.find_element(*self.IMAGE)
        print("image is: ",image.get_attribute("CSS_SELECTOR"))
        print("")


# name
    def name (self): 
        print("---- Name ----")
        name = self.driver.find_element(*self.NAME)
        print("name is: ",name.text)
        print("")


    def ViewCourse_button (self):
        print("---- View Course ----")
        view_course_buttons = self.driver.find_elements(*self.VIEW_COURSE)
        for button in view_course_buttons:
            button.click()
            time.sleep(2)
            print("View Course button clicked")
            print("URL is",button.get_attribute("href"))
            self.driver.back()
        

    
