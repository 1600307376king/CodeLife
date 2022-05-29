#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/21 17:13
# @Author  : jjc
# @File    : main_win.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

"""
主窗口，多种类别资料展示
"""
from PyQt5.QtGui import QFont
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
from db_model.theme_note import ThemeNote
from db_model.chapter_note import ChapterNote


class MainWin(QMainWindow, QDialog):
    """
    主窗体
    """

    def __init__(self):
        super().__init__()
        self.setObjectName("main_window")
        self.resize(*WINDOW_SIZE)
        self.setMinimumSize(QSize(*WINDOW_SIZE))

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setObjectName("grid_layout")
        self.theme_frame = QFrame(self.central_widget)

        self.grid_layout.addWidget(self.theme_frame, 0, 0, 1, 1)

        self.add_theme_btn = QPushButton(self.theme_frame)
        self.theme_font = QFont()
        self.theme_container = QFrame(self.central_widget)
        self.grid_layout.addWidget(self.theme_container, 1, 0, 1, 1)

        self.grid_layout_chapter = QGridLayout(self.theme_container)
        self.grid_layout_chapter.setObjectName("grid_layout_chapter")

        self.sub_chapters = QScrollArea(self.theme_container)
        self.grid_layout_chapter.addWidget(self.sub_chapters, 0, 0, 1, 1)

        self.scroll_area_widget_contents = QWidget()

        self.add_sub_chapter_btn = QPushButton(
            self.scroll_area_widget_contents)

        self.theme_container_label = QLabel(self.theme_container)
        self.grid_layout_chapter.addWidget(
            self.theme_container_label, 0, 1, 1, 1)

        self.menubar = QMenuBar(self)
        self.menu_file = QMenu(self.menubar)
        self.menu_edit = QMenu(self.menubar)
        self.menu_window = QMenu(self.menubar)
        self.menu_help = QMenu(self.menubar)
        self.statusbar = QStatusBar(self)
        self.action_open = QAction(self)
        self.action_new_theme = QAction(self)

        self.chapter_arr = []
        self.chapter_set = set()
        self.theme_arr = []
        self.theme_set = set()

        self.be_select_theme = None

    def add_chapter_data(self, chapter_info):
        """
        新增chapter数据，初始化UI
        :param chapter_info:
        :return:
        """
        if self.be_select_theme is None:
            self.be_select_theme = self.theme_arr[0].text()
        with ChapterNote() as cn:
            cn.insert_note(self.be_select_theme, *chapter_info)
        self._add_chapter_btn(chapter_info)

    def _add_chapter_btn(self, chapter_info):
        """
        添加文章UI
        :param chapter_info:
        :return:
        """
        btn_text_name, content = chapter_info

        if btn_text_name:
            push_button = self._set_chapter_btn(btn_text_name)

            browser = QTextBrowser(self.theme_container)
            # browser.setGeometry(QtCore.QRect(150, 0, 621, 431))
            size_policy = QSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Preferred)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(
                browser.sizePolicy().hasHeightForWidth())
            browser.setSizePolicy(size_policy)
            browser.setMinimumSize(QSize(*BROWSER_MINIMUM_SIZE))
            browser.setReadOnly(True)
            self.grid_layout_chapter.addWidget(browser, 0, 1, 1, 1)

            browser.setObjectName("context")
            browser.setMarkdown(content)
            browser.show()

            # 将之前的textBrowser隐藏，只显示新增的
            if self.chapter_arr:
                self.chapter_arr[-1].browser_content.hide()
            push_button.clicked.connect(lambda: self._switch_chapter_content(push_button.text()))
            one_chapter = OneChapter(push_button, browser)
            self.chapter_arr.append(one_chapter)
            self._set_sub_chapter_scroll()

    def add_theme(self, theme_name):
        """
        添加主题
        :param theme_name:
        :return:
        """
        if theme_name:
            new_theme_btn = self._create_theme_btn(theme_name)
            self.theme_arr.append(new_theme_btn)
            self.theme_set.add(theme_name)
            with ThemeNote() as tn:
                tn.insert_theme(theme_name)
            self.be_select_theme = theme_name

    def _switch_theme_content(self, theme_name):
        """
        切换主题
        :param theme_name:
        :return:
        """
        self.be_select_theme = theme_name
        for ch in self.chapter_arr:
            ch.chapter_btn.deleteLater()
            ch.browser_content.deleteLater()
        self.chapter_arr.clear()
        self.chapter_set.clear()
        for theme in self.theme_arr:
            if theme.text() == theme_name:
                theme.setStyleSheet("border-radius:5px;\nborder:1px solid;background-color: rgb(255, 229, 192);")
            else:
                theme.setStyleSheet("border-radius:5px;\nborder:1px solid")
        with ChapterNote() as cn:
            query_data = cn.select_note(theme_name)
        for row in query_data:
            self._add_chapter_btn(row)

    def _switch_chapter_content(self, chapter_name):
        for chapter in self.chapter_arr:
            if chapter.chapter_btn.text() == chapter_name:
                chapter.chapter_btn.setStyleSheet(
                    "border:10px;\nborder:1px solid rgb(0, 0, 0);\n;background-color: rgb(255, 229, 192);")
                chapter.browser_content.show()
            else:
                chapter.chapter_btn.setStyleSheet("border:10px;\nborder:1px solid rgb(0, 0, 0);\n")
                chapter.browser_content.hide()

    def _create_theme_btn(self, theme_name):
        """
        创建主题按钮
        :param theme_name:
        :return:
        """
        btn_pos_x = THEME_BTN_BASE_X
        if self.theme_arr:
            btn_pos_x = self.theme_arr[-1].x() + THEME_BTN_WIDTH_SPACE
        new_theme_btn = QPushButton(self.theme_frame)
        new_theme_btn.setGeometry(QRect(btn_pos_x, THEME_BASE_Y,
                                        THEME_BASE_X + THEME_WIDTH,
                                        THEME_BASE_Y + THEME_HEIGHT))
        self.theme_font.setFamily("楷体")
        self.theme_font.setPointSize(THEME_FONT_SIZE)
        new_theme_btn.setText(theme_name)
        new_theme_btn.setFont(self.theme_font)
        new_theme_btn.setStyleSheet("border-radius:5px;\nborder:1px solid")
        new_theme_btn.setObjectName(theme_name)
        new_theme_btn.clicked.connect(lambda: self._switch_theme_content(new_theme_btn.text()))
        new_theme_btn.show()
        self.add_theme_btn.move(btn_pos_x + THEME_BTN_WIDTH_SPACE, THEME_BASE_Y)
        return new_theme_btn

    def _set_chapter_btn(self, btn_text_name):
        """
        动态添加的按钮初始化
        :param btn_text_name:
        :return: btn
        """
        btn_pos_y = SUB_CHAPTER_BTN_BASE_Y + SUB_CHAPTER_BTN_HEIGHT_SPACE
        if self.chapter_arr:
            btn_pos_y = \
                self.chapter_arr[-1].chapter_btn.y() + \
                SUB_CHAPTER_BTN_HEIGHT_SPACE
        push_button = QPushButton(self.scroll_area_widget_contents)
        push_button.setObjectName(btn_text_name)
        push_button.setGeometry(
            QRect(
                SUB_CHAPTER_BTN_BASE_X,
                btn_pos_y,
                SUB_CHAPTER_BTN_BASE_X + SUB_CHAPTER_BTN_WIDTH,
                SUB_CHAPTER_BTN_BASE_Y + SUB_CHAPTER_BTN_HEIGHT))
        push_button.setText(btn_text_name)
        push_button.setStyleSheet(
            "border:10px;\nborder:1px solid rgb(0, 0, 0);\n")
        push_button.show()
        return push_button

    def _init_add_note_btn(self):
        """
        初始化添加按钮
        :return:
        """
        self.add_sub_chapter_btn.setGeometry(
            QRect(
                SUB_CHAPTER_BTN_BASE_X, SUB_CHAPTER_BTN_BASE_Y,
                SUB_CHAPTER_BTN_BASE_X + SUB_CHAPTER_BTN_WIDTH,
                SUB_CHAPTER_BTN_BASE_Y + SUB_CHAPTER_BTN_HEIGHT
            ))
        self.add_sub_chapter_btn.setStyleSheet(
            "border:10px;\nborder:1px solid rgb(0, 0, 0);\n")
        self.add_sub_chapter_btn.setObjectName("add_sub_chapter")

    def _init_theme_frame(self):
        """
        主题选择按钮面板
        :return:
        """
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.theme_frame.sizePolicy().hasHeightForWidth())
        self.theme_frame.setSizePolicy(size_policy)
        self.theme_frame.setMinimumSize(QSize(*THEME_FRAME_SIZE))
        self.theme_frame.setMaximumSize(
            QSize(MAX_SIZE_NUM, THEME_FRAME_MAX_HEIGHT))
        self.theme_frame.setStyleSheet("background-color: rgb(174, 255, 181);")
        self.theme_frame.setObjectName("theme_frame")

    def _init_theme(self):
        """
        主题选择按钮
        :return:
        """

        with ThemeNote() as tn:
            theme_names = tn.select_all_theme()
        for theme_name_row in theme_names:
            theme_name = theme_name_row[0]
            theme_btn = self._create_theme_btn(theme_name)
            self.theme_arr.append(theme_btn)
            self.theme_set.add(theme_btn)
        btn_pos_x = THEME_BTN_BASE_X
        if self.theme_arr:
            btn_pos_x = self.theme_arr[-1].x() + THEME_BTN_WIDTH_SPACE
        self.add_theme_btn.setGeometry(QRect(btn_pos_x, THEME_BASE_Y,
                                             THEME_BASE_X + THEME_WIDTH,
                                             THEME_BASE_Y + THEME_HEIGHT))
        self.theme_font.setFamily("楷体")
        self.theme_font.setPointSize(THEME_FONT_SIZE)
        self.add_theme_btn.setFont(self.theme_font)
        self.add_theme_btn.setStyleSheet("border-radius:5px;\nborder:1px solid")
        self.add_theme_btn.setObjectName("theme")

    def _init_theme_container(self):
        """
        主题内容面板
        :return:
        """
        self.theme_container.setFrameShape(QFrame.StyledPanel)
        self.theme_container.setFrameShadow(QFrame.Raised)
        self.theme_container.setStyleSheet(
            "background-color: rgb(79, 208, 255);")
        self.theme_container.setObjectName("theme_container")

    def _init_sub_chapters(self):
        """
        标题列表
        :return:
        """
        self.sub_chapters.setGeometry(
            QRect(
                SUB_CHAPTER_LIST_BASE_X, SUB_CHAPTER_LIST_BASE_Y,
                SUB_CHAPTER_LIST_BASE_X + SUB_CHAPTER_LIST_WIDTH,
                SUB_CHAPTER_LIST_BASE_Y + SUB_CHAPTER_LIST_HEIGHT))
        self.sub_chapters.setWidgetResizable(True)
        self.sub_chapters.setObjectName("sub_chapter")
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.sub_chapters.sizePolicy().hasHeightForWidth())
        self.sub_chapters.setSizePolicy(size_policy)
        self.sub_chapters.setMinimumSize(QSize(*SUB_CHAPTER_LIST_MINIMUM_SIZE))
        self.sub_chapters.setMaximumSize(
            QSize(SUB_CHAPTER_LIST_MAX_WIDTH, MAX_SIZE_NUM))
        self.sub_chapters.setBaseSize(QSize(*SUB_CHAPTER_LIST_MINIMUM_SIZE))
        self.scroll_area_widget_contents.setGeometry(
            QRect(*SUB_CHAPTER_SCROLL_SHAPE))
        self.scroll_area_widget_contents.setObjectName(
            "scrollAreaWidgetContents")
        self._set_sub_chapter_scroll()
        self.sub_chapters.setWidget(self.scroll_area_widget_contents)

    def _set_sub_chapter_scroll(self):
        """
        重置滚动条大小
        :return:
        """
        chapter_count = len(self.chapter_arr)
        self.scroll_area_widget_contents.setMinimumSize(
            SUB_CHAPTER_SCROLL_WIDTH,
            SUB_CHAPTER_BTN_HEIGHT_SPACE * chapter_count)

    def _init_theme_container_label(self):
        """
        空白主题内容提示label
        :return:
        """
        self.theme_container_label.setAlignment(Qt.AlignCenter)
        self.theme_container_label.setMinimumSize(
            QSize(*THEME_CONTAINER_LABEL_SIZE))
        self.theme_container_label.setObjectName("note_content")

    def _init_menubar(self):
        """
        初始化菜单栏设置
        :return:
        """

        self.menubar.setGeometry(QRect(*MENU_GROUP_SHAPE))
        self.menubar.setObjectName("menubar")

        self.menu_file.setObjectName("menuFile")

        self.menu_edit.setObjectName("menuEdit")

        self.menu_window.setObjectName("menuWindow")

        self.menu_help.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)

        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.action_open.setObjectName("actionOpen")

        self.action_new_theme.setObjectName("action_new_theme")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_new_theme)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_window.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

    def setup_ui(self):
        """
        init ui
        :return:
        """
        self._init_theme_frame()
        self._init_theme()
        self._init_theme_container()
        self._init_sub_chapters()
        self._init_add_note_btn()
        self._init_theme_container_label()
        self.setCentralWidget(self.central_widget)
        self._init_menubar()
        self.re_translate_ui()
        QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        """

        :return:
        """
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("main_window", "MainWindow"))
        self.add_theme_btn.setText(_translate("main_window", "添加主题"))
        self.add_sub_chapter_btn.setText(_translate("main_window", "添加"))
        self.theme_container_label.setText(_translate("main_window", "请添加组件"))
        self.menu_file.setTitle(_translate("main_window", "File"))
        self.menu_edit.setTitle(_translate("main_window", "Edit"))
        self.menu_window.setTitle(_translate("main_window", "Window"))
        self.menu_help.setTitle(_translate("main_window", "Help"))
        self.action_open.setText(_translate("main_window", "Open"))
        self.action_new_theme.setText(_translate("main_window", "NewTheme"))
