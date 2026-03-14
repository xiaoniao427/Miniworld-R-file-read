import math
import random

yui=open("编码","r",encoding="utf-8")
yui=yui.readlines()

zhun={}
qwe=0
try:
    while True:
        tyu=eval(yui[qwe])
        try:
            while True:
                try:
                    zhun[tyu["名单"][0]]=zhun[tyu["名单"][0]]+tyu[tyu["名单"][0]]
                except:
                    zhun[tyu["名单"][0]]=tyu[tyu["名单"][0]]
                del tyu["名单"][0]
        except:pass
        qwe=qwe+1
        if qwe%1000==0:
            print(qwe)
except Exception as e:
    print(e)
    print(zhun)