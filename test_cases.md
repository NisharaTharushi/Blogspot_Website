### Test Cases - General Website Behavior

| Test Case ID | Test Case Description                  | Test Steps                                              | Expected Result                                          |
|--------------|-----------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| TC-01        | Verify homepage loads successfully      | Open the URL https://testautomationpractice.blogspot.com/ | Page loads without errors                                |
| TC-02        | Verify page title                       | Open the URL                                             | Page title is correct (e.g., "Test Automation Practice") |
| TC-03        | Verify all main elements are visible    | Check presence of header, form, input fields, buttons, etc. | All main UI elements are displayed correctly             |
| TC-04        | Verify the website is responsive        | Open website on desktop, tablet, and mobile devices      | Website adjusts layout properly without overlapping or cutoff |

---

### Test Cases - Header Section

| Test Case ID | Test Case Description                              | Test Steps                               | Expected Result                                                |
|--------------|-----------------------------------------------------|------------------------------------------|----------------------------------------------------------------|
| HDR-01       | Verify header is visible on page load               | Open the website                          | Header section is visible at the top                          |
| HDR-02       | Verify logo is present in header                    | Check top-left area of header             | Logo is present and correctly displayed                       |
| HDR-03       | Verify logo redirects to home on click              | Click on the logo                         | User is redirected to the homepage                            |
| HDR-04       | Verify blog title is displayed                      | Observe header text                       | Correct blog title is shown (e.g., “Automation Practice”)     |
| HDR-05       | Verify header links are displayed                   | Inspect the header for navigation or social links | Links are visible and accessible                      |
| HDR-06       | Verify navigation menu is present (if any)          | Look for menu items in header             | Navigation menu items are visible                             |
| HDR-07       | Verify hover effect on header links                 | Hover on each link                        | Color or style changes to indicate hover                      |
| HDR-08       | Verify header is fixed/sticky (if applicable)       | Scroll down the page                      | Header remains at top (if sticky), else scrolls away          |
| HDR-09       | Verify accessibility attributes in header           | Inspect elements (e.g., using dev tools)  | Elements contain ARIA roles/labels                            |
| HDR-10       | Verify responsiveness of header on different screen sizes | Resize browser or use developer tools | Header and its elements adjust responsively                   |
| HDR-11       | Verify social media icons are visible and clickable | Click on social icons                     | Redirects to the correct social page                          |
| HDR-12       | Verify page title in browser tab matches blog name  | Check browser tab                         | Correct title is displayed (e.g., “Automation Testing Practice Site”) |

---

### Test Cases - Form Inputs and Validation

| Test Case ID | Test Case Description                             | Test Steps                                        | Expected Result                                      |
|--------------|----------------------------------------------------|--------------------------------------------------|------------------------------------------------------|
| Form_01      | Verify name input field is present                | Locate name input field                          | Name input field is displayed and editable           |
| Form_02      | Verify email input field is present               | Locate email input field                         | Email input field is displayed and editable          |
| Form_03      | Verify entering valid name                        | Enter valid characters in name input             | Text appears correctly in the input field            |
| Form_04      | Verify entering invalid characters                | Enter special characters in name input (if restricted) | Proper validation error or accepts based on requirements |
| Form_05      | Verify entering valid email                       | Enter a valid email format (e.g., test@example.com) | Email accepted without error                         |
| Form_06      | Verify entering invalid email                     | Enter invalid email (e.g., test@com)             | Validation error message displayed                   |
| Form_07      | Verify input fields clear after reset             | Fill inputs and click Reset button               | All input fields clear to blank                      |

---

### Test Cases - Dropdown Functionality

| Test Case ID | Test Case Description                  | Test Steps                              | Expected Result                             |
|--------------|-----------------------------------------|------------------------------------------|---------------------------------------------|
| Form_08      | Verify dropdown is displayed           | Locate dropdown menu                      | Dropdown visible and clickable              |
| Form_09      | Verify dropdown default option         | Open dropdown                             | Default option selected is as expected      |
| Form_10      | Verify selecting an option             | Select each dropdown option one by one    | Selected option appears and registers correctly |
| Form_11      | Verify invalid selection handling      | Attempt invalid selection if possible     | Invalid selections are not accepted or prompt error |

---

### Test Cases - Checkbox Functionality

