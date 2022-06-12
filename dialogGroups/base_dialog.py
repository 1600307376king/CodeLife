#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/12 3:06
# @Author  : jjc
# @File    : base_dialog.py
# @Software: PyCharm
from PyQt5.QtWidgets import QMainWindow
from signal_manager import SignalManager


class BaseDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.send = SignalManager()

    def close_dialog(self):
        """
        close dialog
        :return:
        """
        self.close()
