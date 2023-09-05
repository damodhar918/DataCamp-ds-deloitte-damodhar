from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager


def authenticate_gp():
    print('############## Authenticating Green Pages ##############')
        
    # Set options to make browsing easier

    options = webdriver.EdgeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    # r"D:\selenium web drivers\edge driver\msedgedriver.exe"
    # driver = webdriver.Edge(r"C:\Users\jdamodhar\Desktop\10 doc\msedgedriver.exe",options=options)

    desired_cap={}


    driver = webdriver.Edge(executable_path=r'C:\10 doc\msedgedriver.exe ', capabilities=desired_cap,options=options)
  
    
    # # Set options to make browsing easier
    # options = webdriver.ChromeOptions()
    # options.add_argument("disable-infobars")
    # options.add_argument("start-maximized")
    # options.add_argument("disable-dev-shm-usage")
    # options.add_argument("no-sandbox")
    # options.add_argument("--headless")
    # options.add_argument("--log-level=OFF")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("disable-blink-features=AutomationControlled")

    # driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    url = "http://greenpagesqaadmin.wm.com/eAgent/" #configparser
    # url = "http://greenpagesdevadmin.wm.com/eAgent/" #configparser
    user = "admin001"
    # user = "nbass"
    
    password = "#1234567!"

    driver = login(driver, url, user, password)

    cookies = get_cookies(driver)

    driver.close()

    return cookies

def login(driver, url, user, password):
    driver.get(url)
    
    driver.find_element(by="id", value="user").send_keys(user)
    driver.find_element(by="id", value="password").send_keys(password + Keys.RETURN)
    # driver.find_element(by="name", value="USER").send_keys(user)
    # driver.find_element(by="name", value="PASSWORD").send_keys(password + Keys.RETURN)
    return driver

def get_cookies(driver):
    cookies = {}
    selenium_cookies = driver.get_cookies()
    for cookie in selenium_cookies:
        cookies[cookie['name']] = cookie['value']
    # print(cookies)    
    return cookies
