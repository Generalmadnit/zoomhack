"""

project stopped because i dont getting how to automate greatlearning 
website .site elements have only classes.
"""


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys



class bot():
    def __init__(self, id,password ,driver):
        self.id = id
        self.password  = password
        driver = driver 

    def login(self):
        """
        LOgin to greating olympus - great learning 
        """
        driver.get("https://olympus.greatlearning.in/dashboard")
        login_id  = driver.find_element_by_id("login")
        login_id.clear()
        login_id.send_keys(self.id)
        login_password = driver.find_element_by_id("password")
        login_password.clear()
        login_password.send_keys(self.password)
        login_button = driver.find_element_by_id("reCaptchaLoginSubmitButton")
        login_button.click()


    def authenticate(self):
        """
        It will authenticate your greatlearning account
        """
        code = input()
        code_field = driver.find_element_by_id("mfaCode")
        code_field.send_keys(code)
        code_field.send_keys(Keys.RETURN)
       
  


PATH  = "C:\Program Files (x86)\chromedriver" 
driver= webdriver.Chrome(PATH)  

a =bot("baramsivarami@gmail.com" ,"7032753722",driver)
a.login()
a.authenticate()

# a.changeToOnlineclass()
# a = bot("kakumanulalitha@gmail.com","K.MRT.31",driver)
# a.login()
# a =bot("gantahanumantharao123@gmail.com" ,"hanumanth123",driver)
# a.login()
# a.changeToOnlineclass()
# a.authenticate()