# -*-coding: utf-8 -*-
import os,re,sys

if len(sys.argv) != 2 :
    print 'Usage : python logaudit.py <path>'
    sys.exit()

logpath = sys.argv[1]

#获取输入参数的文件路径'

merge = re.compile(r'.*(\d[10])')
for root , dirs , files in os.walk(logpath):
    for line in files:
        #遍历日志文件夹，合并所有内容到一个文件
        pipei = merge.match(line)
        if pipei != None:
            tmppath = root + '\\' +line
            logread1 = open(tmppath,'r')
            logread = logread1.read()
            log2txt = open('.\\log.txt','a')
            log2txt.write(logread)
            log2txt.close()
            logread1.close()
        else:
            exit



log = open('.//log.txt','r')


logread = log.readlines()

auditString = re.compile(r'.*[^_][sS][eE][lL][eE][cC][tT][^.].*|.*[uU][nN][iI][Oo][nN].*|.*[bB][aA][sS][eE][^.].*|.*[oO][gG][nN][lL].*|.*[eE][vV][aA][lL][(].*|.*[eE][xX][cC][uU][tT][eE].*')

writelog = open('.//result.txt','a')
for lines in logread:
    auditResult = auditString.match(lines)
    if auditResult != None:
        writelog.write(auditResult.group())
        writelog.write('\n')
    else:
        exit

writelog.close()
log.close()
