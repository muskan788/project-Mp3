# importing webdriver from selenium
from xml.dom.minidom import Element

from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Users\Muskan Raju Attar\\Desktop\\Selenium ESE\\chromedriver.exe")

url = "http://automationpractice.com/index.php"


driver.get(url)

element  = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a");
time.sleep(2);
element.click();

element  = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[3]");
time.sleep(2);
element.click();




