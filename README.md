## 🔧 Selenium Test Automation for "Blogspot Automation Website ##

# 🌐 Project Overview

This project contains **automated test scripts written in Python using Selenium WebDriver** for the demo website:

🔗 [Test Automation Practice](https://testautomationpractice.blogspot.com/)

**Blogspot Automation Website** is a comprehensive web-based playground for practicing UI test automation. It includes various real-world web components like forms, buttons, alerts, tables, sliders, and more — making it ideal for developing and testing Selenium skills.

---

## ✅ What This Project Covers

I built automated **Python test scripts using the Page Object Model (POM)** design pattern.  
Each script focuses on:

- Functional and UI validations  
- Form field entry, submission, and validations  
- Header, buttons, and links testing  
- Table structure and data verification  
- Alerts, prompts, sliders, and dynamic elements  
- Cross-device responsiveness and accessibility checks  

---

## 📄 Features and Pages Tested

The following pages were automated:

-  Home Page  
-  Online Training Page  
-  Playwright Page  
-  Udemy Page  
-  Blog Page  

Each page has its own Page Object class and corresponding test script.

Each page and feature is handled by dedicated test files and Page Object classes for maximum modularity and maintainability.

---

## 🧰 Tools & Technologies Used

- **Language:** Python 3.x  
- **Automation Tool:** Selenium WebDriver  
- **Testing Framework:** Pytest  
- **Design Pattern:** Page Object Model (POM)  
- **Browser Driver:** ChromeDriver (via `webdriver_manager`)  
- **Execution Platform:** Local (can be integrated with CI like GitHub Actions)

---

## 📁 Project Structure

<pre>
Blogspot-Website/
│
├── pages/
│ ├── Home_page.py
│ ├── Online_training_page.py
│ ├── Playwright_page.py
│ ├── Udemy_page.py
│ └── Blog_page.py
│
├── tests/
│ ├── Home_test.py
│ ├── OnlineTraining_test.py
│ ├── Playwright_test.py
│ ├── Udemy_test.py
│ └── Blog_test.py
│
├── test_cases.md # Manual test case documentation
├── requirements.txt # Python dependencies
├── README.md # Project documentation (this file)
└── .gitignore # Git ignore rules

</pre>

## 🚀 How to Run the Tests

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce-ui-testing.git
   cd ecommerce-ui-testing
