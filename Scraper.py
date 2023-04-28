import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def format_search_string(string):
    if "/" in string:
        return string.split("/")[0]
    else:
        return string


class Scraper:
    __url = "https://tureng.com/en/turkish-english"
    __search_bar_xpath = '//*[@id="searchTerm"]'
    __result_table_xpath = '//*[@id="englishResultsTable"]'

    def __init__(self):
        options = uc.ChromeOptions()
        # options.add_argument('--headless')
        self.driver = uc.Chrome(use_subprocess=True, options=options)
        self.driver.get(self.__url)
        self.driver.maximize_window()

    def fetch_result(self, word_to_search):
        formatted_word = format_search_string(word_to_search)
        search_bar = self.driver.find_element(By.XPATH, self.__search_bar_xpath)
        search_bar.send_keys(formatted_word)
        search_bar.send_keys(Keys.ENTER)
        result_table = self.driver.find_element(By.XPATH, self.__result_table_xpath)
        rows = result_table.find_elements(By.TAG_NAME, "tr")
        counter = 0
        turkish_equals = []
        for row in rows:
            if counter == 5:
                break
            if row.text == "" or row.text.startswith("Category English Turkish"):
                continue
            else:
                counter = counter + 1
                turkish_equals.append(row.text.split(".")[1].strip())
        return turkish_equals

    def close_driver(self):
        self.driver.close()
