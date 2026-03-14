import os
import zlib
import pickle

DATA_FILE = 'data.nb'
INDEX_FILE = 'index.nb'

# 1. 初始化数据库
def init_db():
    open(DATA_FILE, 'wb').close()  # 创建/清空 数据文件
    with open(INDEX_FILE, 'wb') as f:
        pickle.dump({}, f)  # 创建空字典索引文件

# 2. 存入数据（key: str, value: any）
def store_data(key, value):
    global zong
    zong=zong+1
    #print(key)
    # 压缩数据
    compressed = zlib.compress(pickle.dumps(value))

    # 获取当前文件末尾位置
    start = os.path.getsize(DATA_FILE)
    end = start + len(compressed)

    # 写入压缩数据
    with open(DATA_FILE, 'ab') as f:
        f.write(compressed)

    # 更新索引
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'rb') as f:
            index = pickle.load(f)
    else:
        index = {}

    index[key] = (start, end)

    with open(INDEX_FILE, 'wb') as f:
        pickle.dump(index, f)

# 3. 读取数据（通过 key）
def load_data(key):
    with open(INDEX_FILE, 'rb') as f:
        index = pickle.load(f)

    if key not in index:
        raise KeyError(f"{key} 不存在")

    start, end = index[key]
    length = end - start

    with open(DATA_FILE, 'rb') as f:
        f.seek(start)
        compressed = f.read(length)

    value = pickle.loads(zlib.decompress(compressed))
    return value


zong=0
init_db()
asd=os.listdir()
while True:
    while asd[0][0]!="x":
        del asd[0]
    qwe=open(asd[0],"r")
    print("————————————————————————")
    print(asd[0])
    print(len(asd))
    print("已录入"+str(zong)+"个区块")
    del asd[0]
    qwe=qwe.readlines()
    uio=0
    ert=[]
    suo_yin=""
    try:
        while True:
            qwe[uio]=qwe[uio].replace("\n","")
            if qwe[uio][0]=="奉":
                if suo_yin!="":
                    store_data(suo_yin,ert)
                suo_yin=qwe[uio]
                ert=[]
            else:
                ert.append(qwe[uio])
            uio=uio+1
    except Exception as e:
        print(e)
        if suo_yin!="":
            store_data(suo_yin,ert)
            print("收个尾")




