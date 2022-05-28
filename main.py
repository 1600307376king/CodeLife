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
from PyQt5.QtWidgets import QApplication, QMainWindow
from dialogGroups.add_note_dialog import AddNoteDialog
from dialogGroups.add_theme_dialog import AddThemeDialog
from main_win import MainWin


class MyWindow(MainWin, QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.add_dialog = AddNoteDialog()
        self.add_theme_dialog = AddThemeDialog()

        self.setup_ui()
        self.set_dialog_bind()
        self.add_sub_chapter_btn.clicked.connect(self.add_dialog.show)
        self.add_theme_btn.clicked.connect(self.add_theme_dialog.show)
        self.set_add_dialog_signal_bind()

    def set_dialog_bind(self):
        self.add_dialog.setup_ui()
        self.add_theme_dialog.setup_ui()

    def set_add_dialog_signal_bind(self):
        self.add_dialog.send.signal.connect(self.add_chapter_btn)
        self.add_theme_dialog.send.signal_str.connect(self.add_theme)


def main():
    app = QApplication(sys.argv)
    ct = MyWindow()
    ct.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
