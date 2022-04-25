import os
from dotenv import load_dotenv
from urlbox import UrlboxClient
import imgkit
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.ravsam.in')
driver.save_screenshot('my_screenshot.png')
driver.quit()


options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://news.ycombinator.com/")
driver.save_screenshot('hn_homepage.png')
driver.quit()


imgkit.from_url('https://youtube.com', 'youtube.png')


load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

urlbox_client = UrlboxClient(api_key=API_KEY, api_secret=API_SECRET)
response = urlbox_client.get({"url": "https://urlbox.io/"})

with open("screenshot.png", "wb") as f:
    f.write(response.content)
