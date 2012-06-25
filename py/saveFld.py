# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

from lazy import checkInput

render = web.template.render('templates')

class skipThisOne:
    def POST(self):
        flag = True
        runData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()
        # 检查必填项是否都有值
        mustName = ['data_no',]
        runData = checkInput( req, mustName, runData)

        cx = getConn()
        cu = cx.cursor()
        
        strUpdate = "UPDATE temp_data SET use_flag='2' where data_no='" + req['data_no'] + "'"
        print strUpdate
        cu.execute(strUpdate)
        cx.commit()

        cu.close()
        cx.close
        
        raise web.redirect('/')





class saveFld:
    def POST(self):
        flag = True
        msg = "lost : "
        renderData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()
        
        # 检查必填项是否都有值
        mustName = ['fld_no','data_no','c1','c2','c3','c4','c5','c6','c7','c8','c9','c9','c10','c11']
        
        renderData = checkInput( req, mustName, renderData)

        if not renderData['runFlag']:
            msg = "输入参数不正确，请按照正常操作流程使用系统。"
            renderData['showMsg'] = msg + renderData['showMsg']  
            return render.err(renderData)

        cx = getConn()
        cu = cx.cursor()

        strInsert = "INSERT INTO fld (fld_no, khmc, khdz, lxdh, ssds, xqdh, lsh, " \
            + "zdrq, ckrq, flck, jedx, jehj ) VALUES ('" \
            + req['fld_no'] + "','" + req['c1'] + "','" + req['c2'] + "','" + req['c3'] \
            + "','" + req['c4'] + "','" + req['c5']  + "','" + req['fld_no'] + "','" + req['c6'] \
            + "','" + req['c7'] + "','" + req['c8']  + "','" + req['c1'] + "','" + req['c1'] + "')"
        print strInsert
        cu.execute(strInsert)
        cx.commit()
        
        strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
            + req['fld_no'] + "','1','" + req['c9'] + "','" + req['c10'] + "','" + req['c11'] \
            + "','" + req['c12'] + "','" + req['c13'] + "','"+  req['c14'] +"')"
        print strInsert
        cu.execute(strInsert)
        cx.commit()

        strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['data_no'] + "'"
        print strUpdate
        cu.execute(strUpdate)
        cx.commit()

        cu.close()
        cx.close()

        #return "success"
        host = web.ctx.get('host', '192.168.1.101')
        tempIndex = host.find(':')
        if tempIndex < 1 :
            renderData['runFlag'] = False

        print host[:tempIndex]
        ip = host[:tempIndex]

        raise web.redirect('http://'+ ip +':8000/zdgs/report?type=fld&id=' + req['fld_no'] )




def getConn():
    return sqlite3.connect("/Applications/Java/apache-tomcat-7.0.27/bin/test.db")

