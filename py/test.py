# -*- coding: utf-8 -*-  

import web

import lazy 

urls = (
    '/testcookie', 'testCookie',
    '/(.*)', 'defaultPage',
    '/(.*)/', 'defaultPage'
)
web.config.debug = True #False
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

render = web.template.render('templates')

class testCookie:
    def GET(self):
        c = web.cookies(age="25")
        print c
        web.setcookie('age', '19', 3600000)
        return "Age set in your cookie"


class defaultPage:
    def GET(self, name):
        # Do some application logic here, and then:
        raise web.seeother('/static/index.html')

