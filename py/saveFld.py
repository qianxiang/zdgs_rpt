# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

render = web.template.render('templates')

class saveFld:
    def POST(self):
        flag = True
        msg = "lost : "
        renderData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()
        
        # 检查必填项是否都有值
        mustName = ['fld_no','data_no','c1','c2','c3','c4','c5','c6','c7','c8','c9','c9','c10','c11']
        for name in mustName:
            if req.has_key(name) :
                flag = True
            else:
                flag = False
                msg = msg + " " + name

        if not flag :
            msg = msg + "输入参数不正确，请按照正常流程使用系统。"
            renderData['showMsg'] = msg
            return render.err(renderData)

        cx = getConn()
        cu = cx.cursor()

        strInsert = "INSERT INTO fld (fld_no, xmh, xm, mc, ssds, dz, flbh ) VALUES ('" \
            + req['fld_no'] + "','" + req['c1'] + "','" + req['c2'] + "','" + req['c3'] \
            + "','" + req['c4'] + "','" + req['c5'] + "','" + req['c6'] + "')"
        print strInsert
        cu.execute(strInsert)
        cx.commit()
        
        strInsert = "INSERT INTO fld_list (fld_no, wzbh, mcjgg, jldw, fcsl, jxbm, dj, kh, dh ) VALUES ('" \
            + req['fld_no'] + "','1','" + req['c7'] + "','" + req['c8'] + "','" + req['c9'] \
            + "','" + req['c10'] + "','" + req['c11'] + "','--', '--')"
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
        raise web.redirect('http://localhost:8000/zdgs/report?type=fld&id=' + req['fld_no'] )


def getConn():
    return sqlite3.connect("/Applications/Java/apache-tomcat-7.0.27/bin/test.db")

