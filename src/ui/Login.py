'''
@coding=UTF-8
@auther:Yan Chen, Fei JianLin, Yang Cheng, Tang YuHao
@time:2020-06
@ui:Log In
'''

# 导入模块
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter
import PIL as pil
import random
import string
from src.ui.HomeRoot import HomeRoot
from src.ui.HomeStu import HomeStu
from src.ui.UserID import *

# 定义全局变量
global geneCode             # 生成的验证码
global img                  # 生成的验证码图片
global photo                # 获取的验证码图片
global geneNumber           # 生成几位数的验证码
geneNumber = 4              # 验证码位数设置为4位

'''
下面是生成登录窗体的代码
'''
def Login():
    login = tk.Tk()
    login.title('登录')
    login.geometry('300x450+200+200')
    login.attributes('-alpha', 0.9)

    # 获取当前时间
    def getTime():
        timeStr = time.strftime('%H:%M:%S')         # 获取当前时间并转换为字符串
        lab_time.configure(text=timeStr)            # 重新设置标签文本
        login.after(1000, getTime)                  # 每隔1s调用函数自身获取时间

    # 点击'确定登录'按钮的操作
    def btnOK():
        if entryUserName.get() == 'root' and entryPassword.get() == 'root':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                messagebox.showinfo('提示', '登录成功！')
                HomeRoot()
        elif entryUserName.get() == '20001' and entryPassword.get() == '20001':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20002' and entryPassword.get() == '20002':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20003' and entryPassword.get() == '20003':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20004' and entryPassword.get() == '20004':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20005' and entryPassword.get() == '20005':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20006' and entryPassword.get() == '20006':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20007' and entryPassword.get() == '20007':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20008' and entryPassword.get() == '20008':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20009' and entryPassword.get() == '20009':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20010' and entryPassword.get() == '20010':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        else:
            messagebox.showwarning('警告！', '用户名或密码输入错误！')

    def btnEnterOK(event):
        if entryUserName.get() == 'root' and entryPassword.get() == 'root':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                messagebox.showinfo('提示', '登录成功！')
                HomeRoot()
        elif entryUserName.get() == '20001' and entryPassword.get() == '20001':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20002' and entryPassword.get() == '20002':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20003' and entryPassword.get() == '20003':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20004' and entryPassword.get() == '20004':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20005' and entryPassword.get() == '20005':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20006' and entryPassword.get() == '20006':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20007' and entryPassword.get() == '20007':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20008' and entryPassword.get() == '20008':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20009' and entryPassword.get() == '20009':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        elif entryUserName.get() == '20010' and entryPassword.get() == '20010':
            if entryVerify.get() != geneCode:
                messagebox.showwarning('警告！', '验证码输入错误！')
            else:
                setID(int(entryUserName.get()) - 19999)
                messagebox.showinfo('提示', '登录成功！')
                HomeStu()
        else:
            messagebox.showwarning('警告！', '用户名或密码输入错误！')

    # 点击'重置输入'按钮的操作
    def btnReset():
        var_username.set('')                        # 用户名输入框置空
        var_password.set('')                        # 密码输入框置空
        var_verify.set('')                          # 验证码输入框置空
        messagebox.showinfo('提示', '重置输入成功！')

    # 点击'更换验证码'按钮的操作
    def btnSet():
        gene_code()
        photo = pil.Image.open('../lib/gene_code.png')
        img = pil.ImageTk.PhotoImage(photo)
        verifyImage.configure(image=img)
        login.update_idletasks()
        messagebox.showinfo('提示', '验证码更换成功！')

    # 初始化控件
    gene_code()                                        # 生成验证码
    f_time = tk.Frame(login)                           # 时间框架
    f_time.pack()
    f_username = tk.Frame(login)                       # 用户名框架
    f_username.pack()
    f_password = tk.Frame(login)                       # 密码框架
    f_password.pack()
    f_verify = tk.Frame(login)                         # 验证码框架
    f_verify.pack()
    f_log = tk.Frame(login)                            # 按钮框架
    f_log.pack()

    # 获取验证码图片
    photo = pil.Image.open('../lib/gene_code.png')
    img = pil.ImageTk.PhotoImage(photo)

    # 输入获取
    var_username = tk.StringVar()
    var_password = tk.StringVar()
    var_verify = tk.StringVar()

    # 时间显示
    lab_time = tk.Label(f_time, text='')
    lab_time.grid(row=0)
    getTime()

    # 用户名控件
    tk.Label(f_username, text='用户名').grid(row=1, column=0, ipady=30, ipadx=10)
    entryUserName = tk.Entry(f_username, textvariable=var_username)
    entryUserName.grid(row=1, column=1, columnspan=3)

    # 密码控件
    tk.Label(f_password, text='密   码').grid(row=2, column=0, ipady=30, ipadx=10)
    entryPassword = tk.Entry(f_password, show='*', textvariable=var_password)
    entryPassword.grid(row=2, column=1, columnspan=3)

    # 验证码控件
    tk.Label(f_verify, text='验证码').grid(row=3, column=0, ipady=30, ipadx=10)
    entryVerify = tk.Entry(f_verify, textvariable=var_verify)
    entryVerify.grid(row=3, column=1, columnspan=3)
    verifyImage = tk.Label(f_verify, image=img)
    verifyImage.grid(row=4, column=1, ipady=10)

    # 按钮控件
    tk.Button(f_log, text='更换验证', command=btnSet, relief=GROOVE).grid(row=5, column=1, ipady=5, pady=3, columnspan=2)
    tk.Button(f_log, text='重置输入', command=btnReset, relief=GROOVE).grid(row=6, column=0, ipady=5, pady=3, columnspan=2, padx=1)
    tk.Button(f_log, text='确定登录', command=btnOK, relief=GROOVE).grid(row=6, column=2, ipady=5, pady=3, columnspan=2, padx=1)

    login.bind('<Return>', btnEnterOK)
    login.mainloop()

'''
下面是生成验证码的代码
'''
# 随机生成一个字符串
def gene_text():
    source = list(string.ascii_letters)
    for index in range(0, 10):
        source.append(str(index))
    return ''.join(random.sample(source, geneNumber))
# 绘制干扰线
def gene_line(draw, width, height):
    line_number = (1, 5)                                            # 加入干扰线条数的上下限
    linecolor = (255, 0, 0)                                         # 干扰线颜色。默认为红色
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)
# 生成验证码
def gene_code():
    font_path = '/System/Library/Fonts/NewYork.ttf'
    # font_path = 'C:\\Windows\\Fonts\\TIMESBD.TTF'             # 字体的位置，不同版本的系统会有不同
    size = (70, 30)                                             # 生成验证码图片的高度和宽度
    bgcolor = 'lightblue'                                       # 背景颜色，默认为白色
    fontcolor = (0, 0, 255)                                     # 字体颜色，默认为蓝色
    draw_line = True                                            # 是否要加入干扰线
    width, height = size                                        # 宽和高
    image = pil.Image.new('RGBA', (width, height), bgcolor)     # 创建图片
    font = pil.ImageFont.truetype(font_path, 25)                # 验证码的字体
    draw = pil.ImageDraw.Draw(image)                            # 创建画笔
    text = gene_text()                                          # 生成字符串
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / geneNumber, (height - font_height) / geneNumber), text,
              font=font, fill=fontcolor)                        # 填充字符串
    if draw_line:
        gene_line(draw, width, height)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)         # 滤镜，边界加强
    image.save('../lib/gene_code.png')                          # 保存验证码图片
    global geneCode
    geneCode = text                                             # 保存生成的验证码

if __name__ == '__main__':
    Login()