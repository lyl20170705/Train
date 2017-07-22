#-*- coding: cp936 -*-
import os
import ConfigParser
import string, os, sys
##########################################################
def InitConf(file_path):
    print 'hello'
       

##########################################################
def GitClone(url,save_path):
    i=0
    while i<len(url):
        os.chdir(save_path[i])
        os.popen('git clone '+url[i])
        i=i+1
##########################################################
def GitLog(cwd):
    os.chdir(cwd)
    log=os.popen('git log').read()
    return log
##########################################################
def ChangeDir(url,save_path):
    i=len(url)-5
    filename=''
    flag=True
    while flag:
        if url[i]!='/':
            filename=url[i]+filename
            i=i-1
        else:
            flag=False
            filename='/'+filename
    cwd=save_path+filename
    return cwd
##########################################################
def AnalyseLog(log):

##########################################################
#file_path='d:/Python练习/test.conf'
#InitConf(file_path)

url=['git@gitlab.zte.com.cn:10222813/EXP1.git']
save_path=['e:']

GitClone(url,save_path)
cwd=ChangeDir(url[0],save_path[0])
log=GitLog(cwd)

print log
