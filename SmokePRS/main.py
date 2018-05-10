#encoding=utf-8
import unittest     #导入单元测试类unittest
import testPRS

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for i in range(1):
            test = testPRS.TestPRS()    #实例化TestPRS
            test.login()    #调用登录
            test.tonghang() #调用同行账单
            test.yierjijijian() #调用一二级寄件账单
            test.quitBrowser()  #退出浏览器

if __name__ == '__main__':
    unittest.main()