| Test Case ID | Test Case Description                       | Test Steps                        | Expected Result                              |
|--------------|----------------------------------------------|-----------------------------------|----------------------------------------------|
| Form_12      | Verify checkboxes are visible                | Locate all checkboxes on the page | Checkboxes are displayed                     |
| Form_13      | Verify checkbox can be checked               | Click on each checkbox            | Checkbox state changes to checked            |
| Form_14      | Verify checkbox can be unchecked             | Click again on checked checkbox   | Checkbox state changes to unchecked          |
| Form_15      | Verify multiple checkboxes can be checked    | Select multiple checkboxes        | All selected checkboxes remain checked       |
| Form_16      | Verify checkboxes clear on Reset             | Check boxes and click Reset       | All checkboxes get unchecked                 |

---

### Test Cases - Radio Button Functionality

| Test Case ID | Test Case Description                        | Test Steps                                      | Expected Result                                |
|--------------|-----------------------------------------------|--------------------------------------------------|------------------------------------------------|
| Form_17      | Verify radio buttons are displayed           | Locate all radio buttons                         | Radio buttons are visible                      |
| Form_18      | Verify only one radio button selectable      | Select one radio button, then another            | Only one radio button remains selected         |
| Form_19      | Verify default selected radio button         | Check which radio button is pre-selected         | Default radio button is selected or none       |
| Form_20      | Verify radio buttons reset on Reset          | Select any radio button and click Reset          | All radio buttons get deselected or default selected |

---

### Test Cases - Buttons & Form Actions

| Test Case ID | Test Case Description                        | Test Steps                                        | Expected Result                                      |
|--------------|-----------------------------------------------|--------------------------------------------------|------------------------------------------------------|
| Form_21      | Verify Submit button is visible              | Locate the submit button                         | Submit button is visible and clickable               |
| Form_22      | Verify Reset button is visible               | Locate the reset button                          | Reset button is visible and clickable                |
| Form_23      | Verify clicking Submit without filling required fields | Click Submit with empty mandatory fields | Proper validation messages are shown         |
| Form_24      | Verify clicking Submit with valid data       | Fill form correctly and click Submit             | Form submits successfully, confirmation message shown |
| Form_25      | Verify clicking Reset clears form            | Fill the form, click Reset                       | All input fields, checkboxes, radio buttons, dropdowns reset |
| Form_26      | Verify required fields validation            | Submit form without filling mandatory fields     | Error messages shown for required fields             |
| Form_27      | Verify email format validation               | Enter invalid email and submit form              | Validation error message displayed                   |
| Form_28      | Verify number input validation               | Enter alphabets in phone number field (if any)   | Validation error shown or input blocked              |
| Form_29      | Verify character limit in text fields        | Enter more characters than allowed               | Input restricted or error message shown              |
| Form_30      | Verify all hyperlinks on page         | Click all links present on the homepage  | Links open correct pages in new or same tab |
| Form_31      | Verify clicking Home link reloads homepage | Click Home or logo link               | Page reloads homepage without errors        |

---

### Test Cases - File Upload

| Test Case ID | Test Case Description                         | Test Steps                                                        | Expected Result                                    |
|--------------|------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------|
| UPL-01       | Verify file upload button is visible          | Locate the file upload input/button                              | File upload input/button is displayed and enabled  |
| UPL-02       | Verify file upload dialog opens               | Click on the upload button                                       | File selection dialog opens                        |
| UPL-03       | Verify upload of a valid file                 | Select and upload a supported file type (e.g., .jpg, .png, .pdf) | File uploads successfully without errors           |
| UPL-04       | Verify upload of unsupported file             | Select a file with unsupported extension (e.g., .exe)            | Error message or file rejection                    |
| UPL-05       | Verify upload of large file                   | Select a file exceeding max allowed size (if limit exists)       | Upload rejected or warning/error displayed         |
| UPL-06       | Verify file name display after upload         | Upload a file and observe the file name display                  | Correct file name displayed                        |
| UPL-07       | Verify multiple file uploads (if allowed)     | Attempt to upload multiple files at once                         | Multiple files uploaded or appropriate message shown |
| UPL-08       | Verify reset or clear file upload             | Upload a file and then reset/clear                               | File selection cleared                             |
| UPL-09       | Verify cancel upload functionality            | Cancel file selection in dialog                                  | Upload is cancelled, no file selected              |
| UPL-10       | Verify upload button disabled after upload    | Upload file and check button state                               | Upload button disabled/enabled as per design       |

---

### Test Cases - Static Web Table

