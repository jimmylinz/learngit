import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver

class Test(unittest.TestCase):
    def setUp(self):

        self.verificationError = []
        self.accept_next_alert = True


    def setTest(self):

        #webdriver = self.driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("baidu.com")

    def testdown(self):
        self.driver.quit()

if __name__=="__main__":
    testunit = unittest.TestSuite()
    testunit.addTests(Test("testTest"))
    filename = ""
    fp = open(filename,"wb")
    runner = HTMLTestRunner(
        stream=fp,
        title='test',
        description='s'
    )
    runner.run(testunit)
    fp.close()