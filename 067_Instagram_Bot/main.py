from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "salmansaeed1359@gmail.com"
PASSWORD = "mYKz3v3iAIDO2tZg"

URL = "https://app.100daysofpython.dev/services/share-a-naan/welcome"
TARGET_FOLLOWERS = "elaineducasse"


class InstagramFollowersBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(URL)
        self.driver.implicitly_wait(10)

        username_input = self.driver.find_element(By.XPATH, '/html/body/div/aside/div/form/input[1]')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.XPATH, '/html/body/div/aside/div/form/input[2]')
        password_input.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.XPATH, '/html/body/div/aside/div/form/button')
        login_button.click()
        save_info = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info:
            save_info[0].click()
        time.sleep(1)

        notifications = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications[0].click()

        def login(self):
            pass

        def find_followers(self):
            pass

        def follow(self):
            pass


instagram_bot = InstagramFollowersBot()
instagram_bot.login()
