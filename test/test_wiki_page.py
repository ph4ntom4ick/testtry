from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import By
import time
import pytest
from pages.wiki_page import WikiPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Chromservice(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

url = "https://www.wikipedia.org/"
query = "python"

def test_wiki_search(driver):
    wiki_page = WikiPage(driver)
    time.sleep(2)
    wiki_page.open_page(url)
    time.sleep(2)
    wiki_page.enter_query(query)
    time.sleep(2)
    wiki_page.click_search()
    time.sleep(2)
