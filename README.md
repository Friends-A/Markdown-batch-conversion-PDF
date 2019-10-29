# Markdown-batch-conversion-PDF
将当前目录和子目录下的.md文件转换成.pdf文件

**目前只支持Linux下的转换**

Windows改改源码应该可以运行，没有Mac系统，所以不知道能不能运行
## 使用说明
需要安装pandoc和xelatex环境

将需要转换的markdown文件放在同一个文件夹下，将该文件夹与code.py和template.latex放在同一个父文件夹下

命令行执行
```
$ python code.py
```
## 存在的问题
- latex字体库里没有的字符会出现warning，但是不影响文件的输出
- py文件和latex文件所在目录下的md文件不能转换，只能转换子目录下的.md文件（~~这个以后有时间了会改的~~）
- .md文件里应用的本地图片的文件夹名必须相同，可以在template.latex中更改文件夹名称
- 还有一些未知的错误导致文件无法输出，但是这种情况很少，大部分都可以正常输出
