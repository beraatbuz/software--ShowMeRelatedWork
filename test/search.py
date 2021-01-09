import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SearchTest(unittest.TestCase):
    def test_search_url_failure(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://127.0.0.1:5000/dashboard")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='url']/div/form[1]/input").send_keys("https://www.resealedsfctual.com")
        driver.find_element_by_xpath("//*[@id='url']/div/form[1]/div/button/strong").click()
        print("Paper URL Search Failure test is successfully completed!")
        time.sleep(2)
        driver.quit()

    def test_search_author(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://127.0.0.1:5000/dashboard")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='warningAuthors']/button").click()
        driver.find_element_by_xpath("//*[@id='Demo']/a[4]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='author']/div/form[1]/input").send_keys("Samer Eid Dahiyat")
        driver.find_element_by_xpath("//*[@id='author']/div/form[1]/div/button/strong").click()
        driver.find_element_by_xpath("//*[@id='home']/div[2]/div/div/div/table/tbody/tr[1]/td/button").click()
        driver.find_element_by_xpath("//*[@id='home']/div[2]/div/div/div/table/tbody/tr[1]/td/button").click()
        print("Author Search test is successfully completed!")
        time.sleep(2)
        driver.quit()

    def test_recommended_paper(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://127.0.0.1:5000/dashboard")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='url']/div/form[2]/button/strong").click()
        print("Recommended Paper test is successfully completed!")
        time.sleep(2)
        driver.quit()

    def test_search_url(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://127.0.0.1:5000/dashboard")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='url']/div/form[1]/input").send_keys("https://www.researchgate.net/publication/326319011_Intellectual_capital_knowledge_management_and_social_capital_within_the_ICT_sector_in_Jordan")
        driver.find_element_by_xpath("//*[@id='url']/div/form[1]/div/button/strong").click()
        print("Paper URL Search test is successfully completed!")
        time.sleep(2)
        driver.quit()

    def test_search_keyword(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://127.0.0.1:5000/dashboard")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='warningAuthors']/button").click()
        driver.find_element_by_xpath("//*[@id='Demo']/a[3]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='keyword']/div/form[1]/input").send_keys("ai")
        driver.find_element_by_xpath("//*[@id='keyword']/div/form[1]/div/button/strong").click()
        driver.find_element_by_xpath("//*[@id='home']/div[2]/div/div/div/table/tbody/tr[1]/td/button").click()
        print("Keyword Search test is successfully completed!")
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    unittest.main()


