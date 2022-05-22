#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 12:21
# @Author  : jjc
# @File    : signalManager.py
# @Software: PyCharm
from PyQt5.QtCore import pyqtSignal, QObject


class SignalManager(QObject):
    signal = pyqtSignal(tuple)

    def send_signal(self, str_arr):
        self.signal.emit(str_arr)
