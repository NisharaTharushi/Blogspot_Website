from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
 

class PageName: # Define the HomePage class
    def __init__(self, driver):
        self.driver = driver


    # Lcators
    TITLE = (By.CLASS_NAME, "title")
    HEADER = (By.ID, "PageList2")
    HEADER_LINKS = (By.TAG_NAME, "ul")
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    ADDRESS = (By.ID, "textarea")
    GENDER = (By.ID, "female")
    DAY = (By.ID, "monday")
    COUNTRY = (By.ID, "country")
    COLOUR = (By.ID, "colors")
    ANIMAL = (By.ID, "animals")
    DATEPICKER = (By.ID, "datepicker")
    DATEPICKER2 = (By.ID, "txtDate")
    MONTH_DATEPICKER = (By.CLASS_NAME, "ui-datepicker-month")
    YEAR_DATEPICKER = (By.CLASS_NAME, "ui-datepicker-year")
    CALENDAR = (By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
    DATEPICKER3 = (By.ID, "17")
    SUBMIT = (By.CLASS_NAME, "submit-btn")
    START_DATE = (By.ID, "start-date")
    END_DATE = (By.ID, "end-date")
    SEVENTEEN = (By.ID, "17")
    SUBMIT_BUTTON = (By.CLASS_NAME, "submit-btn")
    BLOGSPOT = (By.XPATH, "//a[@href='https://testautomationpractice.blogspot.com/feeds/posts/default']")
    SINGLE_BROWSE = (By.ID, "singleFileInput")
    MULTIPLE_BROWSE = (By.ID, "multipleFilesInput")
    STATIC_TABLE =(By.ID, "HTML1")
    DYNAMIC_TABLE = (By.ID, "taskTable")
    PAGINATION_TABLE = (By.ID, "productTable")
    PEGINATE_BUTTON = (By.CLASS_NAME, "pagination")
    PEGINATE_BUTTON2 = (By.LINK_TEXT, "2")
    PAGINATE_CHECKBOX = (By.XPATH, ".//input[@type='checkbox']")
    FORM = (By.ID, "HTML6")
    SECTION1 = (By.XPATH, "//h4[normalize-space()='Section 1']")
    INPUT1 = (By.ID, "input1")
    SUBMIT1 = (By.ID, "btn1")
    INPUT2 = (By.ID, "input2")
    SUBMIT2 = (By.ID, "btn2")
    INPUT3 = (By.ID, "input3")
    SUBMIT3 = (By.ID, "btn3")
    TABS = (By.ID, "Wikipedia1_wikipedia-search-input")
    SHADOW_DOM = (By.ID, "HTML16")
    MOUSEOVER = (By.XPATH, "//h2[normalize-space()='Mouse Hover']") 
    FOOTER = (By.ID, "footer-2-1")
    FOOTER_LINKS = (By.TAG_NAME, "ul")
    TAB_TEXT = (By.CLASS_NAME, "title")
    TAB_INPUT =(By.ID, "Wikipedia1_wikipedia-search-input")
    TAB_SUBMIT = (By.XPATH, "//input[@type='submit']")
    DYNAMIC_BUTTON_TEXT =(By.XPATH, "//h2[normalize-space()='Dynamic Button']")
    DYNAMIC_BUTTON = (By.XPATH, "//button[normalize-space()='START']")
    ALERT_TEXT = (By.XPATH, "//h2[normalize-space()='Alerts & Popups']")
    ALERT_BUTTON = (By.ID, "alertBtn") 
    CONFIRM_BUTTON = (By.ID, "confirmBtn")
    PROMPT_BUTTON = (By.ID, "promptBtn")
    NEW_TAB_BUTTON = (By.XPATH, "//button[normalize-space()='New Tab']")
    POPUP_BUTTON = (By.ID, "PopUp")
    MOUSEOVER_TEXT = (By.XPATH, "//h2[normalize-space()='Mouse Hover']")
    MOUSEOVER_BUTTON = (By.XPATH, "//button[normalize-space()='Point Me']")
    DOUBLECLICK_BUTTON = (By.ID , "field1")
    DRAG = (By.ID, "draggable")
    DROP = (By.ID, "droppable")
    SLIDER = (By.CSS_SELECTOR, "#slider-range span")
    MOBILE_LABELS = (By.XPATH,"//h4[normalize-space()='Mobile Labels']")
    SAMSUNG_LABEL = (By.ID, "samsung")
    REALME_LABEL = (By.ID, "realme")  
    LAPTOP_LINKS = (By.XPATH,"//h4[normalize-space()='Laptop Links']")
    APPLE_LINK = (By.ID, "apple")
    LENOVO_LINK = (By.ID, "lenovo")
    BROCKEN_LINK_400 = (By.LINK_TEXT, "Errorcode 400")
    BROCKEN_LINK_404 = (By.LINK_TEXT, "Errorcode 404") 
    SHADOW_DOM_TEXT = (By.XPATH, "//h2[normalize-space()='ShadowDOM']")
    BLOG_LINK = (By.CSS_SELECTOR, "a[href='https://www.pavantestingtools.com/']")
    BROWSE_BUTTON = (By.CSS_SELECTOR, "input[type='file']")
    YOUTUBE_LINK = (By.XPATH, "//a[normalize-space()='Youtube']")
 
    
    # Title
    def title(self):
        print("---- Home Page ----")
        title = self.driver.find_element(*PageName.TITLE)
        title_text = title.text
        print("Title is: ", title_text)

        expected_title = "Automation Testing Practice"
        if title_text == expected_title:    
            print("✅ Title text is correct.")
        else:
            print(f"❌ Title text is Failed: Expected '{expected_title}', but got '{title_text}'.")
        print("")
    
   
    # Logo
    def logo (self):
        print("---- Logo ----")
        logo = self.driver.find_element(*PageName.LOGO)
        logo_text = logo.text
        print("Logo is: ", logo_text)


    # Header links
    def header_links(self):
        print("---- Header links ----")
        header = self.driver.find_element(*PageName.HEADER)
        header_links = header.find_elements(*PageName.HEADER_LINKS)
        for link in header_links:
            print(link.text)
        print("\n")

    
    # go back 
    def go_back(self):
        self.driver.back()
        print("\n")
       

    # Form 1
    def form1(self, name_input, email_input, phone_input, address_input,country_input,colour_input,animal_input,date_input):
        print("---- Form 1 ----")
        
        name = self.driver.find_element(By.ID, "name")
        name.clear()
        name.send_keys(name_input)
        print("Name entered",name_input)


        email = self.driver.find_element(*PageName.EMAIL)
        email.clear()
        email.send_keys(email_input)
        print("Email entered",email_input)


        phone = self.driver.find_element(*PageName.PHONE)
        phone.clear()
        phone.send_keys(phone_input)
        print("Phone number entered",phone_input)


        address = self.driver.find_element(*PageName.ADDRESS)
        address.clear()
        address.send_keys(address_input)
        print("Address entered",address_input)

    
        gender = self.driver.find_element(*PageName.GENDER)
        gender.click()
        get_attribute = gender.get_attribute("value")
        print("Gender entered",get_attribute)
        

        day = self.driver.find_element(*PageName.DAY)
        self.driver.execute_script("arguments[0].click();", day)
        get_attribute = day.get_attribute("value")
        print("Day entered",get_attribute)
        

        country = self.driver.find_element(*PageName.COUNTRY)
        country.click()
        option = Select(country)
        option.select_by_visible_text(country_input)
        get_attribute = country.get_attribute("value")
        print("Country entered",get_attribute)


        colour = self.driver.find_element(*PageName.COLOUR)
        colour.click()
        option = Select(colour)
        option.select_by_visible_text(colour_input)
        get_attribute = colour.get_attribute("value")
        print("Colour entered",get_attribute)


        animal = self.driver.find_element(*PageName.ANIMAL)
        self.driver.execute_script("arguments[0].scrollIntoView();", animal)
        self.driver.execute_script("arguments[0].click();", animal)
        time.sleep(2)
        option = Select(animal)
        option.select_by_visible_text(animal_input)
        get_attribute = animal.get_attribute("value")
        print("Animal entered",get_attribute)


    # Date picker
        date = self.driver.find_element(*PageName.DATEPICKER)
        self.driver.execute_script("arguments[0].scrollIntoView();", date)
        date.clear()
        date.send_keys(date_input)
        print("Date entered",date_input)
        
        get_attribute = date.get_attribute("value")
        print("Date entered",get_attribute)
        print("✅ Form 1 completed.")
        print("")        

    
    # Links
    def links(self):
        print("---- Blogspot link ----")
        link1 = self.driver.find_element(*PageName.BLOGSPOT)
        self.driver.execute_script("arguments[0].scrollIntoView();", link1)
        self.driver.execute_script("arguments[0].click();", link1)  
        print("Blogspot link clicked")
        time.sleep(2)        

        link_input = link1.get_attribute("href")
        print("Blogpost page open and URL is :", link_input)

        # print the current page URL
        actual_url = "https://testautomationpractice.blogspot.com/feeds/posts/default"
        if link_input == actual_url:
            print("✅ blogspot Link Clicked. Correct page opened.")
        else:
            print(f"❌  Failed: Expected '{actual_url}', but got '{link_input}'.")
        print("")


    # Upload file
    def upload_file(self, file_path_1):
        print("---- Upload single file ----")
        single_browse = self.driver.find_element(*PageName.SINGLE_BROWSE)

        # Scroll to file upload element using JavaScript 
        self.driver.execute_script("arguments[0].scrollIntoView();", single_browse)
        self.driver.execute_script("arguments[0].click();", single_browse)
        print("✅ Browse button clicked")

        # Upload a file from your PC
        single_browse.send_keys(file_path_1)  # ✅ Use raw string or double slashes
        print("✅ File selected")

        # find upload button and click
        single_button = self.driver.find_element(By.XPATH, "//button[text()='Upload Single File']")
        self.driver.execute_script("arguments[0].click();", single_button)
        print("✅ File uploaded")
        print("")    
        time.sleep(4)


    # Upload multiple files 
    def Upload_files_multiple(self, file_1, file_2):
        print("---- Upload multiple files ----")
        browse = self.driver.find_element(*PageName.MULTIPLE_BROWSE)
        self.driver.execute_script("arguments[0].scrollIntoView();", browse)
        self.driver.execute_script("arguments[0].click();", browse)
        print("✅ Browse button clicked")
        time.sleep(2)

        browse.send_keys(file_2)
        browse.send_keys(file_1)
        print("✅ File selected")
        time.sleep(2)

        upload = self.driver.find_element(By.XPATH, "//button[normalize-space()='Upload Multiple Files']")
        self.driver.execute_script("arguments[0].click();", upload) #upload.click()
        print("✅ Files uploaded")
        print("")
        time.sleep(4)
   

    # Static web table
    def static_web_table(self):
        print("---- Static web table ----")

        table = self.driver.find_element(*PageName.STATIC_TABLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", table)  
        time.sleep(2)

        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows: 
            cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
            for cell in cells: 
                 print(cell.text, end=" | ")             
            print("")
        print("")
        time.sleep(4)


    # Dynamic web table 
    def dynamic_web_table(self):
        print("---- Dynamic web table ----")
        table = self.driver.find_element(*PageName.DYNAMIC_TABLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", table)  
        
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows: 
            cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
            for cell in cells: 
                 print(cell.text, end=" | ")
            print("")
        print("")
        time.sleep(4)


    # Pagination Web Table
    def pagination_web_table(self):
        print("---- Pagination web table ----")
        table = self.driver.find_element(*PageName.PAGINATION_TABLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", table)  
        
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows: 
            cells = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
            for cell in cells: 
                 print(cell.text, end=" | ")
            print("")        
        print("")
        time.sleep(4)

     
        # find peginate button 
        self.driver.find_element(*PageName.PEGINATE_BUTTON).click()
        print("Peginate button 1 clicked")
        self.driver.find_element(*PageName.PEGINATE_BUTTON2).click()
        print("Peginate buttons 2 clicked")
        print("")
        time.sleep(2)


    # Checkbox
    def checkbox(self):
        print("---- Checkboxes ----")
        # find the productTable element by its ID
        productTable = self.driver.find_element(*PageName.PAGINATE_CHECKBOX)
        # Scroll to the productTable element
        self.driver.execute_script("arguments[0].scrollIntoView();", productTable)
        time.sleep(2)   

        # find all checkboxes in the productTable
        checkboxes = productTable.find_elements(*PageName.PAGINATE_CHECKBOX)
        # Iterate through each checkbox and print its state
        for checkbox in checkboxes:
            checkbox.click()  # Click the checkbox to select it
            print(f"Checkbox state: {checkbox.is_selected()}")  # Print the state of the checkbox

            time.sleep(2)  # Just for demonstration, not recommended in production code
        print("✅ All checkboxes are selected.")
        print("")


    # Form 3
    def form_3(self, input_element1_text, input_element2_text, input_element3_text):
        print("---- Form 3 ----")
        form_element = self.driver.find_element(*PageName.FORM)
        #scroll to the form element
        self.driver.execute_script("arguments[0].scrollIntoView();", form_element)
        time.sleep(2)

    # input element 1
        input_element1 = self.driver.find_element(*PageName.INPUT1)
        input_element1.send_keys(input_element1_text)  # Enter text into the input field
        print("✅ Input field entered",input_element1.get_attribute("value"))
        time.sleep(2)

    # click SUBMIT button 1 
        self.driver.find_element(*PageName.SUBMIT1).click() 
        print("✅ Button 1 clicked")
        time.sleep(2)  
        print("")

    # input element 2
        input_element = self.driver.find_element(*PageName.INPUT2)
        input_element.send_keys(input_element2_text)  # Enter text into the input field
        print("✅ Input field 2 entered",input_element.get_attribute("value"))
        time.sleep(2)

    # click SUBMIT button 2
        self.driver.find_element(*PageName.SUBMIT2).click()
        print("✅ Button 2 clicked") 
        time.sleep(2) 
        print("")

    # find 3rd input element
        input_element = self.driver.find_element(*PageName.INPUT3)
        input_element.send_keys(input_element3_text)  # Enter text into the input field
        print("✅ Input field 3 entered",input_element.get_attribute("value"))
        time.sleep(2)

        # click SUBMIT button 3
        self.driver.find_element(*PageName.SUBMIT3).click()
        print("✅ Button 3 clicked")
        time.sleep(2)
        print("")



    # footer links 
    def footer_links(self):
        print("---- Footer links ----")
        footer = self.driver.find_element(*PageName.FOOTER)
        self.driver.execute_script("arguments[0].scrollIntoView();", footer)
        time.sleep(2)

        # get links inside footer
        footer_links = footer.find_elements(*PageName.FOOTER_LINKS)
        for link in footer_links:
            print(link.text)
            self.driver.back()
            time.sleep(2)
        print("")


    # Tabs 
    def tabs(self):
        print("Tabs")
        # tab text 
        tabs = self.driver.find_element(*PageName.TABS)
        self.driver.execute_script("arguments[0].scrollIntoView();", tabs)
        print("Tabs label is",tabs.get_attribute("innerHTML"))
        print("")
        time.sleep(2)


    # Search input
    def search_input(self,search_text):
        Search = self.driver.find_element(*PageName.TAB_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", Search)
        time.sleep(2)
        Search.send_keys(search_text)
        print("✅ Search field entered",Search.get_attribute("value"))
        time.sleep(2)


    # Submit search button 
    def submit_search(self):
        submit = self.driver.find_element(*PageName.TAB_SUBMIT)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        self.driver.execute_script("arguments[0].click();", submit)
        print("✅ Search submit button clicked")
        print("")


    # Dynamic Button
    def Dynamic_Button(self):
        print("---- Dynamic Button ----")
        Dynamic_Button = self.driver.find_element(*PageName.DYNAMIC_BUTTON_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", Dynamic_Button)
        print("Dynamic Button label text is:",Dynamic_Button.text)

        button = self.driver.find_element(*PageName.DYNAMIC_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)
        print("✅ Dynamic Button clicked")
        time.sleep(2)
        print("")


    # Alerts and Popups
    def Alert_button(self):
        print("---- Alert & Popups ----")
        alert = self.driver.find_element(*PageName.ALERT_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", alert)
        print("Alert label text is: ",alert.text)
        print("")

        button = self.driver.find_element(*PageName.ALERT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)
        print("✅ Alert Button clicked")
        time.sleep(2)

        # accept Alert
        alert = self.driver.switch_to.alert
        alert.accept()
        print("✅ alert accepted")
        time.sleep(2)
        print("")


    # Confirm button 
    def Confirm_button(self):
        confirm = self.driver.find_element(*PageName.CONFIRM_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", confirm)
        self.driver.execute_script("arguments[0].click();", confirm)
        print("✅ Confirm Button clicked")
        time.sleep(2)

        # accept alert
        alert = self.driver.switch_to.alert
        alert.accept()
        print("✅ alert accepted")
        time.sleep(2)
        print("")

    
    # Prompt
    def Prompt_button(self):
        prompt = self.driver.find_element(*PageName.PROMPT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", prompt)
        self.driver.execute_script("arguments[0].click();", prompt)
        print("✅ prompt Button clicked")
        time.sleep(2)

        # accept alert
        alert = self.driver.switch_to.alert
        alert.accept()
        print("✅ alert accepted")
        time.sleep(2)
        print("")

    
    # New tab
    def NewTab(self):
        print("---- New Tab ----")
        NewTab = self.driver.find_element(*PageName.NEW_TAB_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", NewTab)
        self.driver.execute_script("arguments[0].click();", NewTab)
        print("✅ NewTab Button clicked")
        self.driver.back()
        time.sleep(2)
        print("")

    
    # Popup
    def Popup(self):
        Popup = self.driver.find_element(*PageName.POPUP_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", Popup)
        self.driver.execute_script("arguments[0].click();", Popup)
        print("✅ Popup Button clicked")
        self.driver.back()
        time.sleep(2)
        self.driver.back()
        print("")


    # Mouse over
    def MouseOver(self):
        print("---- MouseOver ----")
        MouseOver = self.driver.find_element(*PageName.MOUSEOVER_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", MouseOver)
        print("MouseOver label text is:",MouseOver.text)

        
        button = self.driver.find_element(*PageName.MOUSEOVER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        ActionChains(self.driver).move_to_element(button).perform()
        print("✅ Point Me Button hovered")
        time.sleep(2)

        # Select Mobiles by visisble text
        select = self.driver.find_element(By.LINK_TEXT, "Mobiles")
        select.click()
        print("✅ Mobiles clicked")
        time.sleep(2)
        print("")


    # Double click
    def DoubleClick(self,input_text):
        print("---- Double Click ----")
        DoubleClick = self.driver.find_element(*PageName.DOUBLECLICK_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", DoubleClick)
        time.sleep(2)

       # clear the first text field
        DoubleClick.clear()

        # send text to the first text field
        DoubleClick.send_keys(input_text)
        time.sleep(2)

        # get the value of the first text field
        value = DoubleClick.get_attribute("value")
        print("✅ Double Click Button Clicked and Value of the first text field:", value)
        print("")



    # Drag and Drop
    def DragAndDrop(self):
        print("---- Drag and Drop ----")
        Drag = self.driver.find_element(*PageName.DRAG)
        Drop = self.driver.find_element(*PageName.DROP)
        self.driver.execute_script("arguments[0].scrollIntoView();", Drag)
        self.driver.execute_script("arguments[0].scrollIntoView();", Drop)
        ActionChains(self.driver).drag_and_drop(Drag, Drop).perform()
        time.sleep(2)
        print("✅ Drag and Drop done")
        print("")


    # Slider 
    def Slider(self):
        Slider = self.driver.find_element(*PageName.SLIDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", Slider)

        ActionChains(self.driver).click_and_hold(Slider).perform()
        time.sleep(2)
        ActionChains(self.driver).move_by_offset(100, 0).perform()
        time.sleep(2)
        ActionChains(self.driver).release().perform()
        time.sleep(2)
        print("✅ Slider moved")
        

        # Get the value of the slider after moving it
        value = self.driver.find_element(By.ID, "amount").get_attribute("value") 
        print("✅ Slider value after moving:", value)
        time.sleep(2)
        print("")



    # Labels 
    def Labels(self):
        print("---- Labels ----")
        
        # Mobile labels
        label = self.driver.find_element(*PageName.MOBILE_LABELS)
        print("Mobile labels",label.text)
        time.sleep(2)


        Label = self.driver.find_element(*PageName.SAMSUNG_LABEL)
        check = Label.get_attribute("innerText")
        print("Samsung Label text",check)
        time.sleep(2)

        RealMe = self.driver.find_element(*PageName.REALME_LABEL)
        check = RealMe.get_attribute("innerText")
        print("RealMe Label text",check)
        print("")
        time.sleep(2)


    # Laptops Links
    def laptops(self):
        print("---- Laptops Links ----")
        Laptops = self.driver.find_element(*PageName.LAPTOP_LINKS)
        print("Laptops Link is: ",Laptops.text)


        apple = self.driver.find_element(*PageName.APPLE_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", apple)
        self.driver.execute_script("arguments[0].click();", apple)
        print("✅ Apple Laptops clicked")
        self.driver.get("https://testautomationpractice.blogspot.com/")
        time.sleep(2)

        lenovo = self.driver.find_element(*PageName.LENOVO_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", lenovo)
        self.driver.execute_script("arguments[0].click();", lenovo)
        print("✅ Lenovo Laptops clicked")
        self.driver.get("https://testautomationpractice.blogspot.com/")
        print("")
        time.sleep(2)



    # Broken links
    def broken_links(self):
        print("---- Broken Links ----")

        self.driver.find_element(*PageName.BROCKEN_LINK_400).click()
        time.sleep(2)

        if "Bad Request" in self.driver.page_source:
             print("✅ 400 Error page displayed.")
        else:
             print("❌ 400 Error page not displayed.")
        self.driver.back()


        self.driver.find_element(*PageName.BROCKEN_LINK_404).click()
        time.sleep(2)

        if "404 - File or directory not found." in self.driver.page_source:
             print("✅ 404 Error page displayed.")
        else:
             print("❌ 404 Error page not displayed.")
        self.driver.back()
        print("")


    # Shadow DOM
    def shadow_dom(self):
        print("---- Shadow DOM ----")
        Shadow = self.driver.find_element(*PageName.SHADOW_DOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", Shadow)
        print("Shadow DOM found and text is",Shadow.text)
        print("")

    
    def mobile_labels(self):
        print("---- Mobile labels ----")
        
        # Mobiles link
        mobiles = self.driver.find_element(By.CSS_SELECTOR, ".info")
        print("Mobiles link text",mobiles.text)
        time.sleep(4)

        # laptop 
        laptop = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1)")
        print("Laptops link text",laptop.text)
        time.sleep(4)
        print("")


    # click on blog link
    def click_blog_link(self):
        blog = self.driver.find_element(*PageName.BLOG_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", blog)
        self.driver.execute_script("arguments[0].click();", blog)
        print("✅ Blog link clicked")
        self.driver.back()
        time.sleep(2)
        print("")

    
    # Upload file
    def upload_file2(self, file_path):
        browse = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        self.driver.execute_script("arguments[0].scrollIntoView();", browse)
        self.driver.execute_script("arguments[0].click();", browse)
        time.sleep(4)
        browse.send_keys(file_path)
        print("✅ File uploaded")
        time.sleep(2)
        print("")


    # Click on Youtube link
    def click_youtube_link(self):
        youtube = self.driver.find_element(*PageName.YOUTUBE_LINK)
        self.driver.execute_script("arguments[0].scrollIntoView();", youtube)
        self.driver.execute_script("arguments[0].click();", youtube)
        print("✅ Youtube link clicked")


    
