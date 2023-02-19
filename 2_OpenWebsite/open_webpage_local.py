from selenium import webdriver


def open_webpage_online():
    driver = webdriver.Firefox(executable_path="C:\\Users\\User\\Documents\\SQA "
                                               "Project\\Automation\\Drivers\\geckodriver.exe")
    driver.get("http://localhost:8080/")
    driver.close()


open_webpage_online()
