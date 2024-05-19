from selenium.webdriver.common import By

class WikiPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.ID,"searchInput")
        self.search_button = (By.XPATH,"//button[@class='pure-button pure-button-primary-progressive']").click()

    def open_page(self, url):
        self.driver.get(url)

    def enter_query(self, query):
        self.driver.find_element(self.search_bar).send_keys(query)

    def click_search(self):
        self.driver.find_element(self.search_button).click()