# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

from lazy import getConn
from lazy import getYmdhms
from phoneInfo import getAllPhoneInfo
from phoneInfo import findInvalidPhoneName

render = web.template.render('templates')

class makeFld:
    def GET(self):
        flag = True
        runData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()

        #检查机型名称能否对应到机型代码，如果不能，去机型名称出错页面。
        invalidPhone = findInvalidPhoneName();
        if len(invalidPhone) == 0 :
            #print '机型名称检查合格。'
            allPhoneInfo = getAllPhoneInfo()
        else:
            runData['showMsg']='某些机型名称无法找到对应的机型代码，请先检查上传文件是否正确，或者维护好机型信息再进行制单操作。'
            runData['invalidPhone']=invalidPhone
            return render.phoneNameLost(runData)

                
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
            runData['c0_' +  str(dataCount) ] = sqlrow[0]
            runData['c1_' +  str(dataCount) ] = sqlrow[1]
            runData['c2_' +  str(dataCount) ] = sqlrow[2]
            runData['c3_' +  str(dataCount) ] = sqlrow[3]
            runData['c4_' +  str(dataCount) ] = sqlrow[4]
            thisNo = sqlrow[5]
            runData['c5_' +  str(dataCount) ] = thisNo
            runData['c6_' +  str(dataCount) ] = sqlrow[6]
            runData['c7_' +  str(dataCount) ] = sqlrow[7]
            runData['c8_' +  str(dataCount) ] = sqlrow[8]
            
            # 机型代码通过机型名称查表得到
            phoneName = sqlrow[9]
            runData['c9_' +  str(dataCount) ] = phoneName
            #runData['c10_'+  str(dataCount) ] = sqlrow[10]
            runData['c10_'+  str(dataCount) ] = allPhoneInfo[phoneName]

            runData['c11_'+  str(dataCount) ] = sqlrow[11]
            runData['c12_'+  str(dataCount) ] = sqlrow[12]
            runData['c13_'+  str(dataCount) ] = sqlrow[13]
            runData['c14_'+  str(dataCount) ] = sqlrow[14]

            #print "thisNo=" + thisNo
            #print "prevNo=" + prevNo
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
                #print "tian chong kong bai hang"
                runData['c0_'+  str(loopCount) ] = '' 
                runData['c9_'+  str(loopCount) ] = ''
                runData['c10_'+ str(loopCount) ] = ''
                runData['c11_'+ str(loopCount) ] = ''
                runData['c12_'+ str(loopCount) ] = ''
                runData['c13_'+ str(loopCount) ] = ''
                runData['c14_'+ str(loopCount) ] = ''



        if dataCount == 0 :
            runData['showMsg'] = "太好了，所有发料单都已经生成了。"
            return render.msg(runData)        
            
        #runData['fld_no'] = getFldNo()
        runData['fld_no'] = 'Auto'
        #print runData

        pageCookie = web.cookies(automode='n')
        if cmp(pageCookie.automode, 'y') == 0:
            runData['automodeChecked'] = 'checked'
        else:
            runData['automodeChecked'] = ''

        return render.makeFld(runData)

class delInvalidFld:
    def GET(self):
        flag = True
        runData = {'runFlag':True,'showMsg':'已经删除所有未处理的发料单。'}
        
        cx = getConn()
        cu = cx.cursor()

        strSql = "delete from temp_data WHERE data_type='fld' and use_flag='0'"
        print strSql
        cu.execute(strSql)
        cx.commit()
        cu.close()
        cx.close()
        
        return render.msg(runData)







