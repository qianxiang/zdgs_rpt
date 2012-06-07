# -*- coding: utf-8 -*-  

import web

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
            msg = "输入参数不正确，请按照规则使用系统。"
            renderData['showMsg'] = msg
            return render.err(renderData)

        reportType =  req["report_type"]
        return "data:" +  str(req.has_key("filename")) + req["filename"]

