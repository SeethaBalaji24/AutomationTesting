from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Global Declarations
driver = webdriver.Chrome()
searchKeyword = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard",
                 "Directory", "Maintenance", "Buzz"]
tabsInPIM = ["Personal Details", "Contact Details", "Emergency Contacts", "Dependents", "Immigration", "Job",
             "Salary", "Tax Exemptions", "Report-to", "Qualifications", "Memberships"]


# Launch the Orange HRM Portal and Login
class launch_and_login:
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, '//button[text()=" Login "]').click()


# Validate the search box in admin homepage
class tc_pim_01:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    for Keyword in searchKeyword:
        driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys(Keyword)
        getkeyword = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']") \
            .get_attribute("text()")
        print("tc_pim_01 - The Extracted Keyword is - " + getkeyword)
        time.sleep(3)
    driver.close()


# Validate Page headers Drop down on admin page
class tc_pim_02:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="Admin"]').click()
    driver.find_element(By.XPATH, '//span[text()="User Management "]').click()
    driver.find_element(By.XPATH, '//a[text()="Users"]').click()
    userrole = driver.find_element(By.XPATH, '//div[text()="User Role"]/following-sibling::div').get_attribute("text()")
    print("Extracted Userrole is " + userrole)
    status = driver.find_element(By.XPATH, '//div[text()="Status"]/following-sibling::div').get_attribute("text()")
    print("tc_pim_02 - Extracted Status is " + status)
    driver.close()


# Create new employee under PIM
class tc_pim_03:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    tabname = driver.find_element(By.XPATH, '//a[@class="orangehrm-tabs-item --active"]').get_attribute("text()")
    print("tc_pim_03 - Current Active tabname - " + tabname)
    driver.close()


# Validate Employee Personal details page post user creation
class tc_pim_04:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    for tab in tabsInPIM:
        driver.find_element(By.XPATH, "//a[text()='" + tab + "']").click()
        print("tc_pim_04 - Clicked -" + tab + "- Under PIM")
        time.sleep(3)
    driver.close()


# Update Employee Personal details page post user creation
class tc_pim_05:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seethalakshmi")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    employeefullname = driver.find_element(By.NAME, "firstName").get_attribute("text()")
    print("tc_pim_05 - The updated employee full name is - " + employeefullname)
    driver.close()


# Update Employee Contact details page post user creation
class tc_pim_06:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Contact Details']").click()
    driver.find_element(By.XPATH, '//label[text()="Street 1"]/parent::div/parent::div/div[2]/input').send_keys(
        "N0.123, North cross road")
    driver.find_element(By.XPATH, '//label[text()="Street 2"]/parent::div/parent::div/div[2]/input').send_keys(
        "Ecity 1")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    street1 = driver.find_element(By.NAME, "Street 1").get_attribute("text()")
    street2 = driver.find_element(By.NAME, "Street 2").get_attribute("text()")
    print("tc_pim_06 - The Contact detail as updated is - " + street1 + "" + street2)
    driver.close()


# Update Employee Emergency Contact details page post user creation
class tc_pim_07:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Emergency Contacts']").click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.XPATH, '//label[text()="Name"]/parent::div/parent::div/div[2]/input').send_keys("Balaji")
    driver.find_element(By.XPATH, '//label[text()="Relationship"]/parent::div/parent::div/div[2]/input').send_keys(
        "Father")
    driver.find_element(By.XPATH, '//label[text()="Home Telephone"]/parent::div/parent::div/div[2]/input').send_keys(
        "1234556")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    print("tc_pim_07 - Emergency Contact Details Saved successfully")
    driver.close()


# Update Employee Dependants Contact details page post user creation
class tc_pim_08:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Dependents']").click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.XPATH, '//label[text()="Name"]/parent::div/parent::div/div[2]/input').send_keys("Balaji")
    dropdown = Select(driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]'))
    dropdown.select_by_index(3)
    driver.find_element(By.XPATH, '//label[text()="Please Specify"]/parent::div/parent::div/div[2]/input').send_keys(
        "Father")
    driver.find_element(By.XPATH, '//label[text()="Date of Birth"]/parent::div/parent::div/div[2]/input').send_keys(
        "1966-04-24")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    print("tc_pim_08 - Dependants Details Saved successfully")
    driver.close()


