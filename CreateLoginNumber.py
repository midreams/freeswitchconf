#!/bin/python
# -*- coding:UTF-8 -*-
# open file and add
# 2018-7-5  by lei  TEST  python2.3 + liunx
import os
#choose = ['CroIsp01OutBound', 'NexmoOutBound', 'EBZoutbound' ]  #  呼出线路前缀
#path = "/usr/local/freeswitch/conf/dialplan/default/" #  fs系统 实际 选择线路的文件夹目录
pathd = "./freeswitch/directory/default/"  # 测试路径
filename = '0000.xml'  # 模版名字

def update(pathd,filename,mind,maxd):
        a=int(mind)
        files=pathd+filename

        if not os.path.isdir(files):  # 判断是否是文件夹，不是文件夹才打开
            print("reading now...")
            linesOne=[]
            
            with open(files) as  lins:  # 打开读取文件内容
                linesOne = lins.readlines()
            print("createing now...")
            while a<=int(maxd) :
                 linesTwo=[]
                 for line in linesOne:
                   #        print line
			if line.find('abcde')==-1:
                                pass
                        else:
                             
                                line = line.replace('abcde',mind)
                        linesTwo.append(line)
                 filenames=pathd+mind+".xml"
                 f = open(filenames, 'wa')
                 for line in linesTwo:
                      f.write(line)
                 f.close()
                 a=a+1

def which(): # 获取 创建号码范围
    mind = raw_input("Please min number ！ Enter:")
    while (not mind.isdigit()) :
        min = raw_input("min have error! Pls Einter again:")
    maxd = raw_input("Please max number ！ Enter:")
    while (not maxd.isdigit()) :
        strs = raw_input("man have error! Pls Einter again:")
#    print("input:",str(mind),str(maxd))
    if  int(mind) > int(maxd):
	     mind,maxd=maxd,mind      
    return  mind,maxd


if __name__ == "__main__":
    mind,maxd=which()
    update(pathd,filename,mind,maxd)
    print('creat is over!')

