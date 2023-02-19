from selenium import webdriver


def open_webpage_online():
    driver = webdriver.Firefox(executable_path="C:\\Users\\User\\Documents\\SQA "
                                               "Project\\Automation\\2_OpenWebsite\\geckodriver.log")
    driver.get("file:///C:/Users/User/Documents/SQA Project/Your Store.html")
    driver.close()


open_webpage_online()