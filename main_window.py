#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 22:08
# @Author  : jjc
# @File    : main_window.py
# @Software: PyCharm
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QAbstractButton
from PyQt6.QtWidgets import QPushButton, QButtonGroup, QStyleOption, QMdiSubWindow, \
    QMenu, QWidgetAction, QPlainTextEdit
from PyQt6.QtGui import QAction
from main_menu import MainMenu
# from base_window import BaseWindow
from config import window_height
from config import window_width
from config import window_title
from config import window_init_position


class CodeManagerTool(MainMenu):

    def run(self):
        """
        run tools
        :return:
        """

        self.resize(self.window_width, self.window_height)
        self.move(*self.init_position)
        self.show()
