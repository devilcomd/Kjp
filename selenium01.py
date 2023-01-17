from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('미국10년국채금리')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)


driver.find_elements_by_css_selector('.yuRUbf')[0].click()