from selenium import webdriver
import time

driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
driver.get("https://ozelhd.github.io/Web2/i2.html")

time.sleep(10)

#Chrome will close when the python file ends. (note to myself)