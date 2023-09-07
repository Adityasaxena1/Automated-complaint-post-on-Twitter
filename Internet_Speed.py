from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self, url):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url)
        self.twitter_password = "Uttarakhand2255@"
        self.twitter_username = "Adi1594538"


    def get_internet_speed(self):
        cookie_cancel = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[3]/button")
        cookie_cancel.click()

        time.sleep(3)
        go = self.driver.find_element(By.XPATH,
                                      value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()
        time.sleep(50)

        download_speed = self.driver.find_element(By.XPATH,
                                                  value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.driver.quit()
        return download_speed

    def twitter_login(self):
        time.sleep(5)
        login = self.driver.find_element(By.XPATH,
                                         value="/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
        login.click()

        time.sleep(5)
        username_input = self.driver.find_element(By.XPATH,
                                                  value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username_input.send_keys(self.twitter_username)

        time.sleep(2)

        next_button = self.driver.find_element(By.XPATH,
                                               value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()

        time.sleep(2)
        password_input = self.driver.find_element(By.XPATH,
                                                  value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_input.send_keys(self.twitter_password)

        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH,
                                                value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        login_button.click()

    def twitter_post(self, post_description):
        time.sleep(5)
        post_button = self.driver.find_element(By.XPATH,
                                               value="/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        post_button.click()

        time.sleep(5)
        post = self.driver.find_element(By.XPATH,
                                        value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div")
        post.send_keys(post_description)

        time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH,
                                                value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]")
        tweet_button.click()
