#encoding=utf-8
from testPRS import TestPRS   #从login文件中导入TestPRS类

if __name__ == '__main__':
    for i in range(1):
        test = TestPRS()    #类实例化
        test.login()    #登录

        #以下为账单模块调用方法，同行账单为该模块的入口
        test.tongHangZhangDan()     #执行同行账单
        # test.yiErJiJiJianZhangDan()     #执行一二级寄件账单
        # test.yiErJiPaiJianZhangDan()    #执行一二级派件账单
        # test.zhangDanBianJi()   #执行账单编辑
        # test.shiXiaoPaiFeiPaiJianZhangDan()     #执行时效派费派件账单
        # test.wangDianChuHuoDuiZhang()   #执行网点出货对账
        # test.wangDianPaiJianDuiZhang()  #执行网点派件对账
        # test.zhangDanTiaoZheng()    #执行账单调整
        # test.zhiDaPaiFeiZhangDanBianJi()    #执行直达派费账单编辑
        # test.zhiDaPaiFeiJieSuanChaXun()     #执行直达派费结算查询
        # test.zhongZhuanZhangDanChaXun()     #执行中转账单查询
        # test.zhongZhuanZhangDanJieSuan()    #执行中转账单结算
        # test.guDingFeiYongKouKuan()     #执行固定费用费用扣款
        # test.guDingFeiYongMingXiWeiHu()     #执行固定费用明细维护
        # test.guDingFeiYongKouKuanJiLu()     #执行固定费用扣款记录
        # test.xiTongShiYongFeiZhangDan()     #执行系统使用费账单
        # test.daiShouKuanJiFangWangDian()    #代收款账单编辑(寄方网点)
        # test.daiShouKuanJiFangZhongXin()    #代收款账单编辑(寄方中心)
        # test.daiShouKuanPaiFangZhongXin()   #代收款账单编辑(派方中心)
        # test.daiShouKuanPaiFangWangDian()   #代收款账单编辑(派方网点)
        # test.daiShouKuanZhiTuiShenDan()     #执行代收款直退审单
        # test.daiShouKuanZhiTuiDengJi()      #执行代收款直退登记
        # test.daiShouKuanZhiTuiShenHe()      #执行代收款直退审核
        # test.daiShouKuanZhiTuiChaXun()      #执行代收款直退查询
        # test.daiShouDuiZhangChaXun()        #执行代收对账单查询
        # test.daoFuKuanJiFangWangDian()      #执行 到付款账单编辑(寄方网点)
        # test.daoFuKuanJiFangZhongXin()      #执行 到付款账单编辑(寄方中心)
        # test.daoFuKuanPaiFangWangDian()     #执行 到付款账单编辑(派方网点)
        # test.daoFuKuanPaiFangZhongXin()     #执行 到付款账单编辑(派方中心)
        # test.feiYongTiaoZhengDengJi()       #执行 费用调整登记
        # test.feiYongTiaoZhengJieShouFangQueRen()     #执行 费用调整接收方确认
        # test.feiYongTiaoZhengDengJiFangChaXun()      #执行 费用调整登记方查询
        # test.feiYongTiaoZhengShenHeKouKuan()        #执行 费用调整审核扣款（接收方中心）
        # test.huiDanZhangDanChaXun()         #执行 回单账单查询
        # test.zhanDianCaiWuShuJuChongTui()       #执行 站点财务数据重推
        # test.zhangDanFeiYongPiDai()         #执行 账单费用批带
        # test.shuJuDaoChuChaKan()            #执行 数据导出查看
        # test.shuJuDaoChuChaKan()            #执行 数据导出查看
        # test.wangDianGuanXiChaXun()         #执行 网点关系查询

        #以下为基础数据模块调用方法，业务规则类型为该模块的入口
        test.yeWuGuiZeLeiXing()             #执行 业务规则类型
        test.yeWuGuiZeSheZhi()              #执行 业务规则设置


        test.quitBrowser()      #退出浏览器