# Update Employee Job details page
class tc_pim_09:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Job']").click()
    driver.find_element(By.XPATH, '//label[text()="Joined Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2015-04-24")
    driver.find_element(By.XPATH, '//label[text()="Name"]/parent::div/parent::div/div[2]/input').send_keys("Balaji")
    dropdown = Select(driver.find_element(By.XPATH,
                                          '//label[text()="Job Title"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown.select_by_value("Software Engineer")
    dropdown2 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Job Category"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown2.select_by_value("Professionals")
    dropdown2 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Sub Unit"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown2.select_by_value("Engineering")
    dropdown3 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Location"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown3.select_by_value("Texas R&D")
    dropdown4 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Employment Status"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown4.select_by_value("Full-Time Permanent")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Contract Start Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2016-04-24")
    driver.find_element(By.XPATH,
                        '//label[text()="Contract End Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2017-04-24")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    print("tc_pim_09 - Employee job Details Saved successfully")
    driver.close()


#  Update Employee Job details page
class tc_pim_10:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Job']").click()
    driver.find_element(By.XPATH, '//label[text()="Joined Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2015-04-24")
    driver.find_element(By.XPATH, '//label[text()="Name"]/parent::div/parent::div/div[2]/input').send_keys("Balaji")
    dropdown = Select(driver.find_element(By.XPATH,
                                          '//label[text()="Job Title"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown.select_by_value("Software Engineer")
    dropdown2 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Job Category"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown2.select_by_value("Professionals")
    dropdown2 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Sub Unit"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown2.select_by_value("Engineering")
    dropdown3 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Location"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown3.select_by_value("Texas R&D")
    dropdown4 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Employment Status"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown4.select_by_value("Full-Time Permanent")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH,
                        '//label[text()="Contract Start Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2016-04-24")
    driver.find_element(By.XPATH,
                        '//label[text()="Contract End Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2017-04-24")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, '//button[text()=" Terminate Employment "]').click()
    driver.find_element(By.XPATH,
                        '//label[text()="Termination Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2022-04-24")
    dropdown5 = Select(driver.find_element(By.XPATH,
                        '//label[text()="Termination Reason"]/parent::div/parent::div/div[2]/input'))
    dropdown5.select_by_value("Resigned")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    print("tc_pim_10 - Employee job Termination Details Saved successfully")
    driver.close()


# Update Employee Job Activation on Job details page
class tc_pim_11:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Job']").click()
    driver.find_element(By.XPATH, '//label[text()="Joined Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2015-04-24")
    driver.find_element(By.XPATH, '//label[text()="Name"]/parent::div/parent::div/div[2]/input').send_keys("Balaji")
    dropdown = Select(driver.find_element(By.XPATH,
                                          '//label[text()="Job Title"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown.select_by_value("Software Engineer")
    dropdown2 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Job Category"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown2.select_by_value("Professionals")
    dropdown2 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Sub Unit"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown2.select_by_value("Engineering")
    dropdown3 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Location"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown3.select_by_value("Texas R&D")
    dropdown4 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Employment Status"]/parent::div/parent::div/div[2]/div/div/div'))
    dropdown4.select_by_value("Full-Time Permanent")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH,
                        '//label[text()="Contract Start Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2016-04-24")
    driver.find_element(By.XPATH,
                        '//label[text()="Contract End Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2017-04-24")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, '//button[text()=" Terminate Employment "]').click()
    driver.find_element(By.XPATH,
                        '//label[text()="Termination Date"]/parent::div/parent::div/div[2]/input').send_keys(
        "2022-04-24")
    dropdown5 = Select(driver.find_element(By.XPATH,
                                           '//label[text()="Termination Reason"]/parent::div/parent::div/div[2]/input'))
    dropdown5.select_by_value("Resigned")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, '//button[text()=" Activate Employment "]').click()
    driver.find_element(By.XPATH, '//button[text()=" Terminate Employment "]')
    print("tc_pim_11 - Employee job Activation done successfully")
    driver.close()


# Update Employee Salary on Salary Component Page
class tc_pim_12:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Salary']").click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.XPATH,
                        '//label[text()="Salary Component"]/parent::div/parent::div/div[2]/input').send_keys(
        "1234500")
    dropdown1 = Select(driver.find_element(By.XPATH, '//label[text()="Pay Grade"]/parent::div/parent::div/div[2]/input'))
    dropdown1.select_by_value("Grade 3")
    dropdown2 = Select(
        driver.find_element(By.XPATH, '//label[text()="Pay Frequency"]/parent::div/parent::div/div[2]/input'))
    dropdown2.select_by_value("Bi Weekly")
    dropdown3 = Select(
        driver.find_element(By.XPATH, '//label[text()="Currency"]/parent::div/parent::div/div[2]/input'))
    dropdown3.select_by_value("United State Dollar")
    driver.find_element(By.XPATH,
                        '//label[text()="Amount"]/parent::div/parent::div/div[2]/input').send_keys(
        "45000")
    driver.find_element(By.XPATH,
                        '//label[text()="Include Direct Deposit Details"]').click()
    driver.find_element(By.XPATH,
                        '//label[text()="Account Number"]/parent::div/parent::div/div[2]/input').send_keys("123456788")
    dropdown3 = Select(
        driver.find_element(By.XPATH, '//label[text()="Account Type"]/parent::div/parent::div/div[2]/input'))
    dropdown3.select_by_value("Savings")
    driver.find_element(By.XPATH,
                        '//label[text()="Routing Number"]/parent::div/parent::div/div[2]/input').send_keys("123456788")
    driver.find_element(By.XPATH,
                        '//label[text()="Amount"]/parent::div/parent::div/div[2]/input').send_keys("40000")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    print("tc_pim_12 - Employee Salary Component details are saved successfully")
    driver.close()


# Update Employee Salary on Tax Exemption Page
class tc_pim_13:
    launch_and_login()
    driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-list oxd-topbar-header-hamburger"]').click()
    driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.NAME, "firstName").send_keys("Seetha")
    driver.find_element(By.NAME, "middleName").send_keys("Lakshmi")
    driver.find_element(By.NAME, "lastName").send_keys("Balaji")
    driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    driver.find_element(By.XPATH, '//label[text()="Username"]/parent::div/parent::div/div[2]/input').send_keys("Seetha")
    driver.find_element(By.XPATH, '//label[text()="Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/parent::div/parent::div/div[2]/input').send_keys(
        "Mercury24495@")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    driver.find_element(By.XPATH, "//a[text()='Tax Exemptions']").click()
    dropdown1 = Select(driver.find_element(By.XPATH, '//label[text()="Status"]/parent::div/parent::div/div[2]/input'))
    dropdown1.select_by_value("Single")
    driver.find_element(By.XPATH, '//label[text()="Exemptions"]/parent::div/parent::div/div[2]/input').send_keys(
        "20")
    dropdown2 = Select(driver.find_element(By.XPATH, '//label[text()="State"]/parent::div/parent::div/div[2]/input'))
    dropdown2.select_by_value("California")
    dropdown3 = Select(driver.find_element(By.XPATH, '//label[text()="Status"]/parent::div/parent::div/div[2]/input'))
    dropdown3.select_by_value("Single")
    driver.find_element(By.XPATH, '//label[text()="Exemptions"]/parent::div/parent::div/div[2]/input').send_keys(
        "15")
    dropdown4 = Select(driver.find_element(By.XPATH, '//label[text()="Unemployment State"]/parent::div/parent::div/div[2]/input'))
    dropdown4.select_by_value("California")
    dropdown4 = Select(
        driver.find_element(By.XPATH, '//label[text()="Work State"]/parent::div/parent::div/div[2]/input'))
    dropdown4.select_by_value("Alaska")
    driver.find_element(By.XPATH, '//button[text()=" Save "]').click()
    print("tc_pim_13 - Employee Salary Tax Exemption details are saved successfully")
    driver.close()

