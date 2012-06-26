# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

from lazy import getConn
from lazy import getYmdhms

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

        if dataCount < 10 :
            for loopCount in range(dataCount+1,11):
                print "tian chong kong bai hang"
                renderData['c0_'+  str(loopCount) ] = '' 
                renderData['c9_'+  str(loopCount) ] = ''
                renderData['c10_'+ str(loopCount) ] = ''
                renderData['c11_'+ str(loopCount) ] = ''
                renderData['c12_'+ str(loopCount) ] = ''
                renderData['c13_'+ str(loopCount) ] = ''
                renderData['c14_'+ str(loopCount) ] = ''



        if dataCount == 0 :
            renderData['showMsg'] = "太好了，所有发料单都已经生成了。"
            return render.msg(renderData)        
            
        renderData['fld_no'] = getYmdhms()
        print renderData

        return render.makeFld(renderData)

        


