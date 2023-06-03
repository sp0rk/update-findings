from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def download_csv(url, form_id, login, password):
	def login_service_account(driver, url, login, password):
		driver.get(url)

		field_login = driver.find_element(By.ID, 'user_login')
		field_login.send_keys(login)

		field_pass = driver.find_element(By.ID, 'user_pass')
		field_pass.send_keys(password + Keys.RETURN)

	def download_csv_file(driver, form_url):
		driver.get(form_url)

		btn_export = driver.find_element(By.LINK_TEXT, 'Export CSV')
		btn_export.click()

		time.sleep(5)

	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome("chromedriver", options=options)

	login_service_account(driver, url, login, password)
	download_csv_file(driver, f'{url}/admin.php?page=cfdb7-list.php&fid={form_id}')
	
	driver.quit()