#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 22:08
# @Author  : jjc
# @File    : main_window.py
# @Software: PyCharm
from PyQt6.QtWidgets import QWidget
from main_win_ui import UiForm


class CodeManagerTool(QWidget):
    def __init__(self):
        super(CodeManagerTool, self).__init__()
        self._ui = UiForm()
        self._ui.setup_ui(self)

