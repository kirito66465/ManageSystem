'''
@coding=UTF-8
@auther:Yan Chen, Fei JianLin, Yang Cheng, Tang YuHao
@time:2020-06
@ui:Home of Root
'''

# 导入模块
import tkinter as tk
from tkinter import *
import time
import PIL as pil
from src.ui.ViewInfoRoot import ViewInfoRoot
from src.ui.ModifyRoot import ModifyRoot

'''
下面是生成首页窗体的代码
'''
def HomeRoot():
    homeRoot = tk.Toplevel()
    homeRoot.title('欢迎来到学生管理系统！')
    homeRoot.geometry('400x300+300+300')
    homeRoot['bg'] = 'lightblue'
    homeRoot.attributes('-alpha', 0.9)

    # 获取当前时间
    def getTime():
        timeStr = time.strftime('%H:%M:%S')
        Rtime.configure(text=timeStr)
        homeRoot.after(1000, getTime)

    # 点击“查看学生信息”按钮的操作
    def clickBtnr1():
        ViewInfoRoot()

    # 点击“修改学生信息”按钮的操作
    def clickBtnr2():
        ModifyRoot()

    # 点击"退出登录"按钮的操作
    def clickBtnr3():
        homeRoot.destroy()

    # 初始化变量
    rWelStr = '您好，' + 'Teacher'

    # 图片获取
    rPhoto = pil.Image.open('../lib/root.png')
    rImg = pil.ImageTk.PhotoImage(rPhoto)

    # 图片显示
    rImgShow = tk.Label(homeRoot, image=rImg, bg='lightblue')
    rImgShow.grid(row=0, column=0, rowspan=6, columnspan=6, ipady=60)

    # 时间显示
    Rtime = tk.Label(homeRoot, text='', bg='lightblue')
    Rtime.grid(row=0, column=8)
    getTime()

    # 欢迎显示
    Rwel = tk.Label(homeRoot, text=rWelStr, bg='lightblue')
    Rwel.grid(row=1, column=8)

    # 按钮显示
    tk.Button(homeRoot, text='查看学生信息', width=15, height=1, command=clickBtnr1, relief=GROOVE).grid(row=2, column=8, ipady=10, padx=20)
    tk.Button(homeRoot, text='修改学生信息', width=15, height=1, command=clickBtnr2, relief=GROOVE).grid(row=3, column=8, ipady=10, padx=20)
    tk.Button(homeRoot, text='退出登录', width=15, height=1, command=clickBtnr3, relief=GROOVE).grid(row=4, column=8, ipady=10, padx=20)

    homeRoot.mainloop()

if __name__ == '__main__':
    HomeRoot()