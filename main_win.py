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
import shutil
import os
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView
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
from config import WINDOW_SIZE
from config import THEME_FRAME_SIZE
from config import THEME_FRAME_MAX_HEIGHT
from config import MAX_SIZE_NUM
from config import THEME_BTN_BASE_Y
from config import THEME_BTN_WIDTH
from config import THEME_BTN_HEIGHT
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
from base_window import BaseWindow
import win32api


class MainWin(BaseWindow):
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

        self.tools_bar = QFrame(self.central_widget)

        self.grid_layout.addWidget(self.tools_bar, 0, 0, 1, 1)

        self.theme_frame = QFrame(self.central_widget)
        self.grid_layout.addWidget(self.theme_frame, 1, 0, 1, 1)

        self.theme_container = QFrame(self.central_widget)
        self.grid_layout.addWidget(self.theme_container, 2, 0, 1, 1)

        # self.switch_btn = SwitchButton(self.tools_bar)
        self.typora_exec_btn = QPushButton(self.tools_bar)

        self.add_theme_btn = QPushButton(self.theme_frame)

        self.grid_layout_chapter = QGridLayout(self.theme_container)
        self.grid_layout_chapter.setObjectName("grid_layout_chapter")
        self.grid_layout_chapter.setContentsMargins(0, 0, 0, 0)

        self.sub_chapters = QScrollArea(self.theme_container)
        self.grid_layout_chapter.addWidget(self.sub_chapters, 0, 0, 1, 1)
        # 章节滚动条
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

    def _init_typora_btn(self):
        self.typora_exec_btn.setObjectName("switch_btn")
        self.typora_exec_btn.setFont(self.tools_bar_font)
        self.typora_exec_btn.setText("打开Typora")
        self.typora_exec_btn.clicked.connect(self._exec_typora)

    @staticmethod
    def _exec_typora():
        if os.path.exists(os.path.join(os.getcwd(), "Typora\\Typora.exe")):
            subprocess.getstatusoutput(os.path.join(os.getcwd(), "Typora\\Typora.exe"))

    def add_chapter_data(self, chapter_info):
        """
        新增chapter数据，初始化UI
        :param chapter_info:
        :return:
        """
        if self.be_select_theme is None:
            self.be_select_theme = self.theme_arr[0].text()
        with ChapterNote() as cn:
            btn_text_name, file_path = chapter_info
            relative_path = "src/typora_src/src_html/%s" % self.be_select_theme
            file_name = "%s.html" % btn_text_name
            dst_path = os.path.join(os.getcwd(), relative_path)
            os.makedirs(dst_path, exist_ok=True)
            shutil.copy(file_path, os.path.join(dst_path, file_name))
            relative_fail_path = os.path.join(relative_path, file_name)
            cn.insert_note(self.be_select_theme, btn_text_name, relative_fail_path)
            self._add_chapter_btn((btn_text_name, relative_fail_path))

    def _add_chapter_btn(self, chapter_info):
        """
        添加文章UI
        :param chapter_info:
        :return:
        """
        btn_text_name, relative_path = chapter_info

        if btn_text_name:
            push_button = self._set_chapter_btn(btn_text_name)
            browser = QWebEngineView(self.theme_container)
            size_policy = QSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Preferred)
            size_policy.setHorizontalStretch(0)
            size_policy.setVerticalStretch(0)
            size_policy.setHeightForWidth(
                browser.sizePolicy().hasHeightForWidth())
            browser.setSizePolicy(size_policy)
            browser.setStyleSheet(THEME_BROWSER_STYLE)
            self.grid_layout_chapter.addWidget(browser, 0, 1, 1, 1)

            browser.setObjectName("context")
            dst_file_path = os.path.join(os.getcwd(), relative_path)

            if relative_path.endswith(".html") and os.path.exists(dst_file_path):
                with open(dst_file_path, "r", encoding="utf-8") as f:
                    browser.setHtml(f.read())
            else:
                browser.setHtml("<p>加载html失败，请检查文件格式</p>")
            browser.show()

            one_chapter = OneChapter(push_button, browser)
            self.chapter_arr.append(one_chapter)
            self.chapter_set.add(one_chapter.chapter_btn.text())
            self._set_sub_chapter_scroll()
            # 将之前的textBrowser隐藏，只显示新增的
            self._switch_chapter_content(btn_text_name)

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
            self._switch_theme_content(theme_name)

    def _switch_theme_content(self, theme_name):
        """
        切换主题
        :param theme_name:
        :return:
        """
        if not isinstance(theme_name, str):
            raise RuntimeError("theme name must be str")
        self.be_select_theme = theme_name
        for ch in self.chapter_arr:
            ch.chapter_btn.deleteLater()
            ch.browser_content.deleteLater()
        self.chapter_arr.clear()
        for theme in self.theme_arr:
            if theme.text() == theme_name:
                theme.setStyleSheet(THEME_HIGHLIGHT_STYLE)
            else:
                theme.setStyleSheet(THEME_NORMAL_STYLE)
        with ChapterNote() as cn:
            query_data = cn.select_note(theme_name)
        for row in query_data:
            self._add_chapter_btn(row)
        # 默认第一个chapter 为选中状态
        for index, chapter in enumerate(self.chapter_arr):
            if index > 0:
                chapter.browser_content.hide()
                chapter.chapter_btn.setStyleSheet(SUB_CHAPTER_NORMAL_STYLE)
            else:
                chapter.browser_content.show()
                chapter.chapter_btn.setStyleSheet(SUB_CHAPTER_HIGHLIGHT_STYLE)

    def _switch_chapter_content(self, chapter_name):
        for chapter in self.chapter_arr:
            if chapter.chapter_btn.text() == chapter_name:
                chapter.chapter_btn.setStyleSheet(SUB_CHAPTER_HIGHLIGHT_STYLE)
                chapter.browser_content.show()
            else:
                chapter.chapter_btn.setStyleSheet(SUB_CHAPTER_NORMAL_STYLE)
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
        new_theme_btn.setGeometry(QRect(btn_pos_x, THEME_BTN_BASE_Y,
                                        THEME_BTN_BASE_X + THEME_BTN_WIDTH,
                                        THEME_BTN_BASE_Y + THEME_BTN_HEIGHT))
        new_theme_btn.setText(theme_name)
        new_theme_btn.setFont(self.theme_font)
        new_theme_btn.setStyleSheet(THEME_NORMAL_STYLE)
        new_theme_btn.setObjectName(theme_name)
        new_theme_btn.clicked.connect(lambda: self._switch_theme_content(new_theme_btn.text()))
        # 允许按钮右键创建子菜单
        new_theme_btn.setContextMenuPolicy(Qt.CustomContextMenu)
        # 绑定菜单创建函数
        new_theme_btn.customContextMenuRequested.connect(lambda: self._show_btn_menu(new_theme_btn.text()))

        new_theme_btn.show()
        self.add_theme_btn.move(btn_pos_x + THEME_BTN_WIDTH_SPACE, THEME_BTN_BASE_Y)
        return new_theme_btn

    def _show_btn_menu(self, btn_name):
        """
        创建右键菜单
        :param btn_name:
        :return:
        """
        # 创建子菜单
        self.group_menu = QMenu(self)
        # 创建菜单元素， 删除选项
        self.action_del = QAction(QIcon("./src/icon/trash.png"), "删除", self)
        self.group_menu.addAction(self.action_del)
        self.action_del.triggered.connect(lambda: self._del_cur_theme_btn(btn_name))
        self.group_menu.popup(QCursor.pos())

    def _show_chapter_btn_menu(self, btn_name):
        # 创建子菜单
        self.group_menu = QMenu(self)
        # 创建菜单元素， 删除选项
        self.action_del = QAction(QIcon("./src/icon/trash.png"), "删除", self)
        self.action_edit = QAction(QIcon("./src/icon/edit.png"), "编辑", self)
        self.group_menu.addAction(self.action_del)
        self.group_menu.addAction(self.action_edit)
        self.action_del.triggered.connect(lambda: self._del_cur_chapter_btn(btn_name))
        self.action_edit.triggered.connect(lambda: self._edit_chapter(btn_name))
        self.group_menu.popup(QCursor.pos())

    @staticmethod
    def _edit_chapter(chapter_name):
        """
        edit chapter with typora
        :param chapter_name:
        :return:
        """
        md_file_path = os.path.join(os.getcwd(), chapter_name, ".md")
        if os.path.exists(md_file_path):
            win32api.ShellExecute(0, 'open', 'Typora.exe', md_file_path, "", 1)

    def _del_cur_theme_btn(self, btn_name):
        """
        发送删除主题按钮命令
        :param btn_name:
        :return:
        """
        next_theme_index = 0
        for index, theme in enumerate(self.theme_arr):
            if theme.text() == btn_name:
                theme.hide()
                self.theme_arr.remove(theme)
                self.theme_set.remove(theme.text())
                next_theme_index = index
                break

        # 如果被删除的按钮时最右边的，则索引向左移
        if next_theme_index >= len(self.theme_arr):
            next_theme_index -= 1
        # 删除按钮后变更其他按钮的位置
        base_pos = [THEME_BTN_BASE_X, THEME_BTN_BASE_X]
        for theme in self.theme_arr:
            theme.move(*base_pos)
            base_pos[0] += THEME_BTN_WIDTH_SPACE
            theme.show()
        self.add_theme_btn.move(*base_pos)
        self.add_theme_btn.show()

        # 删除关联主题内容
        if self.theme_arr:
            # 切换到最近的theme
            self._switch_theme_content(self.theme_arr[next_theme_index].text())
        else:
            # 删除最后一个主题内容
            for chapter in self.chapter_arr:
                chapter.browser_content.hide()
                chapter.chapter_btn.hide()
            self.chapter_arr.clear()
        with ThemeNote() as tn:
            tn.del_theme(btn_name)
            with ChapterNote() as cn:
                cn.del_note(btn_name)

    def _del_cur_chapter_btn(self, btn_name):
        next_chapter_index = 0
        for index, chapter in enumerate(self.chapter_arr):
            if chapter.chapter_btn.text() == btn_name:
                chapter.chapter_btn.hide()
                chapter.browser_content.hide()
                self.chapter_arr.remove(chapter)
                self.chapter_set.remove(chapter.chapter_btn.text())
                next_chapter_index = index
                break

        if next_chapter_index >= len(self.chapter_arr):
            next_chapter_index -= 1

        base_pos = [SUB_CHAPTER_BTN_BASE_X, SUB_CHAPTER_BTN_BASE_Y]
        self.add_sub_chapter_btn.move(*base_pos)
        self.add_sub_chapter_btn.show()
        base_pos[1] += SUB_CHAPTER_BTN_HEIGHT_SPACE
        for chapter in self.chapter_arr:
            chapter.chapter_btn.move(*base_pos)
            base_pos[1] += SUB_CHAPTER_BTN_HEIGHT_SPACE

        if self.chapter_arr:
            for index, chapter in enumerate(self.chapter_arr):
                if index == next_chapter_index:
                    chapter.chapter_btn.show()
                    chapter.browser_content.show()
                else:
                    chapter.browser_content.hide()

        with ChapterNote() as cn:
            cn.del_chapter(btn_name)

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
        push_button.setObjectName("push_button")
        push_button.setGeometry(
            QRect(
                SUB_CHAPTER_BTN_BASE_X,
                btn_pos_y,
                SUB_CHAPTER_BTN_BASE_X + SUB_CHAPTER_BTN_WIDTH,
                SUB_CHAPTER_BTN_BASE_Y + SUB_CHAPTER_BTN_HEIGHT))
        push_button.setText(btn_text_name)
        push_button.setStyleSheet(
            SUB_CHAPTER_NORMAL_STYLE)
        push_button.clicked.connect(lambda: self._switch_chapter_content(push_button.text()))
        # chapter 右键显示子菜单初始化
        push_button.setContextMenuPolicy(Qt.CustomContextMenu)
        push_button.customContextMenuRequested.connect(lambda: self._show_chapter_btn_menu(push_button.text()))
        push_button.show()
        return push_button

    def _init_tools_bar(self):
        self.tools_bar.setObjectName(u"tools_bar")
        self.tools_bar.setMinimumSize(QSize(160, 24))
        self.tools_bar.setMaximumSize(QSize(16777215, 25))
        self.tools_bar.setFrameShape(QFrame.StyledPanel)
        self.tools_bar.setStyleSheet(TOOLS_BAR_STYLE)
        self.tools_bar.setFrameShadow(QFrame.Raised)

    def _init_add_chapter_btn(self):
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
        self.add_sub_chapter_btn.setStyleSheet(SUB_CHAPTER_NORMAL_STYLE)
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
        self.theme_frame.setStyleSheet(THEME_FRAME_STYLE)
        self.theme_frame.setObjectName("theme_frame")

    def _init_theme(self):
        """
        主题选择按钮
        :return:
        """

        with ThemeNote() as tn:
            theme_names = tn.select_all_theme()
        for index, theme_name_row in enumerate(theme_names):
            theme_name = theme_name_row[0]
            theme_btn = self._create_theme_btn(theme_name)
            if index == 0:
                self._switch_theme_content(theme_name)
                theme_btn.setStyleSheet(THEME_HIGHLIGHT_STYLE)
            self.theme_arr.append(theme_btn)
            self.theme_set.add(theme_name)

        btn_pos_x = THEME_BTN_BASE_X
        if self.theme_arr:
            btn_pos_x = self.theme_arr[-1].x() + THEME_BTN_WIDTH_SPACE
        self.add_theme_btn.setGeometry(QRect(btn_pos_x, THEME_BTN_BASE_Y,
                                             THEME_BTN_BASE_X + THEME_BTN_WIDTH,
                                             THEME_BTN_BASE_Y + THEME_BTN_HEIGHT))

        self.add_theme_btn.setFont(self.theme_font)
        self.add_theme_btn.setStyleSheet(THEME_NORMAL_STYLE)
        self.add_theme_btn.setObjectName("theme")

    def _init_theme_container(self):
        """
        主题内容面板
        :return:
        """
        self.theme_container.setFrameShape(QFrame.StyledPanel)
        self.theme_container.setFrameShadow(QFrame.Raised)
        self.theme_container.setStyleSheet(THEME_CONTAINER_STYLE)
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
        # self.sub_chapters.setBaseSize(QSize(*SUB_CHAPTER_LIST_MINIMUM_SIZE))
        self.sub_chapters.setStyleSheet(SUB_CHAPTER_AREA_STYLE)
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
        self._init_tools_bar()
        self._init_typora_btn()
        self._init_theme_frame()
        self._init_theme()
        self._init_theme_container()
        self._init_sub_chapters()
        self._init_add_chapter_btn()
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
