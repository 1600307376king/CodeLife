#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 23:16
# @Author  : jjc
# @File    : base_window.py
# @Software: PyCharm
from PyQt6.QtWidgets import QMainWindow
from config import window_height
from config import window_width
from config import window_title


class BaseWindow(QMainWindow):
    def __init__(self):
        super(BaseWindow, self).__init__()
        # self.window_width = window_width
        # self.window_height = window_height
        # self.window_title = window_title
        # self.init_position = window_init_position
        # self.screen =
