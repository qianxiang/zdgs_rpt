# -*- coding: utf-8 -*-  

from xlrd import open_workbook


# 从Excel文件中读取数据，放入一个数组中。
def getExcelData( filename ):
    #    return "abc"
#def abc():
    retValue = {'runFlag':True,'showMsg':'OK'}
    tables = []
    
    wb = open_workbook(filename)
    #t1 = None
    for s in wb.sheets():
        print 'Sheet:',s.name
        t1 = dict()
        t1 = {'name': s.name }
        t_data = []
        for row in range(s.nrows):
            #print row
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
            t_data.append(values)
        t1['t_data'] = t_data
        print retValue
        tables.append(t1)
    retValue['tables'] = tables
    return retValue 