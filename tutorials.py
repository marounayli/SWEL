# Import the webdriver and keys modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from bs4 import BeautifulSoup
import locator as lc
import time 
# Create a new Chrome browser
driver = webdriver.Chrome()

# Navigate to the Google website
driver.maximize_window()
driver.get('https://tutorialspoint.com/')
time.sleep(5)

# elt = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/header/div[2]/div/div/div/div/nav/ul/li[3]/a")
# actions=  ActionChains(driver)
# actions.move_to_element(elt).perform()

# elt2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/header/div[2]/div/div/div/div/nav/ul/li[3]/ul/li/div/div[1]/ul/li[3]/a")
# elt2.click()

def find_elem(description):
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    html_soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')
    elem =  lc.Elem(description["tag"],description["attrs"],description["value"])
    xp = lc.get_xpath(html_soup,elem)
    return xp



search=find_elem({"tag":"input", "attrs": {"placeholder" : "Search your favorite tutorials"}, "value" :""})
res = driver.find_element(By.XPATH,search)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.send_keys("C++ tutorial")


time.sleep(3)


dossier = find_elem({"tag":"a", "attrs": {"href":"/about_careers/"}, "value":""})
res = driver.find_element(By.XPATH,dossier)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.click()

time.sleep(3)
email = find_elem({"tag":"a", "attrs": {"href":"/Team/"}, "value":"Team"})
res = driver.find_element(By.XPATH,email)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.click()

time.sleep(3)
email = find_elem({"tag":"a", "attrs": {}, "value":"Next Page"})
res = driver.find_element(By.XPATH,email)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.click()
