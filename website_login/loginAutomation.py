from selenium import webdriver
import yml

conf = yaml.load(open('loginDetails.yml'))
myInstaEmail = conf['insta_user']['email']
myInstaPass = conf['insta_user']['password']

driver  = webdriver.Chrome()

def login(url, usernameId, username, passwordId, password, submit_buttonId): 
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()


login("https://www.instagram.com", "username" , myInstaEmail, "pass", myInstaPass, "loginbutton")
