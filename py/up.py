# -*- coding: utf-8 -*-  

import web
urls = (
  "", "goPage",
  "/(.*)", "upload"
)

class goPage:
    def GET(self): raise web.seeother('/')

class upload:
    def GET(self, path):
        return "blog " + path

app_up = web.application(urls, locals())

