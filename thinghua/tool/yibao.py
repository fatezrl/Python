import re
#with open('E:/code/pycharm/venv/tsing/tools/file/3.1.7.2.txt', 'w') as f:
#    f.write('Hello, world!')
#with open('E:/code/pycharm/venv/tsing/tools/file/1.txt', 'r',encoding='utf-8') as f:
#   print(f.read())
f = input('文件名')
sourcesessionis = open("E:/code/pycharm/venv/tsing/tools/file/"+f,'r')
sourcesessionis2=sourcesessionis.read()
print(sourcesessionis2)
filename =sourcesessionis.name
filename2 = filename.replace('.txt','_666.txt')
filename3 = filename.replace('.txt','_taskid.txt')
print(sourcesessionis.name)
s =sourcesessionis2
ssf5 = s.replace('\n','').replace(' ','')
s =ssf5
# addtime 戳
#reg = r'SessionId=(.{32})'
rega = r'addTime(.{15})'#只取SessionId=字符后面32位字符串
addreg = re.compile(rega)
addreglist = re.findall(addreg,s)
temp_ss =s
for ac in addreglist:
    s_c =temp_ss.replace(ac,'\":戳')
    temp_ss = s_c
print(s_c)

#uid 用
regu = r'uid(.{8})'#只取SessionId=字符后面32位字符串
uidreg = re.compile(regu)
uidreglist = re.findall(uidreg,s_c)
temp_c = s_c
for uy in uidreglist:
    s_y =temp_c.replace(uy,'\":\"用')
    temp_c = s_y
s_y=temp_c
print(s_y)


# studydate 学
regs = r'studyDate(.{16})'#只取SessionId=字符后面32位字符串
stdreg = re.compile(regs)
stdreglist = re.findall(stdreg,s_y)

temp_y =s_y
for sd in stdreglist:
    s_x =temp_y.replace(sd,'\":\"学')
    temp_y=s_x
s_x =temp_y
print(s_x)

#seconds 时
#re.findall(r"a(.+?)b",str)          只取ab间的字符串
regss = r"(?<=seconds\":\")\d+"
scsreg = re.compile(regss)
scsreglist = re.findall(scsreg,s_x)
temp_x = s_x
for ss in scsreglist:
    s_s =temp_x.replace('\"'+ss+'\",\"chapterId','\"时\",\"chapterId')
    temp_x = s_s
print(s_s)

#score 分

#reg=re.compile(r"(?<=指定字符)\d+") (?<=指定字符)此部分定位指定字符，查找但不包含  \d+此部分为一个以上数字
#match=reg.search("待查找文本")
#print match.group(0)
#regf_t=re.compile(r"(?<=score\":\")\d+")
#sfreglist2=regf_t.findall(s_s)
#sfreglist2= re.findall(regf_t,s_s)
#print(sfreglist2)

regf = r"(?<=score\":\")\d+"#score 后的数字
sfreg = re.compile(regf)
sfreglist = re.findall(sfreg,s_s)
temp_s =s_s
for sf in sfreglist:
    s_f =temp_s.replace('\"'+sf+'\",\"bookId','\"分\",\"bookId')
    temp_s = s_f
print(s_f)

#删除数字



sfregszlist = range(1,100)
temp_s_f =s_f
for sfsz in sfregszlist:
    s_f2 =temp_s_f.replace(str(sfsz)+'ut=','ut=')
    temp_s_f = s_f2
print(s_f2)

s_f1 =s_f2

#taskid
regtaskid = r'taskId\":\"(.{32})'#只取SessionId=字符后面32位字符串
taskidreg = re.compile(regtaskid)
taskidreglist = re.findall(taskidreg,s)



#sf1 = s_f.replace('ut=','\",\"ut=')
sf3 = s_f1.replace("\\","\\\\")
sf3_1 = sf3.replace("\'","\"")
sf4 = sf3_1.replace("\"", "\\\"")
sf4_1 = sf4.replace('ut=','\",\"ut=')
sf5 = sf4_1.replace('\n','').replace(' ','')
sf6 = sf5.replace("\",\"ut","\"ut",1).replace('\"ut=','\n\n\"ut=')
with open(filename2, 'w') as f:
    f.write(sf6)
with open(filename3, 'w') as f:
    f.write(str(taskidreglist))
a =1
