from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# class for the Twitter bot
class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # with the use of the FireFox instance we can interact with the FireFox browser
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        user_name = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        user_name.clear()
        password.clear()
        user_name.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


mc = TwitterBot('USERNAME', 'PASSWORD')
mc.login()
mc.like_tweet('bernie')