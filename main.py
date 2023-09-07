from Internet_Speed import InternetSpeedTwitterBot
import time

PROMISE_DOWN = 30

Internet_bot = InternetSpeedTwitterBot("https://www.speedtest.net/")

time.sleep(5)
speed = Internet_bot.get_internet_speed()

twitter_bot = InternetSpeedTwitterBot("https://twitter.com/")
twitter_bot.twitter_login()

twitter_bot.twitter_post(
    f"Hey Internet Provider my internet download speed is {speed}Mbps, when I pay for {PROMISE_DOWN}Mbps? ")
