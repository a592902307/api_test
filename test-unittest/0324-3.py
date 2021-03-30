# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/3/24 14:03
@file:0324-3.py
@desc:
'''

file=r'C:\Users\18358\Desktop\LogAnalyse\file1.txt'
newfile=r'C:\Users\18358\Desktop\LogAnalyse\newfile.txt'

with open(file,'r') as rf,open(newfile,'w') as wf:
    info_list=rf.read().splitlines()
    # print(info_list)

    for line in info_list:
        if ';' in line:
            temp=line.split(';')
            # print(temp)
            if ':' in temp[0] and ':' in temp[1]:
                name=temp[0].split(':')[1].strip()
                salary=temp[1].split(':')[1].strip()
                if salary.isdigit():
                    salary=int(salary)
                # print(name,salary)
                outStr='name: {}   ;    salary:  {} ;  tax: {} ; income:  {}'.format(name,salary,int(salary*0.1),int(salary*0.9))
                wf.write(outStr+'\n')
            else:
                outStr="this line has not':'"
                wf.write(outStr+'\n')
        else:
            outStr = "this line has not';'"
            wf.write(outStr+'\n')
