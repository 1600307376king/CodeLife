#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 22:08
# @Author  : jjc
# @File    : main_window.py
# @Software: PyCharm
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from config import window_height
from config import window_width
from config import window_title
from config import window_init_position


class CodeManagerTool(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window_width = window_width
        self.window_height = window_height
        self.window_title = window_title
        self.init_position = window_init_position


    def run(self):
        """
        run tools
        :return:
        """

        self.resize(self.window_width, self.window_height)
        self.move(*self.init_position)
        self.setWindowTitle(window_title)
        self.show()


