from selenium import webdriver
from time import sleep
from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint

class Bot():

    links = []

    comments = [
        'Thanks for posting!', ';)'
    ]

    def __init__(self):
        self.login('michaelcurtismcnulty',pw)
        self.like_comment_by_hashtag('programming')

    def login(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://instagram.com/')
        sleep(5)
        usernameInput = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        usernameInput.sendKeys(username)
        sleep(1)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.sendKeys(password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(5)
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").sendKeys(self.comments[randint(0,1)])
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()

def main():
    while True:
        myBot = Bot()
        sleep(60*60)

if __name__ == '__main__':
    main()
