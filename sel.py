# Import the webdriver and keys modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import locator as lc
import time 
# Create a new Chrome browser
driver = webdriver.Chrome()

# Navigate to the Google website
driver.maximize_window()
driver.get('https://murex.com/')
time.sleep(3)

def find_elem(description):
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    html_soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')
    elem =  lc.Elem(description["tag"],description["attrs"],description["value"])
    xp = lc.get_xpath(html_soup,elem)
    res = driver.find_element(By.XPATH,xp)
    actions = ActionChains(driver)
    actions.move_to_element(res).perform()
    return res



make_chart=find_elem({"tag":"a", "attrs":{"href":"contact us"}, "value" :"Contact Us"})
make_chart.click()

time.sleep(10)


# donuts = find_elem({"tag":"div", "attrs":{"href":""}, "value" :"Donut"})
# donuts.click()

# time.sleep(10)


# chart_title = find_elem({"tag":"input", "attrs":{"placeholder":"chart title"}, "value":""})
# chart_title.send_keys("chart alpha")

# time.sleep(10)


# make_chart_button = find_elem({"tag":"button", "attrs":{}, "value":"Make Chart"})
# make_chart_button.click()
# time.sleep(10)


# clients = find_elem({"tag":"button", "attrs":{}, "value":"Share via your device"})
# actions = ActionChains(driver)
# actions.move_to_element(clients).perform()
# time.sleep(10)






# case_studies = driver.find_element(By.XPATH,"/html/body/div/div/main/section[3]/div[2]/div/div/div[5]/a")
# # case_study = find_elem({"tag":"a", "attrs":{"href":"/en/case-studies/leading-mexican-bank-banorte-strengthens-credit-risk-management-practices"}, "value" :"Read More "})
# driver.execute_script("arguments[0].scrollIntoView();", case_studies)
# actions = ActionChains(driver)
# actions.move_to_element(case_studies).perform()
# # Click on the element
# case_studies.click()
# time.sleep(10)


# search_input = lc.Elem("input",{},"search")
# xp = "html/body"+lc.get_xpath(html_soup,search_input)
# search_input = driver.find_element(By.XPATH,xp)
# search_input.send_keys("music 2022")

# time.sleep(5)

# html_source_code = driver.execute_script("return document.body.innerHTML;")
# html_soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')

# searchButton = lc.Elem("button", {"id" :"search"} , "Search")
# search_button = "html/body"+lc.get_xpath(html_soup,searchButton)
# searchButton = driver.find_element(By.XPATH,search_button)

# searchButton.click()
driver.close()