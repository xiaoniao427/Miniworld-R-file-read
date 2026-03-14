qwe=open("出云","r",encoding="utf-8")
qwe=qwe.readlines()
asd=0
gao=[]
gao_=open("高度","w")
lei_=open("类型","w")
try:
    while True:
        zxc=eval(qwe[asd])
        try:
            rty=0
            while True:
                gao_.write(str([zxc[0],zxc[1],zxc[3]])+"\n")
                lei_.write(str([zxc[0],zxc[1],zxc[2]])+"\n")
                rty=rty+1
        except:
            asd=asd+1
            print(asd)

except:
    pass
