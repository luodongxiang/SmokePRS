#encoding=utf-8
from selenium import webdriver  #导入webdriver模块
from selenium.webdriver.common.keys import Keys #导入Keys模块
from selenium.common.exceptions import NoSuchElementException   #导入异常类
import traceback    #导入traceback堆栈异常类
import time
import sys  #导入sys系统模块
reload(sys) #重新加载sys模块
sys.setdefaultencoding("utf-8") #设置系统默认编码方式为“utf-8”方式


class TestPRS(object):
    def __init__(self): #定义init方法
        try:
            global logFile  # 将日志文件logFile定义为全局变量
            logFile = open("log", "w")  # 定义文件对象
            #time.asctime() 返回为可读的当前时间，参数默认为本地时间
            logFile.write("\n" + time.asctime() + "  ----------------------------------------------   Begin Test  ----------------------------------------------\n\n")
            logFile.write(u"------TestPRS类实例化init方法开始执行：------\n")
            # 定义url
            url = "http://sitsso.uce.cn/omg-sso-main/toLogin.action?systemCode=PRS&refUrl=http://prs.sit.uce.cn/prs-common-main/login/loginAuthc.do"
            self.driver = webdriver.Chrome()  # 启动chrome浏览器
            self.driver.maximize_window()  # 窗口最大化
            self.driver.get(url)  # 访问url
            self.driver.implicitly_wait(10) #隐式等待10S，只需设置一次则在driver周期中都有效
            time.sleep(3)  # 等待3S
            assert self.driver.title.find(u"优速统一登录平台-登录") >= 0, u"打开登录界面网页错误"  # 断言打开界面是否成功
        except AssertionError,e:
            logFile.write(u"失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------TestPRS类实例化init方法测试通过Success！------\n")


    def login(self):    #登录界面
        try:
            username = "019404"  # 定义登录用户名-总部身份
            password = "UC48690&"  # 定义登录密码
            logFile.write(u"------登录界面开始执行：------\n")
            self.driver.find_element_by_id("userName").send_keys(username)  # 输入用户名
            self.driver.find_element_by_id("password").send_keys(password)  # 输入密码
            self.driver.find_element_by_id("btnLogin").click()  # 点击登录
            time.sleep(5)  # 等待5S
            # 断言打开界面是否成功
            assert self.driver.title.find(u"定价与结算管理系统") >= 0, "输入用户名、密码进入PRS系统错误"
        except NoSuchElementException,e:
            logFile.write(u"登录失败Fail:\n" + traceback.format_exc() + "\n")
        except AssertionError,e:
            logFile.write(u"登录失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"登录失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------登录界面测试通过Success！------\n")


    def quitBrowser(self):  #退出浏览器
        try:
            self.driver.quit()  #退出浏览器
        except Exception,e:
            logFile.write(u"退出浏览器失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"\n------退出浏览器测试通过Success！------\n")
        finally:
            #time.asctime() 返回为可读的当前时间，参数默认为本地时间
            logFile.write("\n" + time.asctime() + "  ----------------------------------------------  Test Over   ----------------------------------------------\n\n\n")
            logFile.close()



#----------------------------------------------------------------------以下为账单模块--------------------------------------------------------------------------

    def tongHangZhangDan(self): #同行账单
        try:
            logFile.write(u"------同行账单开始执行：------\n")
            # 打开同行账单界面
            self.driver.find_element_by_xpath('//*[@id="311"]/a').click()  # 点击账单结算管理
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="12297"]/a').click()  # 点击分成账单
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="261"]/a').click()  # 点击同行出货账单编辑
            time.sleep(3)

            # 进入同行账单测试
            self.driver.switch_to.frame(self.driver.find_element_by_id('indextab261'))  # 跳转到iframe内
            assert u"同行所属网点" in self.driver.page_source,u"同行所属网点断言失败"  # 断言“同行所属网点”是否在页面源码中
            #设置变量chaXun
            chaXun = self.driver.find_element_by_link_text(u'查询')   #通过文本链接元素定位
            chaXun.click()  # 点击查询
            #等待5S
            time.sleep(5)


            #测试查询条件
            for i in range(3):
                #寄件财务中心
                jiJiancwzx = self.driver.find_element_by_id('_easyui_textbox_input10')
                jiJiancwzx.click()  #点击
                jiJiancwzx.send_keys(Keys.ARROW_DOWN)   #鼠标按键下
                #寄件分拨中心
                jiJianfbzx = self.driver.find_element_by_id('_easyui_textbox_input11')
                jiJianfbzx.click()  #点击
                jiJianfbzx.send_keys(Keys.ARROW_DOWN)   #鼠标按键下
                #寄件结算点
                jiJianjsd = self.driver.find_element_by_id('_easyui_textbox_input12')
                jiJianjsd.click()   #点击
                jiJianjsd.send_keys(Keys.ARROW_DOWN)    #鼠标按键下
                #派件财务中心
                paiJiancwzx = self.driver.find_element_by_id('_easyui_textbox_input13')
                paiJiancwzx.click() #点击
                paiJiancwzx.send_keys(Keys.ARROW_DOWN)  #鼠标按键下
                #派件分拨中心
                paiJianfbzx = self.driver.find_element_by_id('_easyui_textbox_input14')
                paiJianfbzx.click() #点击
                paiJianfbzx.send_keys(Keys.ARROW_DOWN)  #鼠标按键下
                #派件结算点
                paiJianjsd = self.driver.find_element_by_id('_easyui_textbox_input15')
                paiJianjsd.click()  #点击
                paiJianjsd.send_keys(Keys.ARROW_DOWN)   #鼠标按键下
                #同行所属网点
                tongHangsswd = self.driver.find_element_by_id('_easyui_textbox_input16')
                tongHangsswd.click()    #点击
                tongHangsswd.send_keys(Keys.ARROW_DOWN) #鼠标按键下
                #点击查询
                chaXun.click()
                time.sleep(3)   #等待3S


            #测试运单编号查询是否有查询结果
            billcode = 'LDX2018041012'
            self.driver.find_element_by_id('billCode').send_keys(billcode)  #在运单编号输入框中输入运单编号
            time.sleep(1)
            # 点击查询
            chaXun.click()
            #等待3S
            time.sleep(3)
            #点击清除单号
            # self.driver.find_element_by_xpath('//*[@id="formFindDictType"]/div/div[1]/a/div').click()
            # time.sleep(1)
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[2]/div').text == billcode,u"运单编号断言失败" #断言运单编号
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[5]/div').text == u"虎门",u"寄件结算点断言失败" #断言寄件结算点
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[7]/div').text == u"广园一1",u"同行所属网点断言失败"  #断言同行所属网点
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[14]/div/a').text == "50",u"同行管理费断言失败"   #断言同行管理费

            #定义变量jiSuan重新计算分配额
            jiSuan = self.driver.find_element_by_xpath('//*[@id="tlbDictType"]/div/a[1]/span/span[1]')
            jiSuan.click()   #未选中数据，点击重新计算分配额
            time.sleep(1)
            #断言弹窗内容是否相同
            assert self.driver.find_element_by_xpath("/html/body/div[19]/div[2]/div[2]/p").text == u"请选择数据！",u"弹窗内容断言失败"
            time.sleep(1)
            self.driver.find_element_by_link_text(u"确定").click()     #文字超链接元素定位
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').click()  # 点击表格上方复选框选中数据
            time.sleep(1)
            jiSuan.click()   #点击重新计算分配额
            time.sleep(1)
            # self.driver.find_element_by_link_text("取消").click() #点击取消
            self.driver.find_element_by_xpath('/html/body/div[19]/div[3]/a[1]/span/span').click() #点击确定
            time.sleep(3)


            # self.driver.find_element_by_xpath('//*[@id="reportButton"]/span/span[1]').click()   #点击导出按钮
            # time.sleep(1)
            # self.driver.find_element_by_xpath('//*[@id="openExportNameButton"]/a[1]/span/span[1]').click()  #点击确定
            # time.sleep(3)


            # 关闭 同行账单标签页
            self.driver.switch_to.default_content()     #跳回到默认iframe内——关闭标签页一定要跳出同行账单的iframe
            #方法一：使用js语句关闭
            js = "document.getElementsByClassName('tabs-close')[0].click()"
            self.driver.execute_script(js)  #调用execute_script()方法
            # #方法二：使用xpath方式定位
            # self.driver.find_element_by_xpath('//*[@id="mainTab"]/div[1]/div[3]/ul/li[2]/a[2]').click()
            time.sleep(2)


        except NoSuchElementException,e:
            logFile.write(u"同行账单执行失败Fail:\n" + traceback.format_exc() + "\n")
        except AssertionError,e:
            logFile.write(u"同行账单执行失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"同行账单执行失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------同行账单测试通过Success！------\n")


    def yiErJiJiJianZhangDan(self): #一二级网点寄件账单
        try:
            logFile.write(u"------一二级网点寄件账单开始执行：------\n")
            self.driver.switch_to.default_content() #跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="229"]/a').click()   #点击一二级网点寄件账单
            time.sleep(2)
            self.driver.switch_to.frame('indextab229')  #跳转到一二级寄件账单iframe内
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="formFindDictType"]/div/div[2]/table/tbody/tr[4]/td[3]/a/span').click()  #点击查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"一二级寄件账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"一二级寄件账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------一二级网点寄件账单测试通过Success！------\n")


    def yiErJiPaiJianZhangDan(self):    #一二级派件账单
        try:
            logFile.write(u"------一二级网点派件账单开始执行：------\n")
            self.driver.switch_to.default_content() #跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="230"]/a').click()   #点击一二级网点派件账单
            time.sleep(2)
            self.driver.switch_to.frame('indextab230')  #跳转到一二级派件账单iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"一二级派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"一二级派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------一二级派件账单测试通过Success！------\n")


    def zhangDanBianJi(self):    #账单编辑
        try:
            logFile.write(u"------账单编辑开始执行：------\n")
            self.driver.switch_to.default_content() #跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"运单结算").click()  #点击运单结算
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'账单编辑').click()  #点击账单编辑
            time.sleep(2)
            self.driver.switch_to.frame('indextab205')  #跳转到账单编辑iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------账单编辑测试通过Success！------\n")


    def shiXiaoPaiFeiPaiJianZhangDan(self):  #时效派费派件账单
        try:
            logFile.write(u"------时效派费派件账单开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"时效派费派件账单").click()  # 点击 时效派费派件账单
            time.sleep(2)
            self.driver.switch_to.frame('indextab1000026001')  # 跳转到时效派费派件账单iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"时效派费派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"时效派费派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------时效派费派件账单测试通过Success！------\n")


    def wangDianChuHuoDuiZhang(self):  #网点出货对账
        try:
            logFile.write(u"------网点出货对账开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"网点出货对账").click()  # 点击 网点出货对账
            time.sleep(2)
            self.driver.switch_to.frame('indextab208')  # 跳转到网点出货对账iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"网点出货对账失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"网点出货对账失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------网点出货对账测试通过Success！------\n")


    def wangDianPaiJianDuiZhang(self):  #网点派件对账
        try:
            logFile.write(u"------网点派件对账开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"网点派件对账").click()  # 点击 网点派件对账
            time.sleep(2)
            self.driver.switch_to.frame('indextab220')  # 跳转到网点派件对账iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"网点派件对账失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"网点派件对账失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------网点派件对账测试通过Success！------\n")


    def zhangDanTiaoZheng(self):  #账单调整
        try:
            logFile.write(u"------账单调整开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"账单调整").click()  # 点击 账单调整
            time.sleep(2)
            self.driver.switch_to.frame('indextab330')  # 跳转到账单调整iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"账单调整失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"账单调整失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------账单调整测试通过Success！------\n")


    def zhiDaPaiFeiZhangDanBianJi(self):  #直达派费账单编辑
        try:
            logFile.write(u"------直达派费账单编辑开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"直达派费").click()  # 点击 直达派费
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'直达派费账单编辑').click()  #点击 直达派费账单编辑
            time.sleep(2)
            self.driver.switch_to.frame('indextab260')  # 跳转到直达派费账单编辑iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"直达派费账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"直达派费账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------直达派费账单编辑测试通过Success！------\n")


    def zhiDaPaiFeiJieSuanChaXun(self):  #直达派费结算查询
        try:
            logFile.write(u"------直达派费结算查询开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'直达派费结算查询').click()  #点击 直达派费结算查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab259')  # 跳转到直达派费结算查询iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"直达派费结算查询失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"直达派费结算查询失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------直达派费结算查询测试通过Success！------\n")


    def zhongZhuanZhangDanChaXun(self):  #中转账单查询
        try:
            logFile.write(u"------中转账单查询开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"中转账单").click()  # 点击 中转账单
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'中转账单查询').click()  #点击 中转账单查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab327')  # 跳转到中转账单查询iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"中转账单查询失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"中转账单查询失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------中转账单查询测试通过Success！------\n")


    def zhongZhuanZhangDanJieSuan(self):  #中转账单结算
        try:
            logFile.write(u"------中转账单结算开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'中转账单结算').click()  #点击 中转账单结算
            time.sleep(2)
            self.driver.switch_to.frame('indextab328')  # 跳转到中转账单结算iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"中转账单结算失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"中转账单结算失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------中转账单结算测试通过Success！------\n")


    def guDingFeiYongKouKuan(self):  #固定费用扣款
        try:
            logFile.write(u"------固定费用扣款开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'其他费用').click()  #点击 其他费用
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'固定费用扣款').click()    #点击 固定费用扣款
            time.sleep(2)
            self.driver.switch_to.frame('indextab235')  # 跳转到固定费用扣款iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"固定费用扣款失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"固定费用扣款失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------固定费用扣款测试通过Success！------\n")


    def guDingFeiYongMingXiWeiHu(self):  #固定费用明细维护
        try:
            logFile.write(u"------固定费用明细维护开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'固定费用明细维护').click()    #点击 固定费用明细维护
            time.sleep(2)
            self.driver.switch_to.frame('indextab236')  # 跳转到固定费用明细维护iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"固定费用明细维护失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"固定费用明细维护失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------固定费用明细维护测试通过Success！------\n")


    def guDingFeiYongKouKuanJiLu(self):  #固定费用扣款记录
        try:
            logFile.write(u"------固定费用扣款记录开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'固定费用扣款记录').click()    #点击 固定费用扣款记录
            time.sleep(2)
            self.driver.switch_to.frame('indextab237')  # 跳转到固定费用扣款记录iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"固定费用扣款记录失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"固定费用扣款记录失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------固定费用扣款记录测试通过Success！------\n")


    def xiTongShiYongFeiZhangDan(self):  #系统使用费账单
        try:
            logFile.write(u"------系统使用费账单开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'系统使用费账单').click()    #点击 系统使用费账单
            time.sleep(2)
            self.driver.switch_to.frame('indextab198')  # 跳转到系统使用费账单iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"系统使用费账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"系统使用费账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------系统使用费账单测试通过Success！------\n")


    def daiShouKuanJiFangWangDian(self):  #代收款账单编辑(寄方网点)
        try:
            logFile.write(u"------ 代收款账单编辑(寄方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收账单').click()    #点击 代收账单
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(寄方网点)').click()     #点击 代收款账单编辑(寄方网点)
            time.sleep(2)
            self.driver.switch_to.frame('indextab160')  # 跳转到 代收款账单编辑(寄方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(寄方网点) 测试通过Success！------\n")


    def daiShouKuanJiFangZhongXin(self):  #代收款账单编辑(寄方中心)
        try:
            logFile.write(u"------ 代收款账单编辑(寄方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(寄方中心)').click()     #点击 代收款账单编辑(寄方中心)
            time.sleep(2)
            self.driver.switch_to.frame('indextab207')  # 跳转到 代收款账单编辑(寄方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(寄方中心) 测试通过Success！------\n")


    def daiShouKuanPaiFangZhongXin(self):  #代收款账单编辑(派方中心)
        try:
            logFile.write(u"------ 代收款账单编辑(派方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(派方中心)').click()     #点击 代收款账单编辑(派方中心)
            time.sleep(2)
            self.driver.switch_to.frame('indextab209')  # 跳转到 代收款账单编辑(派方中心) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(派方中心) 测试通过Success！------\n")


    def daiShouKuanPaiFangWangDian(self):  #代收款账单编辑(派方网点)
        try:
            logFile.write(u"------ 代收款账单编辑(派方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(派方网点)').click()     #点击 代收款账单编辑(派方网点)
            time.sleep(2)
            self.driver.switch_to.frame('indextab210')  # 跳转到 代收款账单编辑(派方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(派方网点) 测试通过Success！------\n")


    def daiShouKuanZhiTuiShenDan(self):  #代收款直退审单
        try:
            logFile.write(u"------ 代收款直退审单 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退').click()     #点击 代收款直退
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退审单').click()     #点击 代收款直退审单
            time.sleep(2)
            self.driver.switch_to.frame('indextab216')  # 跳转到 代收款直退审单 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款直退审单 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退审单 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退审单 测试通过Success！------\n")


    def daiShouKuanZhiTuiDengJi(self):  #代收款直退登记
        try:
            logFile.write(u"------ 代收款直退登记 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退登记').click()     #点击 代收款直退登记
            time.sleep(2)
            self.driver.switch_to.frame('indextab219')  # 跳转到 代收款直退登记 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款直退登记 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退登记 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退登记 测试通过Success！------\n")


    def daiShouKuanZhiTuiShenHe(self):  #代收款直退审核
        try:
            logFile.write(u"------ 代收款直退审核 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退审核').click()     #点击 代收款直退审核
            time.sleep(2)
            self.driver.switch_to.frame('indextab222')  # 跳转到 代收款直退审核 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款直退审核 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退审核 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退审核 测试通过Success！------\n")


    def daiShouKuanZhiTuiChaXun(self):  #代收款直退查询
        try:
            logFile.write(u"------ 代收款直退查询 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退查询').click()     #点击 代收款直退查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab238')  # 跳转到 代收款直退查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收款直退查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退查询 测试通过Success！------\n")


    def daiShouDuiZhangChaXun(self):  #代收对账单查询
        try:
            logFile.write(u"------ 代收对账单查询 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收对账单查询').click()     #点击 代收对账单查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab324')  # 跳转到 代收对账单查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"代收对账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收对账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收对账单查询 测试通过Success！------\n")


    def daoFuKuanJiFangWangDian(self):  #到付款账单编辑(寄方网点)
        try:
            logFile.write(u"------ 到付款账单编辑(寄方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单').click()     #点击 到付款账单
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(寄方网点)').click()     #点击 到付款账单编辑(寄方网点)
            time.sleep(2)
            self.driver.switch_to.frame('indextab280')  # 跳转到 到付款账单编辑(寄方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(寄方网点) 测试通过Success！------\n")


    def daoFuKuanJiFangZhongXin(self):  #到付款账单编辑(寄方中心)
        try:
            logFile.write(u"------ 到付款账单编辑(寄方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(寄方中心)').click()     #点击 到付款账单编辑(寄方中心)
            time.sleep(2)
            self.driver.switch_to.frame('indextab281')  # 跳转到 到付款账单编辑(寄方中心) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(寄方中心) 测试通过Success！------\n")


    def daoFuKuanPaiFangWangDian(self):  #到付款账单编辑(派方网点)
        try:
            logFile.write(u"------ 到付款账单编辑(派方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(派方网点)').click()     #点击 到付款账单编辑(派方网点)
            time.sleep(2)
            self.driver.switch_to.frame('indextab282')  # 跳转到 到付款账单编辑(派方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(派方网点) 测试通过Success！------\n")


    def daoFuKuanPaiFangZhongXin(self):  #到付款账单编辑(派方中心)
        try:
            logFile.write(u"------ 到付款账单编辑(派方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(派方中心)').click()     #点击 到付款账单编辑(派方中心)
            time.sleep(2)
            self.driver.switch_to.frame('indextab283')  # 跳转到 到付款账单编辑(派方中心) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)
        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(派方中心) 测试通过Success！------\n")


    def feiYongTiaoZhengDengJi(self):   #费用调整登记
        try:
            logFile.write(u"------ 费用调整登记 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整').click()  #点击 费用调整
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整登记').click()    #点击 费用调整登记
            time.sleep(2)
            self.driver.switch_to.frame('indextab223')  #跳转到 费用调整 iframe内
            time.sleep(1)
            self.driver.find_element_by_id('add').click()   #点击 添加
            time.sleep(2)

            #定义变量-调整类型tiaoZhengLeiXin
            # tiaoZhengLeiXin = self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input24"]')
            # tiaoZhengLeiXin.click()    #点击调整类型
            # time.sleep(1)
            # tiaoZhengLeiXin.send_keys(Keys.ARROW_DOWN)
            # time.sleep(1)
            # tiaoZhengLeiXin.send_keys(Keys.ENTER)
            # time.sleep(1)

            #运单编号
            self.driver.find_element_by_id('billCode').send_keys('LDX2018042515')
            time.sleep(1)

            #定义变量-登记方
            # dengJiFang = self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input42"]')
            # dengJiFang.click()
            # dengJiFang.send_keys(Keys.ARROW_DOWN)
            # time.sleep(1)
            # #定义变量-接收方
            # jieShouFang = self.driver.find_element_by_xpath('//*[@id="_easyui_textbox_input43"]')
            # jieShouFang.click()
            # jieShouFang.send_keys(Keys.ARROW_DOWN)
            # time.sleep(1)



        except NoSuchElementException,e:
            logFile.write(u"费用调整登记 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整登记 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整登记 测试通过Success！------\n")


    def feiYongTiaoZhengJieShouFangQueRen(self):   #费用调整接收方确认
        try:
            logFile.write(u"------ 费用调整接收方确认 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整接收方确认').click()    #点击 费用调整接收方确认
            time.sleep(2)
            self.driver.switch_to.frame('indextab224')  #跳转到 费用调整接收方确认 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"费用调整接收方确认 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整接收方确认 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整接收方确认 测试通过Success！------\n")


    def feiYongTiaoZhengDengJiFangChaXun(self):   #费用调整登记方查询
        try:
            logFile.write(u"------ 费用调整登记方查询 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整登记方查询').click()    #点击 费用调整登记方查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab225')  #跳转到 费用调整登记方查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"费用调整登记方查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整登记方查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整登记方查询 测试通过Success！------\n")


    def feiYongTiaoZhengShenHeKouKuan(self):   #费用调整审核扣款（接收方中心）
        try:
            logFile.write(u"------ 费用调整审核扣款（接收方中心） 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整审核扣款').click()    #点击 费用调整审核扣款（接收方中心）
            time.sleep(2)
            self.driver.switch_to.frame('indextab226')  #跳转到 费用调整审核扣款（接收方中心） iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"费用调整审核扣款（接收方中心） 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整审核扣款（接收方中心） 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整审核扣款（接收方中心） 测试通过Success！------\n")


    def huiDanZhangDanChaXun(self):   #回单账单查询
        try:
            logFile.write(u"------ 回单账单查询 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'回单账单查询').click()    #点击 回单账单查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab150')  #跳转到 回单账单查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"回单账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"回单账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------回单账单查询 测试通过Success！------\n")


    def zhanDianCaiWuShuJuChongTui(self):   #站点财务数据重推
        try:
            logFile.write(u"------ 站点财务数据重推 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'站点财务数据重推').click()    #点击 站点财务数据重推
            time.sleep(2)
            self.driver.switch_to.frame('indextab1000013000')  #跳转到 站点财务数据重推 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"站点财务数据重推 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"站点财务数据重推 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------站点财务数据重推 测试通过Success！------\n")


    def zhangDanFeiYongPiDai(self):   #账单费用批带
        try:
            logFile.write(u"------ 账单费用批带 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'账单费用批带').click()    #点击 账单费用批带
            time.sleep(2)
            self.driver.switch_to.frame('indextab329')  #跳转到 账单费用批带 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"账单费用批带 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"账单费用批带 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------账单费用批带 测试通过Success！------\n")


    def shuJuDaoChuChaKan(self):   #数据导出查看
        try:
            logFile.write(u"------ 数据导出查看 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'数据导出查看').click()    #点击 数据导出查看
            time.sleep(2)
            self.driver.switch_to.frame('indextab1000012000')  #跳转到 数据导出查看 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"数据导出查看 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"数据导出查看 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------数据导出查看 测试通过Success！------\n")


    def wangDianGuanXiChaXun(self):   #网点关系查询
        try:
            logFile.write(u"------ 网点关系查询 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'网点关系查询').click()    #点击 网点关系查询
            time.sleep(2)
            self.driver.switch_to.frame('indextab1000035000')  #跳转到 网点关系查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)
        except NoSuchElementException,e:
            logFile.write(u"网点关系查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"网点关系查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------网点关系查询 测试通过Success！------\n")


    def yeWuGuiZeLeiXing(self):   #业务规则类型
        try:
            logFile.write(u"------ 业务规则类型 开始执行：------\n")
            self.driver.find_element_by_partial_link_text(u'基础数据管理').click()     #点击 基础数据管理
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'业务规则管理').click()     #点击 业务规则管理
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'业务规则类型').click()    #点击 业务规则类型
            time.sleep(2)
            self.driver.switch_to.frame('indextab155')  #跳转到 业务规则类型 iframe内
            time.sleep(1)
            assert u"业务规则名称:" in self.driver.page_source,u"业务规则名称-断言失败" #添加断言

            for i in xrange(2): #设置循环
                #测试 新增 功能
                yeWuGuiZeBiaoHao = "autoTest" + str(i)
                self.driver.find_element_by_partial_link_text(u'新增').click()       #点击 新增
                time.sleep(2)
                self.driver.find_element_by_id('_easyui_textbox_input2').send_keys(yeWuGuiZeBiaoHao)  #业务规则编码 输入测试内容
                time.sleep(1)
                self.driver.find_element_by_id('_easyui_textbox_input3').send_keys(u'自动化测试')    #业务规则名称 输入测试内容
                time.sleep(1)
                #定义变量 参数类型
                canShuLeiXing =  self.driver.find_element_by_xpath('//*[@id="formBusiness"]/table/tbody/tr[3]/td[2]/span/span/a')
                canShuLeiXing.click()    #点击参数类型下拉框
                time.sleep(1)
                self.driver.find_element_by_id('_easyui_combobox_i1_1').click()     #选择下拉内容 布尔型
                time.sleep(1)
                baoCun = self.driver.find_element_by_link_text(u'保存')   #定义变量 保存
                baoCun.click()        #点击 保存
                time.sleep(2)

                #在查询条件中输入业务规则编号
                chaXunTiaoJian = self.driver.find_element_by_id('_easyui_textbox_input1')   #定义查询条件 变量
                chaXunTiaoJian.clear()      #清空查询条件
                time.sleep(1)
                chaXunTiaoJian.send_keys(yeWuGuiZeBiaoHao) #在查询条件中输入编号
                time.sleep(1)
                chaXun = self.driver.find_element_by_link_text(u'查询')
                chaXun.click()    #点击 查询
                time.sleep(1)
                # 添加断言 判断是否新增成功
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[5]/div').text == yeWuGuiZeBiaoHao,u"新增失败"
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[7]/div').text == u"布尔型",u"新增失败"
                time.sleep(1)

                #测试 修改 功能
                self.driver.find_element_by_name('id').click()      #点击 勾选
                time.sleep(1)
                self.driver.find_element_by_partial_link_text(u'修改').click()    #点击 修改
                time.sleep(2)
                canShuLeiXing.click()   #点击 参数类型
                time.sleep(1)
                self.driver.find_element_by_id('_easyui_combobox_i1_5').click()     #修改为 字符型
                time.sleep(1)
                baoCun.click()  #点击 保存
                time.sleep(2)
                chaXun.click()  #点击 查询
                time.sleep(1)
                #添加断言 判断是否修改成功
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[7]/div').text == u'字符型',u"修改失败"
                time.sleep(1)

                #测试 删除 功能
                self.driver.find_element_by_name('id').click()      #点击 勾选
                time.sleep(1)
                self.driver.find_element_by_partial_link_text(u'删除').click()    #点击 删除
                time.sleep(2)
                self.driver.find_element_by_partial_link_text(u'确定').click()    #点击 确定
                time.sleep(2)
                chaXun.click()  #点击 查询
                time.sleep(1)
                #添加断言 判断是否删除成功
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[5]/div').text != yeWuGuiZeBiaoHao,u"删除失败"
                time.sleep(1)


            #关闭业务规则类型界面
            self.driver.switch_to.default_content() #一定要跳出iframe，才能关闭界面
            #定义js变量为js语句
            js = "document.getElementsByClassName('tabs-close')[0].click()"
            #执行js脚本
            self.driver.execute_script(js)  #调用execute_script()方法
            time.sleep(1)

        except NoSuchElementException,e:
            logFile.write(u"业务规则类型 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"业务规则类型 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------业务规则类型 测试通过Success！------\n")


    def yeWuGuiZeSheZhi(self):   #业务规则设置
        try:
            logFile.write(u"------ 业务规则设置 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转进入默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'业务规则设置').click()    #点击 业务规则设置
            time.sleep(2)
            self.driver.switch_to.frame('indextab159')  #跳转到 业务规则设置 iframe内
            time.sleep(1)
            assert u"启用:" in self.driver.page_source,u"启用-断言失败" #添加断言

            #查询按钮
            chaXun = self.driver.find_element_by_link_text(u'查询')
            chaXun.click()  #点击 查询
            time.sleep(2)   #等待2S

            #定义变量-测试数据业务规则名称
            testDataYeWuGuiZeMingCheng = 'AAAAA'

            #测试新增模块
            self.driver.find_element_by_partial_link_text(u'新增').click()    #点击新增
            time.sleep(1)
            #变量-业务规则名称
            yeWuGuiZeMingCheng = self.driver.find_element_by_id('_easyui_textbox_input8')
            yeWuGuiZeMingCheng.send_keys(testDataYeWuGuiZeMingCheng)    #业务规则名称 输入
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r5-2-0"]/td[2]/div').click()   #选择 业务规则名称
            time.sleep(1)
            #变量-参数值-新增界面
            # 此元素为动态id，直接使用id定位失败，需使用xpath定位：基于上层元素；
            canShuZhiXinZheng = self.driver.find_element_by_xpath('//*[@id="txtbusinessValue"]/span/input[1]')
            canShuZhiXinZheng.send_keys('90')
            time.sleep(1)
            #变量-网点名称
            wangDianMingCheng = self.driver.find_element_by_id('_easyui_textbox_input7')
            wangDianMingCheng.send_keys(u'总部')  # 网点名称 输入内容
            time.sleep(1)
            canShuZhiXinZheng.click()   #点击 参数值，便于选中 网点名称内容
            time.sleep(1)
            #定义是否启用
            qiYong = self.driver.find_element_by_id('checkboxState')
            qiYong.click() #选择 启用
            time.sleep(1)
            #定义-保存
            baoCun = self.driver.find_element_by_partial_link_text(u'保存')
            baoCun.click()    #点击 保存
            time.sleep(2)

            #测试修改模块
            #查询条件-网点名称
            chaXunWangDianMingCheng = self.driver.find_element_by_id('_easyui_textbox_input6')
            chaXunWangDianMingCheng.send_keys(u"总部")
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r4-2-0"]/td[4]/div').click()   #选择 总部
            time.sleep(1)
            #查询条件-业务规则名称
            chaXunGuiZe = self.driver.find_element_by_id('_easyui_textbox_input4')
            chaXunGuiZe.send_keys(testDataYeWuGuiZeMingCheng)  #输入内容
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[2]/div').click()   #选择内容
            time.sleep(1)
            #查询条件-启用
            qiYongXiaLa = self.driver.find_element_by_xpath('//*[@id="formFindRules"]/div[1]/span[3]/span/a')
            qiYongXiaLa.click() #点击 启用 下拉
            time.sleep(1)
            #启用-选择 是
            self.driver.find_element_by_id('_easyui_combobox_i1_2').click() #点击 是
            time.sleep(1)
            chaXun.click()  #点击查询
            time.sleep(2)
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[9]/div').text == testDataYeWuGuiZeMingCheng,u"业务规则名称断言失败"
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[10]/div').text == "90",u"参数值断言失败"
            #断言 启用状态-使用xpath定位，再使用get_attribute获取属性值 进行判断
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div/input').get_attribute("value") == "1",u"启用状态 断言失败"
            time.sleep(1)


            #勾选
            gouXuan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input')
            gouXuan.click() #点击勾选
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'修改').click()    #点击 修改按钮
            time.sleep(1)
            #参数值-修改界面
            canShuZhiXiuGai = self.driver.find_element_by_xpath('//*[@id="txtbusinessValue"]/span/input[1]')
            canShuZhiXiuGai.clear() #清空 参数值内容
            time.sleep(1)
            canShuZhiXiuGai.send_keys('91')   #修改 参数值
            time.sleep(1)
            qiYong.click()  #取消 启用
            time.sleep(1)
            baoCun.click()  #点击 保存
            time.sleep(2)

            # 查询条件-启用 选择否
            qiYongXiaLa.click()
            time.sleep(1)
            self.driver.find_element_by_id('_easyui_combobox_i1_1').click()  #选择 否
            time.sleep(1)
            chaXun.click()  #点击 查询
            time.sleep(2)
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[10]/div').text == "91",u"参数值断言失败"
            #断言 启用状态-使用xpath定位，再使用get_attribute获取属性值 进行判断
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div/input').get_attribute("value") == "0",u"启用状态 断言失败"
            time.sleep(1)


            #测试 删除模块
            gouXuan.click() #点击 勾选
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'删除').click()    #点击 删除
            time.sleep(1)
            self.driver.find_element_by_link_text(u'确定').click()    #点击 确定
            time.sleep(1)
            qiYongXiaLa.click() #点击查询条件-启用 下拉
            time.sleep(1)
            self.driver.find_element_by_id('_easyui_combobox_i1_0').click()  #选择 全部
            time.sleep(1)
            chaXun.click()  #点击 查询
            time.sleep(2)
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[9]/div').text != testDataYeWuGuiZeMingCheng,u"业务规则名称断言失败"
            time.sleep(1)


            #关闭业务规则设置界面
            self.driver.switch_to.default_content() #一定要跳出iframe，才能关闭界面
            #使用xpath定位关闭界面
            self.driver.find_element_by_xpath('//*[@id="mainTab"]/div[1]/div[3]/ul/li[2]/a[2]').click()
            time.sleep(1)

        except NoSuchElementException,e:
            logFile.write(u"业务规则设置 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"业务规则设置 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------业务规则设置 测试通过Success！------\n")