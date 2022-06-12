#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/20 23:16
# @Author  : jjc
# @File    : base_window.py
# @Software: PyCharm

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from config import TOOLS_BAR_FAMILY
from config import TOOLS_BAR_FONT_SIZE
from config import THEME_FAMILY
from config import THEME_FONT_SIZE
from config import SUB_CHAPTER_FAMILY
from config import SUB_CHAPTER_FONT_SIZE


class BaseWindow(QMainWindow, QDialog):
    def __init__(self):
        super().__init__()
        self.theme_font = QFont()
        self.tools_bar_font = QFont()
        self.sub_chapter_font = QFont()
        self._init_font()

    def _init_font(self):
        """
        init main window all component font
        :return:
        """
        self.theme_font.setFamily(THEME_FAMILY)
        self.theme_font.setPointSize(THEME_FONT_SIZE)

        self.tools_bar_font.setFamily(TOOLS_BAR_FAMILY)
        self.tools_bar_font.setPointSize(TOOLS_BAR_FONT_SIZE)

        self.sub_chapter_font.setFamily(SUB_CHAPTER_FAMILY)
        self.sub_chapter_font.setPointSize(SUB_CHAPTER_FONT_SIZE)

