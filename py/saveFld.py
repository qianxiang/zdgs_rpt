# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

from lazy import checkInput
from lazy import getConn

render = web.template.render('templates')

class showReport:
    def GET(self):
        flag = True
        runData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()
        # 检查必填项是否都有值
        mustName = ['type','id']
        runData = checkInput( req, mustName, runData)

        if not runData['runFlag']:
            msg = "输入参数不正确，请按照正常操作流程使用系统。"
            runData['showMsg'] = msg + runData['showMsg']  
            return render.err(runData)
        
        host = web.ctx.get('host', '192.168.1.101')
        tempIndex = host.find(':')
        if tempIndex < 1 :
            runData['runFlag'] = False

        print host[:tempIndex]
        ip = host[:tempIndex]

        runData['iframeUrl'] = 'http://'+ ip +':8000/zdgs/report?type=' + req['type'] +'&id=' + req['id']
        return render.showreport(runData)
        


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
        try:
            cu.execute(strInsert)
        except:
            renderData['runFlag'] = False
            msg = "被禁止的数据库操作，请按照正常操作流程使用系统。"
            renderData['showMsg'] = msg + renderData['showMsg']  
            return render.err(renderData)

        
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
        
        if cmp(req['c0_7'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','7','" + req['c9_7'] + "','" + req['c10_7'] + "','" + req['c11_7'] \
                + "','" + req['c12_7'] + "','" + req['c13_7'] + "','"+  req['c14_7'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_7'] + "'"
            print strUpdate
            cu.execute(strUpdate)
        
        if cmp(req['c0_8'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','8','" + req['c9_8'] + "','" + req['c10_8'] + "','" + req['c11_8'] \
                + "','" + req['c12_8'] + "','" + req['c13_8'] + "','"+  req['c14_8'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_8'] + "'"
            print strUpdate
            cu.execute(strUpdate)
        
        if cmp(req['c0_9'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','9','" + req['c9_9'] + "','" + req['c10_9'] + "','" + req['c11_9'] \
                + "','" + req['c12_9'] + "','" + req['c13_9'] + "','"+  req['c14_9'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_9'] + "'"
            print strUpdate
            cu.execute(strUpdate)
        
        if cmp(req['c0_10'], '')!=0 :
            strInsert = "INSERT INTO fld_list (fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz ) VALUES ('" \
                + req['fld_no'] + "','10','" + req['c9_10'] + "','" + req['c10_10'] + "','" + req['c11_10'] \
                + "','" + req['c12_10'] + "','" + req['c13_10'] + "','"+  req['c14_10'] +"')"
            print strInsert
            cu.execute(strInsert)
            strUpdate = "UPDATE temp_data SET use_flag='1' where data_no='" + req['c0_10'] + "'"
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

        
        if req.has_key('automode') :
            web.setcookie('automode', 'y', 3600000)
            raise web.redirect('/makeFld')
        else:    
            web.setcookie('automode', 'n', 3600000)
            raise web.redirect('/showReport?type=fld&id=' + req['fld_no'] )
    # raise web.redirect('http://'+ ip +':8000/zdgs/report?type=fld&id=' + req['fld_no'] )


