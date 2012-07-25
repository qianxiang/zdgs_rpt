# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

import lazy

render = web.template.render('templates')

class uploadPhoneInfoPage:
    def GET(self):
        # Do some application logic here, and then:
        raise web.seeother('/static/upload_phone_info.html')

class addPhoneInfo:
    def GET(self):
        flag = True
        renderData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()
        
        cx = lazy.getConn()
        cu = cx.cursor()

        strSql = "SELECT data_no, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14 from temp_data WHERE data_type='fld' and use_flag='0' ORDER BY c1,c5" 
        print strSql
        cu.execute(strSql)

        dataCount = 0
        prevNo = 'abcdefghijklmn'
        thisNo = ''
        for sqlrow in cu:
            dataCount = dataCount + 1
            renderData['c0_' +  str(dataCount) ] = sqlrow[0]
            renderData['c1_' +  str(dataCount) ] = sqlrow[1]
            renderData['c2_' +  str(dataCount) ] = sqlrow[2]
            renderData['c3_' +  str(dataCount) ] = sqlrow[3]
            renderData['c4_' +  str(dataCount) ] = sqlrow[4]
            thisNo = sqlrow[5]
            renderData['c5_' +  str(dataCount) ] = thisNo
            renderData['c6_' +  str(dataCount) ] = sqlrow[6]
            renderData['c7_' +  str(dataCount) ] = sqlrow[7]
            renderData['c8_' +  str(dataCount) ] = sqlrow[8]
            renderData['c9_' +  str(dataCount) ] = sqlrow[9]
            renderData['c10_'+  str(dataCount) ] = sqlrow[10]
            renderData['c11_'+  str(dataCount) ] = sqlrow[11]
            renderData['c12_'+  str(dataCount) ] = sqlrow[12]
            renderData['c13_'+  str(dataCount) ] = sqlrow[13]
            renderData['c14_'+  str(dataCount) ] = sqlrow[14]

            print "thisNo=" + thisNo
            print "prevNo=" + prevNo
            if cmp(prevNo, 'abcdefghijklmn')==0:
                prevNo = thisNo
            elif cmp(prevNo, thisNo) != 0 :
                dataCount = dataCount - 1
                break
            elif dataCount == 10 :
                break

        cu.close()
        cx.close()
   



        return render.makeFld(renderData)

        


