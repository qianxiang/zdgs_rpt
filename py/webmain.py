# -*- coding: utf-8 -*-  

import web
import xlsUtil

from saveToTemp import saveToTemp 
from makeFld import makeFld 
from makeFld import delInvalidFld
from saveFld import saveFld 
from saveFld import skipThisOne 
from saveFld import showReport
from phoneInfo import uploadPhoneInfoPage
from phoneInfo import addPhoneInfo
import lazy 
import up

urls = (
    '/working', 'working' ,
    '/uploadPage', 'uploadPage' ,
    '/upload', 'upload' ,
    '/uploadPhoneInfoPage', 'uploadPhoneInfoPage' ,
    '/addPhoneInfo', 'addPhoneInfo' ,
    '/previewPage', 'previewPage' ,
    '/makeFld', 'makeFld' ,
    '/delInvalidFld', 'delInvalidFld' ,
    '/saveFld', 'saveFld' ,
    '/showReport', 'showReport' ,
    '/skipThisOne', 'skipThisOne' ,
    '/app_up', up.app_up ,
    '/saveToTemp', "saveToTemp",
    '/favicon.ico', 'favicon',
    '/(.*)', 'defaultPage',
    '/(.*)/', 'defaultPage'
)
web.config.debug = True #False
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()


render = web.template.render('templates')


class uploadPage:
    def GET(self):
        # Do some application logic here, and then:
        raise web.seeother('/static/upload.html')

class upload:
    def GET(self):
        # Do some application logic here, and then:
        raise web.seeother('/static/upload.html')
    
    def POST(self):
        x = web.input(myfile={})
        filedir = "static/upload"
        if 'myfile' in x: # to check if the file-object is created
            # replaces the windows-style slashes with linux ones.
            filepath=x.myfile.filename.replace('\\','/')

            # splits the and chooses the last part (the filename with extension)
            filename=filepath.split('/')[-1] 
            
            # creates the file where the uploaded file should be stored

            fullpath = filedir +'/'+ lazy.getYmdhms() + '.xls'
            fout = open( fullpath,'wb') #使用 wb 是为了在windows下能正确的上传文件。
            
            # writes the uploaded file to the newly created file.
            fout.write(x.myfile.file.read())            

            # closes the file, upload complete.
            fout.close()
        # 去预览数据，并进行挑选
        print fullpath 
        print unicode('/previewPage?filename=') 
        print unicode(fullpath)
        raise web.seeother('/previewPage?filename=' + fullpath)



class previewPage:
    def GET(self):
        #web.debug(name)

        runData = {'runFlag':True}

        user_data = web.input()
        if user_data.has_key("filename") :
            filename = user_data.filename
            data = xlsUtil.getExcelData(filename)
            data['filename'] = filename
            return render.selectcolumn(data)        
        else:
            runData['showMsg']= "请先上传需要打印的excel文件..." 
            return render.msg(runData)        

class defaultPage:
    def GET(self, name):
        # Do some application logic here, and then:
        raise web.seeother('/static/index.html')

class working:
    def GET(self):
        # Do some application logic here, and then:
        raise web.seeother('/static/working.html')


class favicon:
    def GET(self):
        # Do some application logic here, and then:
        raise web.redirect('/static/favicon.ico')



