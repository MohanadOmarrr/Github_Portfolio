import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ESTIMATED_DOWN = 60
ESTIMATED_UP = 10

TWITTER_URL = "https://twitter.com/login"
SPEED_TEST_URL = "https://www.speedtest.net/"
EMAIL = "mohanadomark@yahoo.com"
PASSWORD = "mohanad124578"


class InternetTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="F:\Development\chrome driver\chromedriver")
        self.down = 0
        self.up = 0

    def test_internet(self):
        self.driver.get(SPEED_TEST_URL)

        time.sleep(5)
        button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]'
                                                    '/a/span[4]')
        button.click()
        time.sleep(40)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div'
                                                       '/div/div[2]/div[3]/div[3]/div/div[3]/div'
                                                       '/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def twitter_login(self):
        self.driver.get(TWITTER_URL)

        time.sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'div input')
        email_input.send_keys(f"{EMAIL}{Keys.ENTER}")

        time.sleep(5)
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'div input')
        password_input.send_keys(f"{PASSWORD}{Keys.ENTER}")

    def post_complaint(self):
        time.sleep(5)

        label = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]'
                                                   '/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/'
                                                   'div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label')

        label.send_keys(f"Why I am receiving {self.down}/Down {self.up}/Up "
                        f"while I should receive {ESTIMATED_DOWN}/Down {ESTIMATED_UP}/Up ?!")