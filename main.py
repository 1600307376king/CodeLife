#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 13:28
# @Author  : jjc
# @File    : main.py
# @Software: PyCharm
# file: statusbar.py
# !/usr/bin/python

"""
ZetCode PyQt6 tutorial

This program creates a statusbar.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from dialogGroups.addNoteDialog import AddNoteDialog
from mainWin import MainWin


class MyWindow(MainWin, QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.add_dialog = AddNoteDialog()

        self.setup_ui()
        self.set_dialog_bind()
        self.add_sub_title.clicked.connect(self.add_dialog.show)
        self.set_add_dialog_signal_bind()

    def set_dialog_bind(self):
        self.add_dialog.setup_ui()

    def set_add_dialog_signal_bind(self):
        self.add_dialog.send.signal.connect(self.add_title_btn)


def main():
    app = QApplication(sys.argv)
    ct = MyWindow()
    ct.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
