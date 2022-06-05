#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/4 13:07
# @Author  : jjc
# @File    : theme_frame.py
# @Software: PyCharm
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize

from chapter import OneChapter
from config import SUB_CHAPTER_BTN_WIDTH
from config import SUB_CHAPTER_BTN_HEIGHT
from config import SUB_CHAPTER_BTN_BASE_X
from config import SUB_CHAPTER_BTN_BASE_Y
from config import SUB_CHAPTER_BTN_HEIGHT_SPACE
from config import BROWSER_MINIMUM_SIZE
from config import WINDOW_SIZE
from config import THEME_FRAME_SIZE
from config import THEME_FRAME_MAX_HEIGHT
from config import MAX_SIZE_NUM
from config import THEME_BASE_X
from config import THEME_BASE_Y
from config import THEME_WIDTH
from config import THEME_HEIGHT
from config import THEME_FONT_SIZE
from config import SUB_CHAPTER_LIST_BASE_X
from config import SUB_CHAPTER_LIST_BASE_Y
from config import SUB_CHAPTER_LIST_WIDTH
from config import SUB_CHAPTER_LIST_HEIGHT
from config import SUB_CHAPTER_LIST_MINIMUM_SIZE
from config import SUB_CHAPTER_LIST_MAX_WIDTH
from config import SUB_CHAPTER_SCROLL_SHAPE
from config import MENU_GROUP_SHAPE
from config import THEME_CONTAINER_LABEL_SIZE
from config import SUB_CHAPTER_SCROLL_WIDTH
from config import THEME_BTN_BASE_X
from config import THEME_BTN_WIDTH_SPACE
from config import SUB_CHAPTER_HIGHLIGHT_STYLE
from config import SUB_CHAPTER_NORMAL_STYLE
from config import THEME_NORMAL_STYLE
from config import THEME_HIGHLIGHT_STYLE
from config import THEME_FRAME_STYLE
from config import SUB_CHAPTER_AREA_STYLE
from config import TOOLS_BAR_STYLE
from config import THEME_BROWSER_STYLE
from config import THEME_CONTAINER_STYLE
from db_model.theme_note import ThemeNote
from db_model.chapter_note import ChapterNote
from tools_bar_group.switch_button import SwitchButton
from signal_manager import SignalManager


# class ThemeFrame:
#     def __init__(self, central_widget):
#         self.frame = QFrame(central_widget)
#         self.add_theme_btn = QPushButton(self.frame)
#         self.theme_arr = []
#
#
#     def _create_theme_btn(self, theme_name):
#         """
#         创建主题按钮
#         :param theme_name:
#         :return:
#         """
#         btn_pos_x = THEME_BTN_BASE_X
#         if self.theme_arr:
#             btn_pos_x = self.theme_arr[-1].x() + THEME_BTN_WIDTH_SPACE
#         new_theme_btn = QPushButton(self.frame)
#         new_theme_btn.setGeometry(QRect(btn_pos_x, THEME_BASE_Y,
#                                         THEME_BASE_X + THEME_WIDTH,
#                                         THEME_BASE_Y + THEME_HEIGHT))
#         self.theme_font.setFamily("楷体")
#         self.theme_font.setPointSize(THEME_FONT_SIZE)
#         new_theme_btn.setText(theme_name)
#         new_theme_btn.setFont(self.theme_font)
#         new_theme_btn.setStyleSheet(THEME_NORMAL_STYLE)
#         new_theme_btn.setObjectName(theme_name)
#         new_theme_btn.clicked.connect(lambda: self._switch_theme_content(new_theme_btn.text()))
#         # 允许按钮右键创建子菜单
#         new_theme_btn.setContextMenuPolicy(Qt.CustomContextMenu)
#         # 绑定菜单创建函数
#         new_theme_btn.customContextMenuRequested.connect(lambda: self._show_btn_menu(new_theme_btn.text()))
#
#         new_theme_btn.show()
#         self.add_theme_btn.move(btn_pos_x + THEME_BTN_WIDTH_SPACE, THEME_BASE_Y)
#         return new_theme_btn