from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\dbabich\\AppData\Local\\Programs\\Python\\Python35-32\\selenium\\webdriver\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://evernote.com/")
driver.set_page_load_timeout(20)


#   Login Credentials:
email = 'qa@123.com'
password = 'password'

driver.find_element_by_xpath('/html/body/header/div[2]/a[1]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys(str(email))
driver.find_element_by_xpath('//*[@id="password"]').send_keys(str(password))
driver.find_element_by_xpath('//*[@id="login"]').click()
time.sleep(5)

web_element = driver.find_element_by_xpath('//*[@id="gwt-debug-NotesHeader-title"]')
assert web_element.text == 'NOTES'
driver.quit()
