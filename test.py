# coding=utf-8
from mdtable2excel import mdtable2excel

mdTb = '''|        标志        |                           含义                           |
| :----------------: | :------------------------------------------------------: |
|    re.S(DOTALL)    |             使`.`匹配包括换行在内的所有字符              |
| re.I（IGNORECASE） |                   使匹配对大小写不敏感                   |
|   re.L（LOCALE）   |         做本地化识别（locale-aware)匹配，法语等          |
|  re.M(MULTILINE)   |                    多行匹配，影响^和$                    |
|   re.X(VERBOSE)    | 该标志通过给予更灵活的格式以便将正则表达式写得更易于理解 |
|        re.U        |    根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B    |'''

mdtable2excel(mdTb, 'test', 'table.xls')