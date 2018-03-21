# coding:utf-8
from selenium import webdriver
import unittest,time,sys
sys.path.append("..")
from page.loginPage import LoginPage

class Test1(unittest.TestCase):
    u'''搜索测试'''

    #@classmethod
    def setUp(self):
        self.driver = webdriver.Ie()
    

    def test_02(self):
        try:
            driver=self.driver
            po=LoginPage(driver)
            po.start()
            po.log_home()
            po.log_user("qupan")
            po.log_pass("qp66666")
            po.log_click()
            time.sleep(3)
            po.end()
        except Exception as e:
            po.end()
            po.error(e)
            raise



    #@classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



