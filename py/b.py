# -*- coding: utf-8 -*-  

# 学习读取excel 

from xlrd import open_workbook
wb = open_workbook('s.xls')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        print row
    print "s.ncols=" + str(s.ncols)
    print "s.nrows=" + str(s.nrows)
    #    values = []
    #    for col in range(s.ncols):
    #        values.append(s.cell(row,col).value)
    #    print ','.join(values)
