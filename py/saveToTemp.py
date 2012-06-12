# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

render = web.template.render('templates')


class saveToTemp:
    def POST(self):
        flag = True
        renderData = {'runFlag':True,'showMsg':'OK'}
        
        req = web.input()

        # 检查必填项是否都有值
        mustName = ['report_type','filename']
        for name in mustName:
            if req.has_key(name) :
                flag = True
            else:
                flag = False

        if not flag :
            msg = "输入参数不正确，请按照正常流程使用系统。"
            renderData['showMsg'] = msg
            return render.err(renderData)
        
        # 取出所有的excel表中的列和数据库中的field的对应关系
        fld_data_col = []
        fld_data_col.append( req['fld_data_col_1'])
        fld_data_col.append( req['fld_data_col_2'])
        fld_data_col.append( req['fld_data_col_3'])
        fld_data_col.append( req['fld_data_col_4'])
        fld_data_col.append( req['fld_data_col_5'])
        fld_data_col.append( req['fld_data_col_6'])
        fld_data_col.append( req['fld_data_col_7'])
        fld_data_col.append( req['fld_data_col_8'])
        fld_data_col.append( req['fld_data_col_9'])
        fld_data_col.append( req['fld_data_col_10'])
        fld_data_col.append( req['fld_data_col_11'])
        print( fld_data_col )
        report_type =  req["report_type"]

        # 读出excel文件中的数据，并取出第一个sheet
        filename = req["filename"]
        data = xlsUtil.getExcelData(filename)
        tables = data['tables']
        table1 = tables[0]
        sheet1 = table1['t_data']


        strInsertTail = ''
        iCount = 0
        cx = getConn()
        cu = cx.cursor()

        for row in sheet1:
            strInsertTail = ''
            for strIndex in fld_data_col :
                if strIndex == u'' :
                    strInsertTail = strInsertTail + ",''"
                else:
                    iIndex = int(strIndex)
                    strText = row[iIndex-1]
                    strInsertTail = strInsertTail + ",'" + unicode(strText) + "'"
            data_no = getDataNo() + "_" + str(iCount)
            strInsertHead = "INSERT INTO temp_data (data_no, data_type, use_flag, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 ) VALUES  ( '" + data_no + "', '" + report_type + "', '0'"
            strSql = strInsertHead + strInsertTail + ")"
            iCount = iCount + 1 
            print strSql
            cu.execute(strSql)
        cx.commit()
        cu.close()
        #cx.close()



        reportType =  req["report_type"]

        if reportType == "fld" :
            saveFld()
        elif reportType == "sld" :
            saveSld()
        elif reportType == "jld" :
            saveJld()
        elif reportType == "lyd" :
            saveLyd()
        elif reportType == "nbdbd" :
            saveNbdbd()
        elif reportType == "rkd" :
            saveRkd()
        else :
            msg = "报表类型不正确"
            renderData['showMsg'] = msg
            return render.err(renderData)

        msg = "导入操作执行成功，共导入数据" + str(iCount) + "条。"
        renderData['showMsg'] = msg
        return render.msg(renderData)


def saveFld():
    return ""

def saveSld():
    return ""

def saveJld():
    return ""

def saveLyd():
    return ""

def saveNbdbd():
    return ""

def saveRkd():
    return ""

def getDataNo():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) 

def getConn():
    return sqlite3.connect("/Applications/Java/apache-tomcat-7.0.27/bin/test.db")

