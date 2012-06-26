# -*- coding: utf-8 -*-  

import time

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
    return sqlite3.connect("../tomcat7/bin/test.db")

