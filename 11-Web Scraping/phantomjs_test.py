from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# print(driver.current_url)

driver.get("https://tinyhouselistings.com/search?area_max=700&area_min=200&location_type=mobile&page=1&price_max=5000000&price_min=100&purchase_type=purchase")
cards = driver.find_elements(By.CLASS_NAME, "listing-card-body")
links = []
for card in cards:
  links.append(card.find_element_by_tag_name('a') )

for link in links:
  print(link.get_attribute('href'))

driver.quit()