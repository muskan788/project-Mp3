from selenium import webdriver     
  
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded.
import time 
   
from selenium.webdriver.common.keys import Keys 
  
# Creating an instance webdriver
browser = webdriver.Firefox() 
browser.get('https://www.godaddy.com/en-in')
  
# Let's the user see and also load the element 
time.sleep(9000)
   
  
# closing the browser
browser.close() 