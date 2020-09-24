# run.py

source = open("./GroundTruth.txt","r")        #源文件的路径
nameset = set()
num = len(source.readlines())
source.seek(0)
# print(num)

for i in range(num):
    line = source.readline()
    line_s = line.split(";")
    end =line_s[-1][:-1]+" 000"+"".join(line_s[1:5])+"0000000\n"
    filename = line_s[0][:-3]+"txt"
    nameset.add(line_s[0])
    with open("./dist/%s"%filename,"a") as fo: #目标文件夹
        fo.write(end)
        
source.close()   
print("一共%d张图片"%(len(nameset)))