| Test Case ID | Test Case Description                        | Test Steps                              | Expected Result                                      |
|--------------|-----------------------------------------------|------------------------------------------|------------------------------------------------------|
| ST-01        | Verify static web table presence             | Locate the static web table              | Static table is displayed                            |
| ST-02        | Verify number of rows in table               | Count table rows                         | Rows count matches expected number                   |
| ST-03        | Verify number of columns in table            | Count table columns                      | Columns count matches expected number                |
| ST-04        | Verify headers of the table                  | Check all table header names             | Headers are correct and properly labeled             |
| ST-05        | Verify data in each cell is visible          | Inspect each cell content                | Cell data is displayed fully and legibly             |
| ST-06        | Verify data correctness in table             | Validate data content matches expected   | Data matches expected values                         |
| ST-07        | Verify table does not allow editing          | Try to edit any cell                     | Cells are non-editable                               |
| ST-08        | Verify table scroll behavior (if overflow)   | Scroll table vertically/horizontally     | Table scrolls properly without UI glitches           |
| ST-09        | Verify alignment of text in cells            | Check alignment of text (left, center, right) | Text aligned as per design                      |
| ST-10        | Verify presence of links/buttons in table    | Click any link/button inside table       | Links/buttons work correctly and navigate/respond    |
| ST-11        | Verify table responsiveness on screen sizes  | Resize browser/device                    | Table adjusts layout properly or scroll appears      |
| ST-12        | Verify sorting functionality (if applicable) | Click column headers to sort             | Table sorts data ascending/descending                |
| ST-13        | Verify pagination functionality (if applicable) | Navigate through pages                | Table loads correct data for each page               |

---

### Test Cases - Date Picker

| Test Case ID | Test Case Description                             | Test Steps                                            | Expected Result                                     |
|--------------|----------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| DATE-01      | Verify date picker input field is visible          | Check if the date input box is present and enabled    | Date input field is visible and enabled             |
| DATE-02      | Verify date picker icon is visible                 | Check if the calendar icon is displayed next to input | Calendar icon is displayed                          |
| DATE-03      | Verify clicking input field opens date picker      | Click on the date input field                         | Calendar widget should appear                       |
| DATE-04      | Verify clicking calendar icon opens picker         | Click on the calendar icon                            | Calendar widget should appear                       |
| DATE-05      | Verify accessibility via keyboard                  | Press Tab and Enter to open calendar                  | Calendar widget opens using keyboard                |
| DATE-06      | Select a valid date from calendar                  | Click on a valid date in the calendar                 | Date appears correctly in the input field           |
| DATE-07      | Select today's date                                | Click on today’s date in the calendar                 | Today’s date is selected and shown                  |
| DATE-08      | Select future date                                 | Choose a future date from calendar                    | Future date is accepted and filled in input         |
| DATE-09      | Select past date                                   | Choose a past date from calendar                      | Past date is accepted and shown in input            |
| DATE-10      | Select end-of-month date                           | Select 30th or 31st (if applicable)                   | Correct date is selected                            |
| DATE-11      | Navigate to next month                             | Click “Next” arrow in calendar                        | Calendar moves to next month                        |
| DATE-12      | Navigate to previous month                         | Click “Previous” arrow in calendar                    | Calendar moves to previous month                    |
| DATE-13      | Navigate to specific year                          | Use year dropdown or arrows to change year            | Year changes as expected                            |
| DATE-14      | Verify calendar closes on date selection           | Select a date from calendar                           | Calendar closes after selecting a date              |
| DATE-15      | Verify calendar closes on outside click            | Click outside the calendar popup                      | Calendar popup disappears                           |
| DATE-16      | Manually type a valid date                         | Enter date manually in correct format (e.g., mm/dd/yyyy) | Date is accepted and displayed correctly          |
| DATE-17      | Enter invalid date format                          | Type invalid format (e.g., 32/13/2023)                | Validation message shown or input rejected          |
| DATE-18      | Leave date field empty and submit                  | Leave field blank and click Submit (if validation present) | Error message shown or accepted based on rules  |
| DATE-19      | Enter alphanumeric characters                      | Type "abc123" in the date field                       | Input rejected or cleared                           |
| DATE-20      | Check date format validation                       | Enter date in different formats (e.g., dd-mm-yyyy)    | Field accepts or rejects based on config            |
| DATE-21      | Select leap year date                              | Navigate to February 29 of a leap year                | Date should be selectable                           |
| DATE-22      | Select non-leap year Feb 29                        | Navigate to Feb 2023 and try to select Feb 29         | Feb 29 not available or throws error                |
| DATE-23      | Select date from minimum range (if restricted)     | Navigate to the earliest selectable date              | Only allowed dates should be selectable             |
| DATE-24      | Select date from maximum range (if restricted)     | Navigate to the latest allowed date                   | Dates beyond max range should be disabled           |
| DATE-25      | Enter date far in the past or future manually      | Enter 01/01/1800 or 01/01/3000 in input               | Input accepted or error shown as per rules          |
| DATE-26      | Verify placeholder text                            | Check if input shows placeholder (e.g., “MM/DD/YYYY”) | Placeholder text visible                            |
| DATE-27      | Verify calendar widget design                      | Check that calendar layout is aligned and responsive  | All calendar parts are properly displayed           |
| DATE-28      | Verify calendar on mobile devices                  | Open site on mobile and test date picker              | Calendar adapts to mobile screen properly           |

