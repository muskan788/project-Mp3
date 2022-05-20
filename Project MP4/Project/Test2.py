from selenium import webdriver     
  
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
   
from selenium.webdriver.common.keys import Keys 
  
# Creating an instance webdriver
driver = webdriver.Firefox() 
  
driver.maximize_window()

driver.get('https://www.godaddy.com/en-in')

# to print the page title in console
print("Title of the WebPage= "+driver.title)
# to print the current URL in console
print("Link of the Webpage= "+driver.current_url)
#to refresh the browser
driver.refresh()
#to close the browser
driver.close()