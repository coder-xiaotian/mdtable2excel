# coding=utf-8
import xlwt

def mdtable2excel(mdTable, sheetName, excelName):
    mdTable = stripLF(mdTable.strip())
    lines = mdTable.splitlines(False)
    if len(lines) == 0:
        return
    # 去掉第二行，因为是markdown表格的分割线，是没用的
    lines.pop(1)

    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workbook.add_sheet(sheetName)
    for i, line in enumerate(lines):
        items = line.strip().split('|')
        for j, item in enumerate(items):
            sheet.write(i, j, item)

    workbook.save(excelName)

def stripLF(str):
    if str.startswith('\n'):
        str = str[1:]
    if str.endswith('\n'):
        str = str[:-1]
    return str