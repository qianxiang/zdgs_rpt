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
        
         

        runData['showMsg'] = '增加机型信息成功'

        return render.phoneInfo(runData)

        


