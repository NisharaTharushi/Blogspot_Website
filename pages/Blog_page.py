from selenium.webdriver.common.by import By
import time

class Blog:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    TITLE = (By.TAG_NAME, "title")
    HEADER = (By.ID, "PageList1")
    HEADER_LINKS = (By.TAG_NAME, "li")
    SEARCH = (By.NAME, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "gsc-search-button")
    FOOTER = (By.TAG_NAME, "footer")
    FOOTER_LINKS = (By.CSS_SELECTOR, "footer a")
    BUTTONS = (By.TAG_NAME, "a")


    # print page title
    def print_title(self):
        title = self.driver.title
        print("Page title is:", title)
        return title


    # print all header links
    def print_header_links(self):
        print("Header navigation links:")
        header = self.driver.find_element(*self.HEADER)
        header_links = header.find_elements(*self.HEADER_LINKS)
        for link in header_links:
            print(link.text)
        print("")

    
    # click all header links
    def click_header_links(self):
        print("Clicking all header links...")
        
        header = self.driver.find_element(*self.HEADER)
        links = header.find_elements(*self.HEADER_LINKS)
        hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href")]

        for href in hrefs:
            try:
                self.driver.get(href)
                time.sleep(2)
                print(f"Clicked and opened: {href}")
                self.driver.back()
                time.sleep(2)
            except Exception as e:
                print(f"Failed to open link {href}: {str(e)}")

        print("Finished clicking all header links.\n")
  


    # Page content
    def print_h3_Paragraph(self):
        print("Page content:")
        h3s = self.driver.find_elements(By.TAG_NAME, "h3")
        for h3 in h3s:
            print(" -", h3.text.strip())
        paragraphs = self.driver.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(" -", paragraph.text.strip())
        print("")


    # Search    
    def search(self):
        search_input = self.driver.find_element(*self.SEARCH)
        search_input.clear()
        search_input.send_keys("selenium")
        print("Search entered",search_input.get_attribute("value"))

        # Click the search button
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        self.driver.execute_script("arguments[0].click();", search_button)
        time.sleep(4) 
        print("") 


    # Click all buttons
    def click_all_buttons(self):
        print("🧪 Clicking all buttons on the page...")
        
        # First, find the total number of buttons
        total_buttons = len(self.driver.find_elements(*self.BUTTONS))
        print(f"Found {total_buttons} buttons on the page.")

        for i in range(total_buttons):
            try:
                # Re-locate buttons fresh on each loop to avoid stale element
                buttons = self.driver.find_elements(*self.BUTTONS)
                button = buttons[i]

                if button.is_displayed() and button.is_enabled():
                    print(f"Clicking button #{i + 1} with text: '{button.text}'")
                    button.click()
                    time.sleep(2)
                    print("✅ Button clicked successfully.")
                    self.driver.back()
                    time.sleep(2)
            except Exception as e:
                print(f"❌ Could not click button #{i + 1}: {e}")

        print("✅ Finished clicking all buttons.\n")

    
    # Footer links
    def print_footer_links(self):
        print("Footer links:")
        links = self.driver.find_elements(*self.FOOTER_LINKS)
        for link in links:
            print(link.text.strip(), "->", link.get_attribute("href"))
            print("link clicked")
        print("")

  

