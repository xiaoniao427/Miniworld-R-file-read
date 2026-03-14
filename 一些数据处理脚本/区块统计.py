import os



dian={}
schu=open("编码","a",encoding="utf-8")
def iop(a,b):
    global dian
    try:
        dian[a]=dian[a]+b
    except:
        dian[a]=b
        dian["名单"].append(a)




def decompress_string(s):
    s = s.rstrip('\n')
    for segment in s.split('/'):
        if not segment:  # 跳过空片段（如末尾的/）
            continue
        count_str, value_str = segment.split('-', 1)  # 只分割一次
        count = int(count_str)
        value = int(value_str)
        iop(value,count)  # 直接执行函数调用




asd=os.listdir()
while True:
    while True:
        if asd[0][-1]!="r":
            del asd[0]
        else:
            break
    try:
        qwe=open(asd[0],"r",encoding="gb2312")
    except:
        qwe=open(asd[0],"r",encoding="utf-8")
    print(asd[0])
    print(len(asd))
    qwe=qwe.readlines()
    del asd[0]
    try:
        uio=0
        sgu_f=0
        while True:
            if qwe[uio][0]=="空":
                if sgu_f==1:
                    schu.write(str(dian)+"\n")
                dian={}
                dian["名单"]=[]
                sgu_f=0
            if sgu_f==1:
                if qwe[uio][0]!="奉":
                    decompress_string(qwe[uio])
            if qwe[uio][0]=="奉":
                if sgu_f==1:
                    schu.write(str(dian)+"\n")
                #schu.write(qwe[uio])
                dian={}
                dian["名单"]=[]
                dian["归属"]=qwe[uio].rstrip('\n')
                sgu_f=1
            if qwe[uio][0]=="\n":
                if sgu_f==1:
                    schu.write(str(dian)+"\n")
                dian={}
                dian["名单"]=[]
            uio=uio+1
    except Exception as e:
        print(e)
        pass







