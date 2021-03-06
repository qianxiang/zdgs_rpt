# -*- coding: utf-8 -*-  

from xlrd import open_workbook
import xlrd


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
                tempValue = s.cell(row,col).value
                
                if s.cell_type(row, col) == xlrd.XL_CELL_DATE :
                    tempDate = xlrd.xldate_as_tuple(tempValue, 0)
                    tempValue = getStrDate(tempDate)
                elif isinstance( tempValue, float ):
                    tempInt = int(tempValue)
                    if (tempValue-tempInt) < 0.00001 :
                        tempValue = format(tempValue, '.0f')
                        #print tempValue
                #print "Type: " + str(type(tempValue)) + "  " + unicode(tempValue)
                values.append(tempValue)
            t_data.append(values)
        t1['t_data'] = t_data
        print retValue
        tables.append(t1)
    retValue['tables'] = tables
    return retValue 

def getStrDate( tupleDate ):
    return str(tupleDate[0]) + '/' + str(tupleDate[1]) + '/' + str(tupleDate[2])
