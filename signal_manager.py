#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 12:21
# @Author  : jjc
# @File    : signal_manager.py
# @Software: PyCharm
from PyQt5.QtCore import pyqtSignal, QObject


class SignalManager(QObject):
    signal = pyqtSignal(tuple)
    signal_str = pyqtSignal(str)

    def send_signal(self, str_arr):
        self.signal.emit(str_arr)

    def send_del_theme_btn(self, btn_name):
        self.signal.emit(btn_name)

    def send_theme_name(self, theme_name):
        self.signal_str.emit(theme_name)
