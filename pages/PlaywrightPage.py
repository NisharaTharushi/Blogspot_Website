from selenium.webdriver.common.by import By
import time
# explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Playwright:

    def __init__(self, driver):
        self.driver = driver

    
    TITLE = (By.XPATH, "//a[normalize-space()='Automation Testing Practice']")
    TITLE2 = (By.XPATH, "//span[normalize-space()='For Selenium, Cypress & Playwright']")
    HEADER = (By.ID, "PageList2")
    HEADER_LINKS = (By.TAG_NAME, "ul")
    PLAYWRIGHT_TEXT = (By.XPATH, "//h3[normalize-space()='PlaywrightPractice']")
    GETBYROLE_TEXT = (By.XPATH, "//span[normalize-space()='getByRole()']")
    BUTTONS_TEXT = (By.XPATH, "//h3[normalize-space()='Buttons']")
    PRIMARY_BUTTON = (By.XPATH, "//button[normalize-space()='Primary Action']")
    TOGGLE_BUTTON = (By.XPATH, "//button[normalize-space()='Toggle Button']")
    FORMUSERNAME_LABEL = (By.XPATH, "//label[normalize-space()='Username:']")
    USERNAME_INPUT = (By.ID, "username")
    NAVIGATION_TEXT = (By.XPATH, "//h3[normalize-space()='Navigation']")
    NAVIALLINKS = (By.XPATH, "//nav[@role='navigation']")
    ACCEPT_TERMS_LABEL = (By.XPATH, "//label[normalize-space()='Accept terms']")
    GETBYTEXTS = (By.ID, "text-locators")
    LINK = (By.XPATH, "//a[normalize-space()='link']")
    SUBMIT = (By.XPATH, "//button[normalize-space()='Submit Form']")
    GETBYLABEL = (By.XPATH, "//h2[contains(text(),'3.')]")
    EMAIL_LABEL = (By.XPATH, "//label[normalize-space()='Email Address:']")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_LABEL = (By.XPATH, "//label[normalize-space()='Password:']")
    PASSWORD_INPUT = (By.NAME, "password")
    AGE_LABEL = (By.ID, "age-label")  
    AGE_INPUT = (By.XPATH, "//input[@type='number']")
    STANDARD_LABEL = (By.XPATH, "//label[normalize-space()='Standard']")
    express_label = (By.XPATH, "//label[normalize-space()='Express']")
    GETPLACEHOLDER_TEXT = (By.XPATH, "//h2[contains(text(),'4.')]")
    FULLNAME_INPUT = (By.XPATH, "//input[@placeholder='Enter your full name']")
    PHONENUMBER_INPUT = (By.XPATH, "//input[@placeholder='Phone number (xxx-xxx-xxxx)']")
    MESSAGE_INPUT = (By.XPATH, "//textarea[@placeholder='Type your message here...']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search products...']")
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    GETBYTITLE = (By.ID, "title-locators")
    GETBYTITLE_TAG = (By.TAG_NAME, "P")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    GETBYTESTID = (By.XPATH, "//section[@id='testid-locators']//p[contains(text(),'Locate elements by their')]")
    EDIT_BUTTON = (By.XPATH, "//button[normalize-space()='Edit Profile']")
    PRODUCT_GRID = (By.CSS_SELECTOR, "div[data-testid='product-grid']")
    LINKS = (By.XPATH, "//nav[@data-testid='main-navigation']")


    def title(self):
        print("---- Title ----")
        title = self.driver.find_element(*self.TITLE)
        print("Title is: ", title.text)
        time.sleep(4)
        print("")

    def title2(self):
        print("---- Title2 ----")
        # explicit wait
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TITLE2))   
        title2 = self.driver.find_element(*self.TITLE2)
        print("Title2 is: ", title2.text)
        time.sleep(4)
        print("")


    def header(self):
        print("---- Header ----")
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.HEADER))
        header = self.driver.find_element(*self.HEADER)
        header_links = header.find_elements(*self.HEADER_LINKS)
        for link in header_links:
            print(link.text)
            link.click()
            time.sleep(3)
            self.driver.get("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        print("")    

        print("header links clicked")    
        print("")


    def playwright_text(self):
        print("---- Playwright ----")
        playwright_text = self.driver.find_element(*self.PLAYWRIGHT_TEXT)
        print("Playwright text is: ", playwright_text.text)
        time.sleep(4)
        print("")


    def getbyrole(self):
        print("---- GetByRole ----")
        getbyrole_text = self.driver.find_element(*self.GETBYROLE_TEXT)
        print("GetByRole text is: ", getbyrole_text.text)
        time.sleep(4)
        print("")


    def primary_button(self):
        print("---- Primary Button ----")
        primary_button = self.driver.find_element(*self.PRIMARY_BUTTON)
        print("Primary button is: ", primary_button.text)
        self.driver.execute_script("arguments[0].click();", primary_button)
        print("primary button clicked")
        time.sleep(4)
        print("")


    def toggle_button(self):
        print("---- Toggle Button ----")
        toggle_button = self.driver.find_element(*self.TOGGLE_BUTTON)
        print("Toggle button is: ", toggle_button.text)
        self.driver.execute_script("arguments[0].click();", toggle_button)
        print("toggle button clicked")
        time.sleep(4)
        print("")


    def formusername_label(self):
        print("---- FormUsername Label ----")
        formusername_label = self.driver.find_element(*self.FORMUSERNAME_LABEL)
        print("FormUsername label is: ", formusername_label.text)
        time.sleep(4)
        print("")


    def username_input(self):
        print("---- Username Input ----")
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys("Pavan")
        print("Username input is: ", username_input.text)
        time.sleep(4)
        print("")


    def navigation_text(self):
        print("---- Navigation Text ----")
        navigation_text = self.driver.find_element(*self.NAVIGATION_TEXT)
        print("Navigation text is: ", navigation_text.text)
        time.sleep(4)
        print("")


    def nav_all_links(self):
        print("---- Other Links ----")
        naviallinks = self.driver.find_element(*self.NAVIALLINKS)
        tagname = naviallinks.find_elements(By.TAG_NAME, "ul")
        for link in tagname:
            print(link.text)
            link.click()
            time.sleep(3)
            self.driver.get("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        print("")


    def accept_terms_label(self):
        print("---- Accept Terms Label ----")
        accept_terms_label = self.driver.find_element(*self.ACCEPT_TERMS_LABEL)
        self.driver.execute_script("arguments[0].click();", accept_terms_label)
        print("Accept terms label clicked and is: ", accept_terms_label.text)
        time.sleep(4)
        print("")    


    def getbytext(self):
        print("---- GetByText ----")
        getbytext_text = self.driver.find_element(*self.GETBYTEXTS)
        texts = getbytext_text.find_elements(By.TAG_NAME, "p")
        for text in texts:
            print(text.text)
            time.sleep(2)
        print("")

        getbytext_text = self.driver.find_element(*self.GETBYTEXTS)
        texts = getbytext_text.find_elements(By.TAG_NAME, "li")
        for text in texts:
            print(text.get_attribute("innerText"))
            time.sleep(2)
        print("")


    def links(self):
        print("---- Link ----")
        link = self.driver.find_element(*self.LINK)
        print("Link is: ", link.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", link)
        self.driver.execute_script("arguments[0].click();", link)
        print("Link clicked")
        time.sleep(4)  
        print("")


    def submit_button(self):
        print("---- Submit Button ----")
        submit_button = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        self.driver.execute_script("arguments[0].click();", submit_button)
        print("Submit button clicked")
        time.sleep(4)
        print("")    


    def getByLabel(self):
        print("---- GetByLabel ----")
        getByLabel = self.driver.find_element(*self.GETBYLABEL)
        print("GetByLabel is: ", getByLabel.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", getByLabel)
        time.sleep(4)    
        print("")


    def email(self):
        email_label = self.driver.find_element(*self.EMAIL_LABEL)
        print("Email label is: ", email_label.text)
        time.sleep(4)
        
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys("thar@gmail.com")
        print("Email entered",email_input.get_attribute("value"))
        time.sleep(4)


    def password(self):
        password_label = self.driver.find_element(*self.PASSWORD_LABEL)
        print("Password label is: ", password_label.text)
        time.sleep(4)        

        password = self.driver.find_element(*self.PASSWORD_INPUT)
        password.clear()
        password.send_keys("123456")
        print("Password entered",password.get_attribute("value"))
        time.sleep(4)


    def age(self):
        age_label = self.driver.find_element(*self.AGE_LABEL)
        print("Age label is: ", age_label.text)
        time.sleep(4)

        age = self.driver.find_element(*self.AGE_INPUT)
        age.clear()
        age.send_keys("20")
        print("Age entered",age.get_attribute("value"))
        time.sleep(4)

    def shipping(self):
        standard = self.driver.find_element(*self.STANDARD_LABEL)
        self.driver.execute_script("arguments[0].click();", standard)
        print("Standard clicked")
        time.sleep(4)

        express = self.driver.find_element(*self.express_label)
        self.driver.execute_script("arguments[0].click();", express)
        print("Express clicked")
        time.sleep(4)
        print("")


    def getbyplaceholder(self):
        print("---- GetByPlaceholder ----")

        getbyplaceholder_text = self.driver.find_element(*self.GETPLACEHOLDER_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", getbyplaceholder_text)
        print("GetByPlaceholder text is: ", getbyplaceholder_text.text)
        time.sleep(4)    
    
    def name(self):
        name = self.driver.find_element(*self.FULLNAME_INPUT)
        name.clear()
        name.send_keys("tharushi")
        print("Name entered",name.get_attribute("value"))
        time.sleep(4)

    def phonenumber(self):
        phonenumber = self.driver.find_element(*self.PHONENUMBER_INPUT)
        phonenumber.clear()
        phonenumber.send_keys("0771234567")
        print("Phone number entered",phonenumber.get_attribute("value"))
        time.sleep(4)

    def message(self):
        message = self.driver.find_element(*self.MESSAGE_INPUT)
        message.clear()
        message.send_keys("Hello")
        print("Message entered",message.get_attribute("value"))
        time.sleep(4)

    def search(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys("Nishara")
        print("Search entered",search_input.get_attribute("value"))
        time.sleep(4)

    def searchbutton(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        self.driver.execute_script("arguments[0].click();", search_button)
        print("Search button clicked")
        time.sleep(4)
        print("")


    def getbytitle(self):
        print("---- GetByTitle ----")

        getbytitle = self.driver.find_element(*self.GETBYTITLE)
        tag = getbytitle.find_elements(*self.GETBYTITLE_TAG)
        for p in tag:
            print(p.get_attribute("innerText"))
            time.sleep(2)
        print("") 


        getbytitle = self.driver.find_element(*self.GETBYTITLE)
        tag = getbytitle.find_elements(By.TAG_NAME, "li")
        for p in tag:
            print(p.get_attribute("innerText"))
            time.sleep(2)
        print("") 


    def savebutton(self):
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        self.driver.execute_script("arguments[0].click();", save_button)
        print("Save button clicked")
        time.sleep(4)
        print("")


    def getbyTestId(self):
        print("---- GetByTestId ----")

        getbytestid = self.driver.find_element(*self.GETBYTESTID)
        print("GetByTestId is: ", getbytestid.text)
        time.sleep(4)
        print("")


    def editprofile (self):
        print("---- Edit Profile ----")

        editprofile = self.driver.find_element(*self.EDIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", editprofile)
        print("Edit profile clicked")
        time.sleep(4)    
        print("")
        

    def productBoxes (self):
        print("---- Product Boxes ----")

        product_grid = self.driver.find_element(*self.PRODUCT_GRID)
        cards = product_grid.find_elements(By.CLASS_NAME, "card")
        for c in cards:
            print(c.find_element(By.TAG_NAME, "h4").get_attribute("innerText"))
            print(c.find_element(By.TAG_NAME, "p").get_attribute("innerText"))
            time.sleep(2)
        print("")


    def links2 (self):
        print("---- Links ----") 

        links = self.driver.find_element(*self.LINKS)
        links = links.find_elements(By.TAG_NAME, "a")
        for li in links:
            print(li.get_attribute("href"))
            time.sleep(2)
        print("")   


    








