#!/bin/python
# -*- coding:UTF-8 -*-
# open file and add
# 2018-5-31  by lei  TEST  python2.3 + liunx
import os
#choose = ['CroIsp01OutBound', 'NexmoOutBound', 'EBZoutbound' ]  #  呼出线路前缀

#path = "/usr/local/freeswitch/conf/dialplan/default/" #  fs系统 实际 选择线路的文件夹目录
pathd = "./freeswitch/dialplan/default/"  # 测试路径
department = ['EU', 'Bbet', 'Ruibo','xindeli', 'Haomen',]  #  部门前缀
filename = 'Cro_0000_outbound.xml'  # 模版名字


def update(pathd,filename,mind,maxd,choose):
        a=int(mind)
        b=int(maxd)
        files=pathd+filename
     #   print(a,b)
        if not os.path.isdir(files):  # 判断是否是文件夹，不是文件夹才打开
            print("reading now...")
            linesOne=[]
            
            with open(files) as  lins:  # 打开读取文件内容
                linesOne = lins.readlines()
            print("createing now...")
            while a<=b :
                 linesTwo=[]
                 for line in linesOne:
                   #        print line
			if line.find('abcdef')==-1:
                                pass
                        else:
                               # print("find abcdef")
                                line = line.replace('abcdef',str(a))
                        linesTwo.append(line)
                 filenames=pathd+choose+str(a)+"_outbound.xml"
                 f = open(filenames, 'wa')
                 for line in linesTwo:
                      f.write(line)
                 f.close()
                 a=a+1
				 
def whichdepartment(): # 获取 部门前缀
    for i in range(len(department)):
         print(str(i)+":"+ department[i])
    while 1:
        try:
            chose = input("Pls Einter number of department:")
            if int(chose) in range(len(department)):
                return department[int(chose)]
        except:
            continue		 
    
		 
				 

def which(): # 获取 创建号码范围
    mind = raw_input("Please min number ！ Enter:")
    while (not mind.isdigit()) :
        min = raw_input("min have error! Pls Einter again:")
    maxd = raw_input("Please max number ！ Enter:")
    while (not maxd.isdigit()) :
        strs = raw_input("man have error! Pls Einter again:")
    if  int(mind) > int(maxd):
	     mind,maxd=maxd,mind  
    return  mind,maxd


if __name__ == "__main__":
    choose=whichdepartment()
    mind,maxd=which()
    update(pathd,filename,mind,maxd,choose)
    print('creat is over!')