| DATE-29      | Verify readonly behavior (if input is readonly) | Try typing into readonly field  | Manual input not allowed, only calendar selection             |
| DATE-30      | Verify tooltip/help text (if available)     | Hover over calendar icon           | Tooltip/help info shown                                       |

---

### Test Cases - Dynamic Web Table

| Test Case ID | Test Case Description                       | Test Steps                                             | Expected Result                                     |
|--------------|----------------------------------------------|--------------------------------------------------------|-----------------------------------------------------|
| DWT-01       | Verify table is displayed                   | Navigate to Dynamic Web Table section                 | Table is visible on the page                        |
| DWT-02       | Verify dynamic content loads                | Reload the page or interact with table (if dynamic)   | Table updates dynamically with new data             |
| DWT-03       | Verify column headers                       | Check header titles of each column                    | Column headers are correctly labeled                |
| DWT-04       | Verify row count changes dynamically        | Perform an action that affects rows (if available)    | Row count updates as expected                       |
| DWT-05       | Verify column count remains constant        | Count columns before and after dynamic update         | Number of columns remains the same                  |
| DWT-06       | Verify cell content updates dynamically     | Observe specific cell content across refreshes        | Cell values change based on dynamic source          |
| DWT-07       | Verify sorting functionality                | Click on a column header (if sortable)                | Table rows sort ascending/descending                |
| DWT-08       | Verify search/filter functionality          | Enter a keyword (if search bar present)               | Table filters data as per input                     |
| DWT-09       | Verify table responsiveness                 | Resize browser or check on mobile                     | Table adjusts layout accordingly                    |
| DWT-10       | Verify action buttons (if any in rows)      | Click edit/delete/etc. in a row                       | Corresponding action is triggered correctly         |
| DWT-11       | Verify alignment of content                 | Inspect alignment (left/center/right) of each column  | Content is properly aligned                         |
| DWT-12       | Verify data consistency                     | Cross-check table content with expected source (if known) | Data shown is accurate and relevant              |

---

### Test Cases - Pagination Web Table

| Test Case ID | Test Case Description                      | Test Steps                                  | Expected Result                                         |
|--------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------------|
| PWT-01       | Verify table is displayed                  | Navigate to Pagination Web Table section    | Table is visible on the page                            |
| PWT-02       | Verify pagination controls are visible     | Scroll to bottom of table                   | Pagination buttons (1, 2, Next, Prev) are displayed     |
| PWT-03       | Verify default page load                   | Load the page                               | First page of the table is displayed by default         |
| PWT-04       | Verify data changes on page navigation     | Click on page 2                             | Table data updates to second page                       |
| PWT-05       | Verify "Next" button functionality         | Click "Next"                                | Table shows the next set of rows                        |
| PWT-06       | Verify "Previous" button functionality     | Navigate to page 2, click "Previous"        | Returns to previous page                                |
| PWT-07       | Verify first page navigation               | Click page number 1                         | Loads first page data                                   |
| PWT-08       | Verify last page navigation                | Click on last page number                   | Loads last page data                                    |
| PWT-09       | Verify total number of pages               | Count page numbers or calculate from total records | Matches expected page count                        |
| PWT-10       | Verify row count per page                  | Count number of rows shown per page         | Matches expected rows per page (e.g., 10)               |
| PWT-11       | Verify UI on active page button            | Observe the selected page number            | Active page is highlighted                              |
| PWT-12       | Verify clicking same page again            | Click on current active page                | No reload or change occurs                              |
| PWT-13       | Verify disabled state of Previous on first page | View navigation when on first page      | “Previous” button is disabled                           |
| PWT-14       | Verify disabled state of Next on last page | View navigation when on last page           | “Next” button is disabled                               |
| PWT-15       | Verify keyboard navigation (if supported)  | Use Tab and Enter keys                      | Can navigate between pages using keyboard               |
| PWT-16       | Verify responsiveness                      | Check pagination layout on smaller screens  | Pagination adapts or becomes scrollable                 |
| PWT-17       | Verify invalid page access                 | Try to go to a non-existing page (e.g., 99) | No action or error message shown                        |
| PWT-18       | Verify URL changes (if applicable)         | Observe URL while changing pages            | URL updates based on selected page                      |
| PWT-19       | Verify performance on switching pages      | Quickly switch pages multiple times         | Pages load correctly without lag or crash              |
| PWT-20       | Verify loading indicator (if any)          | Navigate between pages                      | Loading icon shows while data loads (if present)        |

