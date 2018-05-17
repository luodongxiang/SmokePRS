#encoding=utf-8
from selenium import webdriver  #导入webdriver模块
from selenium.webdriver.common.keys import Keys #导入Keys模块
from selenium.common.exceptions import NoSuchElementException   #导入异常类
import traceback    #导入traceback堆栈异常类
import time     #导入time模块
import datetime     #导入日期模块
import sys  #导入sys系统模块
reload(sys) #重新加载sys模块
sys.setdefaultencoding("utf-8") #设置系统默认编码方式为“utf-8”方式


class TestPRS(object):
    # 定义init方法
    def __init__(self):
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


    # 登录界面
    def login(self):
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


    # 关闭浏览器
    def quitBrowser(self):
        try:
            self.driver.quit()  #关闭浏览器
        except Exception,e:
            logFile.write(u"关闭浏览器失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"\n------关闭浏览器测试通过Success！------\n")
        finally:
            #time.asctime() 返回为可读的当前时间，参数默认为本地时间
            logFile.write("\n" + time.asctime() + "  ----------------------------------------------  Test Over   ----------------------------------------------\n\n\n")
            logFile.close()


    #关闭 标签页
    def closeTagPage(self):
        try:
            # 关闭 标签页
            self.driver.switch_to.default_content()  # 跳回到默认iframe内——关闭标签页一定要跳出账单的iframe
            # 方法一：使用js语句关闭
            js = "document.getElementsByClassName('tabs-close')[0].click()"
            self.driver.execute_script(js)  # 调用execute_script()方法
            # #方法二：使用xpath方式定位
            # self.driver.find_element_by_xpath('//*[@id="mainTab"]/div[1]/div[3]/ul/li[2]/a[2]').click()
            time.sleep(2)
        except Exception, e:
            logFile.write(u"关闭标签页执行失败Fail:\n" + traceback.format_exc() + "\n")


    #判断 页面元素是否存在
    def isElementExist(self,by,value):
        try:
            self.driver.find_element(by = by,value = value)   #去找界面元素
        except NoSuchElementException,e:
            return False        #没有找到元素，返回False
        else:
            return True     #找到了元素，返回True


    #定义点击全部链接按钮的方法
    def clickLinkAnNiu(self,linkWords,sleepTime = 2):
        try:
            anNiu = self.driver.find_element_by_link_text(linkWords)
            anNiu.click()  # 点击 按钮
            time.sleep(sleepTime)   #等待时间
        except NoSuchElementException,e:
            logFile.write(u"按钮定位失败Fail:\n" + traceback.format_exc() + "\n")


    #定义点击部分链接按钮的方法
    def clickPartialLinkAnNiu(self,partialLinkWords,sleepTime = 1):
        try:
            anNiu = self.driver.find_element_by_partial_link_text(partialLinkWords)
            anNiu.click()  # 点击 按钮
            time.sleep(sleepTime)   #等待时间
        except NoSuchElementException,e:
            logFile.write(u"按钮定位失败Fail:\n" + traceback.format_exc() + "\n")


    #定义初次进入三级模块下菜单的方法
    def firstEnterThirdMenu(self,menu1,menu2,menu3,menu3FrameID,minSleepTime = 1,maxSleepTime = 2):
        try:
            self.driver.find_element_by_partial_link_text(menu1).click()  # 点击 一级菜单
            time.sleep(minSleepTime)    #等待最小时间
            self.driver.find_element_by_partial_link_text(menu2).click()  # 点击 二级菜单
            time.sleep(minSleepTime)    #等待最小时间
            self.driver.find_element_by_partial_link_text(menu3).click()  # 点击 三级菜单
            time.sleep(maxSleepTime)    #等待最大时间
            self.driver.switch_to.frame(menu3FrameID)  # 跳转到 三级菜单的 iframe内
            time.sleep(minSleepTime)    #等待最小时间
        except NoSuchElementException,e:
            logFile.write(u"按钮定位失败Fail:\n" + traceback.format_exc() + "\n")


    #定义从三级模块退出并进入相同一级模块下菜单的方法
    def thirdQuitEnterSameFirstMenu(self,secondOrThirdMenu,menuFrameID,minSleepTime = 1,maxSleepTime = 2):
        try:
            self.driver.switch_to.default_content()  # 跳转进入默认iframe内
            self.driver.find_element_by_partial_link_text(secondOrThirdMenu).click()  # 点击 二级或三级菜单
            time.sleep(maxSleepTime)    #等待最大时间
            self.driver.switch_to.frame(menuFrameID)  # 跳转到 二级或三级菜单 iframe内
            time.sleep(minSleepTime)    #等待最小时间
        except NoSuchElementException, e:
            logFile.write(u"元素定位失败Fail:\n" + traceback.format_exc() + "\n")


    #定义循环按下键选择下拉内容
    def enterDownToChoice(self,by,value,num,minSleepTime = 0.1,maxSleepTime = 0.2):
        try:
            element = self.driver.find_element(by = by,value = value)   #元素定位方法及值
            element.click()     #点击 元素
            #循环num次按下键
            for i in range(num):
                element.send_keys(Keys.ARROW_DOWN)  # 模拟键盘按键-下
                time.sleep(minSleepTime)    #等待最小时间
            element.send_keys(Keys.ENTER)  # 模拟键盘按键-回车
            time.sleep(maxSleepTime)    #等待最大时间
        except NoSuchElementException, e:
            logFile.write(u"元素定位失败Fail:\n" + traceback.format_exc() + "\n")


    #定义通过id 使用js语句删除元素的只读属性
    def deleteReadonlyById(self,elementId):
        #elementId 为字符串型
        try:
            deleteReadonly = "document.getElementById(" + elementId + ").removeAttribute('readonly')"
            self.driver.execute_script(deleteReadonly)  # 调用execute_script方法 执行js语句
        except Exception, e:
            pass



    #----------------------------------------------------------------------以下为账单模块--------------------------------------------------------------------------
    # 同行账单
    def tongHangZhangDan(self):
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
            self.driver.switch_to.frame(u'indextabPRS同行出货账单编辑')  # 跳转到iframe内
            assert u"同行所属网点" in self.driver.page_source,u"同行所属网点断言失败"  # 断言“同行所属网点”是否在页面源码中
            #设置变量chaXun
            chaXun = self.driver.find_element_by_link_text(u'查询')   #通过文本链接元素定位
            chaXun.click()  # 点击查询
            #等待5S
            time.sleep(5)


            # 测试查询条件
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


            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"同行账单执行失败Fail:\n" + traceback.format_exc() + "\n")
        except AssertionError,e:
            logFile.write(u"同行账单执行失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"同行账单执行失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------同行账单测试通过Success！------\n")


    # 一二级网点寄件账单
    def yiErJiJiJianZhangDan(self):
        try:
            logFile.write(u"------一二级网点寄件账单开始执行：------\n")
            #调用公用方法，进入 一二级网点寄件账单
            self.thirdQuitEnterSameFirstMenu(u"一二级网点寄件账单",u'indextabPRS一二级网点寄件账单',1,2)
            self.clickLinkAnNiu(u"查询",3)    #点击查询


            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"一二级寄件账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"一二级寄件账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------一二级网点寄件账单测试通过Success！------\n")


    # 一二级派件账单
    def yiErJiPaiJianZhangDan(self):
        try:
            logFile.write(u"------一二级网点派件账单开始执行：------\n")
            #调用公用方法，进入一二级网点派件账单
            self.thirdQuitEnterSameFirstMenu(u"一二级网点派件账单",u'indextabPRS一二级网点派件账单',1,2)
            self.clickLinkAnNiu(u"查询",3)    #点击查询


            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"一二级派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"一二级派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------一二级派件账单测试通过Success！------\n")


    # 账单编辑
    def zhangDanBianJi(self):
        try:
            logFile.write(u"------账单编辑开始执行：------\n")
            self.driver.switch_to.default_content() #跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"运单结算").click()  #点击运单结算
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'账单编辑').click()  #点击账单编辑
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS账单编辑')  #跳转到账单编辑iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------账单编辑测试通过Success！------\n")


    # 时效派费派件账单
    def shiXiaoPaiFeiPaiJianZhangDan(self):
        try:
            logFile.write(u"------时效派费派件账单开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"时效派费派件账单").click()  # 点击 时效派费派件账单
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS时效派费派件账单')  # 跳转到时效派费派件账单iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"时效派费派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"时效派费派件账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------时效派费派件账单测试通过Success！------\n")


    # 网点出货对账
    def wangDianChuHuoDuiZhang(self):
        try:
            logFile.write(u"------网点出货对账开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"网点出货对账").click()  # 点击 网点出货对账
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS网点出货对账')  # 跳转到网点出货对账iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"网点出货对账失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"网点出货对账失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------网点出货对账测试通过Success！------\n")


    # 网点派件对账
    def wangDianPaiJianDuiZhang(self):
        try:
            logFile.write(u"------网点派件对账开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"网点派件对账").click()  # 点击 网点派件对账
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS网点派件对账')  # 跳转到网点派件对账iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"网点派件对账失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"网点派件对账失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------网点派件对账测试通过Success！------\n")


    # 账单调整
    def zhangDanTiaoZheng(self):
        try:
            logFile.write(u"------账单调整开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"账单调整").click()  # 点击 账单调整
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS账单调整')  # 跳转到账单调整iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"账单调整失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"账单调整失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------账单调整测试通过Success！------\n")


    # 直达派费账单编辑
    def zhiDaPaiFeiZhangDanBianJi(self):
        try:
            logFile.write(u"------直达派费账单编辑开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"直达派费").click()  # 点击 直达派费
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'直达派费账单编辑').click()  #点击 直达派费账单编辑
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS直达派费账单编辑')  # 跳转到直达派费账单编辑iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"直达派费账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"直达派费账单编辑失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------直达派费账单编辑测试通过Success！------\n")


    # 直达派费结算查询
    def zhiDaPaiFeiJieSuanChaXun(self):
        try:
            logFile.write(u"------直达派费结算查询开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'直达派费结算查询').click()  #点击 直达派费结算查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS直达派费结算查询')  # 跳转到直达派费结算查询iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"直达派费结算查询失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"直达派费结算查询失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------直达派费结算查询测试通过Success！------\n")


    # 中转账单查询
    def zhongZhuanZhangDanChaXun(self):
        try:
            logFile.write(u"------中转账单查询开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u"中转账单").click()  # 点击 中转账单
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'中转账单查询').click()  #点击 中转账单查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS中转账单查询')  # 跳转到中转账单查询iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"中转账单查询失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"中转账单查询失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------中转账单查询测试通过Success！------\n")


    # 中转账单结算
    def zhongZhuanZhangDanJieSuan(self):
        try:
            logFile.write(u"------中转账单结算开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'中转账单结算').click()  #点击 中转账单结算
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS中转账单结算')  # 跳转到中转账单结算iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"中转账单结算失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"中转账单结算失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------中转账单结算测试通过Success！------\n")


    # 固定费用扣款
    def guDingFeiYongKouKuan(self):
        try:
            logFile.write(u"------固定费用扣款开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'其他费用').click()  #点击 其他费用
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'固定费用扣款').click()    #点击 固定费用扣款
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS固定费用扣款')  # 跳转到固定费用扣款iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"固定费用扣款失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"固定费用扣款失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------固定费用扣款测试通过Success！------\n")


    # 固定费用明细维护
    def guDingFeiYongMingXiWeiHu(self):
        try:
            logFile.write(u"------固定费用明细维护开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'固定费用明细维护').click()    #点击 固定费用明细维护
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS固定费用明细维护')  # 跳转到固定费用明细维护iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"固定费用明细维护失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"固定费用明细维护失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------固定费用明细维护测试通过Success！------\n")


    # 固定费用扣款记录
    def guDingFeiYongKouKuanJiLu(self):
        try:
            logFile.write(u"------固定费用扣款记录开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'固定费用扣款记录').click()    #点击 固定费用扣款记录
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS固定费用扣款记录')  # 跳转到固定费用扣款记录iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"固定费用扣款记录失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"固定费用扣款记录失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------固定费用扣款记录测试通过Success！------\n")


    # 系统使用费账单
    def xiTongShiYongFeiZhangDan(self):
        try:
            logFile.write(u"------系统使用费账单开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'系统使用费账单').click()    #点击 系统使用费账单
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS系统使用费账单')  # 跳转到系统使用费账单iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"系统使用费账单失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"系统使用费账单失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------系统使用费账单测试通过Success！------\n")


    # 代收款账单编辑(寄方网点)
    def daiShouKuanJiFangWangDian(self):
        try:
            logFile.write(u"------ 代收款账单编辑(寄方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收账单').click()    #点击 代收账单
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(寄方网点)').click()     #点击 代收款账单编辑(寄方网点)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款账单编辑(寄方网点)')  # 跳转到 代收款账单编辑(寄方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(寄方网点) 测试通过Success！------\n")


    # 代收款账单编辑(寄方中心)
    def daiShouKuanJiFangZhongXin(self):
        try:
            logFile.write(u"------ 代收款账单编辑(寄方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(寄方中心)').click()     #点击 代收款账单编辑(寄方中心)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款账单编辑(寄方中心)')  # 跳转到 代收款账单编辑(寄方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(寄方中心) 测试通过Success！------\n")


    # 代收款账单编辑(派方中心)
    def daiShouKuanPaiFangZhongXin(self):
        try:
            logFile.write(u"------ 代收款账单编辑(派方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(派方中心)').click()     #点击 代收款账单编辑(派方中心)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款账单编辑(派方中心)')  # 跳转到 代收款账单编辑(派方中心) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(派方中心) 测试通过Success！------\n")


    # 代收款账单编辑(派方网点)
    def daiShouKuanPaiFangWangDian(self):
        try:
            logFile.write(u"------ 代收款账单编辑(派方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款账单编辑(派方网点)').click()     #点击 代收款账单编辑(派方网点)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款账单编辑(派方网点)')  # 跳转到 代收款账单编辑(派方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款账单编辑(派方网点) 测试通过Success！------\n")


    # 代收款直退审单
    def daiShouKuanZhiTuiShenDan(self):
        try:
            logFile.write(u"------ 代收款直退审单 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退').click()     #点击 代收款直退
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退审单').click()     #点击 代收款直退审单
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款直退审单')  # 跳转到 代收款直退审单 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款直退审单 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退审单 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退审单 测试通过Success！------\n")


    # 代收款直退登记
    def daiShouKuanZhiTuiDengJi(self):
        try:
            logFile.write(u"------ 代收款直退登记 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退登记').click()     #点击 代收款直退登记
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款直退登记')  # 跳转到 代收款直退登记 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款直退登记 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退登记 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退登记 测试通过Success！------\n")


    # 代收款直退审核
    def daiShouKuanZhiTuiShenHe(self):
        try:
            logFile.write(u"------ 代收款直退审核 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退审核').click()     #点击 代收款直退审核
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款直退审核')  # 跳转到 代收款直退审核 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款直退审核 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退审核 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退审核 测试通过Success！------\n")


    # 代收款直退查询
    def daiShouKuanZhiTuiChaXun(self):
        try:
            logFile.write(u"------ 代收款直退查询 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收款直退查询').click()     #点击 代收款直退查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收款直退查询')  # 跳转到 代收款直退查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收款直退查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收款直退查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收款直退查询 测试通过Success！------\n")


    # 代收对账单查询
    def daiShouDuiZhangChaXun(self):
        try:
            logFile.write(u"------ 代收对账单查询 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'代收对账单查询').click()     #点击 代收对账单查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS代收对账单查询')  # 跳转到 代收对账单查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"代收对账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"代收对账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------代收对账单查询 测试通过Success！------\n")


    # 到付款账单编辑(寄方网点)
    def daoFuKuanJiFangWangDian(self):
        try:
            logFile.write(u"------ 到付款账单编辑(寄方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单').click()     #点击 到付款账单
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(寄方网点)').click()     #点击 到付款账单编辑(寄方网点)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS到付款账单编辑(寄方网点)')  # 跳转到 到付款账单编辑(寄方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(寄方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(寄方网点) 测试通过Success！------\n")


    # 到付款账单编辑(寄方中心)
    def daoFuKuanJiFangZhongXin(self):
        try:
            logFile.write(u"------ 到付款账单编辑(寄方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(寄方中心)').click()     #点击 到付款账单编辑(寄方中心)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS到付款账单编辑(寄方中心)')  # 跳转到 到付款账单编辑(寄方中心) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(寄方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(寄方中心) 测试通过Success！------\n")


    # 到付款账单编辑(派方网点)
    def daoFuKuanPaiFangWangDian(self):
        try:
            logFile.write(u"------ 到付款账单编辑(派方网点) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(派方网点)').click()     #点击 到付款账单编辑(派方网点)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS到付款账单编辑(派方网点)')  # 跳转到 到付款账单编辑(派方网点) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(派方网点) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(派方网点) 测试通过Success！------\n")


    # 到付款账单编辑(派方中心)
    def daoFuKuanPaiFangZhongXin(self):
        try:
            logFile.write(u"------ 到付款账单编辑(派方中心) 开始执行：------\n")
            self.driver.switch_to.default_content()  # 跳回到默认iframe框架内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'到付款账单编辑(派方中心)').click()     #点击 到付款账单编辑(派方中心)
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS到付款账单编辑(派方中心)')  # 跳转到 到付款账单编辑(派方中心) iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()  # 点击查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException, e:
            logFile.write(u"到付款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception, e:
            logFile.write(u"到付款账单编辑(派方中心) 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------到付款账单编辑(派方中心) 测试通过Success！------\n")


    # 费用调整登记
    def feiYongTiaoZhengDengJi(self):
        try:
            logFile.write(u"------ 费用调整登记 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整').click()  #点击 费用调整
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整登记').click()    #点击 费用调整登记
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS费用调整登记')  #跳转到 费用调整 iframe内
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

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"费用调整登记 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整登记 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整登记 测试通过Success！------\n")


    # 费用调整接收方确认
    def feiYongTiaoZhengJieShouFangQueRen(self):
        try:
            logFile.write(u"------ 费用调整接收方确认 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整接收方确认').click()    #点击 费用调整接收方确认
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS费用调整接收方确认')  #跳转到 费用调整接收方确认 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"费用调整接收方确认 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整接收方确认 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整接收方确认 测试通过Success！------\n")


    # 费用调整登记方查询
    def feiYongTiaoZhengDengJiFangChaXun(self):
        try:
            logFile.write(u"------ 费用调整登记方查询 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整登记方查询').click()    #点击 费用调整登记方查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS费用调整登记方查询')  #跳转到 费用调整登记方查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"费用调整登记方查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整登记方查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整登记方查询 测试通过Success！------\n")


    # 费用调整审核扣款（接收方中心）
    def feiYongTiaoZhengShenHeKouKuan(self):
        try:
            logFile.write(u"------ 费用调整审核扣款（接收方中心） 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'费用调整审核扣款').click()    #点击 费用调整审核扣款（接收方中心）
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS费用调整审核扣款（接收方中心）')  #跳转到 费用调整审核扣款（接收方中心） iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"费用调整审核扣款（接收方中心） 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"费用调整审核扣款（接收方中心） 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------费用调整审核扣款（接收方中心） 测试通过Success！------\n")


    # 回单账单查询
    def huiDanZhangDanChaXun(self):
        try:
            logFile.write(u"------ 回单账单查询 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'回单账单查询').click()    #点击 回单账单查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS回单账单查询')  #跳转到 回单账单查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"回单账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"回单账单查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------回单账单查询 测试通过Success！------\n")


    # 站点财务数据重推
    def zhanDianCaiWuShuJuChongTui(self):
        try:
            logFile.write(u"------ 站点财务数据重推 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'站点财务数据重推').click()    #点击 站点财务数据重推
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS站点财务数据重推')  #跳转到 站点财务数据重推 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"站点财务数据重推 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"站点财务数据重推 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------站点财务数据重推 测试通过Success！------\n")


    # 账单费用批带
    def zhangDanFeiYongPiDai(self):
        try:
            logFile.write(u"------ 账单费用批带 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'账单费用批带').click()    #点击 账单费用批带
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS账单费用批带')  #跳转到 账单费用批带 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"账单费用批带 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"账单费用批带 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------账单费用批带 测试通过Success！------\n")


    # 数据导出查看
    def shuJuDaoChuChaKan(self):
        try:
            logFile.write(u"------ 数据导出查看 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'数据导出查看').click()    #点击 数据导出查看
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS数据导出查看')  #跳转到 数据导出查看 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"数据导出查看 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"数据导出查看 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------数据导出查看 测试通过Success！------\n")


    # 网点关系查询
    def wangDianGuanXiChaXun(self):
        try:
            logFile.write(u"------ 网点关系查询 开始执行：------\n")
            self.driver.switch_to.default_content()     #跳转到默认iframe内
            time.sleep(1)
            self.driver.find_element_by_partial_link_text(u'网点关系查询').click()    #点击 网点关系查询
            time.sleep(2)
            self.driver.switch_to.frame(u'indextabPRS网点关系查询')  #跳转到 网点关系查询 iframe内
            time.sleep(1)
            self.driver.find_element_by_link_text(u'查询').click()    #点击 查询
            time.sleep(3)

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"网点关系查询 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"网点关系查询 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------网点关系查询 测试通过Success！------\n")


    # ----------------------------------------------------------------------以下为基础模块--------------------------------------------------------------------------
    # 业务规则类型
    def yeWuGuiZeLeiXing(self):
        try:
            logFile.write(u"------ 业务规则类型 开始执行：------\n")
            #调用公用方法，进入三级菜单业务规则类型界面
            self.firstEnterThirdMenu(u"基础数据管理",u"业务规则管理",u"业务规则类型",u"indextabPRS业务规则类型",1,2)
            assert u"业务规则名称:" in self.driver.page_source,u"业务规则名称-断言失败" #添加断言

            for i in xrange(1): #设置循环
                ##########  测试 新增 功能    ##########
                #定义变量-业务规则编号
                yeWuGuiZeBiaoHao = "autoTest" + str(i+1)
                self.clickPartialLinkAnNiu(u'新增',1)     #点击 新增
                # 业务规则编号 输入测试内容
                self.driver.find_element_by_id('_easyui_textbox_input2').send_keys(yeWuGuiZeBiaoHao)
                time.sleep(0.2)
                #定义变量-业务规则名称
                yeWuGuiZeMingCheng =  self.driver.find_element_by_id('_easyui_textbox_input3')
                yeWuGuiZeMingCheng.send_keys(u'自动化测试')    #业务规则名称 输入测试内容
                time.sleep(0.2)
                #定义变量 参数类型
                canShuLeiXing =  self.driver.find_element_by_xpath('//*[@id="formBusiness"]/table/tbody/tr[3]/td[2]/span/span/a')
                canShuLeiXing.click()    #点击参数类型下拉框
                time.sleep(0.5)
                self.driver.find_element_by_id('_easyui_combobox_i1_1').click()     #选择下拉内容 布尔型
                time.sleep(0.2)
                self.clickLinkAnNiu(u'保存',2)    #点击 保存

                #在查询条件中输入业务规则编号
                # 定义变量 查询条件
                chaXunTiaoJian = self.driver.find_element_by_id('_easyui_textbox_input1')
                chaXunTiaoJian.clear()      #清空查询条件
                chaXunTiaoJian.send_keys(yeWuGuiZeBiaoHao) #在查询条件中输入编号
                time.sleep(0.2)
                self.clickLinkAnNiu(u"查询",2)    #点击 查询
                # 添加断言 判断是否新增成功
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[5]/div').text == yeWuGuiZeBiaoHao,u"新增失败"
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[7]/div').text == u"布尔型",u"新增失败"


                ##########  测试 修改 功能    ##########
                self.driver.find_element_by_name('id').click()      #点击 勾选
                time.sleep(0.2)
                self.clickPartialLinkAnNiu(u'修改',1)      #点击 修改
                canShuLeiXing.click()   #点击 参数类型
                time.sleep(0.5)
                self.driver.find_element_by_id('_easyui_combobox_i1_5').click()     #修改为 字符型
                time.sleep(0.2)
                self.clickLinkAnNiu(u'保存',2)    #点击 保存
                self.clickLinkAnNiu(u'查询',2)    #点击 查询
                #添加断言 判断是否修改成功
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[7]/div').text == u'字符型',u"修改失败"


                ##########  测试 删除 功能    ##########
                self.driver.find_element_by_name('id').click()      #点击 勾选
                time.sleep(0.2)
                self.clickPartialLinkAnNiu(u'删除',1)      #点击 删除
                self.clickLinkAnNiu(u'确定',1)     #点击 确定
                self.clickLinkAnNiu(u'查询',2)    #点击 查询
                #添加断言 判断是否删除成功
                assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[5]/div').text != yeWuGuiZeBiaoHao,u"删除失败"

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"业务规则类型 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"业务规则类型 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------业务规则类型 测试通过Success！------\n")


    # 业务规则设置
    def yeWuGuiZeSheZhi(self):
        try:
            logFile.write(u"------ 业务规则设置 开始执行：------\n")
            #调用公用方法，进入同一级目录下的业务规则设置界面
            self.thirdQuitEnterSameFirstMenu(u'业务规则设置',u'indextabPRS业务规则设置',1,2)
            assert u"启用:" in self.driver.page_source,u"启用-断言失败" #添加断言

            #点击查询按钮
            self.clickLinkAnNiu(u"查询",2)

            #定义变量-测试数据业务规则名称
            testDataYeWuGuiZeMingCheng = 'AAAAA'


            ##########      测试  新增  功能      ##########
            self.clickPartialLinkAnNiu(u'新增',1)     #点击新增
            #变量-业务规则名称
            yeWuGuiZeMingCheng = self.driver.find_element_by_id('_easyui_textbox_input8')
            yeWuGuiZeMingCheng.send_keys(testDataYeWuGuiZeMingCheng)    #业务规则名称 输入
            time.sleep(0.5)
            # 选择 业务规则名称
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r5-2-0"]/td[2]/div').click()
            time.sleep(0.5)
            #变量-参数值-新增界面
            # 此元素为动态id，直接使用id定位失败，需使用xpath定位：基于上层元素；
            canShuZhiXinZheng = self.driver.find_element_by_xpath('//*[@id="txtbusinessValue"]/span/input[1]')
            canShuZhiXinZheng.send_keys('90')
            time.sleep(0.2)
            #变量-网点名称
            wangDianMingCheng = self.driver.find_element_by_id('_easyui_textbox_input7')
            wangDianMingCheng.send_keys(u'总部')  # 网点名称 输入内容
            time.sleep(0.5)
            canShuZhiXinZheng.click()   #点击 参数值，便于选中 网点名称内容
            time.sleep(0.5)
            #定义是否启用
            qiYong = self.driver.find_element_by_id('checkboxState')
            qiYong.click() #选择 启用
            time.sleep(0.2)
            self.clickLinkAnNiu(u'保存',2)     #点击 保存

            #查询条件-网点名称
            chaXunWangDianMingCheng = self.driver.find_element_by_id('_easyui_textbox_input6')
            chaXunWangDianMingCheng.send_keys(u"总部")
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r4-2-0"]/td[4]/div').click()   #选择 总部
            time.sleep(0.5)
            #查询条件-业务规则名称
            chaXunGuiZe = self.driver.find_element_by_id('_easyui_textbox_input4')
            chaXunGuiZe.send_keys(testDataYeWuGuiZeMingCheng)  #输入内容
            time.sleep(0.5)
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[2]/div').click()   #选择内容
            time.sleep(0.5)
            #查询条件-启用
            qiYongXiaLa = self.driver.find_element_by_xpath('//*[@id="formFindRules"]/div[1]/span[3]/span/a')
            qiYongXiaLa.click() #点击 启用 下拉
            time.sleep(0.5)
            #启用-选择 是
            self.driver.find_element_by_id('_easyui_combobox_i1_2').click() #点击 是
            time.sleep(0.5)
            # 点击查询按钮
            self.clickLinkAnNiu(u"查询", 2)
            #判断是否新增成功
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[9]/div').text == testDataYeWuGuiZeMingCheng,u"业务规则名称断言失败"
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[10]/div').text == "90",u"参数值断言失败"
            #断言 启用状态-使用xpath定位，再使用get_attribute获取属性值 进行判断
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div/input').get_attribute("value") == "1",u"启用状态 断言失败"


            ##########      测试 修改 功能    ##########
            #定义变量-勾选
            gouXuan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input')
            gouXuan.click() #点击勾选
            time.sleep(0.2)
            self.clickPartialLinkAnNiu(u'修改',1)     #点击 修改按钮
            #参数值-修改界面
            canShuZhiXiuGai = self.driver.find_element_by_xpath('//*[@id="txtbusinessValue"]/span/input[1]')
            canShuZhiXiuGai.clear() #清空 参数值内容
            canShuZhiXiuGai.send_keys('91')   #修改 参数值
            time.sleep(0.5)
            qiYong.click()  #取消 启用
            time.sleep(0.2)
            self.clickLinkAnNiu(u'保存',2)        #点击 保存

            # 查询条件-启用 选择否
            qiYongXiaLa.click()
            time.sleep(0.5)
            self.driver.find_element_by_id('_easyui_combobox_i1_1').click()  #选择 否
            time.sleep(0.5)
            self.clickLinkAnNiu(u"查询", 2)       # 点击查询按钮
            #判断是否修改成功
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[10]/div').text == "91",u"参数值断言失败"
            #断言 启用状态-使用xpath定位，再使用get_attribute获取属性值 进行判断
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div/input').get_attribute("value") == "0",u"启用状态 断言失败"


            ##########      测试 删除 功能    ##########
            gouXuan.click() #点击 勾选
            time.sleep(0.2)
            self.clickPartialLinkAnNiu(u'删除',1)     #点击 删除
            self.clickLinkAnNiu(u'确定',1)    #点击 确定
            qiYongXiaLa.click() #点击查询条件-启用 下拉
            time.sleep(0.5)
            self.driver.find_element_by_id('_easyui_combobox_i1_0').click()  #选择 全部
            time.sleep(0.5)
            self.clickLinkAnNiu(u"查询", 2)               # 点击   查询按钮
            #判断是否删除成功
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[9]/div').text != testDataYeWuGuiZeMingCheng,u"业务规则名称断言失败"

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"业务规则设置 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"业务规则设置 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------业务规则设置 测试通过Success！------\n")


    # 汇率维护
    def huiLvWeiHu(self):
        try:
            logFile.write(u"------ 汇率维护 开始执行：------\n")
            #调用公用方法，进入汇率维护界面
            self.thirdQuitEnterSameFirstMenu(u'汇率维护',u'indextabPRS汇率维护',1,2)
            assert u"返回今天" in self.driver.page_source,u"返回今天-断言失败" #添加断言
            #切换到汇率列表标签页
            self.clickLinkAnNiu(u"汇率列表",2)


            ##########      测试 查询 条件    ##########
            #调用公用方法，删除查询条件-原始货币的只读属性
            self.deleteReadonlyById("_easyui_textbox_input6")
            #调用公用按键方法，循环9次，选中英镑
            self.enterDownToChoice("id","_easyui_textbox_input6",9,0.1,0.2)
            self.clickLinkAnNiu(u"查询",2)    #点击 查询


            ##########  测试 新增  功能  ##########
            self.clickPartialLinkAnNiu(u"新增",1)     #点击 新增 按钮
            #调用公用方法，删除原始货币的只读属性
            self.deleteReadonlyById("_easyui_textbox_input7")
            #调用公用按键方法，循环9次，选中英镑
            self.enterDownToChoice("id","_easyui_textbox_input7",9,0.1,0.2)
            # 汇率元素定位
            huiLv = self.driver.find_element_by_id('_easyui_textbox_input1')
            # 生效日期元素定位
            shengXiaoRiQi = self.driver.find_element_by_id('_easyui_textbox_input3')
            # 失效日期元素定位
            shiXiaoRiQi = self.driver.find_element_by_id('_easyui_textbox_input4')
            huiLv.send_keys('8')                #汇率输入框中输入值
            time.sleep(0.2)
            #使用循环
            for i in xrange(100):
                # 定义测试日期-如果保存失败，则日期自加1，继续保存
                ceShiDate = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
                shengXiaoRiQi.clear()   #清空 生效日期
                shengXiaoRiQi.send_keys(ceShiDate)   #输入生效日期
                time.sleep(0.2)
                #点击汇率输入框，便于选中生效日期值
                huiLv.click()
                shiXiaoRiQi.clear() #清空 失效日期
                shiXiaoRiQi.send_keys(ceShiDate) #输入 失效日期
                time.sleep(0.2)
                #点击汇率输入框，便于选中失效日期值
                huiLv.click()
                self.clickLinkAnNiu(u"保存",2)    #点击 保存 按钮
                #调用该类公用方法，进行判断元素是否存在
                if self.isElementExist("partial link text",u"保存并继续") == False:
                    break       #如果元素不存在，则跳出该整个循坏
                else:
                    continue        #如果元素存在，则继续执行下个循坏
            #判断汇率是否等于新增时的汇率
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[8]/div').text == "8",u"汇率断言失败"
            #判断新增后审核状态是否等于未审核
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div').text == u"未审核",u"状态断言失败"


            ##########      测试   修改   功能  ##########
            # 勾选第一条数据
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[3]/div/input').click()
            time.sleep(0.2)
            self.clickPartialLinkAnNiu(u"修改",1)     #点击 修改 按钮
            huiLv.clear()       #清空汇率
            huiLv.send_keys('9')    #修改汇率
            time.sleep(0.2)   #等待时间
            self.clickLinkAnNiu(u"保存",2)    #点击 保存 按钮
            #判断与修改后的汇率是否相等
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[8]/div').text == "9",u"汇率断言失败"


            ##########      测试 审核 功能    ##########
            # 勾选第一条数据
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[3]/div/input').click()
            time.sleep(0.2)
            self.clickPartialLinkAnNiu(u"审核",1)     #点击 审核 按钮
            self.clickLinkAnNiu(u"确定",2)        #点击 确定 按钮
            #判断审核结果是否等于已审核
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div').text == u"已审核",u"审核状态断言失败"


            ##########      测试  取消审核  功能   ##########
            # 勾选第一条数据
            self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[3]/div/input').click()
            time.sleep(0.2)
            self.clickPartialLinkAnNiu(u"取消审核",1)       #点击 取消审核 按钮
            self.clickLinkAnNiu(u"确定",2)        #点击 确定 按钮
            #判断取消审核结果是否等于未审核
            assert self.driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[12]/div').text == u"未审核",u"审核状态断言失败"

            #关闭标签页
            self.closeTagPage()

        except NoSuchElementException,e:
            logFile.write(u"汇率维护 失败Fail:\n" + traceback.format_exc() + "\n")
        except Exception,e:
            logFile.write(u"汇率维护 失败Fail:\n" + traceback.format_exc() + "\n")
        else:
            logFile.write(u"------汇率维护 测试通过Success！------\n")