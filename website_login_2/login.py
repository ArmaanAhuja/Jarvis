from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

name = "ahujaarmaan_2707"
passW = "Rougewarden_2707_insta"

driver = webdriver.Chrome()

class instaBot(): 
    def __init__(self, userName, passWord):
        self.username = userName
        self.password = passWord

    def login(self): 
        driver.get("https://www.instagram.com")
        time.sleep(5)
        userElem = driver.find_element("xpath",'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        userElem.send_keys(self.username)

        userPass = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        userPass.send_keys(self.password)

        loginButton = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        loginButton.click()
        time.sleep(10)

        msgs = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a')
        msgs.click()

        time.sleep(10)
        home =  driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/span/div/a')
        home.click()

        hom
        time.sleep(100)
        # i = input()

    


armaan = instaBot(name, passW)
# driver.get("https://www.instagram.com")
armaan.login()
# time.sleep(100)
# time.sleep(100)