---

### Test Cases - General Form Validation

| Test Case ID | Test Case Description                       | Test Steps                                     | Expected Result                                  |
|--------------|----------------------------------------------|------------------------------------------------|--------------------------------------------------|
| FORM-01      | Verify form is visible                      | Scroll to the form section                     | Form is displayed on the page                    |
| FORM-02      | Verify all input fields are present         | Check for fields: name, email, message, etc.   | All fields are present                           |
| FORM-03      | Verify placeholder text in input fields     | Check each input box                           | Placeholder text is appropriate                  |
| FORM-04      | Verify input field validation – Required fields | Leave required fields empty and submit     | Shows validation error                           |
| FORM-05      | Verify input field accepts valid data       | Enter valid text/email in fields               | Input is accepted without error                  |
| FORM-06      | Verify input field rejects invalid email    | Enter incorrect email format                   | Error message is shown                           |
| FORM-07      | Verify max character limit in input fields  | Enter more than allowed characters             | Input is restricted or error is shown            |
| FORM-08      | Verify form reset functionality (if any)    | Click reset (if button available)              | All fields are cleared                           |
| FORM-09      | Verify form submission with valid data      | Fill all fields with valid data and submit     | Confirmation message is shown                    |
| FORM-10      | Verify form submission with invalid data    | Enter invalid or blank data and submit         | Error message is shown                           |
| FORM-11      | Verify mandatory fields marked with *       | Check form design                              | Required fields have * indication                |
| FORM-12      | Verify tab navigation between fields        | Use the Tab key to move between inputs         | Focus shifts correctly to the next field         |
| FORM-13      | Verify keyboard input works                 | Enter data using keyboard                      | Inputs are accepted                              |
| FORM-14      | Verify success/error message after submission | Submit form                                  | Appropriate message appears                      |
| FORM-15      | Verify form responsiveness                  | Check form on different screen sizes           | Form layout adjusts correctly                    |
| FORM-16      | Verify spam protection (if CAPTCHA used)    | Submit without CAPTCHA                         | Blocked or error shown (if CAPTCHA present)      |
| FORM-17      | Verify input alignment and styling           | Inspect field alignments           | All elements are aligned properly                |
| FORM-18      | Verify form submission sends data            | Use network tab or inspect post request | Data is submitted to the server              |

---

### Test Cases - Footer

| Test Case ID | Test Case Description                                     | Test Steps                                  | Expected Result                                           |
|--------------|------------------------------------------------------------|---------------------------------------------|-----------------------------------------------------------|
| Footer-01    | Verify footer section is visible                          | Scroll to the bottom of the page            | Footer is displayed                                       |
| Footer-02    | Verify number of links in the footer                      | Count total clickable links                 | Matches expected count                                    |
| Footer-03    | Verify each footer link is clickable                      | Click on each footer link                   | It navigates to the correct page                          |
| Footer-04    | Verify correct redirection URL for each link              | Click and observe URL                       | URL matches expected destination                          |
| Footer-05    | Verify links open in correct tab                          | Click on links                              | Internal links open in same tab, external in new tab      |
| Footer-06    | Verify broken links                                       | Click all links or use link checker         | No 404 or error pages                                     |
| Footer-07    | Verify footer links text                                  | Check for grammar and text clarity          | Text is readable and correct                              |
| Footer-08    | Verify styling and alignment                              | Inspect link appearance and layout          | Properly aligned and styled                               |
| Footer-09    | Verify link hover effects                                 | Hover mouse over links                      | Links change color/underline if styled                    |
| Footer-10    | Verify accessibility                                       | Use keyboard and screen reader              | Footer links are accessible                               |
| Footer-11    | Verify social media links (if present)                    | Click social icons                          | Opens correct profile or page                             |
| Footer-12    | Verify responsiveness of footer                           | Resize screen                               | Footer layout adjusts properly                            |
| Footer-13    | Verify copyright info                                     | Scroll to footer                            | Copyright info is displayed                               |
| Footer-14    | Correct copyright message                                 | Observe the text                            | Message is correct (e.g., “© 2025 Automation Practice”)   |
| Footer-15    | Verify language consistency                               | Check footer text language                  | Matches site’s default language                           |
| Footer-16    | Verify footer anchor link scroll                          | Click anchor link                           | Page scrolls to appropriate section                       |

