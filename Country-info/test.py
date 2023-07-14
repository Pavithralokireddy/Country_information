from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Set up the Selenium WebDriver
driver_path = ("C:\\Users\srika\Downloads\chromedriver_win32\chromedriver.exe")  # Replace with the path to your ChromeDriver executable
selenium_service = Service(driver_path)
driver = webdriver.Chrome(service=selenium_service)

# Open the login page
driver.get("C:\pavi_projects\Country-info\home.html")  # Replace with the local path to your home.html file

# Enter login credentials and submit the form
username_input = driver.find_element("id", "username")
password_input = driver.find_element("id", "password")

username_input.send_keys("pavithralokireddy")
password_input.send_keys("password")
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
driver.implicitly_wait(20)

# Perform a search
search_input = driver.find_element("id", "country-inp")
search_input.send_keys("india")
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(20)

# Extract and print the search results
result_div = driver.find_element("id", "result")
print(result_div.text)

# Close the browser
driver.quit()
