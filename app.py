# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# class for different methods
class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# interact with Firefox browser
        self.bot = webdriver.Firefox()

def login(self):
    bot = self.bot
    bot.get('https://twitter.com/')
    time.sleep(3)
    user_name = bot.find_element_by_class_name('email-input')
    password = bot.find_element_by_name('session[password]')
    user_name.clear()
    password.clear()
    user_name.send.keys(self.username)
    password.send.keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)



mc = TwitterBot('USERNAME', 'PASSWORD')
mc = login() 
