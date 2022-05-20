# importing webdriver from selenium
from xml.dom.minidom import Element

from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Users\Muskan Raju Attar\\Desktop\Selenium ESE\\chromedriver.exe")

url = "http://automationpractice.com/index.php"


driver.get(url)

element  = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[1]/a");
time.sleep(2);
element.click();

element  = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/div[2]/a[2]");
time.sleep(2);
element.click();

element  = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a");
time.sleep(2);
element.click();

element  = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div[1]/p");
time.sleep(2);
element.click();



