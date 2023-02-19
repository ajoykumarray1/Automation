from selenium import webdriver


def firefox_launch():
    driver = webdriver.Firefox(executable_path="C:\\Users\\User\\Documents\\SQA "
                                               "Project\\Automation\\Drivers\\geckodriver.exe")

    driver.close()


firefox_launch()