---

### Test Cases - Tabs

| Test Case ID | Test Case Description                          | Test Steps                       | Expected Result                                  |
|--------------|--------------------------------------------------|----------------------------------|--------------------------------------------------|
| TAB-01       | Verify all tabs are visible                    | Check tab buttons                | All tab headers (e.g., Tab1, Tab2) are visible   |
| TAB-02       | Verify tab content loads correctly             | Click on each tab                | Corresponding tab content is displayed           |
| TAB-03       | Verify only one tab content is visible at a time | Switch between tabs            | Only selected tab's content is shown             |
| TAB-04       | Verify default active tab on page load         | Load the page                    | The default tab is pre-selected                  |
| TAB-05       | Verify tab switching via keyboard              | Use Tab or arrow keys            | Focus changes and content switches               |
| TAB-06       | Verify responsiveness of tab section           | View tabs on different screens   | Tabs adapt or stack responsively                 |
| TAB-07       | Verify tab alignment and styling               | Observe tab layout and style     | Tabs are properly styled and aligned             |

---

### Test Cases - Dynamic Buttons (DBTN)

| Test Case ID | Test Case Description                          | Test Steps                                | Expected Result                              |
|--------------|--------------------------------------------------|-------------------------------------------|----------------------------------------------|
| DBTN-01      | Verify button visibility                        | Locate dynamic button                      | Button is visible on page                    |
| DBTN-02      | Verify button click action                      | Click the button                           | Action/message is triggered                  |
| DBTN-03      | Verify delay in button visibility (if delayed)  | Wait for the button to appear              | Button appears after timeout                 |
| DBTN-04      | Verify button becomes clickable after delay     | Wait and click                             | Button becomes active and clickable          |
| DBTN-05      | Verify disabled button state initially          | Observe initial state                      | Button is disabled                           |
| DBTN-06      | Verify loading icon/message (if any)            | Observe button or surrounding area         | Shows loading before enabling                |

---

### Test Cases - Alerts

| Test Case ID | Test Case Description                | Test Steps              | Expected Result                            |
|--------------|---------------------------------------|-------------------------|--------------------------------------------|
| ALR-01       | Verify alert triggers                | Click alert button      | JavaScript alert box appears               |
| ALR-02       | Verify alert message text            | Read alert message      | Message is correct                         |
| ALR-03       | Verify alert can be accepted         | Click “OK” on alert     | Alert closes, next action triggered        |
| ALR-04       | Verify confirmation popup            | Click confirm button    | Confirmation dialog appears                |
| ALR-05       | Verify cancel option on confirm popup | Click “Cancel”         | Confirmation is canceled                   |
| ALR-06       | Verify prompt popup                  | Click prompt            | Prompt input box appears                   |
| ALR-07       | Verify text input in prompt          | Enter text and click OK | Text is accepted and shown on screen       |
| ALR-08       | Verify cancel on prompt              | Click cancel            | Prompt is dismissed without action         |

---

### Test Cases - Hover Buttons

| Test Case ID | Test Case Description                 | Test Steps                | Expected Result                           |
|--------------|----------------------------------------|---------------------------|-------------------------------------------|
| HBTN-01      | Verify hover action works             | Hover on target element   | Hidden menu or tooltip appears            |
| HBTN-02      | Verify click after hover              | Hover then click          | Action is performed                       |
| HBTN-03      | Verify hover style changes            | Observe element on hover  | Color/style changes                       |
| HBTN-04      | Verify tooltip appears on hover       | Hover on tooltip element  | Tooltip text is visible                   |

---

### Test Cases - Double Click

| Test Case ID | Test Case Description                           | Test Steps                | Expected Result                                |
|--------------|--------------------------------------------------|---------------------------|------------------------------------------------|
| DC-01        | Verify double-click triggers action             | Double click on element   | Corresponding message/action appears           |
| DC-02        | Verify single click does nothing                | Click once                | No action triggered                            |
| DC-03        | Verify text or style change after double click  | Double click on element   | Text/style updates                             |

---

### Test Cases - Drag and Drop

