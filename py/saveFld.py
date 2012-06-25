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
        mustName = ['c0_1',]
        runData = checkInput( req, mustName, runData)

        cx = getConn()
        cu = cx.cursor()
        
        strUpdate = "UPDATE temp_data SET use_flag='2' where data_no='" + req['c0_1'] + "'"
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
        mustName = ['fld_no','c0_1','c1_1','c2_1','c3_1','c4_1','c5_1','c6_1' \
                ,'c7_1','c8_1','c9_1','c9_1','c10_1','c11_1' \
                ]
        
        renderData = checkInput( req, mustName, renderData)

        if not renderData['runFlag']:
            msg = "输入参数不正确，请按照正常操作流程使用系统。"
            renderData['showMsg'] = msg + renderData['showMsg']  
            return render.err(renderData)

        cx = getConn()
        cu = cx.cursor()

        strInsert = "INSERT INTO fld (fld_no, khmc, khdz, lxdh, ssds, xqdh, lsh, " \
            + "zdrq, ckrq, flck, jedx, jehj ) VALUES ('" \
            + req['fld_no'] + "','" + req['c1_1'] + "','" + req['c2_1'] + "','" + req['c3_1'] \
            + "','" + req['c4_1'] + "','" + req['c5_1']  + "','" + req['fld_no'] + "','" + req['c6_1'] \
            + "','" + req['c7_1'] + "','" + req['c8_1']  + "','" + req['c1_1'] + "','" + req['c1_1'] + "')"
        print strInsert
        cu.execute(strInsert)
        
        strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
            + req['fld_no'] + "','1','" + req['c9_1'] + "','" + req['c10_1'] + "','" + req['c11_1'] \
            + "','" + req['c12_1'] + "','" + req['c13_1'] + "','"+  req['c14_1'] +"')"
        print strInsert
        cu.execute(strInsert)
        strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_1'] + "'"
        print strUpdate
        cu.execute(strUpdate)
        
        if cmp(req['c0_2'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','2','" + req['c9_2'] + "','" + req['c10_2'] + "','" + req['c11_2'] \
                + "','" + req['c12_2'] + "','" + req['c13_2'] + "','"+  req['c14_2'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_2'] + "'"
            print strUpdate
            cu.execute(strUpdate)

        
        if cmp(req['c0_3'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','3','" + req['c9_3'] + "','" + req['c10_3'] + "','" + req['c11_3'] \
                + "','" + req['c12_3'] + "','" + req['c13_3'] + "','"+  req['c14_3'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_3'] + "'"
            print strUpdate
            cu.execute(strUpdate)
        
        if cmp(req['c0_4'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','4','" + req['c9_4'] + "','" + req['c10_4'] + "','" + req['c11_4'] \
                + "','" + req['c12_4'] + "','" + req['c13_4'] + "','"+  req['c14_4'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_4'] + "'"
            print strUpdate
            cu.execute(strUpdate)
        
        if cmp(req['c0_5'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','5','" + req['c9_5'] + "','" + req['c10_5'] + "','" + req['c11_5'] \
                + "','" + req['c12_5'] + "','" + req['c13_5'] + "','"+  req['c14_5'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_5'] + "'"
            print strUpdate
            cu.execute(strUpdate)
        
        if cmp(req['c0_6'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','6','" + req['c9_6'] + "','" + req['c10_6'] + "','" + req['c11_6'] \
                + "','" + req['c12_6'] + "','" + req['c13_6'] + "','"+  req['c14_6'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_6'] + "'"
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

