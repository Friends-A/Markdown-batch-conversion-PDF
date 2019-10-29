#-*-coding:utf-8-*-
import os

# 查找当前目录下suffix后缀的文件
def getFiles(dir, suffix):
    res = []
    for root, directory, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    return res

root = os.getcwd()
print(root)
temp = os.path.join(root, 'template.latex')
os.chdir(root)
cnt=len(getFiles('./','.md'))
now=0

f=open('logs.txt','w+')

for file in getFiles('./', '.md'):
    print(file,end=' ',file=f)
    file = file[2:]
    path = os.path.dirname(file)
    file = file[len(path) + 1:]
    filename0 = os.path.splitext(file)[0]
    relname = filename0 + '.pdf'
    os.chdir(path)
    order = 'pandoc --pdf-engine=xelatex --template=' + temp + ' ' + file + ' -o ' + relname
    isok=os.system(order)
    print('当前进度:',end=' ')
    now+=1
    print('%d/%d'%(now,cnt))
    os.chdir(root)
    if isok:
        print('转换失败',file=f)
    else:
        print('转换成功',file=f)
