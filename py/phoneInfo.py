# -*- coding: utf-8 -*-  

import sqlite3
import time
import web
import xlsUtil

from lazy import getConn
from lazy import getYmdhms

render = web.template.render('templates')

class uploadPhoneInfoPage:
    def GET(self):
        # Do some application logic here, and then:
        raise web.seeother('/static/upload_phone_info.html')

class addPhoneInfo:
    def GET(self):
        raise web.seeother('/static/upload_phone_info.html')


    def POST(self):
        flag = True
        runData = {'runFlag':True,'showMsg':'OK'}

        ''' 
        先上传文件，再检查文件，
        包括格式、内容、以及是否和数据库中已有内容冲突， 
        如果不正确，报错，要求重新上传正确文件；
        如果正确，把内容灌入DB。
        灌入数据完成后，将全部机型代码显示在页面上。
        '''
        
        # 上传文件
        x = web.input(myfile={})
        filedir = "static/upload"
        if 'myfile' in x: 
            # replaces the windows-style slashes with linux ones.
            filepath=x.myfile.filename.replace('\\','/')

            # splits the and chooses the last part (the filename with extension)
            filename=filepath.split('/')[-1] 
            
            # creates the file where the uploaded file should be stored
            fullpath = filedir +'/'+ getYmdhms() + '.txt'
            print fullpath
            fout = open( fullpath,'wb') #使用 wb 是为了在windows下能正确的上传文件。
            
            # writes the uploaded file to the newly created file.
            fout.write(x.myfile.file.read())            

            fout.close()
        else:
            runData['showMsg'] = '上传文件出错。'
            return render.err(runData)
        
        # 存放合法数据的列表
        infos = [ ]

        # 检查数据
        phoneInfoFile = open( fullpath, 'r' )
        phoneInfoLine = phoneInfoFile.readlines();
        phoneInfoFile.close()
        for i,line in enumerate(phoneInfoLine):
            line = line.strip()
            if len(line)==0 :
                continue         #空行直接跳过
            else :
                info = line.split(None,1) # 用第一个空格分成两个部分
                if len(info) < 2 :
                    # 格式不对，报错
                    runData['showMsg'] = '文件格式错误。在第 %d 行:%s' %  (i,line)
                    return render.err(runData)
                else:
                    infos.append(info)
        
        con = getConn()
        cur = con.cursor()


        # 检查是否和DB中已有数据冲突。
        for i,info in enumerate(infos):
            strSql = "SELECT * from phone_info WHERE phone_name='%s'" % info[1] 
            print strSql
            cur.execute(strSql)
            if cur.fetchone() :
                # 机型代码和DB中已有数据冲突，报错
                runData['showMsg'] = '数据错误，机型名称已经存在，在第 %d 条数据: %s %s' %  ( i+1,info[0],info[1])
                cur.close()
                con.close()
                return render.err(runData)

        # 内容灌入DB
        for info in infos:
            strSql = "insert into phone_info (phone_no, phone_name) values ('%s','%s') " % (info[0],info[1])
            print strSql
            cur.execute(strSql)

        con.commit()

        # 将DB中的全部机型信息取出
        allPhoneInfo = []
        # strSql = "select phone_no, phone_name from phone_info order by phone_no  " 
        strSql = "select phone_no, phone_name from phone_info order by rowid DESC  " 
        print strSql
        cur.execute(strSql)
        for record in cur:
            phone = dict()
            phone['phone_no'] = record[0]
            phone['phone_name'] = record[1]
            allPhoneInfo.append(phone)


        cur.close()
        con.close()

         
        runData['AllPhoneInfo'] = allPhoneInfo
        runData['showMsg'] = '增加机型信息成功'

        return render.phoneInfo(runData)

def findInvalidPhoneName():
    '''
    检查机型名称，看是否全部都在 phone_info 表中定义了。
    '''
    phoneList = []
    allPhoneInfo = getAllPhoneInfo()
    cx = getConn()
    cu = cx.cursor()

    strSql = "select c9 from temp_data WHERE data_type='fld' and use_flag='0'"
    print strSql
    cu.execute(strSql)

    for sqlrow in cu:
        phoneList.append( sqlrow[0] )

    cu.close()
    cx.close()

    print phoneList
    invalidPhoneName = []
    for phone in phoneList:
        if not allPhoneInfo.has_key(phone) :
            invalidPhoneName.append(phone)

    return invalidPhoneName
        

def getAllPhoneInfo():
    '''
    从 phone_info 表中读出全部的机型名称和机型编码，放入 dict 中返回。
    '''
    allPhoneName = {}
    
    cx = getConn()
    cu = cx.cursor()

    strSql = "select phone_name, phone_no from phone_info"
    print strSql
    cu.execute(strSql)

    for sqlrow in cu:
        allPhoneName[ sqlrow[0] ] = sqlrow[1]
    cu.close()
    cx.close()

    print allPhoneName
    return allPhoneName
