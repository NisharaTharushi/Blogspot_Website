from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Playwright:

    def __init__(self, driver):
        self.driver = driver

    
    # Locators
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
    GETBYPLACEHOLDER = (By.XPATH, "//img[@alt='logo image']")
    GETBYTITLE = (By.ID, "title-locators")
    GETBYTITLE_TAG = (By.TAG_NAME, "P")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    GETBYTESTID = (By.XPATH, "//section[@id='testid-locators']//p[contains(text(),'Locate elements by their')]")
    GETBYTESTID_TAG = (By.TAG_NAME, "P")
    EDIT_BUTTON = (By.XPATH, "//button[normalize-space()='Edit Profile']")
    PRODUCT_GRID = (By.CSS_SELECTOR, "div[data-testid='product-grid']")
    LINKS = (By.XPATH, "//nav[@data-testid='main-navigation']")

    
    print("---- Playwright Page ----")
    
    # Title
    def title(self):
        title = self.driver.find_element(*self.TITLE)
        print("Title is: ", title.text)
        time.sleep(4)
        print("")


    # Sub Title
    def subtitle(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TITLE2))   
        title2 = self.driver.find_element(*self.TITLE2)
        print("sub title is: ", title2.text)
        time.sleep(4)
        print("")


    # Header links
    def header(self):
        print("---- Header Links----")
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
        print("All header links clicked")    
        print("")


    # Playwright
    def playwright_text(self):
        print("---- Playwright Practice ----")
        playwright_text = self.driver.find_element(*self.PLAYWRIGHT_TEXT)
        print("Playwright text is: ", playwright_text.text)
        time.sleep(4)
        print("")

 
    # GetByRole Locators
    def getbyrole(self):
        print("---- GetByRole() Locators ----")
        getbyrole_text = self.driver.find_element(*self.GETBYROLE_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", getbyrole_text)
        print("GetByRole text is: ", getbyrole_text.text)
        time.sleep(4)
        print("")


    # Primary Button
    def primary_button(self):
        primary_button = self.driver.find_element(*self.PRIMARY_BUTTON)
        print("Primary button text is: ", primary_button.text)
        self.driver.execute_script("arguments[0].click();", primary_button)
        print("primary button clicked")
        time.sleep(4)
        print("")


    # Toggle Button
    def toggle_button(self):
        toggle_button = self.driver.find_element(*self.TOGGLE_BUTTON)
        print("Toggle button text is: ", toggle_button.text)
        self.driver.execute_script("arguments[0].click();", toggle_button)
        print("toggle button clicked")
        time.sleep(4)
        print("")


    # Form Username
    def formusername(self, username_input):
        formusername_label = self.driver.find_element(*self.FORMUSERNAME_LABEL)
        print("Form Username label text is: ", formusername_label.text)
        time.sleep(4)
        print("")


    # Username Input
        username = self.driver.find_element(*self.USERNAME_INPUT)
        username.send_keys(username_input)
        print("Username input text is: ", username.get_attribute("value"))
        time.sleep(4)
        print("")


    # Navigation Text
    def navigation_text(self):
        navigation_text = self.driver.find_element(*self.NAVIGATION_TEXT)
        print("Navigation text is: ", navigation_text.text)
        time.sleep(4)
        print("")


    # Navigation All Links
    def nav_all_links(self):
        naviallinks = self.driver.find_element(*self.NAVIALLINKS)
        tagname = naviallinks.find_elements(By.TAG_NAME, "ul")
        for link in tagname:
            print("link is :",link.text)
            link.click()
            time.sleep(3)
            self.driver.get("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        print("")


    # Accept Terms label
    def accept_terms_label(self):
        accept_terms_label = self.driver.find_element(*self.ACCEPT_TERMS_LABEL)
        self.driver.execute_script("arguments[0].click();", accept_terms_label)
        print("Accept terms label clicked and text is: ", accept_terms_label.text)
        time.sleep(4)
        print("")    


    # GetByText Locators
    def getbytext(self):
        print("---- GetByText() Locators ----")
        getbytext_text = self.driver.find_element(*self.GETBYTEXTS)
        self.driver.execute_script("arguments[0].scrollIntoView();", getbytext_text)
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


    # links in List item 2 
    def links(self):
        link = self.driver.find_element(*self.LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", link)
        print("Link text is: ", link.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", link)
        self.driver.execute_script("arguments[0].click();", link)
        print("Link clicked")
        time.sleep(4)  
        print("")


    # Submit Form Button
    def submit_button(self):
        submit_button = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", submit_button)
        print("Submit button clicked")
        time.sleep(2)
        print("")    


    # Get By Label() Locators
    def getByLabel(self, email_input_text, password_input_text, age_input_text):
        print("---- GetByLabel() Locators ----")
        getByLabel = self.driver.find_element(*self.GETBYLABEL)
        print("GetByLabel text is: ", getByLabel.text)
        self.driver.execute_script("arguments[0].scrollIntoView();", getByLabel)
        time.sleep(4)    
        print("")


    # Email
        email_label = self.driver.find_element(*self.EMAIL_LABEL)
        print("Email label text is: ", email_label.text)
        time.sleep(4)
        
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email_input_text)
        print("Email entered: ",email_input.get_attribute("value"))
        time.sleep(4)


    # Password
        password_label = self.driver.find_element(*self.PASSWORD_LABEL)
        print("Password label text is: ", password_label.text)
        time.sleep(4)        

        password = self.driver.find_element(*self.PASSWORD_INPUT)
        password.clear()
        password.send_keys(password_input_text)
        print("Password entered: ",password.get_attribute("value"))
        time.sleep(4)


    # Age
        age_label = self.driver.find_element(*self.AGE_LABEL)
        print("Age label text is: ", age_label.text)
        time.sleep(4)

        age = self.driver.find_element(*self.AGE_INPUT)
        age.clear()
        age.send_keys(age_input_text)
        print("Age entered: ",age.get_attribute("value"))
        time.sleep(4)


    # Shipping
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


    # GetByPlaceholder form
    def getbyplaceholder(self, name_input_text, phonenumber_input_text, message_input_text, search_input_text):
        print("---- GetByPlaceholder() Locators ----")

        getbyplaceholder_text = self.driver.find_element(*self.GETPLACEHOLDER_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", getbyplaceholder_text)
        print("GetByPlaceholder text is: ", getbyplaceholder_text.text)
        time.sleep(4)    
    
        name = self.driver.find_element(*self.FULLNAME_INPUT)
        name.clear()
        name.send_keys(name_input_text)
        print("Name entered: ",name.get_attribute("value"))
        time.sleep(4)

        phonenumber = self.driver.find_element(*self.PHONENUMBER_INPUT)
        phonenumber.clear()
        phonenumber.send_keys(phonenumber_input_text)
        print("Phone number entered: ",phonenumber.get_attribute("value"))
        time.sleep(4)

        message = self.driver.find_element(*self.MESSAGE_INPUT)
        message.clear()
        message.send_keys(message_input_text)
        print("Message entered: ",message.get_attribute("value"))
        time.sleep(4)

        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(search_input_text)
        print("Search entered: ",search_input.get_attribute("value"))
        time.sleep(4)

        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        self.driver.execute_script("arguments[0].click();", search_button)
        print("Search button clicked")
        time.sleep(4)
        print("")


    # GetByAltText() Locators
    def getByAltText(self):
        print("---- GetByAltText() Locators ----")
        getByAltText = self.driver.find_element(*self.GETBYPLACEHOLDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", getByAltText)
        print("GetByAltText is: ", getByAltText.get_attribute("alt"))
        print("")   


    # Get By Title
    def getbytitle(self):
        print("---- GetByTitle() Locators ----")

        getbytitle = self.driver.find_element(*self.GETBYTITLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", getbytitle)
        print("GetByTitle is: ", getbytitle.text)
        time.sleep(2)
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


    # Save button
    def savebutton(self):
        save_button = self.driver.find_element(*self.SAVE_BUTTON)
        self.driver.execute_script("arguments[0].click();", save_button)
        print("Save button clicked")
        time.sleep(2)
        print("")


    # Get by test id
    def getbyTestId(self):
        print("---- GetByTestId() Locators ----")

        getbytestid = self.driver.find_element(*self.GETBYTESTID)
        self.driver.execute_script("arguments[0].scrollIntoView();", getbytestid)
        # print all p elements
        tag = getbytestid.find_elements(By.TAG_NAME, "p")
        for p in tag:
            print(p.get_attribute(tag.get_attribute("innerText")))
            time.sleep(2)
        print("")


    # Edit profile button 
    def editprofile (self):
        editprofile = self.driver.find_element(*self.EDIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", editprofile)
        print("Edit profile clicked")
        time.sleep(4)    
        print("")
        

    # Product Boxes
    def productBoxes (self):
        product_grid = self.driver.find_element(*self.PRODUCT_GRID)
        cards = product_grid.find_elements(By.CLASS_NAME, "card")
        for c in cards:
            print(c.find_element(By.TAG_NAME, "h4").get_attribute("innerText"))
            print(c.find_element(By.TAG_NAME, "p").get_attribute("innerText"))
            time.sleep(2)
        print("")

    
    # Links
    def links2 (self):
        print("---- Links ----") 
        links = self.driver.find_element(*self.LINKS)
        links = links.find_elements(By.TAG_NAME, "a")
        for li in links:
            print(li.get_attribute("href"))
            time.sleep(2)
        print("")   


    








