# -*- coding: utf-8 -*-  

import time

def getYmdhms():
    return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) 

