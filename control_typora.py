#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/12 13:49
# @Author  : jjc
# @File    : control_typora.py
# @Software: PyCharm
import win32api
from pywinauto import Application


# def control_typroa_exe(path):
    # app = Application().start("Typora/Typora.exe")
    # # print(app["Typora"].ChildWindow)
    # f = app.window(title_re=".*Typora.*")
    # f2 = f.child_window(title="Chrome Legacy Window", class_name="Chrome_RenderWidgetHostHWND")
    # f2["帮助"].click()
    # win32api.ShellExecute(0, 'open', 'Typora.exe', path, "", 1)


# def open_txt():
#     app = Application().start("notepad.exe")
#     app["无标题-记事本"].menu_select("帮助->关于记事本").click()
#
#
# def win32_open():
#     path = r"C:\Users\jjc\Desktop\新建文本文档 (4).txt"
#     win32api.ShellExecute(0, 'open', 'Typora.exe', r"C:\Users\jjc\Documents\myTypora\111.md", "", 1)


# if __name__ == '__main__':
#     win32_open()
