from selenium import webdriver
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        '''
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        '''
        self.verificationErrors = []
        self.accept_next_alert = True
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        time.sleep(1)
        """

    def testBaidu(self):
       # driver = self.driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        time.sleep(1)
        driver.find_element_by_id("kw").send_keys("帅哥明")
        time.sleep(3)
        driver.find_element_by_id("su").click()
        time.sleep(10)
        driver.close()
    def testDown(self):
        self.driver.quit()
        self.assertEqual([],self,verificationErrors)


if __name__=="__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("testBaidu"))
    filename = "E:\\learngit\\"+ u"测试报告" + ".html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(
                     stream=fp,
                     title='测试报告',
                     description='用例执行情况：')
    runner.run(testunit)
    fp.close()



