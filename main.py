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
from PyQt6.QtWidgets import QApplication
from main_window import CodeManagerTool


def main():
    app = QApplication(sys.argv)
    ct = CodeManagerTool()
    ct.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
