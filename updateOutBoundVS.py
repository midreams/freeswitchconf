#!/bin/python
# -*- coding:UTF-8 -*-
# open file and add
# 2018-5-31  by lei  TEST  python2.3 + liunx
import os
choose = ['CroIsp01OutBound', 'NexmoOutBound', 'EBZoutbound','pbx305','xiangganghuliaooutboundbak.xml' ]  #  呼出线路
Prefix = ['86','1026388186',' ']  # 呼出线路的前缀

#path = "/usr/local/freeswitch/conf/dialplan/default" #  fs系统 实际 选择线路的文件夹目录
path = "/etc/freeswitch/dialplan/default"  # 测试路径
files= os.listdir(path) #得到文件夹下的所有文件名称

def update(files,up,Prefixsd):
    number = 0
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            number=number+1
            pathd=path + "/" + file
            print "doing:",file
            linesOne=[]
            linesTwo=[]
            with open(pathd) as  lins:  # 打开读取文件内容
                linesOne = lins.readlines()
            with open(pathd,'w') as  linsdel:  # 打开文件并清空文件内容
                 pass

            for line in linesOne:
                    if "gateway" in line:
                       line = line.strip()  # 移除字符串头尾指定的字符（默认为空格或换行符）
                       counts = line.split("/")
                       counts[2]=up
                       countds3 = counts[3].split("$")
                       counts[3]= Prefixsd+'$'+countds3[1]
                       line=counts[0]+'/'+counts[1]+'/'+counts[2]+'/'+counts[3]+'/'+counts[4]+'\n'
                    linesTwo.append(line)
            f = open(pathd, 'wa')
            for line in linesTwo:
                f.write('%s' % line.replace('^M',''))
            f.close()
    return number
 
def which():
    for i in range(len(choose)):
         print(str(i)+":"+ choose[i])

    strs = raw_input("Please choose your Outbount ！ Enter:")
    while (not strs.isdigit()) or (int(strs) > len(choose)-1) :
        strs = raw_input("Input has error or number is big! Pls Einter again:")

    return  choose[int(strs)]
	

def Prefixs(): # 获取 部门前缀
    for i in range(len(Prefix)):
         print(str(i)+":"+ Prefix[i])  
 
    chose = raw_input("Please input number of Prefix ！ Enter:")
    while (not chose.isdigit() ) :
        chose = raw_input("number have error! Pls Einter again:")
    
#    print("input:",str(mind),str(maxd))
    return  Prefix[int(chose)]	

if __name__ == "__main__":
    outbound=which()
    Prefixsd=Prefixs()
    print "you choose ",outbound
   # update(files,outbound)
    print ("Change all is :",update(files,outbound,Prefixsd))