| Test Case ID | Test Case Description               | Test Steps                                     | Expected Result                                           |
|--------------|--------------------------------------|------------------------------------------------|-----------------------------------------------------------|
| DD-01        | Verify elements are draggable       | Try dragging item                              | Item moves with cursor                                   |
| DD-02        | Verify drop functionality           | Drop dragged item on target                    | Item is accepted and snapped into place                  |
| DD-03        | Verify invalid drop location        | Drop item outside drop area                    | Item returns to original position or no action           |
| DD-04        | Verify drag start and end events    | Perform drag and observe console (if events logged) | Events are triggered properly                     |
### Test Cases - Slider (SLD)

| Test Case ID | Test Case Description               | Test Steps                | Expected Result                        |
|--------------|--------------------------------------|---------------------------|----------------------------------------|
| SLD-01       | Verify slider is visible             | Locate slider element     | Slider appears on the page             |
| SLD-02       | Verify slider movement               | Move slider left/right    | Slider thumb moves accordingly         |
| SLD-03       | Verify value updates on movement     | Move slider and observe value | Value reflects slider position     |
| SLD-04       | Verify slider works with keyboard    | Use arrow keys            | Slider moves left/right                |
| SLD-05       | Verify min and max limits            | Move slider to both ends  | Values do not exceed defined range     |

---

### Test Cases - Select Dropdown (SDD)

| Test Case ID | Test Case Description                   | Test Steps             | Expected Result                       |
|--------------|------------------------------------------|------------------------|---------------------------------------|
| SDD-01       | Verify dropdown is visible               | Click dropdown field   | Options are shown                     |
| SDD-02       | Verify options can be scrolled           | Use mouse or keys      | Options scroll up/down                |
| SDD-03       | Verify selection from dropdown           | Select an option       | Selected value appears in the field   |
| SDD-04       | Verify multiple selections (if applicable)| Select multiple options| Multiple options shown                |
| SDD-05       | Verify keyboard navigation               | Use arrow keys         | Options are navigable via keyboard    |

---

### Test Cases - Labels & Links (LBL)

| Test Case ID | Test Case Description                  | Test Steps         | Expected Result                        |
|--------------|-----------------------------------------|--------------------|----------------------------------------|
| LBL-01       | Verify all labels are visible          | Scan page          | Labels for all inputs are visible      |
| LBL-02       | Verify label text accuracy             | Read label text    | Labels match expected field descriptions |
| LBL-03       | Verify links are clickable             | Click on each link | Navigates to correct URL               |
| LBL-04       | Verify external links open in new tab  | Click external links | Opens in a new tab                   |
| LBL-05       | Verify broken links                    | Click all links    | No 404 or invalid pages                |
| LBL-06       | Verify link hover effect               | Hover on links     | Style or color changes                 |

---

### Test Cases - Shadow DOM (SHD)

| Test Case ID | Test Case Description                             | Test Steps                       | Expected Result                                   |
|--------------|----------------------------------------------------|----------------------------------|---------------------------------------------------|
| SHD-01       | Verify shadow DOM element is present              | Inspect developer tools          | Shadow root is visible                           |
| SHD-02       | Verify text/content inside shadow DOM             | Expand shadow DOM in dev tools   | Inner content is accessible                      |
| SHD-03       | Verify styling of shadow DOM elements             | Observe styles                   | CSS styles are applied properly                  |
| SHD-04       | Verify interaction inside shadow DOM              | Click/Type into shadow element   | Interaction works properly                       |
| SHD-05       | Verify automated tools can access shadow elements | Try locating via script          | Shadow DOM needs special handling (e.g., shadowRoot) |

---

### Test Cases - UDEMY Page & Course Cards (UDEMY_P, UCC, UNV)

| Test Case ID   | Test Case Description                        | Test Steps                        | Expected Result                                   |
|----------------|-----------------------------------------------|-----------------------------------|---------------------------------------------------|
| UDEMY_P-01     | Page loads successfully                      | Navigate to URL                   | Page loads in ≤3s, no errors                      |
| UDEMY_P-02     | Title and header are visible                 | Observe page top                  | "UDEMY COURSES" and hero section are present      |
| UDEMY_P-03     | Course list section is visible               | Scroll to list area               | All courses are displayed                         |
| UCC-01         | Verify each course card is visible           | Inspect rendered cards            | Each item has a course card                       |
| UCC-02         | Course title is correct                      | Compare displayed titles          | Matches expected course list                      |
| UCC-03         | Category badge displays                      | Check badge labels                | Badge is visible with correct label               |
| UCC-04         | View Course button/link present              | Inspect each card                 | Each card has a “View Course” button              |
| UCC-05         | Button styling is consistent                 | Visually inspect button UI        | Consistent style across cards                     |
| UCC-06         | Verify featured courses list                 | Compare with search snippet       | All listed courses appear                         |
| UNV-01         | Clicking "View Course" redirects              | Click View Course                 | Opens correct page                                |
| UNV-02         | Check working of social share buttons        | Click share links                 | Share dialog opens correctly                      |
| UNV-03         | Internal navigation links function           | Use header/menu links             | Links redirect as intended                        |

