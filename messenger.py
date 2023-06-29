from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# import undetected_chromedriver as uc
from dotenv import load_dotenv
import os
import time


driver = webdriver.Chrome()
# driver = uc.Chrome()
#going to messenger website
driver.get("https://www.messenger.com")



# setting time sleep for waiting page to be fully loaded
time.sleep(5)


# credential
load_dotenv('.env')
email: str = os.getenv('email')
password: str = os.getenv('password')


#selecting the elements of login field
email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')

#input the credentials on field
email_input.send_keys(email)
password_input.send_keys(password)

time.sleep(3)
#selecting the element of button
login_form = driver.find_element(By.CSS_SELECTOR, 'button[name="login"]')

#submit
login_form.click()
time.sleep(5)

#list of contacts
First_contact: str = os.getenv('first_contact')
Second_contact: str = os.getenv('second_contact')
Third_contact: str = os.getenv('third_contact')
contacts = [First_contact,Second_contact,Third_contact]

#finding the elements of search bar
search_input  = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]') 

#choose the second parameter in the contact list
search_input.send_keys(contacts[0])


time.sleep(2)



# Click  first contact 
click_first_contact = driver.find_element(By.CSS_SELECTOR, 'li[id="100004055240717"]')
click_first_contact.click()

# Click second contact 
# click_second_contact = driver.find_element(By.CSS_SELECTOR, 'li[id="100000292407952"]')
# click_second_contact.click()

# Click third contact 
# click_third_contact = driver.find_element(By.CSS_SELECTOR, 'li[id="1535917644"]')
# click_third_contact.click()


time.sleep(4)

#writing a  message
message = "Hi how are you today?"
write_message = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Message"]')
write_message.send_keys(message)


#send message
time.sleep(9)
send = driver.find_element(By.CSS_SELECTOR, 'svg[class="xsrhx6k"]')
send.click()

#going to logout
out = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Settings, help and more"]')
out.click()


# logout
logout = driver.find_elements(By.CSS_SELECTOR, "div[role='menuitem']")[-1]
logout.click()
time.sleep(8)


#automatically shutdown
# os.system("shutdown /f")

#automatically restart for test
# os.system("shutdown /r /t 3")






















