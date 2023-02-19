from selenium import webdriver


def set_browser_size():
    driver = webdriver.Firefox(executable_path="C:\\Users\\User\\Documents\\SQA "
                                               "Project\\Automation\\Drivers\\geckodriver.exe")
    driver.set_window_size(768, 1024)
    driver.get("https://demo.opencart.com/index.php")


set_browser_size()
