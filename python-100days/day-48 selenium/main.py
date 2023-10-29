import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# Set options to make browsing easier
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument("disable-dev-shm-usage")
options.add_argument("no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

# driver_path = './chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path,options=options)


def login(url):
    # print('Logging in')
    driver.get(url)
    driver.find_element(by="id", value="user").send_keys("admin001")
    time.sleep(.01)
    driver.find_element(by="id", value="password").send_keys("#Waste123!" + Keys.RETURN)
    time.sleep(.01)
    # print('Successfully logged in!')


def get_cookies():
    cookies = {}
    selenium_cookies = driver.get_cookies()
    for cookie in selenium_cookies:
        cookies[cookie['name']] = cookie['value']    
    return cookies



def get_posts(url):    
    cookies = get_cookies()
    response = requests.get(url, cookies=cookies)
    return response

#url
url = "http://greenpagesqaadmin.wm.com/eAgent/"
kb = 'Pacific%20Northwest%20British%20Columbia'
KB = kb.replace('%20',' ')
doc_id = '40c00f50-c823-11e9-74c6-000000000000'
# authentication 
login(url)
# get response
response = get_posts(f'{url}/iq/Ellington/request.do?create=kb:{kb}&view()=r[case{doc_id}]')
#close application

with open(f'{KB} {doc_id}.html','w', encoding="utf-8") as f:
    f.write(response.text)
driver.close()

