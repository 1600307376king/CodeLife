#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 22:06
# @Author  : jjc
# @File    : config.py
# @Software: PyCharm


# 窗口
WINDOW_SIZE = (1280, 960)
WINDOW_TITLE = "Program Manager"

# 组件大小最大上限
MAX_SIZE_NUM = 16777215

# 菜单栏
MENU_GROUP_SHAPE = (0, 0, 800, 25)

# 工具栏
TOOLS_BAR_STYLE = "background-color: rgb(227, 255, 165);"
TOOLS_BAR_FAMILY = "宋体"
TOOLS_BAR_FONT_SIZE = 8

# 主题面板
THEME_FRAME_SIZE = (600, 0)
THEME_FRAME_MAX_HEIGHT = 160

# 主题字体样式
THEME_FAMILY = "宋体"

# 主题面板按钮
THEME_BTN_BASE_X = 10
THEME_BTN_BASE_Y = 10
THEME_BTN_WIDTH = 250
THEME_BTN_HEIGHT = 130
THEME_BTN_WIDTH_SPACE = 270
THEME_FONT_SIZE = 24
THEME_NORMAL_STYLE = "QPushButton{background-color: #f1faee;border-radius:15px;}" \
                    "QPushButton:hover{background-color: #a8dadc;border-radius:10px;" \
                    "font-size:36px;}"
THEME_HIGHLIGHT_STYLE = "QPushButton{background-color: #a8dadc;border-radius:15px;}" \
                    "QPushButton:hover{background-color: #457b9d;border-radius:10px;" \
                    "font-size:36px;}"

# 章节列表
SUB_CHAPTER_LIST_BASE_X = 0
SUB_CHAPTER_LIST_BASE_Y = 0
SUB_CHAPTER_LIST_WIDTH = 130
SUB_CHAPTER_LIST_HEIGHT = 420
SUB_CHAPTER_LIST_MINIMUM_SIZE = (150, 350)
SUB_CHAPTER_LIST_MAX_WIDTH = 150
SUB_CHAPTER_AREA_STYLE = "background-color: rgb(255, 255, 255);border: 1px solid rgb(255, 255, 255);border-radius:10px"


# 章节按钮字体
SUB_CHAPTER_FAMILY = "宋体"
SUB_CHAPTER_FONT_SIZE = 24

# 章节按钮
SUB_CHAPTER_BTN_WIDTH = 120
SUB_CHAPTER_BTN_HEIGHT = 30
SUB_CHAPTER_BTN_BASE_X = 10
SUB_CHAPTER_BTN_BASE_Y = 10
SUB_CHAPTER_BTN_HEIGHT_SPACE = 45
SUB_CHAPTER_NORMAL_STYLE = "QPushButton{background-color: #f1faee;border-radius:10px;}" \
                           "QPushButton:hover{background-color: #a8dadc;border-radius:10px;}"
SUB_CHAPTER_HIGHLIGHT_STYLE = "QPushButton{background-color: #a8dadc;border-radius:10px;}" \
                           "QPushButton:hover{background-color: #457b9d;border-radius:10px;}"

# 章节列表滚动条
SUB_CHAPTER_SCROLL_SHAPE = (0, 0, 130, 420)
SUB_CHAPTER_SCROLL_WIDTH = 10

# 文章主体
BROWSER_MINIMUM_SIZE = (500, 300)

# 文章隐藏时显示的标签
THEME_CONTAINER_LABEL_SIZE = (600, 350)


THEME_FRAME_STYLE = "background-color: rgb(255, 255, 255);border-radius:10px;"
THEME_BROWSER_STYLE = "border:3px solid rgb(255, 255, 255);border-radius:10px;"
THEME_CONTAINER_STYLE = ""
