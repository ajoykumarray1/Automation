from selenium import webdriver
import time


def navigate():
    driver = webdriver.Firefox(executable_path="C:\\Users\\User\\Documents\\SQA "
                                               "Project\\Automation\\Drivers\\geckodriver.exe")
    driver.get("https://demo.opencart.com/index.php")
    time.sleep(3)

    driver.get("https://google.com/")
    time.sleep(3)

    driver.back()
    time.sleep(3)

    driver.forward()
    time.sleep(3)

    driver.refresh()

    driver.close()


navigate()
