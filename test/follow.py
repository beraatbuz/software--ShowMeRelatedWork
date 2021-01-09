import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FollowTest(unittest.TestCase):
    def test_follow(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://127.0.0.1:5000/login")
        driver.maximize_window()
        driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[2]/input").send_keys("enes")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[4]/input").send_keys("1111111111111111")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div[5]/button").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/ul/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div/div/div[16]/div/div[2]/form/button/strong").click()
        driver.find_element_by_xpath("/html/body/nav/div/div/div/span[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[4]/ul/li[3]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[2]/form/button/strong").click()
        print("Follow/Unfollow test is successfully completed!")
        time.sleep(2)
        driver.quit()



if __name__ == "__main__":
    unittest.main()


