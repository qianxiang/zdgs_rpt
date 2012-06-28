# -*- coding: utf-8 -*-  

import time
import sqlite3

def getFldNo(  ):
    year_month = time.strftime('%Y-%m',time.localtime(time.time())) 
    prefix = 'FL-' + year_month + '-'
    return prefix + format(getNextValue(prefix),'04.0f')

def getNextValue( prefix ):
    no = 1
    cx = getConn()
    cu = cx.cursor()

    strSql = "SELECT s_value from qx_sequence WHERE s_name='"+ prefix +"'" 
    print strSql
    cu.execute(strSql)
    
    temp_no = 0
    for sqlrow in cu:
        temp_no = sqlrow[0]

    cu.close()
    cu = cx.cursor()

    if temp_no == 0 :
        strSql = "INSERT INTO qx_sequence (s_name, s_value) VALUES ('" \
                + prefix + "',1)"
        cu.execute(strSql)
        no = 1
    else:
        no = temp_no
    
    strSql = "UPDATE qx_sequence SET s_value='" \
            + str(no+1) +"' WHERE s_name='"+ prefix +"'" 
    cu.execute(strSql)

    cx.commit()
    cu.close()
    cx.close()
    print  str(no)
    return no




def getYmdhms():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) 

def checkInput( inputValue, mustName, runData ):
    flag = True
    msg = ''
    # 检查必填项是否都有值
    for name in mustName:
        if inputValue.has_key(name) :
            flag = True
        else:
            flag = False
            msg = msg + "," + name

    if not flag :
        msg = "缺失必须的输入项:" + msg
        runData['showMsg'] = msg
        runData['runFlag'] = flag
    else:
        runData['showMsg'] = 'OK'

    return runData

def getConn():
    return sqlite3.connect("/Applications/Java/apache-tomcat-7.0.27/bin/test.db")

