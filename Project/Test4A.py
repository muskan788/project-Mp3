from selenium import webdriver    
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
   
from selenium.webdriver.common.keys import Keys 

wait_time_out = 15
  
# Creating an instance webdriver
driver = webdriver.Firefox() 
  
driver.maximize_window()
driver.get('https://www.godaddy.com/en-in')



WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, "id-3a34578f-40f3-4d2f-aaa4-0a1320f3fe6a"))).click()
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)


driver.close()