---

### Test Cases - Responsiveness & Accessibility (UP)

| Test Case ID | Test Case Description                       | Test Steps                     | Expected Result                                 |
|--------------|----------------------------------------------|--------------------------------|-------------------------------------------------|
| UP-01        | Mobile viewport layout                      | Open in mobile                 | Cards stack in 1-column                         |
| UP-02        | Tablet viewport layout                      | Open in tablet                 | Cards adapt to 2-column grid                    |
| UP-03        | Buttons responsive/tappable                 | Tap on mobile                  | Buttons work without layout issues              |
| UP-04        | Images and text resize appropriately        | Resize window                  | Layout adjusts with no overlap                  |
| UP-05        | Test smooth scrolling                       | Scroll through courses         | No jank or lag                                  |
| UP-06        | Button click load performance               | Click “View Course”            | Page opens quickly                              |
| UP-07        | Page performance metric                     | Run audit                      | Lighthouse score ≥90                            |
| UP-08        | All buttons and images have alt/title       | Inspect with DevTools          | No missing attributes                           |
| UP-09        | Page navigable via keyboard                 | Use Tab & Enter                | All elements accessible                         |
| UP-10        | Color contrast is sufficient                | Use contrast checker           | Meets WCAG AA standard                          |
| UP-11        | Page served via HTTPS                       | Check browser bar              | HTTPS lock icon visible                         |
| UP-12        | No personal data leak                       | Inspect network console        | No sensitive data exposed                       |
| UP-13        | Detect updates dynamically                  | Reload after a week            | New courses appear                              |

---

### Test Cases - Feedback Section (TC-FB)

| Test Case ID | Test Case Description                                  | Test Steps                                 | Expected Result                                     |
|--------------|---------------------------------------------------------|--------------------------------------------|-----------------------------------------------------|
| TC-FB-01     | Verify presence of feedback section                    | Scroll to “STUDENTS FEEDBACK”              | Section is visible                                 |
| TC-FB-02     | Check visibility on page load                          | Load the page                              | Section is fully visible                           |
| TC-FB-03     | Google reviews widget loads correctly                  | View widget                                | At least one review or placeholder visible         |
| TC-FB-04     | Spinner/loading message during fetch                   | Refresh page                               | “Syncing…” message shows before reviews load       |
| TC-FB-05     | Validate design/style of heading                       | Inspect “STUDENTS FEEDBACK”                | Font, size, color match website theme              |
| TC-FB-06     | Reviews display on mobile                              | Open on mobile                             | Reviews resize and wrap properly                   |
| TC-FB-07     | Sync message removed after load                        | Refresh and wait                           | “Syncing” disappears after load                    |
| TC-FB-08     | Error handling on failed review load                   | Simulate network failure                   | Error or retry message shown                       |
| TC-FB-09     | Reviews are clickable (if applicable)                  | Click review/reviewer                      | Link opens in tab or expands inline                |
| TC-FB-10     | "More Reviews" link works                              | Click more/external link                   | Full review list loads                             |
| TC-FB-11     | Responsiveness in tablet view                          | Use tablet screen                          | Layout adapts well                                 |
| TC-FB-12     | Layout/readability in small view                       | Use small screen                           | Text is readable, not cut off                      |
| TC-FB-13     | Feedback widget is keyboard accessible                 | Tab to section                             | Elements are keyboard focusable                    |
| TC-FB-14     | ARIA roles/labels and alt attributes                   | Inspect HTML                               | Accessibility tags are present                     |
| TC-FB-15     | Validate text contrast in widget                       | Use contrast checker                       | Meets WCAG standards                               |
| TC-FB-16     | Measure review loading performance                     | Load with normal connection                | Reviews load in ≤10s                               |
| TC-FB-17     | Handle rapid reloads                                   | Reload repeatedly                          | No duplication or crash                            |
| TC-FB-18     | New review appears after sync                          | Add review on Google → refresh             | New review appears                                 |
| TC-FB-19     | Deleted review removed after sync                      | Delete externally → refresh                | Deleted review no longer appears                   |
