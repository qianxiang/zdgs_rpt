# -*- coding: utf-8 -*-  

import web
        
urls = (
    '/temp', 'templatePage' ,
    '/(.*)', 'defaultPage'
)
app = web.application(urls, globals())

class defaultPage:
    def GET(self, name):
        return "Hello world!"

class templatePage:
    def GET(self):
        render = web.template.render('templates/')
        name = "test Page OK"
        data = {'runFlag':True,'showMsg':'OK'}
        
        t1 = {'name':'table_1'}
        t1['t_data'] = [['ab','cd','ef'],['ghi','jkl','mno'],['pqr','stu','vwx']]
        t2 = {'name':'table_2'}
        t2['t_data'] = [['ab','cd','ef'],['ghi','jkl','mno'],['pqr','stu','vwx']]
        t3 = {'name':'table_3'}
        t3['t_data'] = [['ab','cd','ef'],['ghi','jkl','mno'],['pqr','stu','vwx']]
        t4 = {'name':'table_4'}
        t4['t_data'] = [['ab','cd','ef'],['ghi','jkl','mno'],['pqr','stu','vwx']]
        
        tables = []
        tables.append(t1)
        tables.append(t2)
        tables.append(t3)
        tables.append(t4)

        data['tables'] = tables

        #return render.testTemplate(data)
        return render.selectcolumn(data)

if __name__ == "__main__":
    app.run()
