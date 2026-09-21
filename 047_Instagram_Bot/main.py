from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException

USERNAME = "example@email.com"
PASSWORD = "yourPassword"

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

    def find_followers(self):
        self.driver.get(f"{URL.split('/welcome')[0]}/u/{TARGET_FOLLOWERS}/followers")
        time.sleep(2)

        modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()


instagram_bot = InstagramFollowersBot()
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()
