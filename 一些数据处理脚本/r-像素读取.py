import os
import math
import re
from PIL import Image




dai=os.listdir()

def chuasd():
    global yan_se
    global schu
    global ming
    global asd
    global yui
    global bina_l
    global sgu_f
    global y
    global x,z,qwe,chu_yun,yuan_x,yuan_z,qi_x,qi_z


    yan_se={}
    schu=open("总集","a")
    while dai[0][0]!="补":
        del dai[0]
    ming=dai[0]
    del dai[0]
    print(ming)
    asd=open(ming,"r")
    asd=asd.readlines()
    yui={}
    bina_l=0
    sgu_f=0
    y=0
    x,z=0,0
    qwe={}
    chu_yun=[]
    yuan_x=extract_coordinates(ming)[0]*512
    yuan_z=extract_coordinates(ming)[1]*512
    qi_x=0
    qi_z=0




def chushi():
    global yan_se
    yan_se["1"]=(0,0,0,255)
    yan_se["104"]=(138,140,128,255)
    yan_se["402"]=(150,150,150,255)
    yan_se["6"]=(255,0,0,255)
    yan_se["451"]=(123,127,117,255)
    yan_se["101"]=(140,107,46,255)
    yan_se["455"]=(125,125,0,255)
    yan_se["452"]=(255,255,255,255)
    yan_se["0"]=(255,255,255,0)
    yan_se["401"]=(48,71,65,255)
    yan_se["453"]=(124,0,0,255)
    yan_se["406"]=(168,103,60,255)
    yan_se["107"]=(122,83,49,255)
    yan_se["108"]=(252,232,138,255)
    yan_se["106"]=(222,202,108,255)
    yan_se["448"]=(0,30,0,255)
    yan_se["3"]=(13,114,179,255)
    yan_se["454"]=(0,0,124,255)
    yan_se["246"]=(20,100,30,255)
    yan_se["314"]=(200,20,20,255)
    yan_se["598"]=(255,255,255,255)
    yan_se["403"]=(20,255,20,255)
    yan_se["503"]=(123,127,117,255)
    yan_se["5"]=(255,0,0,255)
    yan_se["734"]=(255,255,255,255)
    yan_se["902"]=(255,255,255,255)
    yan_se["801"]=(255,255,255,255)
    yan_se["901"]=(255,255,255,255)
    yan_se["4"]=(13,114,179,255)
    yan_se["904"]=(255,255,255,255)


def extract_numbers(s):
    try:
        # 去掉首字符并分割
        s = s.rstrip('\n')  # 支持末尾多个\n的情况（如"\n\n"）
        content=s[1:]
        num_strs=content.split('/')
        num1=int(num_strs[0])
        num2=int(num_strs[1])

        return (num1,num2)

    except:pass


def extract_coordinates(s):
    numbers = re.findall(r'-?\d+', s)
    return (int(numbers[0]), int(numbers[1])) if len(numbers) >= 2 else None


def lei(x):
    try:
        iop=qwe[x]
    except:
        #print(str(x))
        qwe[x]=0


def fan(x,y,z):
    try:
        return yui[str(x)+"/"+str(y)+"/"+str(z)]
    except:
        return 114514

def yan(s):
    try:
        return yan_se[str(s)]
    except:
        return (255,255,255,255)


def luo_d(x,z):
    y=149
    yuiqwe=fan(x,y,z)
    while yuiqwe!=114514:
        if yuiqwe!="0":
            break
        y=y-1
        yuiqwe=fan(x,y,z)
    return yuiqwe,y


def decompress_string(s):
    s=s.rstrip('\n')  # 支持末尾多个\n的情况（如"\n\n"）
    result=[]
    try:
        for segment in s.split('/'):
            count_str,value=segment.split('-')
            count=int(count_str)
            result.extend([value]*count)

        return result
    except:
        #print(s)
        iop=1/0




def zhu_hs():
    global yan_se
    global schu
    global ming
    global asd
    global yui
    global bina_l
    global sgu_f
    global y
    global x,z,qwe,chu_yun,yuan_x,yuan_z,qi_x,qi_z

    try:
        chuasd()
        chushi()
        while True:
            if asd[bina_l][0]=="空":
                sgu_f=0

            if sgu_f==1:
                if asd[bina_l][0]!="奉":
                    y=y+1
                    dfg=decompress_string(asd[bina_l])
                    try:
                        while True:
                            yui[str(qi_x+x)+"/"+str(y)+"/"+str(qi_z+z)]=dfg[0]
                            lei(dfg[0])
                            del dfg[0]
                            z=z+1
                            if z==16:
                                z=0
                                x=x+1

                    except:
                        #print(x)
                        x=0
                        z=0

            if asd[bina_l][0]=="奉":
                schu.write(asd[bina_l])
                sgu_f=1
                qi_x=extract_numbers(asd[bina_l])[0]
                qi_z=extract_numbers(asd[bina_l])[1]
                y=0
            bina_l=bina_l+1
    except Exception as e:
            print(e)
            print("导入结束")
            x,z=0,0
            schu=open("出云","a")
            try:
                while True:
                    dcf=luo_d(yuan_x+x,yuan_z+z)
                    if dcf[0]!=114514:
                        schu.write(str([yuan_x+x,yuan_z+z,dcf[0],dcf[1]])+"\n")
                    x=x+1
                    if x==512:
                        x=0
                        z=z+1
                        #print(yan(fan(yuan_x+x,50,yuan_z+z)))
                        if z==512:
                            yi=1/0
                            break
            except Exception as e:
                print(e)
                print("渲染结束")


while True:
    zhu_hs()
