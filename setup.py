# coding:utf8

from distutils.core import setup

setup(name="ui",                                                      # 包名
      version="1.0",                                                  # 版本
      description="学生管理系统",                                       # 描述信息
      long_description="管理员和学生可使用的学生管理系统，可查看修改信息",  # 完整描述信息
      author="kirito66045",                                           # 主要作者
      author_email="kiritochen0845@qq.com",                           # 主要作者邮箱
      url="https://www.jianshu.com/u/f52e7e7127b3",                   # 主要作者简书主页
      py_modules=["src.ui.Login",
          "src.ui.HomeRoot",
          "src.ui.HomeStu",
          "src.ui.ViewInfoRoot"
          "src.ui.ModifyRoot"])