'''
@coding=UTF-8
@auther:Yan Chen, Fei JianLin, Yang Cheng, Tang YuHao
@time:2020-06
@ui:Home of Stu
'''

# 导入模块
import tkinter as tk
from tkinter import *
import time
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter
import PIL as pil
from src.ui.ViewInfoStu import ViewInfoStu
from src.ui.ViewScoreStu import ViewScoreStu

'''
下面是生成首页窗体的代码
'''
def HomeStu():
    homeStu = tk.Toplevel()
    homeStu.title('欢迎来到学生管理系统！')
    homeStu.geometry('400x300+300+300')
    homeStu['bg'] = 'lightblue'
    homeStu.attributes('-alpha', 0.9)
    recentTime = ''

    # 获取当前时间
    def getTime():
        timeStr = time.strftime('%H:%M:%S')
        Stime.configure(text=timeStr)
        homeStu.after(1000, getTime)

    # 点击"查看我的信息"按钮的操作
    def clickBtns1():
        ViewInfoStu()

    # 点击"查看我的成绩"按钮的操作
    def clickBtns2():
        ViewScoreStu()

    # 点击"退出登录"按钮的操作
    def clickBtns3():
        homeStu.destroy()

    # 初始化变量
    sWelStr = '您好，' + 'Student'

    # 图片获取
    sPhoto = pil.Image.open('../lib/stu.png')
    sImg = pil.ImageTk.PhotoImage(sPhoto)

    # 图片显示
    sImgShow = tk.Label(homeStu, image=sImg, bg='lightblue')
    sImgShow.grid(row=0, column=0, rowspan=6, columnspan=6, ipady=60)

    # 时间显示
    Stime = tk.Label(homeStu, text='', bg='lightblue')
    Stime.grid(row=0, column=8)
    getTime()

    # 欢迎显示
    Swel = tk.Label(homeStu, text=sWelStr, bg='lightblue')
    Swel.grid(row=1, column=8)

    # 按钮显示
    tk.Button(homeStu, text='查看我的信息', width=15, height=1, command=clickBtns1).grid(row=2, column=8, ipady=10, padx=20)
    tk.Button(homeStu, text='查看我的成绩', width=15, height=1, command=clickBtns2).grid(row=3, column=8, ipady=10, padx=20)
    tk.Button(homeStu, text='退出登录', width=15, height=1, command=clickBtns3).grid(row=4, column=8, ipady=10, padx=20)

    homeStu.mainloop()

if __name__ == '__main__':
    HomeStu()