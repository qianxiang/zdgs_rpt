# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

render = web.template.render('templates')

class makeFld:
    def GET(self):
        flag = True
        renderData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()
        
        cx = getConn()
        cu = cx.cursor()

        strSql = "SELECT data_no, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 from temp_data WHERE data_type='fld' and use_flag='0' ORDER BY c1,c5" 
        print strSql
        cu.execute(strSql)

        for fld in cu:
            renderData['data_no'] = fld[0]
            renderData['c1'] = fld[1]
            renderData['c2'] = fld[2]
            renderData['c3'] = fld[3]
            renderData['c4'] = fld[4]
            renderData['c5'] = fld[5]
            renderData['c6'] = fld[6]
            renderData['c7'] = fld[7]
            renderData['c8'] = fld[8]
            renderData['c9'] = fld[9]
            renderData['c10'] = fld[10]
            renderData['c11'] = fld[11]
            renderData['c12'] = fld[12]
            renderData['c13'] = fld[13]
            renderData['c14'] = fld[14]
            break

        cu.close()
        cx.close()

        renderData['fld_no'] = getDataNo()
        print renderData

        return render.makeFld(renderData)

        
def getDataNo():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) 

def getConn():
    return sqlite3.connect("/Applications/Java/apache-tomcat-7.0.27/bin/test.db")

