from selenium import webdriver
import random

driver = webdriver.Chrome("C:\\Users\\dbabich\\AppData\Local\\Programs\\Python\\Python35-32\\selenium\\webdriver\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://evernote.com/")
driver.set_page_load_timeout(20)
#Sign-up
email_num = random.randint(1, 100)

driver.find_element_by_xpath('//*[@id="email"]').send_keys('newuser' + str(email_num) + '@qa.com')
driver.find_element_by_xpath('//*[@id="password-login"]').send_keys('password')
driver.find_element_by_xpath('//*[@id="create-account"]/div/div[1]/button').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div/div[1]/div').click()
driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div/div[2]/span').click()
driver.implicitly_wait(10)
notes_element = driver.find_element_by_xpath('//*[@id="gwt-debug-NotesHeader-title"]')
assert notes_element.text == 'NOTES'
driver.quit()
