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


#first 
# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, "id-3a34578f-40f3-4d2f-aaa4-0a1320f3fe6a"))).click()
print("\nFirst Menu Link\n");
element = driver.find_element(By.ID,"id-3a34578f-40f3-4d2f-aaa4-0a1320f3fe6a");
# element.click();
driver.execute_script("arguments[0].click();", element)
time.sleep(2);
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)

element = driver.find_element(By.ID,"id-b1c657aa-b81f-4909-86bb-e349818d2dfb");
# element.click();
driver.execute_script("arguments[0].click();", element)
time.sleep(2);
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)

#second
print("\nSecond Menu Link\n")
element = driver.find_element(By.ID,"id-7c8834e5-3239-457a-93d1-9e7432567e4a");
# element.click();
driver.execute_script("arguments[0].click();", element)
time.sleep(2);
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)

element = driver.find_element(By.ID,"id-b1c657aa-b81f-4909-86bb-e349818d2dfb");
# element.click();
driver.execute_script("arguments[0].click();", element)
time.sleep(2);
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)

#third
print("\nThird Menu Link\n")
element = driver.find_element(By.ID,"id-7f7e18ab-b77d-44bb-80f5-09045b8b8d61");
# element.click();
driver.execute_script("arguments[0].click();", element)
time.sleep(2);
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)

element = driver.find_element(By.ID,"id-b1c657aa-b81f-4909-86bb-e349818d2dfb");
# element.click();
driver.execute_script("arguments[0].click();", element)
time.sleep(2);
print("Title of the WebPage= "+driver.title)
print("Link of the Webpage= "+driver.current_url)




driver.close()
