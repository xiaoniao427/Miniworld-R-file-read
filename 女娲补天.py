import os
import re

def extract_coordinates(s):
    numbers = re.findall(r'-?\d+', s)
    return (int(numbers[0]), int(numbers[1])) if len(numbers) >= 2 else None


asd=os.listdir()
schu=open("nsdd","w")
while True:
    print(asd[0])
    if asd[0][-1]=="r":
        qwe=extract_coordinates(asd[0])
        schu.write(str(qwe[0])+"/"+str(qwe[1])+"\n")
    del asd[0]