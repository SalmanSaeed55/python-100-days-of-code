from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        cookie_accept = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie_accept.click()

        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]')
        go_button.click()
        time.sleep(60)

        close_popup = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div/div/div[2]/a')
        close_popup.click()

        self.down = self.driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3'
        ).text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text
        return self.down, self.up


bot = InternetSpeedBot()
download, upload = bot.get_internet_speed()
print(f"Download: {download}, Upload: {upload}")