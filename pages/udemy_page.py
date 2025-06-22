from selenium.webdriver.common.by import By
import time

class Udemy:
    def __init__(self, driver):
        self.driver = driver


    TITLE = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    TEXT = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    HEADER = (By.ID, "PageList1")
    HEADER_LINKS = (By.TAG_NAME, "a")
    IMAGE = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    VIEW_COURSE = (By.LINK_TEXT, "View Course")
    LOAD_MORE_BUTTON = (By.XPATH, "//button[normalize-space()='Load more reviews']")
    EMBED_LINK = (By.XPATH, "//a[normalize-space()='Embed Google Reviews on your Blogger website']")
    ATOM_LINK = (By.XPATH, "//a[normalize-space()='Posts (Atom)']")
    FOOTER_SECTION = (By.CLASS_NAME, "widget-content")
    FOOTER_LINKS = (By.TAG_NAME, "a")
    

    
    print("---- Udemy Page ----")
    # Title   
    def title2 (self):
        title2 = self.driver.find_element(*self.TITLE)
        print("title2 is: " ,title2.get_attribute("innerText"))


    # Background image      
    def images (self):
        image = self.driver.find_element(*self.IMAGE)
        print("image is: ",image.get_attribute("innerText"))
        print("")

    # Header Links
    def header_links (self):
        print("---- Header links ----")

        header = self.driver.find_element(*self.HEADER)
        header_links = header.find_elements(*self.HEADER_LINKS)
        for link in header_links:
            print(link.text)
            print(link.get_attribute("href"))
            print("")
        print("")

    
    # View Course buttons
    def ViewCourse_buttons (self):
        print("---- View Course buttons ----")
        view_course_buttons = self.driver.find_elements(*self.VIEW_COURSE)
        for button in view_course_buttons:
            button.click()
            time.sleep(2)
            print("View Course button clicked")
            print("URL is",button.get_attribute("href"))
            self.driver.back()


    # Load more button
    def loadmore_buttons(self):
        print("---- Load More buttons ----")

        loadmore = self.driver.find_element(*self.LOAD_MORE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", loadmore)
        self.driver.execute_script("arguments[0].click();", loadmore)
        print("Load More link clicked")
        print("")

        self.driver.get("https://www.pavanonlinetrainings.com/")
        time.sleep(2)


    # Embed Link
    def embed_links(self):
        embed = self.driver.find_element(*self.EMBED_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", embed)
        self.driver.execute_script("arguments[0].click();", embed)
        print("Embed link clicked")
        time.sleep(2)
        print("")

        self.driver.back()


    # Footer Links
    def footer_links(self):
        print("---- Footer links ----")

        footer = self.driver.find_element(*self.FOOTER_SECTION)
        footer_links = footer.find_elements(*self.FOOTER_LINKS)
        for link in footer_links:
            print(link.text)
            time.sleep(2)
        print("")        
        

    
