#encoding=utf-8
from testPRS import TestPRS   #从login文件中导入TestPRS类

if __name__ == '__main__':
    for i in range(1):
        test = TestPRS()    #类实例化
        test.login()    #登录

        # 以下为基础数据模块调用方法，业务规则类型为该模块的入口
        test.yeWuGuiZeLeiXing()             #执行 业务规则类型
        test.yeWuGuiZeSheZhi()              #执行 业务规则设置
        test.huiLvWeiHu()               #执行 汇率维护

        #以下为账单模块调用方法，同行账单为该模块的入口
        # test.tongHangZhangDan()     #执行同行账单

        test.quitBrowser()      #退出浏览器