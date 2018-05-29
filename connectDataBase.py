#encoding=utf-8

import MySQLdb

#数据库连接
conn = MySQLdb.connect(host="10.206.34.144",port=8066,user="prs_u",passwd="PRs_udj#0002",db="prs",charset="utf8")
cur = conn.cursor() #创建游标

sql = "SELECT bill_code,bill_code_type from t_prs_acc_bill_prep WHERE id = '88888888';"
cur.execute(sql)

bill_code,bill_code_type = cur.fetchone()
if (bill_code == 'S20170826024') and (bill_code_type == 1001):
    print "bill_code is Equal..."

cur.close()     #关闭游标
conn.commit()   #提交到数据库
conn.close()    #断开数据库的连接
