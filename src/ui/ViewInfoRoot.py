'''
@coding=UTF-8
@auther:Yan Chen, Fei JianLin, Yang Cheng, Tang YuHao
@time:2020-06
@ui:View Info of Root
'''

# 导入模块
from tkinter import *
from tkinter import messagebox
import pandas as pd
from datetime import datetime

'''
下面是生成查看学生信息页面的代码
'''
def ViewInfoRoot():
    viewInfoRoot = Tk()
    viewInfoRoot.title('欢迎来到学生管理系统！')
    viewInfoRoot.geometry('600x350+300+300')
    viewInfoRoot['bg'] = 'lightblue'
    viewInfoRoot.attributes('-alpha', 0.9)

    # 点击"返回"按钮的操作
    def clickReturnR():
        viewInfoRoot.destroy()

    # 点击"导出"按钮的操作
    def clickExportR():
        value = 1
        with open('../lib/export.txt', 'a') as file:
            ntime = datetime.utcnow()
            stime = ntime.strftime("%Y-%m-%d %H:%M:%S")
            file.write(str(readR()))
            file.write('\n')
            file.write(str(ntime))
            file.write('\n')
        messagebox.showinfo('提示', '导出成功！')

    # 初始化控件
    showInfoRoot = Frame(viewInfoRoot)
    showInfoRoot.pack()
    btnRoot = Frame(viewInfoRoot)
    btnRoot.pack()

    # 信息显示
    textR = Text(showInfoRoot)
    textR.grid(row=0)
    textR.insert(END, readR())

    # 按钮显示
    Button(btnRoot, text='返回', width=10, height=1, relief=GROOVE, command=clickReturnR).grid(row=1, column=0)
    Button(btnRoot, text='导出', width=10, height=1, relief=GROOVE, command=clickExportR).grid(row=1, column=1)

    viewInfoRoot.mainloop()

# 读取表格
def readR():
    ioR = r'../lib/Students.xlsx'
    dataR = pd.read_excel(ioR, sheet_name=0, names=['ID', 'Name', 'Sex', 'Age', 'Math', 'C', 'Java'])
    return dataR

if __name__ == '__main__':
    ViewInfoRoot()