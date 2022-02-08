from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys 


class student():
    def __init__(self,id ,password,driver):
        self.login_id = id
        self.password = password
        driver = driver

    def login(self):
        driver.get("https://kitsgunturerp.com/BeesERP/Login.aspx")
        username = driver.find_element_by_id("txtUserName")
        username.send_keys(self.login_id)
        next = driver.find_element_by_id("btnNext")
        next.click()
        password = driver.find_element_by_id("txtPassword")
        password.send_keys(self.password)
        submit=driver.find_element_by_id("btnSubmit")
        submit.click()

    def getAttendence(self):
        attendence_element = driver.find_element_by_id("ctl00_cpStud_lblTotalPercentage")
        attendence = attendence_element.get_attribute('innerHTML')
        print(attendence)
    
    def close_website(self):
        driver.close()
        
    def getDetails(self):
        myinfo_elem = driver.find_element_by_id('ctl00_cpHeader_ucStud_lnkYourInformation')
        myinfo = myinfo_elem.get_attribute('innerHTML')
        print(myinfo)

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

s =student(sys.argv[2], sys.argv[2], driver)
s.login()
s.close_website()

