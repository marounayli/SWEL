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
driver.get('https://usj.edu.lb/')
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



admissions=find_elem({"tag":"a", "attrs":{"href":"Admissions"}, "value" :"Admission"})
res = driver.find_element(By.XPATH,admissions)
actions = ActionChains(driver)
actions.move_to_element(res).perform()

time.sleep(3)


dossier = find_elem({"tag":"a", "attrs": {"href":"dossier"}, "value":"Mon Dossier"})
res = driver.find_element(By.XPATH,dossier)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)
email = find_elem({"tag":"input", "attrs": {"name":"email", "id":"email" ,"placeholder":"email"}, "value":""})
res = driver.find_element(By.XPATH,email)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.send_keys("maroun")


email = find_elem({"tag":"input", "attrs": {"name":"password", "id":"password" ,"placeholder":"email"}, "value":""})
res = driver.find_element(By.XPATH,email)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.send_keys("maroun")





email = find_elem({"tag":"button", "attrs": {"name":"submit", "id":"enter"}, "value":"Enter"})
res = driver.find_element(By.XPATH,email)
actions = ActionChains(driver)
actions.move_to_element(res).perform()
res.click()

