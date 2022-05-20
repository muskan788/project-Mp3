from selenium import webdriver    
from selenium.webdriver.common.by import By 

import time 
   
from selenium.webdriver.common.keys import Keys 
  
# Creating an instance webdriver
driver = webdriver.Firefox() 
  
driver.maximize_window()

driver.get('https://www.godaddy.com/en-in')

expe_title="Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy IN"
actual_title=driver.title

print("Expected Title= "+expe_title)
print("Actual Title= "+actual_title)
if expe_title==actual_title:
    print("Titles matches")
else: 
    print("Fail to match titles")


expe_url="https://www.godaddy.com/en-in"
actual_url=driver.current_url

print()
print("Expected URL= "+expe_url)
print("Actual URL= "+actual_url)
if expe_url==actual_url:
    print("URls matches")
else: 
    print("Fail to match URLs")

element = driver.find_element(By.TAG_NAME, "title")


pageSource = driver.page_source
fileToWrite = open("page_source.html", "w",encoding="utf8")
fileToWrite.write(pageSource)
fileToWrite.close()
print()
print("Page Source Code is written to the file page_source.html")
  
# Get Text
print()
pg_src_title=element.get_attribute("textContent")
print("Title from Source Page= "+pg_src_title)
print("Expected Title= "+expe_title)
if pg_src_title==actual_title:
    print("Titles matches")
else: 
    print("Fail to match titles")



#to refresh the browser
driver.refresh()
#to close the browser
driver.close()